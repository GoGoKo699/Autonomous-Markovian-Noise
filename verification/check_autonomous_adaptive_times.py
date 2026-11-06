"""Adaptive-time check for autonomous bath: retain every measurement outcome."""
import json
import math
import numpy as np
from check_autonomous_bath import (
    I2,X,Y,Z,rotation,jackson_modes,phase_covariance,gaussian_output,
    truncated_output,distance,dyson_tail,first_moment)

def run_check():
    gamma=.8
    plus=np.array([1.,1.])/math.sqrt(2)
    minus=np.array([1.,-1.])/math.sqrt(2)
    zero=np.array([1.,0.])
    one=np.array([0.,1.])
    # Nonmaximally entangled input with a nonzero X Bloch component;
    # first Y-outcome probabilities genuinely depend on the noise history.
    state=math.sqrt(.8)*np.kron(np.kron(plus,zero),zero)
    state+=math.sqrt(.2)*np.kron(np.kron(minus,one),zero)
    rho=np.outer(state,state.conj())
    branches=[]
    for outcome in [0,1]:
        measurement=np.kron(np.kron((I2+(-1)**outcome*Y)/2,I2),I2)
        v1=np.kron(np.kron(rotation(X,.7+.21*outcome),I2),I2)
        v2=np.kron(np.kron(rotation(Y,.5-.18*outcome),I2),I2)
        record=np.kron(np.kron(I2,I2),I2 if outcome==0 else X)
        times=np.array([0.,.12,.28 if outcome==0 else .47,.76 if outcome==0 else .89,1.])
        branches.append((times,[measurement,v1,v2],record))
    def gaussian_device(m=None):
        output=np.zeros((8,8),complex)
        for times,ctrl,record in branches:
            if m is None:
                cov=np.diag(gamma*np.diff(times))
            else:
                omega,weights=jackson_modes(m,gamma)
                cov=phase_covariance(times,omega,weights)
            branch=gaussian_output(cov,rho,ctrl)
            output+=record@branch@record.conj().T
        return output
    white=gaussian_device()
    covariance=[]
    for m in [2,4,8,16,32,64]:
        colored=gaussian_device(m)
        err=distance(colored,white)
        bound=(2*3+1)*first_moment(m,gamma)
        assert err<=bound+1e-11
        assert abs(np.trace(colored)-1)<1e-11
        covariance.append(dict(jackson_m=m,adaptive_output_distance=err,activity_bound=bound))
    omega,weights=jackson_modes(2,gamma)
    colored=gaussian_device(2)
    truncation=[]
    for cutoff in [2,4,6]:
        out=np.zeros((8,8),complex)
        for times,ctrl,record in branches:
            branch,dim=truncated_output(cutoff,omega,weights,times,state,ctrl)
            out+=record@branch@record.conj().T
        err=distance(out,colored)
        bound=dyson_tail(cutoff,gamma)
        assert err<=bound+2e-10
        assert abs(np.trace(out)-1)<2e-10
        truncation.append(dict(cutoff=cutoff,bath_dimension=dim,adaptive_output_distance=err,uniform_dyson_bound=bound,trace=float(np.trace(out).real)))
    result=dict(scope='One Y-measurement followed by outcome-dependent contact times; three contacts per branch, protected reference, all outcomes retained, no postselection.',
        branch_times=[x[0].tolist() for x in branches],covariance_checks=covariance,truncation_checks=truncation)
    return result

if __name__=='__main__':
    print(json.dumps(run_check(),indent=2))
