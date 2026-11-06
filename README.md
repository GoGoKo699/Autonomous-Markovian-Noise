# Autonomous Markovian Noise

**How large and how fast must a finite autonomous environment be to imitate memoryless noise under interventions?** This project answers that question for qubit dephasing over the fixed horizon $`T=1/\gamma`$. A family of closed autonomous baths attains logarithmic memory, square-root interaction strength and linear spectral width as the number of allowed interventions increases.

The target generator and observation horizon are

```math
\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho),\qquad T=\gamma^{-1}.
```

The simulator has a finite bath and one time-independent Hamiltonian

```math
H=I\otimes H_E+Z\otimes B.
```

It is tested by at most $`N`$ instantaneous contacts with the qubit, arbitrary protected quantum memory, and classically adaptive instruments and contact times. All outcomes are included in the comparison. The bath is chosen independently of the tester and operates without resets, incoming ancillas or an external switching schedule.

## Principal result

For every fixed accuracy $`0\lt\epsilon\lt1/64`$ and each $`N\ge1`$, a device chosen for that budget achieves the following bounds simultaneously. Error is the supremum difference in final-event probabilities over the declared tester class; for finite testers this equals the supremum final half trace distance.

| Resource | Achievable order | Necessary order and scope |
|---|---|---|
| Encoded bath qubits, $`\lceil\log_2 D\rceil`$ | $`O_\epsilon(\log(N+2))`$ | $`\Omega(\log(N+2))`$, including initially mixed closed baths |
| Interaction strength, $`\Lambda=\lVert B\rVert`$ | $`O_\epsilon(\gamma\sqrt N)`$ | $`\Omega_\epsilon(\gamma\sqrt N)`$; inherited from the intervention-resolution bound |
| Bath spectral diameter, $`W_E`$ | $`O_\epsilon(\gamma N)`$ | $`\Omega(\gamma N)`$ when $`\Lambda=O_\epsilon(\gamma\sqrt N)`$, in the displayed pure-dephasing interaction class |

The unrestricted spectral obstruction proved here is the sum bound

```math
\frac{W_E}{2}+\Lambda\gt\frac{\gamma(N+1)}{4e},\qquad N\ge1.
```

Thus linear bath width is necessary at the optimal square-root coupling scale. A separate linear width lower bound at arbitrary coupling is not asserted. The [exact resource theorem](science/resource_theorem.md) gives the construction, constants and quantifiers.

## Why the construction works

A positive finite Fourier kernel approximates white phase noise. Its narrow correlation peak requires more frequencies as the tester gains finer access. A fixed total-occupation sector of those modes stores the relevant histories, so the number of modes can grow linearly while the encoded memory grows logarithmically.

Two estimates make this intuition a controlled-process result. The [Gaussian comparison](science/adaptive_comparison.md) charges an error to contacts that actually occur along each adaptive record, rather than to every branch of a timing tree. The [finite-bath construction](science/finite_bath.md) bounds all excursions beyond an occupation cutoff, including paths that subsequently return. That bound is independent of the kernel bandwidth and applies to the actual projected Hamiltonian.

The strength lower bound is an established result of [Markovian Resolution Limit](https://github.com/GoGoKo699/Markovian-Resolution-Limit). The spectral obstruction follows from the rigorous Uhrig–Lidar dynamical-decoupling estimate. Gaussian dilations, discrete modes, Wick expansions and sparse occupation are established ingredients. The [related-work account](references/RELATED_WORK.md) identifies what is inherited and the role of the two uniform estimates in attaining the joint autonomous resource bounds.

## Read the science

| Question | Reading route |
|---|---|
| What is a contact, and what error is controlled? | [Model and tester class](science/model.md) |
| What exactly is attained and what is optimal? | [Resource theorem](science/resource_theorem.md) |
| How can contact times depend on earlier measurement outcomes? | [Adaptive Gaussian comparison](science/adaptive_comparison.md) |
| What is the actual finite Hamiltonian? | [Finite autonomous bath](science/finite_bath.md) |
| Why must the bath retain a growing record? | [Memory converse](science/memory_bound.md) |
| Why must coupling and spectrum grow? | [Dynamical bounds](science/dynamical_bounds.md) |
| What do the resources mean physically? | [Interpretation and limits](science/interpretation.md) |
| Which ingredients are prior results? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| How can the finite calculations be reproduced? | [Verification](verification/README.md) |

The [reading guide](llms.txt) maps these routes to the authoritative statements.

## Learn the project

The educational anchor is Ángel Rivas and Susana F. Huelga, [*Open Quantum Systems: An Introduction*](https://link.springer.com/book/10.1007/978-3-642-23354-8), first edition (2012). Chapters 3–5 supply the foundations in dynamical maps, Markovian generators and microscopic open-system models.

Start with the [source-to-project bridge](learning/bridge.md), which explains how those foundations lead to intervention-based testing and the three resource costs. The [30-milestone map](learning/milestones.md) connects the necessary background to the construction, lower bounds and physical interpretation. It is a map of the project's ideas; the topic pages above remain the authoritative homes of the statements and proofs.

## Reproduce the finite checks

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The checks compare finite projected Hamiltonians with exact Gaussian path sums. They retain a quantum reference, noncommuting controls, measurement outcomes and feedback-dependent contact times. They also check the kernel and occupation-tail estimates. Floating-point tests support the implementation and finite examples; the universal claims are established in the proofs.

## Scope

The result concerns one fixed observation horizon and fixed accuracy as $`N`$ grows. The engineered bath is stationary under its free Hamiltonian but nonthermal and nonpassive. The construction permits global matrices, so encoded memory is not a bound on local hardware, gate complexity or preparation cost. The bandwidth converse uses the pure-dephasing interaction form displayed above. General Lindblad generators, thermal baths, coherent control of contact times and the sharp joint accuracy–resolution frontier are outside the established theorem.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
