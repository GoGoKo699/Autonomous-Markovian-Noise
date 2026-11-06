# Related work and scope of the contribution

This project studies one finite, autonomous reservoir that approximates a qubit dephasing process under interventions. The target is

```math
\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho),\qquad \gamma T=1.
```

The reservoir Hamiltonian has the form $`H=I\otimes H_E+Z\otimes B`$. The charged resources are its memory $`\log_2D`$, coupling $`\Lambda=\|B\|`$, and bath spectral diameter $`W_E`$. The device is fixed before the experimenter chooses a protocol. It has no externally switched interaction schedule or replenished reservoir.

At each fixed sufficiently small error, the [resource theorem](../science/resource_theorem.md) simultaneously attains logarithmic memory, square-root coupling, and linear bath spectral diameter as functions of the contact budget $`N`$. The comparison includes protected quantum memory, retained outcomes, and classically adaptive contact times, first for finite timing trees and then for their specified operational closure. The bandwidth converse is $`W_E/2+\Lambda=\Omega(\gamma N)`$ within the displayed Hamiltonian class. Linear bath bandwidth is therefore necessary when coupling has the optimal square-root order; it is not asserted independently of coupling.

The distinction from earlier work is this joint resource statement and the uniform estimates that establish it. Finite reservoir approximations, sparse excitation histories, Gaussian bath comparison, and dynamical-decoupling obstructions all have substantial antecedents.

## 1. Intervention resolution and the strength converse

