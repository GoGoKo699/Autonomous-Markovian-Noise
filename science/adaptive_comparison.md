# Gaussian comparison under adaptive contacts

This page proves the comparison estimate that turns a narrow positive covariance kernel into a uniform approximation of the controlled Markov process. The bound counts the contacts made on each realized classical history. It has no factor depending on the number of possible contact times, the number of branches, or the size of the protected quantum memory.

The [operational model](model.md) fixes the tester class and distance. The [finite-bath construction](finite_bath.md) supplies the autonomous Hamiltonian and its occupation-cutoff estimate. The two estimates are combined in the [resource theorem](resource_theorem.md). The independent strength and bandwidth converses are in [the dynamical bounds](dynamical_bounds.md).

## 1. Conventions and statement

The target is qubit dephasing,

```math
\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho),
\qquad \gamma\gt 0.
```

Our phase convention is

```math
U(\varphi)=e^{-iZ\varphi}.
```

A centered Gaussian phase of variance $`\gamma h`$ therefore induces $`e^{h\mathcal L_\gamma}`$: its action on an off-diagonal matrix element is multiplication by $`\mathbb E e^{-2i\varphi}=e^{-2\gamma h}`$.

For this page, first consider a finite classical policy tree. The tester starts with an arbitrary state of the qubit $`S`$ and a finite protected memory $`R`$, may use arbitrary finite-outcome instruments, and retains the outcomes needed by its policy. Each node specifies an instrument and its time using only the preceding classical record. Memory-only operations are free. Initial preparation and final readout at the fixed time $`T`$ are free. The counted system contacts occur strictly between zero and $`T`$; every operation there involving $`S`$ is a contact.

The bound of $`N`$ contacts is a structural restriction on every history of the policy tree, including histories that happen to have zero probability for a selected noise model. A declared instrument on $`SR`$ counts as a contact even when it acts as the identity on some quantum components or produces an outcome called “no change.” The count is not decided retrospectively from that instrument's outcome. Several operations at one time can be composed into one contact. Coherent superpositions of contact times and uncounted continuous access to $`S`$ are outside this model.

Let $`K`$ be a real, even, nonnegative periodic covariance kernel, with period $`L=4T`$ and mass

```math
\int_{-L/2}^{L/2}K(u)\,du=\gamma.
```

In addition to pointwise nonnegativity, assume that $`K`$ defines positive semidefinite covariance matrices. Define its first circular moment

```math
\mu=\int_{-L/2}^{L/2}|u|K(u)\,du.
```

Let $`\rho_K^{\mathsf T}`$ and $`\rho_{\mathrm M}^{\mathsf T}`$ be the final accessible states for the same finite tester $`\mathsf T`$, under the centered Gaussian phase process with covariance $`K`$ and under the target Markov process. Classical output registers are part of these states.

**Proposition.** Every such tester with at most $`N`$ contacts obeys

```math
\boxed{
\frac12\left\|\rho_K^{\mathsf T}
                 -\rho_{\mathrm M}^{\mathsf T}\right\|_1
\le (2N+1)\mu .
}
```

The right side can of course be capped at one. The proposition is proved for finite trees and extends to their allowed classical mixtures. Section 8 explains precisely how the final finite-device theorem, rather than an unspecified infinite comparison process, passes to the operational closure.

## 2. One deterministic grid represents a finite timing tree

Form the ordered union of all possible system-contact times in the finite tree:

```math
0=s_0\lt s_1\lt \cdots\lt s_q=T,
\qquad
I_a=(s_{a-1},s_a),
\qquad
h_a=s_a-s_{a-1}.
```

Different histories may use different subsets of these times. Introducing the union does not charge the unused times as contacts. At a grid point a history follows its declared instrument, or continues without a system contact.

There is no system contact inside any open interval $`I_a`$ on any history. Memory-only maps inside it commute, branch by branch, with all rotations of $`S`$. They can therefore be collected with their actual outcomes at interval boundaries when representing the experiment. This commutation preserves subnormalized conditional states even when $`S`$ and $`R`$ are entangled; it is not an independence assumption.

For a deterministic vector of integrated interval phases

```math
\varphi=(\varphi_1,\ldots,\varphi_q),
```

let $`F(\varphi)`$ be the final accessible state under the successive rotations $`U(\varphi_a)`$. The policy is fixed as $`\varphi`$ varies. Its choices depend on recorded outcomes, not on direct access to $`\varphi`$.

