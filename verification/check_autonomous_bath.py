"""Targeted autonomous-bath check; exact Gaussian path sums, no Monte Carlo.

Checks a finite stationary Jackson-kernel boson bath, projected Hamiltonian
at several total occupation cutoffs, and a retained-reference experiment
with noncommuting controls and a recorded measurement/feedback operation.
This is finite numerical evidence, not a substitute for the analytic proof.
"""
from itertools import combinations_with_replacement, product
import json
import math
import numpy as np
from scipy import sparse
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.sparse.linalg import expm_multiply

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
P0, P1 = (I2 + Z)/2, (I2-Z)/2
Z8 = np.kron(np.kron(Z, I2), I2)
P8 = [(np.eye(8)+Z8)/2, (np.eye(8)-Z8)/2]

def rotation(axis, angle):
    return expm(-.5j*angle*axis)

def controls():
    v1=np.kron(np.kron(rotation(X,.63),I2),I2)
    cnot=np.kron(np.kron(P0,I2),I2)+np.kron(np.kron(P1,I2),X)
    u=np.kron(np.kron(rotation(X,math.pi/2),I2),I2)
    v2=u.conj().T @ cnot @ u
    v3=np.kron(np.kron(rotation(X,.91),I2),P0)
    v3+=np.kron(np.kron(rotation(Z,.67)@rotation(Y,.38),I2),P1)
    return [v1,v2,v3]

def jackson_modes(m, gamma=.8, period=4.):
    triangle=np.array([m-abs(j) for j in range(1-m,m)], dtype=float)
    coeff=np.convolve(triangle,triangle)
    c0=(2*m**3+m)/3
    r=np.arange(2-2*m,2*m-1)
    return 2*math.pi*r/period, (gamma/period)*coeff/c0

def phase_covariance(times, omega, weights):
    lengths=np.diff(times)
    mid=(np.array(times[:-1])+np.array(times[1:]))/2
    integrals=lengths[None,:]*np.exp(-1j*omega[:,None]*mid[None,:])
    integrals*=np.sinc(omega[:,None]*lengths[None,:]/(2*math.pi))
    return np.real((integrals.T*weights)@integrals.conj())

def pinch_record(rho):
    idx=np.arange(8)
    return rho*((idx[:,None]%2)==(idx[None,:]%2))

def gaussian_output(cov, rho, ctrl):
    paths=[]
    for bits in product([0,1], repeat=len(ctrl)+1):
        op=np.eye(8,dtype=complex)
        for j,b in enumerate(bits):
            op=P8[b]@op
            if j<len(ctrl):
                op=ctrl[j]@op
        paths.append((1-2*np.array(bits),op))
    out=np.zeros((8,8),dtype=complex)
    for z,a in paths:
        for zz,b in paths:
            diff=z-zz
            out+=np.exp(-.5*diff@cov@diff)*(a@rho@b.conj().T)
    return pinch_record(out)

def boson_basis(modes, cutoff):
    basis=[]
    for total in range(cutoff+1):
        for combo in combinations_with_replacement(range(modes),total):
            basis.append(tuple(np.bincount(combo,minlength=modes)))
    return basis

def truncated_output(cutoff, omega, weights, times, state, ctrl):
    basis=boson_basis(len(omega),cutoff)
    index={b:i for i,b in enumerate(basis)}
    rows,cols,data=[],[],[]
    for col,b in enumerate(basis):
        for j,occ in enumerate(b):
            if occ:
                target=list(b)
                target[j]-=1
                rows.append(index[tuple(target)])
                cols.append(col)
                data.append(math.sqrt(weights[j]*occ))
    dim=len(basis)
    annih=sparse.csr_matrix((data,(rows,cols)),shape=(dim,dim))
    phi=annih+annih.getH()
    hb=sparse.diags(np.array(basis)@omega,format='csr')
    ham=sparse.kron(sparse.eye(8),hb)+sparse.kron(sparse.csr_matrix(Z8),phi)
    psi=np.zeros((8,dim),dtype=complex)
    psi[:,0]=state
    for j,dt in enumerate(np.diff(times)):
        psi=expm_multiply((-1j*dt)*ham,psi.reshape(-1)).reshape(8,dim)
        if j<len(ctrl):
            psi=ctrl[j]@psi
    return pinch_record(psi@psi.conj().T),dim

def distance(a,b):
    return float(np.abs(np.linalg.eigvalsh((a-b+(a-b).conj().T)/2)).sum()/2)

def dyson_tail(k,j):
    a=1.
    tail=0.
    for n in range(1,300):
        a*=math.sqrt((2*n-1)*j)/n
        if n>k:
            tail+=a
    return tail

def first_moment(m,gamma=.8,period=4.):
    c0=(2*m**3+m)/3
    def kernel(t):
        theta=2*math.pi*t/period
        ratio=m if abs(theta)<1e-13 else math.sin(m*theta/2)/math.sin(theta/2)
        return gamma/period*ratio**4/c0
    return 2*quad(lambda t:t*kernel(t),0,period/2,epsabs=1e-11,limit=300)[0]

def run_check():
    gamma=.8
    times=np.array([0.,.13,.39,.74,1.])
    ctrl=controls()
    psi=np.zeros(8,dtype=complex)
    psi[[0,6]]=1/math.sqrt(2)
    rho=np.outer(psi,psi.conj())
    white_cov=np.diag(gamma*np.diff(times))
    white=gaussian_output(white_cov,rho,ctrl)
    covariance_checks=[]
    for m in [2,4,8,16,32,64]:
        omega,weights=jackson_modes(m,gamma)
        cov=phase_covariance(times,omega,weights)
        colored=gaussian_output(cov,rho,ctrl)
        cov_l1=float(np.abs(cov-white_cov).sum())
        moment=first_moment(m,gamma)
        bound=2*(len(times)-1)*moment
        err=distance(colored,white)
        assert err<=cov_l1+1e-11
        assert cov_l1<=bound+1e-11
        assert np.linalg.eigvalsh(cov).min()>-1e-11
        covariance_checks.append(dict(m=m,modes=len(omega),covariance_l1=cov_l1,
          process_distance=err,first_moment_bound=bound,m_scaled_moment=moment*m/(gamma*4)))
    omega,weights=jackson_modes(2,gamma)
    cov=phase_covariance(times,omega,weights)
    colored=gaussian_output(cov,rho,ctrl)
    j=float(cov.sum())
    truncation_checks=[]
    for k in range(1,7):
        out,dim=truncated_output(k,omega,weights,times,psi,ctrl)
        err=distance(out,colored)
        bound=dyson_tail(k,j)
        assert err<=bound+2e-10
        assert abs(np.trace(out)-1)<2e-10
        truncation_checks.append(dict(cutoff=k,bath_dimension=dim,distance_to_exact_gaussian=err,
          dyson_tail_bound=bound,trace=float(np.trace(out).real)))
    result=dict(scope='Three fixed contact times; coherent reference and recorded noncommuting measurement/feedback. Exact Gaussian path sum; no Monte Carlo.',
        gamma=gamma,times=times.tolist(),jackson_period=4.,integrated_covariance=j,
        covariance_checks=covariance_checks,truncation_checks=truncation_checks)
    return result

if __name__=='__main__':
    print(json.dumps(run_check(),indent=2))
