# Joint autonomous resource theorem

[Model](model.md) · [Construction](finite_bath.md) · [Interpretation](interpretation.md)

## Statement

Fix $`\gamma\gt0`$, $`T=1/\gamma`$, an integer $`N\ge1`$, and $`0\lt\epsilon\lt1/64`$. Use the tester class and resource definitions of the [model](model.md).

There is a finite bath in a pure stationary initial state and a time-independent Hamiltonian $`H=I\otimes H_E+Z\otimes B`$, chosen independently of the tester, such that

```math
d_N({\rm dev},{\rm M})\le\epsilon,
```

and, simultaneously,

```math
Q=O_\epsilon(\log(N+2)),\qquad
\Lambda=O_\epsilon(\gamma\sqrt N),\qquad
W_E=O_\epsilon(\gamma N).
```

For every sufficiently accurate finite device, the encoded memory is $`\Omega(\log(N+2))`$ and the interaction strength is $`\Omega_\epsilon(\gamma\sqrt N)`$. In the autonomous pure-dephasing interaction class, the spectral obstruction is

```math
\frac{W_E}{2}+\Lambda\gt\frac{\gamma(N+1)}{4e}.
```

Consequently the upper construction attains all three orders when the interaction is kept at its optimal square-root order. The bandwidth conclusion is conditional on that interaction scale. The theorem does not characterize the full tradeoff at unrestricted coupling.

## Explicit upper parameters

Let $`(-1)!!=1`$ and define

```math
b_n(J)=\frac{\sqrt{(2n-1)!!}}{n!}\,J^{n/2},
\qquad
E_k(J)=\sum_{n=k+1}^{\infty}b_n(J).
```

Choose an integer $`k\ge1`$ with $`E_k(1)\le\epsilon/2`$, and set

```math
m=\left\lceil\frac{6(2N+1)}{\epsilon}\right\rceil,
\qquad M=4m-3.
```

Such a $`k`$ exists because

```math
\frac{b_{n+1}(1)}{b_n(1)}=\frac{\sqrt{2n+1}}{n+1}\longrightarrow0.
```

The [construction](finite_bath.md) uses $`M`$ signed-frequency modes restricted to total occupation at most $`k`$. Its exact dimension and sufficient resource bounds are

```math
D=\binom{M+k}{k},\qquad
\Lambda\le\gamma\sqrt{\frac{3km}{2}},\qquad
W_E\le2\pi k\gamma(m-1).
```

At fixed $`\epsilon`$, the cutoff $`k`$ is independent of $`N`$ and $`m=O_\epsilon(N)`$. Hence the number of encoded bath qubits grows logarithmically, while interaction strength and width grow as the square root and first power of the contact budget. These conservative constants are not asserted to be optimal.

## Proof of the approximation

Use period $`L=4T`$ and the positive Jackson covariance $`K_m`$ defined in the construction. Its total mass over one period is $`\gamma`$. Its circular first moment and integrated covariance satisfy

```math
\mu_m=\int_{-L/2}^{L/2}|u|K_m(u)\,du\le\frac{3\gamma T}{m},
\qquad
J_m=\int_0^T\!\int_0^T K_m(t-s)\,dt\,ds\le\gamma T=1.
```

For every finite timing tree, the [adaptive Gaussian comparison](adaptive_comparison.md) gives

```math
d_{\mathsf T}({\rm Gaussian},{\rm M})\le(2N+1)\mu_m.
```

The full Gaussian oscillator model is an intermediate proof device. The [occupation-cutoff estimate](finite_bath.md) compares its entire controlled evolution with the actual finite projected Hamiltonian:

```math
d_{\mathsf T}({\rm dev},{\rm Gaussian})\le E_k(J_m)\le E_k(1).
```

Adding the two inequalities gives

```math
d_{\mathsf T}({\rm dev},{\rm M})
\le\frac{3(2N+1)}{m}+E_k(1)
\le\frac\epsilon2+\frac\epsilon2=\epsilon.
```

The estimate is independent of the number of nodes in the timing tree, tester-memory dimension and contact spacing. It extends to independent classical mixtures. For an operational-limit tester, apply the combined inequality to each approximating finite tester and each final event. The target and the actual finite device both satisfy the convergence assumption in the model, so the event inequality passes to the limit. Taking the supremum over final events and testers proves the claim. Convergence for the infinite Gaussian reference is not needed.

## Memory necessity

The [Bell-swap witness](memory_bound.md) divides the interval into $`n=N+1`$ equal pieces, uses a fresh Bell pair in each piece, and retains every output and reference. If the initial bath has rank $`r`$, the microscopic accessible output before final readout has rank at most $`Dr`$. Comparison with the ideal product spectrum gives, for $`\epsilon\le1/4`$,

```math
Dr\ge1+\frac{N+1}{8}.
```

Since $`r\le D`$, this implies

```math
Q\ge\frac12\log_2\!\left(1+\frac{N+1}{8}\right).
```

For a pure initial bath the factor $`1/2`$ is absent. This converse concerns encoded memory order. It does not determine the optimal polynomial exponent of $`D`$ at each accuracy.

## Interaction and spectral necessity

The [interaction-resolution theorem](dynamical_bounds.md) inherited from Markovian Resolution Limit yields

```math
\Lambda\ge\gamma\sqrt{\frac{N}{64\epsilon}}.
```

That obstruction already holds for a fixed contact schedule and therefore applies to the larger adaptive tester class. Its microscopic setting allows more freedom than the present autonomous construction.

For the spectral bound, $`N`$ ideal Uhrig pulses preserve target dephasing but suppress a sufficiently slow bounded microscopic bath. The [rigorous decoupling estimate](dynamical_bounds.md), after centering $`H_E`$, gives the stated sum obstruction. It applies to arbitrary initial bath states in this pure-dephasing interaction class.

In particular, suppose $`\Lambda\le C\gamma\sqrt{N+1}`$ with $`C`$ independent of $`N`$. When

```math
N+1\ge64e^2C^2,
```

the sum obstruction implies

```math
W_E\gt\frac{\gamma(N+1)}{4e}.
```

Together with the construction, this establishes the linear width order at optimal interaction strength.

## Quantifiers and limitations

The asymptotic variable is $`N`$. Accuracy, normalized horizon $`\gamma T=1`$ and the qubit target are fixed. The same constructed device works for every admitted tester, but a different design may be chosen when $`N`$, $`\epsilon`$ or $`\gamma`$ changes.

The construction uses an engineered nonpassive bath and allows global interactions; necessity of nonpassivity is not proved. It gives neither a thermal construction nor efficient local synthesis. The spectrum converse is not extended to arbitrary system–bath coupling tensors. Sharp joint dependence on accuracy and contact budget, and indefinite reuse beyond the designed horizon, remain outside the result. [Interpretation](interpretation.md) explains the physical role of these assumptions; [related work](../references/RELATED_WORK.md) records inherited ingredients and comparison limits.