This produces a positive trace-one operator for every $`\varphi`$. Every phase appears once on the physical qubit in a fixed grid circuit. Since the eigenvalues of $`Z`$ are $`+1`$ and $`-1`$, $`F`$ is a finite operator-valued Fourier polynomial with frequencies $`0,+2,-2`$ in each coordinate. The same statement holds for a sum of any specified set of classical histories.

If the tester later erases a record, the analysis may keep a hidden copy of that already classical information. Such copies only label the completely positive branches being summed. They are neither extra observations nor registers made accessible to the tester. No purification is needed for the derivative argument below; a unitary dilation used elsewhere must preserve this same classical history interpretation.

## 3. Positive covariances have a useful difference decomposition

The colored and white interval-phase covariances are

```math
C_{ab}
=\int_{I_a}dt\int_{I_b}ds\,K(t-s),
\qquad
C^0_{ab}=\gamma h_a\delta_{ab}.
```

Both matrices are positive semidefinite. In addition, $`C_{ab}\ge0`$. For each fixed $`t`$, the interval $`[0,T]`$ spans less than one period, so positivity and the period mass imply

```math
\int_0^T K(t-s)\,ds\le\gamma.
```

Consequently

```math
r_a:=\gamma h_a-\sum_bC_{ab}\ge0.
```

Writing $`e_a`$ for the coordinate vectors gives the exact identity

```math
C-C^0
=-\sum_{a\lt b}C_{ab}(e_a-e_b)(e_a-e_b)^{\mathsf T}
  -\mathrm{diag}(r).
```

Two scalar bounds will be used. First,

```math
\begin{aligned}
\sum_a r_a
&=\gamma T-\int_0^Tdt\int_0^Tds\,K(t-s)\\
&=\int_{-L/2}^{L/2}\min\{T,|u|\}K(u)\,du\\
&\le\mu.
\end{aligned}
```

Second, for any cut $`\tau\in[0,T]`$,

```math
\begin{aligned}
Q(\tau)
&:=\int_0^\tau dt\int_\tau^Tds\,K(t-s)\\
&\le\int_0^T uK(u)\,du
\le\frac{\mu}{2}.
\end{aligned}
```

For a fixed positive lag $`u=s-t`$, the measure of pairs crossing $`\tau`$ is at most $`u`$. This proves the second inequality without assuming a minimum separation between contacts.

## 4. A first-contact event has phase-independent probability

Fix $`a\lt b`$. Define $`E_{ab}`$ to be the classical event that the policy declares at least one system contact at a cut

```math
s_j,\qquad a\le j\lt b.
```

Thus a contact just after $`I_a`$ or just before $`I_b`$ belongs to this event. A contact before $`I_a`$ or after $`I_b`$ does not. The event is known before the phase in $`I_b`$ acts.

Sum the subnormalized output operators over the corresponding sets of histories:

```math
F=F_{ab}^{\mathrm{inactive}}+F_{ab}^{\mathrm{active}},
\qquad
p_{ab}(\varphi)=\mathrm{Tr}\,F_{ab}^{\mathrm{active}}(\varphi).
```

Both summands are positive. Their definition uses a fixed subset of the policy tree, even though the probabilities of its histories depend on $`\varphi`$.

### Inactive outputs depend on the phase sum

On each inactive history, every operation between the two phases acts on $`R`$ alone. All such branch maps commute with the rotations of $`S`$, and the other intervening $`Z`$ rotations commute with one another. Thus the two distinguished phases can be combined. Subsequent operations, including subsequent outcome-dependent system contacts, are fixed completely positive branch maps applied to the same resulting state. Therefore

```math
F_{ab}^{\mathrm{inactive}}
(\varphi+x e_a-x e_b)
=F_{ab}^{\mathrm{inactive}}(\varphi)
```

for every real $`x`$, and hence

```math
(\partial_a-\partial_b)^2
F_{ab}^{\mathrm{inactive}}=0.
```

This is an operator identity for subnormalized outputs, not merely an equality of their traces.

### Active probabilities are independent of both distinguished phases

The trace $`p_{ab}`$ is independent of $`\varphi_b`$ by causality: $`E_{ab}`$ is settled before that phase, and all later complete instruments are trace preserving when their outcomes are summed.