The research repository [Markovian-Resolution-Limit, commit b4af5cfb7a86165f29d9cf1e9adcb74f5fe91a8b](https://github.com/GoGoKo699/Markovian-Resolution-Limit/tree/b4af5cfb7a86165f29d9cf1e9adcb74f5fe91a8b) is the direct source of the square-root interaction-strength law and the scheduled-collision construction used in the preceding formulation of this problem. Its [model](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/b4af5cfb7a86165f29d9cf1e9adcb74f5fe91a8b/science/model.md) permits predetermined time-dependent Hamiltonians, does not charge bath-only motion, and retains all collision partners supplied at time zero. It already includes the adaptive tester class. The present coupling lower bound is inherited from its survival-test argument. The additional restrictions here are autonomy and simultaneous accounting for reservoir dimension and spectral diameter. This is a research-repository antecedent, not a journal publication.

[Uhrig and Lidar, Physical Review A 82, 012301 (2010)](https://doi.org/10.1103/PhysRevA.82.012301), supply the other inherited obstruction. Their rigorous Uhrig dynamical-decoupling bound treats bounded pure-dephasing Hamiltonians $`I\otimes B_0+Z\otimes B_z`$, arbitrary bath states, and ideal instantaneous pulses. Its high-order remainder suppresses microscopic dephasing when the total norm is too small compared with the number of pulses. Markovian dephasing survives the same sign reversals. Applying that result after centering $`H_E`$ yields the bandwidth-plus-coupling lower bound used here. Neither the decoupling mechanism nor that obstruction is claimed as a new ingredient.

## 2. Discrete reservoirs and occupation cutoffs

[Trivedi, Malz, and Cirac, Physical Review Letters 127, 250404 (2021)](https://doi.org/10.1103/PhysRevLett.127.250404), prove convergence of discrete-mode approximations to non-Markovian baths. Their [full preprint](https://arxiv.org/html/2107.07196v2) treats arbitrary finite system dimension and time-dependent system Hamiltonians. Main-text Lemma 2 bounds the $`n`$-particle weight by a factorial tail; Theorems 2 and 3 concern pseudomode and chain approximations. Supplemental Lemma 5 explicitly compares full evolution with evolution under a projected Hamiltonian, including a boundary-coupling integral. Thus both sparse occupation and dynamical projection bounds are antecedents. Some of their estimates are independent of the system Hamiltonian and dimension, so enlargement by a tester memory must be considered rather than dismissed on terminology alone.

The comparison needed here concerns the dependence on bath bandwidth. Applying a particle tail and a boundary-coupling estimate directly can introduce the norm of the band-limited field, which grows with bandwidth. The [finite-bath proof](../science/finite_bath.md) instead bounds all omitted creation-and-annihilation histories, including excursions that return below the cutoff. For its pointwise nonnegative covariance, the resulting total-occupation error depends on the integrated covariance, not the increasing equal-time field variance. This permits a fixed total cutoff at fixed error while the number of modes increases with $`N`$.

[Woods, Cramer, and Plenio, Physical Review Letters 115, 130401 (2015)](https://doi.org/10.1103/PhysRevLett.115.130401), already establish certified bosonic-bath truncation. Their [full preprint](https://arxiv.org/pdf/1504.01531) gives a chain-length bound and, in Eqs. (12)–(18), a local Fock-space projection with a bound on the resulting dynamics. These results preclude a broad claim that a finite-dimensional bosonic reservoir with controlled error is itself new. Their local product cutoffs and computable truncation error do not state the fixed total-occupation, simultaneous resource estimate proved here.

Sparse records also appear in [Cleve and Wang's Lindblad-simulation algorithm](https://doi.org/10.4230/LIPIcs.ICALP.2017.17). Section 4.5 of the [extended paper](https://arxiv.org/html/1612.09512v3) compresses the positions of rare nontrivial operations. Such algorithmic compression is an antecedent to economical history storage. It does not by itself specify a single autonomous reservoir that remains available to an unknown intervention protocol.

## 3. Gaussian comparison and collision representations

[Mascherpa, Smirne, Huelga, and Plenio, Physical Review Letters 118, 100401 (2017)](https://doi.org/10.1103/PhysRevLett.118.100401), bound the effect of spectral-density changes in the spin-boson model. Equation (6) of their [full preprint](https://arxiv.org/pdf/1611.03377) controls observable error using an absolute time integral of the difference of bath correlations. This is an important predecessor for covariance-based error analysis. Applying such an absolute-variation estimate directly to a regular covariance and a white-noise delta covariance does not exploit the cancellation that makes the present approximation converge.

The [adaptive comparison](../science/adaptive_comparison.md) uses integrated interval covariances instead. Their difference is a negative weighted graph Laplacian plus boundary deficits. Phase derivatives vanish on branches without an intervening contact, and the remaining terms are weighted by the probability that a contact actually occurs. The estimate consequently counts the $`N`$ contacts on a realized branch, rather than the number of potential nodes in a timing tree. This is the particular uniformity needed for the resource theorem.

[Lacroix, Cilluffo, Huelga, and Plenio, Communications Physics 8, 268 (2025)](https://doi.org/10.1038/s42005-025-02201-2), connect exact collision representations and bath sampling; the [preprint](https://arxiv.org/html/2411.13166v2) discusses a Nyquist condition, local Hilbert-space truncation, and correlation-function error. These are relevant antecedents for mode selection and collision representations.

[Christensen, Agerskov, and Nathan, Physical Review A 114, 042422 (2026)](https://doi.org/10.1103/dc52-844x), develop an ancilla-train simulation algorithm. The [full paper](https://journals.aps.org/pra/pdf/10.1103/dc52-844x) uses Gaussian/Wick comparisons, shifted coupling pulses, oscillator-to-qubit truncation, and ancilla reuse. Bounds uniform in a system Hamiltonian can potentially transfer to an enlarged controlled system. Their presentation as a simulation algorithm or an endpoint estimate is therefore not, by itself, a separation from controlled-process approximation. The distinction established here is the explicitly autonomous finite device, a total occupation cap, and the simultaneous dimension, coupling, and bath-width accounting.

## 4. Autonomous dilations and intervention-sensitive dynamics

[Burgarth, Facchi, Lonigro, and Modi, Physical Review A 104, L050404 (2021)](https://doi.org/10.1103/PhysRevA.104.L050404), exhibit non-Markovian dynamics that remain hidden from interventions within a finite observation window. The [construction](https://arxiv.org/html/2108.05750v1) uses a translation reservoir and singular point couplings. Exact agreement of controlled finite-window statistics is consequently an antecedent; finite resource bounds are a separate question.

[Burgarth, Facchi, and Hillier, Annales Henri Poincaré 24, 325–347 (2023)](https://doi.org/10.1007/s00023-022-01211-y), show that dilations of the same reduced noise can respond differently to control. Their [full article](https://link.springer.com/article/10.1007/s00023-022-01211-y) includes an autonomous construction using an unbounded clock generator and a point-localized clock state. Autonomy alone, or sensitivity to dynamical decoupling alone, therefore does not describe the contribution here.

## 5. Recent closely related preprints and comparison limits

Three September 2026 preprints are particularly relevant. The comparisons below are limited to their primary indexed abstracts and verified bibliographic records. Their full texts could not be retrieved for this review; absence of a result from an abstract is not evidence that the paper lacks it.

| Source | Relevant result reported in the abstract | What remains unverified |
|---|---|---|
| [Douglas, “Bath dimension and initial entropy for closed repeated use of a quantum channel,” arXiv:2609.18267](https://arxiv.org/abs/2609.18267) | Dimension/entropy rates for closed repeated use of a fixed channel, with adaptive users and all ancillary resources counted. | One-shot estimates uniform in the weak-channel limit, and their possible implications for the memory converse or compression used here. |
| [Kitchen, “Causal Query Compression for Lindblad Dynamics: Optimal Queries and Nearly Linear Local Simulation,” arXiv:2609.31312](https://arxiv.org/abs/2609.31312) | Causal compression, factorial history tails, Lindblad simulation, and resource accounting for adaptive protocols. | Whether its compiler or lower bounds imply a finite autonomous reservoir with the present coupling and bath-width budgets. |
| [Fuksa, Wassner, Eisert, and White, “Dilation theorem for continuum quantum stochastic processes,” arXiv:2609.35403](https://arxiv.org/abs/2609.35403) | Approximation of continuum quantum processes by explicit closed bounded-Hamiltonian representatives. | The topology and quantifiers of the approximation, and quantitative bounds jointly controlling $`D,\Lambda,W_E`$ uniformly over an $`N`$-contact tester class. |

These unresolved comparisons limit any broad priority claim. In particular, the present account does not claim novelty for closed-use compression, general continuum dilation, or factorial rare-history tails in isolation.

## 6. What the theorem adds, and what it does not address

The supported contribution is a quantitative autonomous construction in which two uniform estimates work together: the contact-count Gaussian comparison and the bandwidth-independent total-occupation projection bound. They produce one finite device attaining the memory and coupling orders, together with the bath-width order required at optimal coupling. The lower-bound ingredients have been attributed above.

The construction uses symmetric positive and negative mode frequencies before finite-dimensional projection. After shifting the energy origin, its initial stationary state need not be a ground or thermal state. No claim is made for a passive thermal reservoir, spatial locality, economical synthesis of the encoded Hamiltonian, coherent superpositions of contact times, uncharged continuous monitoring, or optimal dependence on the requested error.

Mathematical background includes [Nelson's analytic-vector criterion](https://doi.org/10.2307/1970331) for self-adjointness and [Voigtlaender's generalized Price theorem](https://doi.org/10.1007/s10959-020-01017-w) for differentiation with respect to Gaussian covariance.

Bibliographic data are collected in [references.bib](references.bib). Source access and comparison were last checked on 6 November 2026.
