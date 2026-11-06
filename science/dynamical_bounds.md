# Coupling and bath-width bounds

The dynamical restrictions have different scopes. The coupling bound permits arbitrary bath-only motion and even a prescribed time-dependent device Hamiltonian. The bath-width bound below uses the autonomous pure-dephasing form

```math
H=I\otimes H_E+Z\otimes B,
\qquad
\Lambda=\|B\|,
\qquad
W_E=\lambda_{\max}(H_E)-\lambda_{\min}(H_E).
```

It follows from the existing Uhrig dynamical-decoupling estimate and does not extend here to unrestricted interaction tensors. Throughout this page, the target is $`\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho)`$, the horizon is $`T=1/\gamma`$, $`N\ge1`$, and $`0\lt\epsilon\lt1/64`$. The contact model and distance $`d_N`$ are specified in [the model](model.md).

Every device with $`d_N\le\epsilon`$ satisfies

```math
\Lambda\ge\gamma\sqrt{\frac{N}{64\epsilon}},
\tag{1}
```

and, within the autonomous pure-dephasing class above,

```math
\frac{W_E}{2}+\Lambda\gt\frac{\gamma(N+1)}{4e}.
\tag{2}
```

In particular, if $`\Lambda\le C\gamma\sqrt{N+1}`$, then

```math
N+1\ge64e^2C^2
\quad\Longrightarrow\quad
W_E\gt\frac{\gamma(N+1)}{4e}.
\tag{3}
```

Equation (3) is a conditional bandwidth bound. It does not assert a separate linear lower bound on $`W_E`$ when the coupling is allowed to grow linearly or faster. The [finite construction](finite_bath.md) attains logarithmic memory, square-root coupling, and linear bath width simultaneously. The independent memory restriction is proved in [the memory bound](memory_bound.md), and the precise combined claim appears in [the resource theorem](resource_theorem.md).

## 1. Coupling: the inherited survival witness

The coupling mechanism and its constant are inherited from **Markovian-Resolution-Limit**, revision `b4af5cfb7a86165f29d9cf1e9adcb74f5fe91a8b`, `science/dissipators.md`, Sections 2-3. The following specialization makes the norm convention, contact count, and small-strength case explicit. Further attribution is in [related work](../references/RELATED_WORK.md).

Consider the broader microscopic dynamics

```math
H(t)=I\otimes H_E(t)+K(t),\qquad \|K(t)\|\le\overline\Lambda,
```

where $`\overline\Lambda\ge\gamma`$ is a declared strength cap. Put

```math
q=\frac{\gamma^2}{\overline\Lambda^2}\in(0,1],\qquad
\tau=\frac{q}{8\gamma},\qquad
\ell=\min\{N,\lfloor1/q\rfloor\}.
\tag{4}
```

Prepare $`|+\rangle`$ and perform the complete projective measurement $`\{|+\rangle\langle+|,I-|+\rangle\langle+|\}`$ at times $`\tau,2\tau,\ldots,\ell\tau`$. Retain the outcomes and record the event that every measurement succeeds. These are at most $`N`$ interior contacts, since $`\ell\tau\le T/8`$. Reading the stored event at time $`T`$ needs no further contact. The protocol does not postselect the delivered output.

Conditioned on every preceding success, the system is again $`|+\rangle`$, while the bath state can be arbitrary. Let $`\Pi=|+\rangle\langle+|\otimes I_E`$. Bath-only motion preserves $`\Pi`$. In its interaction frame, Duhamel's formula gives

```math
\|(I-\Pi)U(\tau)\Pi\|\le\overline\Lambda\tau.
```

Thus each conditional microscopic failure probability is at most $`\overline\Lambda^2\tau^2=q/64`$. The ideal success probability on each interval is

```math
p_M(\tau)=\frac{1+e^{-2\gamma\tau}}2
=\frac{1+e^{-q/4}}2
\le1-\frac q8+\frac{q^2}{64}
\le1-\frac q{16}.
```

The complete all-success probabilities obey

```math
p_D\ge(1-q/64)^\ell,
\qquad
p_M\le(1-q/16)^\ell.
```

The difference-of-powers identity and $`\ell q\le1`$ yield

```math
\begin{aligned}
p_D-p_M
&\ge\frac{3\ell q}{64}(1-q/16)^{\ell-1}\\
&\ge\frac{45\ell q}{1024}\\
&\ge\frac1{64}\min\{1,Nq\},
\end{aligned}
\tag{5}
```

where the last step uses $`\ell q\ge\tfrac12\min\{1,Nq\}`$. This recorded probability gap is a lower bound on $`d_N`$.

If the actual coupling is below $`\gamma`$, apply (5) with the valid declared cap $`\overline\Lambda=\gamma`$. It gives $`d_N\ge1/64`$, excluding that case at the specified accuracy. Otherwise take $`\overline\Lambda=\Lambda`$ in (5). Since $`64\epsilon\lt1`$, the accuracy requirement forces $`N\gamma^2/\Lambda^2\le64\epsilon`$, proving (1). Thus (1) does not tacitly assume that the unknown device already has coupling at least $`\gamma`$.