For $`\varphi_a`$, partition the active event according to its first declared system contact after $`I_a`$. Fix a preceding history and one such first-contact time. Before that contact, every operation after the start of $`I_a`$ acts on memory alone. The memory-only branch maps deciding whether and when this first contact occurs commute with all intervening system rotations. In particular, their probability is unchanged by $`U(\varphi_a)`$.

More explicitly, let $`\mathcal A_R`$ be one composed memory-only branch map and let $`\rho_{SR}`$ be its incoming, possibly entangled, state. For any unitary $`V_S`$,

```math
\begin{aligned}
\mathrm{Tr}\!
\left[(\mathrm{id}_S\otimes\mathcal A_R)
 \bigl((V_S\otimes I)\rho_{SR}(V_S^\dagger\otimes I)\bigr)\right]
&=
\mathrm{Tr}\!
\left[(\mathrm{id}_S\otimes\mathcal A_R)(\rho_{SR})\right].
\end{aligned}
```

Summing over the disjoint first-contact alternatives and preceding histories proves

```math
p_{ab}(\varphi+x e_a+y e_b)=p_{ab}(\varphi)
```

for all real $`x,y`$.

The claim remains valid when the first-contact decision is made after the phase in $`I_a`$, using memory measurements performed during the intervening wait. Local system phases cannot alter those memory-only outcome probabilities. It would be false to replace $`E_{ab}`$ by an event postselected on the outcome of the first system contact; that is not the event used here.

## 5. Positive output branches bound the phase derivatives

Every coordinate of a branch output has frequencies $`0,+2,-2`$. The following parameter-shift identities are therefore exact:

```math
\partial_aG(\varphi)
=G\!\left(\varphi+\frac{\pi}{4}e_a\right)
 -G\!\left(\varphi-\frac{\pi}{4}e_a\right),
```

```math
\partial_a^2G(\varphi)
=2\left[
G\!\left(\varphi+\frac{\pi}{2}e_a\right)-G(\varphi)
\right].
```

For $`G=F_{ab}^{\mathrm{active}}`$, every shifted operator in these formulas is positive and has the same trace $`p_{ab}`$. Consequently

```math
\|\partial_a^2F_{ab}^{\mathrm{active}}\|_1\le4p_{ab},
\qquad
\|\partial_a\partial_bF_{ab}^{\mathrm{active}}\|_1\le4p_{ab},
```

and similarly for $`\partial_b^2`$. The inactive derivative vanishes, so

```math
\boxed{
\|(\partial_a-\partial_b)^2F\|_1\le16p_{ab}.
}
```

No normalization by $`p_{ab}`$ is made, including on zero-probability histories. For the complete trace-one output, the same second-derivative identity gives

```math
\|\partial_a^2F\|_1\le4.
```

## 6. Gaussian interpolation and contact accounting

Set $`C_u=(1-u)C^0+uC`$ for $`0\le u\le1`$, and let $`\mathbb E_u`$ denote expectation under the centered Gaussian vector with covariance $`C_u`$. Define

```math
\rho_u=\mathbb E_u F(\varphi).
```

