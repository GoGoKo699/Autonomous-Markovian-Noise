# A finite bath needs logarithmic memory

A closed bath of dimension $`D`$ cannot produce arbitrarily many independent weak-noise outputs without leaving a detectable constraint on their joint state. A tester can expose that constraint by swapping fresh probes through the system and keeping every output until the final readout.

The proof below allows an arbitrary mixed initial bath. It uses neither the dephasing form of the microscopic Hamiltonian nor a bound on its norm. It therefore applies to the autonomous devices in the [model](model.md), and also to the larger class of closed finite baths with externally prescribed unitary dynamics.

The [finite-bath construction](finite_bath.md) gives the matching order of memory at fixed accuracy. The [resource theorem](resource_theorem.md) combines that construction with this converse and the separate [strength and bandwidth bounds](dynamical_bounds.md).

## 1. Statement with explicit constants

Fix the target

```math
\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho),
\qquad
T=\frac1\gamma,
```

and let $`N\ge0`$ be the number of allowed interior system contacts. A microscopic device has a bath $`E`$ of dimension $`D`$, initially in an input-independent state $`\eta_E`$ of rank

```math
r=\operatorname{rank}\eta_E\le D.
```

All bath degrees of freedom used during the run belong to $`E`$. The joint system-bath evolution is unitary between tester contacts; there are no supplied bath resets, discards, or additional environmental systems.

For the fixed device $`\mathcal D`$, write

```math
d_N=\sup_{\mathsf T}
\left|p_{\mathcal D}^{\mathsf T}
      -p_{\mathrm M}^{\mathsf T}\right|
```

for its worst-case operational error against the target under the tester class in the [model](model.md). Equivalently, this is the supremum of final half trace distance, since the tester's final measurement is unrestricted.

Set

```math
n=N+1,\qquad
p_n=\frac{1-e^{-2/n}}2,\qquad
a_n=1-p_n=\frac{1+e^{-2/n}}2.
```

**Proposition.** Every such device satisfies

```math
\boxed{
d_N\ge
\left[
1-a_n^n-(Dr-1)p_na_n^{\,n-1}
\right]_+ ,
}
```

where $`[x]_+=\max\{x,0\}`$. In particular,

```math
\boxed{
d_N\ge
\left[
\frac38-\frac{Dr-1}{N+1}
\right]_+ .
}
```

Consequently an error at most $`\epsilon\le1/4`$ requires

```math
Dr\ge 1+\frac{N+1}{8}.
```

For an arbitrary mixed bath, $`r\le D`$, and therefore

```math
D\ge\sqrt{1+\frac{N+1}{8}},
\qquad
\log_2D\ge
\frac12\log_2\!\left(1+\frac{N+1}{8}\right).
```

For an initially pure bath, $`r=1`$, giving the stronger explicit bound

```math
D\ge1+\frac{N+1}{8},
\qquad
\log_2D\ge
\log_2\!\left(1+\frac{N+1}{8}\right).
```

Both imply $`\log_2D=\Omega(\log(N+2))`$ at fixed error at most $`1/4`$. The constants are deliberately conservative. The proposition is an order converse, not a claim that these bounds give the optimal coefficient of $`\log N`$.

## 2. A swap-only tester archives independent ideal outputs

Let

```math
|\Phi^+\rangle
=\frac{|00\rangle+|11\rangle}{\sqrt2},
\qquad
|\Phi^-\rangle
=\frac{|00\rangle-|11\rangle}{\sqrt2}.
```

Divide the horizon into $`n=N+1`$ equal intervals of length $`h=T/n`$. At time zero the tester prepares $`n`$ pure Bell pairs. One probe half is the physical system $`S`$, paired with a protected reference $`R_1`$. The remaining probe halves $`A_1,\ldots,A_{n-1}`$ are stored in protected memory, with respective partners $`R_2,\ldots,R_n`$.

At each time $`jh`$, for $`j=1,\ldots,n-1`$, swap $`S`$ with $`A_j`$. The swap stores the output from interval $`j`$ and places the next fresh probe half in $`S`$. The tester retains every stored probe and every reference. At time $`T`$ it also retains the final system.

This is an allowed tester with exactly $`N`$ interior contacts, a pure initial tester state, and no intermediate measurements, resets, or classical randomness.

For one target interval,

```math
e^{h\mathcal L_\gamma}(\rho)
=a_n\rho+p_nZ\rho Z.
```

Acting on the probe half of a Bell pair therefore gives

```math
\tau_n
=a_n|\Phi^+\rangle\langle\Phi^+|
 +p_n|\Phi^-\rangle\langle\Phi^-|.
```

The Markov property and the fresh input at every swap make the ideal final tester state, up to a fixed register permutation,

```math
\sigma_n=\tau_n^{\otimes n}.
```

The microscopic bath can retain arbitrary correlations between intervals. No independence assumption is made about its output.

## 3. The microscopic output has rank at most $`Dr`$

Write a spectral decomposition of the initial bath state as

