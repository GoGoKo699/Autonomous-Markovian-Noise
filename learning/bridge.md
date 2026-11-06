# From open-system dynamics to an autonomous finite reservoir

[Project overview](../README.md) · [Thirty milestones](milestones.md) · [Exact theorem](../science/resource_theorem.md)

A qubit can lose interference while its populations remain unchanged. An open-system equation describes that dephasing by tracing out an environment. This project asks how much of a finite environment is needed to reproduce the same noise when an experimenter can intervene during the evolution, keep earlier outputs, and choose later actions from measurement results.

The selected educational anchor is **Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction*, first edition, ©2012, Springer**, DOI [10.1007/978-3-642-23354-8](https://doi.org/10.1007/978-3-642-23354-8). The route below uses three chapters of that one source:

- **Chapter 3, “Time Evolution in Open Quantum Systems,” pp. 19–31:** the starting point for reduced states and dynamical maps. Continue here with the concrete dephasing channel and its finite dilation.
- **Chapter 4, “Quantum Markov Process: Mathematical Structure,” pp. 33–48:** the starting point for the target semigroup. Continue here with the stronger specification of what happens between interventions.
- **Chapter 5, “Microscopic Description: Markovian Case,” pp. 49–80:** the starting point for connecting a bath model to a Markovian description. Continue here with explicit finite resources and error uniform over the declared experiments.

Chapters 1–2 of the same book can refresh mathematical and closed-system prerequisites. Chapter 6 supplies optional context about non-Markovian microscopic dynamics. Neither is required before reading the example below.

These chapter titles and page ranges follow the [publisher's contents](https://link.springer.com/book/10.1007/978-3-642-23354-8). All notation, derivations, and the worked example below use **this project's conventions**; they are not presented as the book's equation numbering or symbol choices. The [milestone map](milestones.md) develops the background in M01–M13 and the project mechanism in M14–M30.

## 1. Fix the objects and the rate convention

The system $`S`$ is a qubit with basis states $`|0\rangle`$ and $`|1\rangle`$. Its density matrix records both populations and coherence:

```math
\rho=
\begin{pmatrix}
a&c\\
c^*&1-a
\end{pmatrix},
\qquad
0\le a\le1,\qquad |c|^2\le a(1-a).
```

The diagonal entries are the probabilities of the two basis outcomes. The complex number $`c`$, called a coherence, contributes to interference measurements; $`c^*`$ is its complex conjugate. A measurement event represented by a projector $`P`$ has probability $`\operatorname{Tr}(P\rho)`$.

The Pauli operator $`Z`$ preserves $`|0\rangle`$ and reverses the sign of $`|1\rangle`$. The Pauli operator $`X`$ interchanges them. For example,

```math
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}.
```

The target evolution obeys

```math
\frac{d\rho}{dt}=\mathcal L_\gamma(\rho),
\qquad
\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho),
\qquad \gamma\gt0.
```

Conjugating by $`Z`$ changes the sign of both off-diagonal entries. The equation therefore gives $`\dot a=0`$ and $`\dot c=-2\gamma c`$, so the interval channel is

```math
\mathcal E_t(\rho)=
\begin{pmatrix}
a&e^{-2\gamma t}c\\
e^{-2\gamma t}c^*&1-a
\end{pmatrix}.
```

Populations stay fixed while interference decays. In this convention the coherence decay rate is $`2\gamma`$. The main horizon $`T=1/\gamma`$ reduces coherence by $`e^{-2}`$. This factor of two also appears in the phase-noise convention later.

Equivalently,

```math
\mathcal E_t(\rho)=(1-p_t)\rho+p_tZ\rho Z,
\qquad
p_t=\frac{1-e^{-2\gamma t}}2.
```

This is a completely positive trace-preserving map: it remains a valid state transformation when the qubit is entangled with an untouched reference. The family is a semigroup, meaning $`\mathcal E_{s+t}=\mathcal E_s\circ\mathcal E_t`$. For the project's **Markov process**, this same interval map is applied after every permitted intervention, with no hidden bath record changing its future action. That controlled-process specification is part of [the model](../science/model.md).

## 2. Translate the open-system description into this project

Write $`E`$ for the device's bath and $`R`$ for the experimenter's protected memory and references. They have different roles: the experimenter controls $`R`$ but cannot access $`E`$.

A reduced channel can be obtained from a joint unitary:

```math
\rho_{SR}(t)=
\operatorname{Tr}_E
\left[
(U_t\otimes I_R)(\rho_{SR}\otimes\omega_E)
(U_t^\dagger\otimes I_R)
\right],
\qquad U_t=e^{-itH}.
```

Here $`U_t`$ acts on $`SE`$; the tensor ordering is understood through the register labels. The partial trace discards the bath from the description of accessible measurement probabilities. It does not physically reset the bath. The product assumption $`\rho_{SR}\otimes\omega_E`$ is imposed at time zero. Later system–bath correlations remain in the joint dynamics.

The following conventions supplement the anchor's reduced-dynamics viewpoint:

| Project notation | Meaning |
|---|---|
| $`\omega_E`$, $`D`$ | Initial bath state and dimension of its entire Hilbert space. |
| $`N`$ | Maximum number of interior contacts with the system on every policy history. |
| $`d_N`$ | Largest discrepancy in a final event probability over the allowed experiments. |
| $`H_E`$, $`B`$ | Free bath Hamiltonian and bath operator coupled to $`Z`$. |
| $`Q=\lceil\log_2D\rceil`$ | Encoded bath-memory cost, measured in qubits. |
| $`\Lambda=\lVert B\rVert`$ | Interaction strength; for Hermitian $`B`$, its largest absolute eigenvalue. |
| $`W_E`$ | Largest free-bath energy minus smallest free-bath energy. |

We set $`\hbar=1`$, so Hamiltonian eigenvalues, $`\Lambda`$, and $`\gamma`$ have frequency units. A scalar shift of $`H_E`$ changes only a global phase; this is why the spectral diameter, rather than an arbitrary choice of energy zero, is charged.

The autonomous device has one time-independent Hamiltonian,

```math
H=I_S\otimes H_E+Z\otimes B.
```

Every degree of freedom used by the device belongs to $`E`$ from the start. No bath reset, incoming ancilla, discarded bath record, or external device-switching schedule is supplied during the run. The experimenter's interventions are external probes of that fixed device and are counted separately.

## 3. Worked example: one final channel can match exactly while one echo distinguishes the process

This example uses a single bath qubit. It is a local derivation illustrating the task, not the construction that attains the resource theorem.

Take

```math
H_E=0,\qquad
B=gZ_E,\qquad
H=gZ_S\otimes Z_E,\qquad
\omega_E=|+\rangle_E\langle+|.
```

Thus $`D=2`$, $`Q=1`$, $`\Lambda=g`$, and $`W_E=0`$. Conditional on the system being in $`|0\rangle`$ or $`|1\rangle`$, the bath evolves with opposite signs. Tracing it out multiplies the system's off-diagonal entry by

```math
\langle+|e^{-2igtZ_E}|+\rangle=\cos(2gt).
```

Choose

```math
g=\frac{1}{2T}\arccos(e^{-2\gamma T}).
```

At the final time $`T`$, the microscopic channel therefore agrees exactly with $`\mathcal E_T`$: its populations and both off-diagonal entries agree for every input. Equality of the linear maps also gives equality on inputs entangled with protected references. This is a valid exact dilation of the desired **one-time** channel.

Now prepare the system in $`|+\rangle`$, apply one $`X`$ pulse at $`T/2`$, and measure the event $`|+\rangle\langle+|`$ at time $`T`$. The pulse is the only interior system contact. Since

```math
(X_S\otimes I_E)H(X_S\otimes I_E)=-H,
```

the two microscopic evolutions cancel:

```math
U_{T/2}(X_S\otimes I_E)U_{T/2}=X_S\otimes I_E.
```

The system finishes in $`|+\rangle`$, because $`X|+\rangle=|+\rangle`$. Its final success probability is one.

For the Markov target, changing $`Z`$ to $`-Z`$ leaves the generator unchanged. Directly, after the first half interval the system state is $`(I+e^{-\gamma T}X)/2`$; conjugation by $`X`$ leaves this state unchanged. The second half interval therefore gives

```math
\rho_{\mathrm M}(T)=\frac{I+e^{-2\gamma T}X}{2},
\qquad
p_{\mathrm M}(+)=\frac{1+e^{-2\gamma T}}2.
```

The final-event probability gap is

```math
p_{\mathrm{dev}}(+)-p_{\mathrm M}(+)
=\frac{1-e^{-2\gamma T}}2.
```

At $`\gamma T=1`$, this is approximately $`0.4323`$. Exact agreement at the final time without intervention has therefore left a large discrepancy in an allowed one-contact experiment. The bath retains a phase record that the echo reverses. The target's independent noise increments continue to dephase.

This example also explains why a narrow bath spectrum matters. The general [dynamical bound](../science/dynamical_bounds.md) uses a longer, carefully timed pulse sequence to turn that sensitivity into a necessary spectral resource. The example alone is not that converse.

## 4. From a channel to an experiment with records and feedback

A **quantum instrument** is a collection of completely positive maps, one per possible measurement outcome, whose sum is trace preserving. The trace of a branch gives its probability. Keeping its outcome permits later feedback. Unitary pulses and swaps are special cases of the allowed contacts.

A tester can store outputs in $`R`$, bring in a fresh entangled probe, measure $`SR`$, and choose its next time and instrument from its existing classical record. Every policy history must have at most $`N`$ declared system contacts, including histories with zero probability for a particular device. The contact count is fixed by the policy, not chosen after seeing whether an outcome changed the system. Initial preparation and the final readout are free; every interior operation involving $`S`$ is counted.

For a finite tester $`\mathsf T`$, its accessible output includes retained quantum systems and classical outcomes. Its distinguishing distance is

```math
d_{\mathsf T}
=\frac12
\left\|\rho_{\mathrm{dev}}^{\mathsf T}
-\rho_{\mathrm M}^{\mathsf T}\right\|_1.
```

The trace norm of a Hermitian matrix is the sum of the absolute values of its eigenvalues. Half trace distance equals the largest difference in the probability of a binary measurement event. Consequently $`d_N\le\epsilon`$ means that every admitted tester and every final event have probability discrepancy at most $`\epsilon`$. All outcomes count; postselecting a favorable result does not define the comparison.

The proof handles arbitrary finite classical timing trees, including arbitrarily close contact times and arbitrarily large finite memory. Its bounds are independent of the size of the union of all possible times. The final event inequality then extends to the **operational closure** defined in [the model](../science/model.md): limits of finite policies whose declared event probabilities converge for the target and each finite device. This does not presume one common quantum-output Hilbert space for every limit.

Classically adaptive timing is included. Coherent superpositions of distinct contact times and uncharged continuous monitoring are outside the model.

## 5. The extra steps from microscopic dynamics to the finite resource theorem

Chapter 5 is the natural point from which to ask how a microscopic reservoir produces a Markovian description. The project adds a quantitative requirement: one explicitly finite autonomous device must approximate all the declared controlled experiments at the same error. Two uniform estimates supply the bridge.

### 5.1 Replace white phase noise by a finite covariance

With the project's phase convention, a random rotation is

```math
U(\varphi)=e^{-iZ\varphi}.
```

If $`\varphi`$ is a centered Gaussian variable of variance $`\gamma h`$, its action on coherence averages to

```math
\mathbb E[e^{-2i\varphi}]=e^{-2\gamma h}.
```

Independent Gaussian increments in separate intervals therefore realize the target process, including its action on entangled inputs. A colored Gaussian field instead has a covariance

```math
K(t-s)=\mathbb E[\xi(t)\xi(s)].
```

This function describes correlations between the field at two times. The finite Fourier kernel used in [the construction](../science/finite_bath.md) is both a valid covariance and pointwise nonnegative. These are distinct properties: validity means every sampled covariance matrix is positive semidefinite; pointwise nonnegativity means each individual value of $`K`$ is nonnegative.

For a kernel of period $`L=4T`$, the first circular moment is

```math
\mu=\int_{-L/2}^{L/2}|u|K(u)\,du.
```

At fixed total kernel mass, a narrow correlation peak has small $`\mu`$. The [adaptive Gaussian comparison](../science/adaptive_comparison.md) establishes

```math
d_{\mathsf T}(\mathrm{Gaussian},\mathrm M)
\le(2N+1)\mu.
```

The difficult point is the dependence on $`N`$. A timing tree can contain many possible contacts, but each actual history uses only $`N`$. Before the first system contact between two phase intervals, operations on protected memory cannot reveal a local system phase, even for an entangled input. The proof uses that causal fact to charge correlation errors to contacts that actually occur. It retains the correlations created by conditioning on earlier outcomes.

The chosen Jackson kernel has $`M=4m-3`$ modes and $`\mu\le3\gamma T/m`$. Symmetric positive and negative frequencies give commuting bath fields, allowing the full oscillator reference to reproduce the Gaussian process under arbitrary allowed instruments. This oscillator reference is an intermediate mathematical model.

### 5.2 Turn the reference into one finite Hamiltonian

Each oscillator mode has occupation numbers $`0,1,2,\ldots`$. Restrict the sum of those occupations across all $`M`$ modes to at most $`k`$. The retained Hilbert space has dimension

```math
D=\binom{M+k}{k}.
```

For fixed $`k`$, this grows polynomially with $`M`$, so its encoded qubit cost grows logarithmically. Occupation is a basis label of the oscillator reference; it is not assumed to be a directly observed jump record.

Let $`P_k`$ denote the projection onto that subspace. The actual bath operators are the finite matrices

```math
H_E^{(k)}=P_kH_E^\infty P_k,
\qquad
B^{(k)}=P_kB^\infty P_k.
```

The device evolves under these matrices throughout the experiment. It does not perform projections or measurements during operation.

A small final probability above the cutoff would be insufficient: an amplitude can visit a removed state and return before the final time. The [occupation proof](../science/finite_bath.md) controls all such excursions. Pointwise positivity of the covariance bounds the omitted creation-and-annihilation paths by positive Wick sums. The resulting error obeys

```math
d_{\mathsf T}(\mathrm{finite},\mathrm{Gaussian})
\le E_k(\gamma T),
\qquad
E_k(J)=
\sum_{n=k+1}^{\infty}
\frac{\sqrt{(2n-1)!!}}{n!}J^{n/2}.
```

Here $`(2n-1)!!`$ is the product of the positive odd integers through $`2n-1`$. At fixed $`J`$, this series tail tends to zero as $`k`$ grows. The decisive feature is that the bound does not grow with the number or bandwidth of the modes.

### 5.3 Combine the errors before passing to operational limits

At $`\gamma T=1`$, choose

```math
m\ge\frac{6(2N+1)}{\epsilon},
\qquad
E_k(1)\le\frac{\epsilon}{2},
```

with integer $`m,k`$. The first choice makes the colored-noise error at most $`\epsilon/2`$; the second does the same for finite occupation. For every finite tester,

```math
d_{\mathsf T}(\mathrm{finite},\mathrm M)
\le\frac{3(2N+1)}{m}+E_k(1)
\le\epsilon.
```

This inequality compares the target directly with the actual finite device. It can then pass to the operational closure without assuming that a limiting tester also converges on the auxiliary infinite oscillator reference.

## 6. Read the three resources together

Fix $`0\lt\epsilon\lt1/64`$, $`N\ge1`$, and $`\gamma T=1`$. The [resource theorem](../science/resource_theorem.md) designs the bath for these parameters before the tester chooses its input, instruments, times, or outcomes. Its explicit bounds are

```math
D=\binom{4m-3+k}{k},
\qquad
\Lambda\le\gamma\sqrt{\frac{3km}{2}},
\qquad
W_E=2\pi k\gamma(m-1).
```

At fixed accuracy, $`k`$ is fixed while $`m`$ grows linearly with $`N`$. Thus one and the same device has

```math
Q=O_\epsilon(\log(N+2)),
\qquad
\Lambda=O_\epsilon(\gamma\sqrt N),
\qquad
W_E=O_\epsilon(\gamma N).
```

The notation $`O_\epsilon`$ allows a constant depending on accuracy but not on $`N`$. Changing $`N`$, $`\epsilon`$, or $`\gamma`$ may require a different device. The guarantee is uniform over testers for a chosen design.

Three distinct witnesses explain the necessary scales:

- **Memory:** a tester swaps fresh halves of entangled Bell pairs through the system and retains every output. A bath of dimension $`D`$ and initial rank $`r`$ can leave an accessible output of rank at most $`Dr\le D^2`$. The ideal outputs spread weight over more distinguishable directions as the number of intervals grows. The [memory proof](../science/memory_bound.md) turns this into $`Q=\Omega(\log(N+2))`$, including mixed baths.
- **Coupling:** bounded unitary dynamics gives quadratic short-time survival loss, whereas the target has a linear dissipative term. Repeated measurements expose that difference. The inherited [interaction-resolution bound](../science/dynamical_bounds.md) requires $`\Lambda=\Omega_\epsilon(\gamma\sqrt N)`$.
- **Bath width:** sign-reversing pulses can suppress a slowly varying bounded microscopic interaction while leaving the target generator unchanged. The rigorous decoupling argument yields the sum bound

```math
\frac{W_E}{2}+\Lambda
\gt\frac{\gamma(N+1)}{4e}.
```

The last bound is conditional information about bandwidth. When coupling is restricted to the optimal square-root order, it cannot supply the linear term for large $`N`$, so $`W_E=\Omega(\gamma N)`$ follows. If coupling is allowed to grow linearly or faster, the displayed inequality does not give a separate linear lower bound on bath width. The statement also relies on the specified autonomous $`Z`$-coupled Hamiltonian class.

## 7. Physical meaning and limits

The construction stores a bounded amount of occupation among an increasing number of possible modes. This separates the amount of retained activity from the resolution of where that activity can occur. It explains how logarithmic encoded memory can coexist with a frequency range growing linearly with the contact budget.

The encoded memory is a Hilbert-space count. It does not assert that a local laboratory implementation uses only that many physical oscillator modes or that its Hamiltonian has an efficient gate decomposition. Preparation, spatial locality, and compilation are separate implementation questions.

The constructed bath is initially pure and stationary under its free Hamiltonian. Its signed-frequency reference becomes a finite spectrum after truncation, and that spectrum can be shifted above zero. The vacuum remains an excited state after this shift. The theorem therefore does not supply a thermal or passive reservoir.

The error and resource orders concern a fixed observation horizon and fixed accuracy as $`N`$ grows. They do not establish indefinite reuse, sharp joint dependence on $`N`$ and vanishing error, general Lindblad dissipators, arbitrary coupling tensors, or coherent timing control. The [interpretation](../science/interpretation.md) connects these limits to the physical model.

## 8. Source and proof routes

The sole educational anchor is Rivas–Huelga. Its publisher chapter pages are [Chapter 3](https://link.springer.com/chapter/10.1007/978-3-642-23354-8_3), [Chapter 4](https://link.springer.com/chapter/10.1007/978-3-642-23354-8_4), and [Chapter 5](https://link.springer.com/chapter/10.1007/978-3-642-23354-8_5). The derivations and example on this page are supplied locally in the project's notation.

The [thirty milestones](milestones.md) organize the full conceptual route. The canonical research statements remain in [the model](../science/model.md), [the theorem](../science/resource_theorem.md), [the adaptive comparison](../science/adaptive_comparison.md), [the finite-bath construction](../science/finite_bath.md), [the memory proof](../science/memory_bound.md), and [the dynamical bounds](../science/dynamical_bounds.md).

Research citations have a different purpose from the educational anchor. The coupling converse is inherited from Markovian Resolution Limit; the spectral obstruction uses Uhrig–Lidar; Gaussian, dilation, and truncation arguments have the antecedents documented in [related work](../references/RELATED_WORK.md). That account also records unresolved source-comparison limits. The [bibliography](../references/references.bib) preserves their identities, and the [verification guide](../verification/README.md) explains the finite calculations and their distinction from the analytical proofs.