The covariance differentiation identity used here is a finite Fourier-polynomial instance of [Price's theorem](https://arxiv.org/abs/1710.03576v2). It has a direct proof in the present setting. Write

```math
F(\varphi)=\sum_{\ell}A_\ell e^{i\ell\cdot\varphi},
\qquad
\ell\in\{-2,0,2\}^{q}.
```

The sum is finite and

```math
\rho_u=\sum_\ell A_\ell
\exp\!\left(-\frac12\ell^{\mathsf T}C_u\ell\right).
```

Differentiating this expression gives

```math
\frac{d\rho_u}{du}
=\frac12\sum_{a,b}(C-C^0)_{ab}
          \mathbb E_u[\partial_a\partial_bF].
```

The calculation is valid even when the endpoint covariance $`C`$ is singular. Substituting the difference decomposition,

```math
\frac{d\rho_u}{du}
=-\frac12\sum_{a\lt b}C_{ab}
       \mathbb E_u[(\partial_a-\partial_b)^2F]
 -\frac12\sum_a r_a\mathbb E_u[\partial_a^2F].
```

The derivative bounds yield

```math
\frac12\left\|\frac{d\rho_u}{du}\right\|_1
\le
4\sum_{a\lt b}C_{ab}\mathbb E_u p_{ab}
+\sum_a r_a.
```

At a fixed $`u`$, every probability $`\mathbb E_u p_{ab}`$ is evaluated in the same experiment: sample one phase vector with covariance $`C_u`$ and run the fixed tester policy with all its actual instrument outcomes. They are not probabilities taken from different replacement histories.

For any realized history $`z`$, let $`\mathcal C(z)`$ be its list of declared system-contact times. The structural budget gives $`|\mathcal C(z)|\le N`$, and

```math
\mathbf 1_{E_{ab}(z)}
\le
\sum_{\tau\in\mathcal C(z)}
\mathbf 1\{I_a\text{ precedes }\tau
                    \text{ and }I_b\text{ follows }\tau\}.
```

Since $`C_{ab}\ge0`$, averaging and interchanging finite sums gives

```math
\begin{aligned}
\sum_{a\lt b}C_{ab}\mathbb E_u p_{ab}
&\le
\mathbb E_u
\sum_{\tau\in\mathcal C(z)}
\int_0^\tau dt\int_\tau^Tds\,K(t-s)\\
&\le\frac{N\mu}{2}.
\end{aligned}
```

This step counts contacts on each history, rather than the union of all contacts that could occur on different histories. Together with $`\sum_a r_a\le\mu`$, it proves

```math
\frac12\left\|\frac{d\rho_u}{du}\right\|_1
\le(2N+1)\mu.
```

Integration from $`u=0`$ to $`u=1`$ proves the proposition.

## 7. Why the endpoints are the required controlled processes

At $`u=0`$, the phases in distinct grid intervals are independent Gaussians of variances $`\gamma h_a`$. Averaging their rotations gives the target semigroup on each interval, including when the input is entangled with memory. Future phase increments are independent of the earlier classical record. Thus $`\rho_0=\rho_{\mathrm M}^{\mathsf T}`$ for the adaptive policy.

At $`u=1`$, the interval phases have the covariance obtained by integrating the colored field. The joint phase vector is sampled once for the whole run; conditioning on tester outcomes can correlate its future and past coordinates. The calculation retains those correlations. It does not replace the colored process by independent interval channels. The [commuting-field construction](finite_bath.md) identifies this Gaussian process with the intermediate bosonic model.

An independent classical mixture of allowed finite policies also satisfies the bound by conditioning on its seed and averaging. The seed may be retained among the tester's outputs; the estimate is uniform in its value.

## 8. Passing the finite-device result to the operational closure

The [model](model.md) permits operational limits of finite policies when the declared output probabilities converge for the target and for every admissible finite microscopic device. That definition need not require convergence for the intermediate infinite-dimensional Gaussian comparison process.

The correct order of the proof is therefore as follows. For each finite policy, first combine this proposition with the occupation-cutoff estimate from [the finite-bath construction](finite_bath.md):

```math
\left|p_{\mathrm M}^{\mathsf T}
        -p_{\mathcal D_k}^{\mathsf T}\right|
\le (2N+1)\mu+\delta_k,
```

where $`\mathcal D_k`$ is the actual fixed finite autonomous device and $`\delta_k`$ is its uniform truncation bound. This holds for every allowed final binary readout; it follows from the stronger finite-policy half trace-distance estimate.

Now let $`\mathsf T_j`$ be a sequence defining an allowed operational-limit tester, with the same contact budget. Its probabilities converge for the target and for this particular finite $`\mathcal D_k`$, so

```math
\left|p_{\mathrm M}^{\mathsf T}
        -p_{\mathcal D_k}^{\mathsf T}\right|
=
\lim_{j\to\infty}
\left|p_{\mathrm M}^{\mathsf T_j}
        -p_{\mathcal D_k}^{\mathsf T_j}\right|
\le(2N+1)\mu+\delta_k.
```

This proves the final operational-distance bound in the stated closure. It requires no convergence assumption for the comparison Gaussian bath and no common trace-norm topology for quantum outputs of growing dimension.

Arbitrary continuous-outcome controllers are covered only when they belong to this specified closure, or to the allowed classical-mixture class. No assertion that every conceivable continuous controller has such an approximation is needed. In particular, the closure does not add coherent control of contact times, continuous system monitoring, or an outcome-dependent relaxation of the contact budget.