## 2. Autonomous bath width from an existing UDD theorem

For this section, the Hamiltonian is time independent and has precisely the pure-dephasing form displayed above. The bath is finite, so both $`H_E`$ and $`B`$ are bounded. The initial system and bath are independent; the bath may be mixed and need not be stationary, thermal, or passive. A scalar component of $`B`$ is allowed.

Apply $`N`$ instantaneous pi rotations about $`X`$ at

```math
t_j=T\sin^2\!\left(\frac{j\pi}{2N+2}\right),
\qquad j=1,\ldots,N.
\tag{6}
```

These are admissible contacts in the model. There is no assumed lower bound on their spacing.

Uhrig and Lidar's *Rigorous Bounds for Optimal Dynamical Decoupling*, Physical Review A 82, 012301 (2010), [arXiv:1002.1484](https://arxiv.org/pdf/1002.1484), Eqs. 14-21 and 34, imply the following for a pure initial qubit and arbitrary independent bath state. The final protected qubit, in the pulse frame, has half trace distance from the uncoupled qubit at most

```math
\min\{1,\Delta_N+\Delta_N^2\},
\qquad
\Delta_N=
\sum_{j=N+1}^{\infty}
\frac{T^j[(J_0+J_z)^j-(J_0-J_z)^j]}{2j!},
\tag{7}
```

where $`J_0=\|H_E-cI\|`$ and $`J_z=\|B\|`$. Centering the free-bath spectrum at $`c=(\lambda_{\max}(H_E)+\lambda_{\min}(H_E))/2`$ changes only a global phase and gives $`J_0=W_E/2`$. Formula (7) remains well defined at $`J_0=0`$; no division by that quantity is needed.

### Turning suppression into a necessary resource

Choose the initial qubit to be $`|+\rangle`$. Under the target Markov process, conjugation by an $`X`$ pulse leaves the dephasing generator unchanged. Its final state remains a fixed distance

```math
d_*:=\frac{1-e^{-2\gamma T}}2
=\frac{1-e^{-2}}2
```

from $`|+\rangle`$. The net $`X`$ pulse also leaves $`|+\rangle`$ invariant, so no additional system contact is needed to undo the pulse frame. The triangle inequality implies that an $`\epsilon`$-accurate device must obey

```math
\Delta_N+\Delta_N^2\ge d_*-\epsilon.
\tag{8}
```

Let

```math
n=N+1,\qquad
x=T\left(\frac{W_E}{2}+\Lambda\right).
```

All coefficients in (7) are nonnegative, and

```math
\Delta_N\le R_n(x):=\sum_{j=n}^{\infty}\frac{x^j}{j!}.
```

Suppose $`x\le n/(4e)`$. The bound $`n!\ge(n/e)^n`$ controls the first term, and the ratio of every successive term is at most $`1/(4e)`$. Therefore

```math
R_n(x)
\le\frac{(ex/n)^n}{1-1/(4e)}
\lt2\cdot4^{-n}.
\tag{9}
```

For $`N\ge1`$, we have $`n\ge2`$, so (9) gives

```math
\Delta_N+\Delta_N^2
\lt\frac18+\frac1{64}=\frac9{64}=0.140625.
```

But $`d_*-\epsilon\gt d_*-1/64\approx0.416707`$. This contradicts (8). Thus $`x\gt n/(4e)`$, which is precisely (2). The sum bound is valid for every $`N\ge1`$ at the stated accuracy, rather than only asymptotically.

### A fully explicit threshold for the conditional width bound

If a family of accurate devices satisfies $`\Lambda\le C\gamma\sqrt{N+1}`$, then

```math
N+1\ge64e^2C^2
\quad\Longrightarrow\quad
\Lambda\le\frac{\gamma(N+1)}{8e}.
```

Subtracting this from (2) gives (3). For a fixed coupling prefactor $`C`$, this is an explicit sufficient threshold for a linear lower bound on the bath spectral diameter.

## 3. Scope of the conclusion

The square-root coupling law is inherited from the survival experiment in Markovian-Resolution-Limit. The width obstruction is a consequence of the existing bounded-Hamiltonian UDD theorem. Neither is claimed as a new survival or decoupling mechanism. Their role is to identify the resource orders attained simultaneously by [the autonomous construction](finite_bath.md).

The UDD argument uses an autonomous Hamiltonian with one system coupling axis, bounded bath operators, and ideal instantaneous pulses. It does not establish the same linear sum bound for a general interaction containing several system Pauli tensors, for a time-dependent device, or for an unbounded bath Hamiltonian. The infinite oscillator reference used to prove the construction is therefore not a device to which this converse is applied; the final finite Hamiltonian is.

Equation (2) allows a larger coupling to supply part or all of the necessary dynamical scale. The separate linear width in (3) follows only after the square-root coupling cap is imposed. No complete Pareto frontier for unrestricted coupling is established.