```math
\eta_E=\sum_{\alpha=1}^{r}
w_\alpha|e_\alpha\rangle\langle e_\alpha|.
```

The tester preparation is pure, and all intermediate tester operations are swaps. Combining these swaps with the device evolution yields one unitary $`V`$ on the bath and all tester registers. The final joint state is thus

```math
\sum_{\alpha=1}^{r}
w_\alpha|\Psi_\alpha\rangle\langle\Psi_\alpha|,
\qquad
|\Psi_\alpha\rangle
=V\bigl(|\psi_{\mathrm{test}}\rangle\otimes|e_\alpha\rangle\bigr).
```

For each $`\alpha`$, tracing a bath of dimension $`D`$ leaves a tester state of rank at most $`D`$, by the Schmidt decomposition. The rank of a sum of positive operators is at most the sum of their ranks. Hence the final accessible state $`\rho_D`$ obeys

```math
\operatorname{rank}\rho_D\le Dr\le D^2.
```

Equivalently, one can purify $`\eta_E`$ with an analytical reference of dimension $`r`$, leave that reference untouched, and trace a total inaccessible space of dimension $`Dr`$ at the end. This purification is a proof device; it does not assume that a mixed bath was physically prepared together with an extra resource accessible to the tester.

The rank statement is applied **before** the final measurement. It is not asserted for arbitrary testers that inject classical randomness, perform intermediate measurements, or discard their own registers. The selected swap-only tester does none of those things, and all its quantum outputs are retained.

## 4. A rank constraint produces a distinguishing event

The nonzero eigenvalues of $`\sigma_n`$ are

```math
a_n^{\,n-w}p_n^{\,w},
\qquad w=0,\ldots,n,
```

with multiplicity $`\binom nw`$. Since $`0\lt p_n\lt a_n`$, the largest eigenvalue is

```math
\lambda_0=a_n^n,
\qquad
|\Omega_n\rangle=|\Phi^+\rangle^{\otimes n},
```

and every other eigenvalue is at most

```math
\lambda_1=p_na_n^{\,n-1}.
```

Let $`P`$ be the support projector of $`\rho_D`$, of rank $`R\le Dr`$. The binary measurement $`\{P,I-P\}`$ finds the microscopic output in $`P`$ with probability one. For the target,

```math
\operatorname{Tr}(P\sigma_n)
\le\lambda_0+(R-1)\lambda_1
\le\lambda_0+(Dr-1)\lambda_1.
```

For example, this follows directly from

```math
\sigma_n
\le
\lambda_1 I+
(\lambda_0-\lambda_1)|\Omega_n\rangle\langle\Omega_n|,
```

and taking the trace against $`P`$ uses $`\operatorname{Tr}P=R`$ and a rank-one overlap at most one.

The difference of the probabilities of outcome $`I-P`$ is therefore at least

```math
1-\lambda_0-(Dr-1)\lambda_1.
```

The trace-distance variational principle, or this explicit binary event by itself, proves the first bound in the proposition.

The final projector $`P`$ can depend on the microscopic device. This is permitted by the operational distance: the device is fixed first, and its error is the supremum over all allowed testers and final readouts. The proof does not claim a single device-independent final measurement that certifies every bath dimension. In particular, measuring only the Bell labels would not by itself turn a quantum rank bound into a classical support bound.

## 5. Uniform fixed-error constants

The identity

```math
a_n=e^{-1/n}\cosh(1/n)
```

and $`\log\cosh x\le x^2/2`$ imply

```math
a_n^n
=e^{-1}\cosh(1/n)^n
\le e^{-1+1/(2n)}
\le e^{-1/2}\lt \frac58.
```

The elementary inequality for $`\log\cosh`$ follows by integrating $`\tanh x\le x`$ from zero. Also,

```math
p_n=\frac{1-e^{-2/n}}2\le\frac1n,
\qquad
p_na_n^{n-1}\le\frac1n.
```

Substitution yields

```math
d_N\ge
\left[\frac38-\frac{Dr-1}{n}\right]_+.
```

If $`d_N\le\epsilon\le1/4`$, the bracket must be at most $`1/4`$, so $`Dr-1\ge n/8`$. This establishes all the stated dimension and memory bounds.

## 6. What is counted and what the result establishes

The bath dimension counts all degrees of freedom belonging to the closed device. An uncounted classical random choice of Hamiltonian, a supply of fresh ancillas, or an external record carrying new noise during the run would change the model and invalidate this rank accounting. An arbitrary mixed initial state of the counted bath is already allowed through its rank $`r`$.

The argument applies to the finite swap tester itself, so it requires no approximation or closure argument. It also uses no bath energy bound, no assumption about bath purity or equilibrium, and no restriction to fixed-time testers for the upper theorem: this one fixed-time tester is sufficient for a converse against the larger adaptive class.

Combined with [the finite autonomous construction](finite_bath.md), the result establishes the logarithmic order of required bath memory at fixed accuracy. The simultaneous system-affecting strength and bath-bandwidth claims require the separate [dynamical bounds](dynamical_bounds.md), as stated in the [resource theorem](resource_theorem.md).
