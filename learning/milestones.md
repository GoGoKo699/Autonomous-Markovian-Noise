# Thirty milestones for Autonomous Markovian Noise

[Project overview](../README.md) · [Source-to-project bridge](bridge.md) · [Exact theorem](../science/resource_theorem.md)

This map follows one scientific question: how can a finite, closed, autonomous bath imitate a memoryless dephasing process when an experimenter can repeatedly intervene? Its thirty understanding targets connect the basic objects to the construction, the three resource restrictions, and their physical meaning. They do not replace the detailed proofs or cover every technical lemma.

## Anchor and allocation

The single educational anchor is Ángel Rivas and Susana F. Huelga, [*Open Quantum Systems: An Introduction*, first edition, ©2012][RH]. The selected chapter-level pointers are:

- **RH3:** [Chapter 3, “Time Evolution in Open Quantum Systems”][RH3].
- **RH4:** [Chapter 4, “Quantum Markov Process: Mathematical Structure”][RH4].
- **RH5:** [Chapter 5, “Microscopic Description: Markovian Case”][RH5].

The anchor supplies the open-system, dynamical-map, Markovian, and microscopic language. The [bridge](bridge.md) translates it into this project's conventions and supplies local explanations. The repository's science pages contain the controlled-process arguments and resource theorem; the [research references](../references/RELATED_WORK.md) identify imported proof ingredients. Chapter pointers below are at the published chapter level, without assigning unverified subsection numbers.

**M01–M13 are background/preliminaries; M14–M30 are narrative/innovation.** Thirteen background milestones are needed because the problem joins reduced quantum states, reference-assisted interventions, Gaussian correlations, and several different physical resource measures. Seventeen narrative milestones then build the two uniform approximation estimates, assemble one autonomous device, establish the three converses, and interpret the combined result. This allocation follows the project's argument rather than the textbook's chapter count.

Each phase runs from local objects and mechanisms to a global synthesis. The phase boundary is M13's complete formulation of the task. The final synthesis is M30.

## Background/preliminaries — M01–M13

### M01 — Qubit coherence

- **Phase:** Background/preliminaries.
- **Central question:** What changes when a qubit loses phase coherence?
- **Understanding target:** Distinguish populations from off-diagonal coherences in a density matrix. Explain how a $`Z`$ rotation changes relative phase and how averaging phases can reduce coherence while preserving populations.
- **Dependencies and story role:** Entry point. Establishes the local system and the observable effect that the simulator must reproduce.
- **Conceptual connection:** Connects a concrete qubit experiment to the distinction between a reversible phase rotation and a dephasing channel.
- **Source pointers:** [RH3]; [bridge](bridge.md); [model, “Target and simulator”](../science/model.md#target-and-simulator).

### M02 — Reduced states from closed dynamics

- **Phase:** Background/preliminaries.
- **Central question:** How can a closed unitary evolution produce mixed reduced states?
- **Understanding target:** Explain the roles of the tensor product, system–bath correlations, and partial trace. Distinguish a pure joint state from a pure subsystem state and identify the initially independent state $`\rho_{SR}\otimes\omega_E`$ used here.
- **Dependencies and story role:** Depends on M01. Adds the environment while keeping the local system's measured output in view.
- **Conceptual connection:** Connects ordinary open-system dynamics to the requirement that this simulator retain its entire bath rather than replace it between observations.
- **Source pointers:** [RH3]; [bridge](bridge.md); [model, “Target and simulator”](../science/model.md#target-and-simulator).

### M03 — Channels and protected references

- **Phase:** Background/preliminaries.
- **Central question:** Why must a noise model remain valid when the qubit is entangled with another register?
- **Understanding target:** Interpret a completely positive trace-preserving map as an evolution compatible with a protected reference. Explain why checking selected unentangled inputs is weaker than the input-uniform comparison required by the project.
- **Dependencies and story role:** Depends on M02. Extends the local state description to a physical input–output rule.
- **Conceptual connection:** Connects dynamical maps to entangled probes, arbitrary tester memory, and the Bell-pair witness used later.
- **Source pointers:** [RH3]; [model, “Testers and the contact budget”](../science/model.md#testers-and-the-contact-budget); [memory bound, “A swap-only tester archives independent ideal outputs”](../science/memory_bound.md#2-a-swap-only-tester-archives-independent-ideal-outputs).

### M04 — The Markov target and its rate convention

- **Phase:** Background/preliminaries.
- **Central question:** What does the dephasing generator prescribe between successive contacts?
- **Understanding target:** Connect the semigroup rule to
  $`\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho)`$ and
  $`p_t=(1-e^{-2\gamma t})/2`$ in the channel
  $`(1-p_t)\rho+p_tZ\rho Z`$. Keep the coherence decay $`e^{-2\gamma t}`$ distinct from the chosen horizon $`T=1/\gamma`$.
- **Dependencies and story role:** Depends on M01 and M03. Fixes the ideal local evolution before comparing entire experiments.
- **Conceptual connection:** Connects a Markov generator with the project's calibrated noise scale and prevents a factor-of-two change of convention.
- **Source pointers:** [RH4]; [bridge](bridge.md); [model, “Target and simulator”](../science/model.md#target-and-simulator).

### M05 — Instruments and recorded outcomes

- **Phase:** Background/preliminaries.
- **Central question:** What mathematical object describes an intervention that both changes a state and produces an outcome?
- **Understanding target:** Treat each instrument outcome as a completely positive subnormalized branch, with its trace giving its probability. Explain why the complete instrument preserves total probability and why renormalizing only successful branches changes the comparison.
- **Dependencies and story role:** Depends on M02 and M03. Introduces the elementary operation from which the experimenter's policy is assembled.
- **Conceptual connection:** Connects the language of dynamical maps to measurements, feedback, and the positive branch outputs used in the adaptive proof.
- **Source pointers:** [RH3] for the map framework; [bridge](bridge.md) for the project-specific intervention description; [model, “Testers and the contact budget”](../science/model.md#testers-and-the-contact-budget).

### M06 — Classical timing and a structural contact budget

- **Phase:** Background/preliminaries.
- **Central question:** What may the experimenter adapt, and what counts as access to the qubit?
- **Understanding target:** Describe a finite classical policy tree with at most $`N`$ declared system contacts on every history. Distinguish free memory-only processing from system access, including contacts whose outcomes happen to leave the qubit unchanged. Keep classically chosen times separate from coherent superpositions of times.
- **Dependencies and story role:** Depends on M05. Assembles individual instruments into the precise controller allowed by the theorem.
- **Conceptual connection:** Connects causal feedback to the resource being varied: the number of opportunities to interrogate the system, rather than the number of possible branches.
- **Source pointers:** [model, “Testers and the contact budget”](../science/model.md#testers-and-the-contact-budget); [adaptive comparison, “Conventions and statement”](../science/adaptive_comparison.md#1-conventions-and-statement).

### M07 — Operational distinguishability

- **Phase:** Background/preliminaries.
- **Central question:** What does it mean for two devices to agree on an experiment?
- **Understanding target:** Interpret half trace distance as the largest final-event probability gap for finite outputs. Explain why protected quantum registers and classical records remain part of the output. Understand that operational limits are defined through event probabilities, without presuming a common limiting quantum-output state.
- **Dependencies and story role:** Depends on M03, M05, and M06. Supplies the error criterion for the complete controlled experiment.
- **Conceptual connection:** Connects state comparison to observable experimental decisions and to the later passage from finite trees to the specified operational closure.
- **Source pointers:** [model, “Distance and operational closure”](../science/model.md#distance-and-operational-closure); [bridge](bridge.md); [adaptive comparison, Section 8](../science/adaptive_comparison.md#8-passing-the-finite-device-result-to-the-operational-closure).

### M08 — A channel is not a controlled process

- **Phase:** Background/preliminaries.
- **Central question:** Why can two models agree at one final time and disagree after an intervention?
- **Understanding target:** Distinguish an uninterrupted reduced channel from the rule producing all multitime outcomes. Explain how a retained bath can affect later behavior even when an earlier reduced channel matches the target.
- **Dependencies and story role:** Depends on M04, M06, and M07. Combines local dynamics, interventions, and error into the global object being approximated.
- **Conceptual connection:** Connects the anchor's open-system framework to the project's stronger demand of uniform agreement under unknown control policies.
- **Source pointers:** [RH3] and [RH4]; [bridge](bridge.md); [model, “The question”](../science/model.md#the-question); [interpretation, “What repeated access detects”](../science/interpretation.md#what-repeated-access-detects).

### M09 — Autonomy and three different resources

- **Phase:** Background/preliminaries.
- **Central question:** Which physical resources belong to the simulator?
- **Understanding target:** Explain the fixed Hamiltonian $`H=I\otimes H_E+Z\otimes B`$ and distinguish encoded memory $`Q=\lceil\log_2D\rceil`$, interaction strength $`\Lambda=\|B\|`$, and free-bath spectral diameter $`W_E`$. A shift of the bath's energy origin changes none of its dynamics or width.
- **Dependencies and story role:** Depends on M02 and M08. Adds the resource accounting needed to turn process approximation into a quantitative problem.
- **Conceptual connection:** Connects a microscopic system–bath model to closed operation without resets, incoming ancillas, or external switching, while keeping encoded size separate from local hardware cost.
- **Source pointers:** [RH5] for microscopic context; [model, “Charged resources”](../science/model.md#charged-resources); [interpretation](../science/interpretation.md).

### M10 — Correlations and two kinds of positivity

- **Phase:** Background/preliminaries.
- **Central question:** What information does a bath covariance contain?
- **Understanding target:** Interpret $`K(t-s)`$ as a two-time correlation and distinguish independent white increments from a correlated field. Separate positive semidefinite covariance matrices from the additional condition $`K(u)\ge0`$ at every lag; the project uses both for different reasons.
- **Dependencies and story role:** Depends on M04 and M09. Introduces the local time-correlation object from which the reference bath will be designed.
- **Conceptual connection:** Connects microscopic correlation functions with the cancellation and positivity properties needed for controlled error bounds.
- **Source pointers:** [RH5]; [bridge](bridge.md); [finite bath, “A finite positive covariance”](../science/finite_bath.md#1-a-finite-positive-covariance); [adaptive comparison, Section 3](../science/adaptive_comparison.md#3-positive-covariances-have-a-useful-difference-decomposition).

### M11 — Gaussian phase noise

- **Phase:** Background/preliminaries.
- **Central question:** How does a Gaussian phase distribution reproduce the specified dephasing channel?
- **Understanding target:** Relate the rotation $`e^{-iZ\varphi}`$ to the Gaussian characteristic function. A phase variance $`\gamma h`$ gives coherence factor $`e^{-2\gamma h}`$. Understand why a correlated experiment requires the joint distribution of all interval phases.
- **Dependencies and story role:** Depends on M01, M04, and M10. Provides the exact noise representation used in the comparison argument.
- **Conceptual connection:** Connects the dephasing generator to covariance matrices without replacing a colored process by independent interval channels.
- **Source pointers:** [bridge](bridge.md); [adaptive comparison, Sections 1 and 7](../science/adaptive_comparison.md); [finite bath, “Commuting fields and the complete Gaussian process”](../science/finite_bath.md#commuting-fields-and-the-complete-gaussian-process).

### M12 — Truncating states versus truncating dynamics

- **Phase:** Background/preliminaries.
- **Central question:** Why does a small final high-occupation probability not justify deleting high-occupation states from a Hamiltonian?
- **Understanding target:** Interpret a mode-occupation basis, a total-number projector, and a time-ordered sequence of interaction events. Explain how the interaction expansion can include excursions that leave a retained subspace and return, changing its final low-occupation amplitudes.
- **Dependencies and story role:** Depends on M02, M09, and M10. Introduces the approximation issue that a genuinely finite bath must solve.
- **Conceptual connection:** Connects Hilbert-space compression with a dynamical error bound, rather than a postselected or renormalized state approximation.
- **Source pointers:** [interpretation, “Why the finite projection needs a dynamical proof”](../science/interpretation.md#why-the-finite-projection-needs-a-dynamical-proof); [finite bath, Sections 3 and 4](../science/finite_bath.md).

### M13 — The complete simulation task

- **Phase:** Background/preliminaries.
- **Central question:** What is fixed, what grows, and which choices must one device withstand?
- **Understanding target:** Assemble the model at fixed $`\gamma T=1`$ and fixed $`0\lt\epsilon\lt1/64`$. For each $`N\ge1`$, a device may be designed for that budget and accuracy, then must work for every admitted tester. Identify the three simultaneous upper bounds and the separate necessity questions.
- **Dependencies and story role:** Integrates M01–M12. Completes the background phase by formulating the global task and its quantifiers.
- **Conceptual connection:** Connects textbook open-system notions to this project's finite-resource, autonomous, controlled-process problem.
- **Source pointers:** [bridge](bridge.md); [model](../science/model.md); [resource theorem, “Statement” and “Quantifiers and limitations”](../science/resource_theorem.md).

## Narrative/innovation — M14–M30

### M14 — A positive finite Fourier kernel

- **Phase:** Narrative/innovation.
- **Central question:** How can finitely many frequencies approximate white phase noise while retaining the positivity needed by both proofs?
- **Understanding target:** Explain why the squared finite Fourier sum defining the Jackson kernel has nonnegative Fourier coefficients and nonnegative values. Track its period $`L=4T`$, periodic mass $`\gamma`$, and first moment $`\mu_m`$, which decreases with the number of frequencies.
- **Dependencies and story role:** Depends on M10, M11, and M13. Starts the construction with the local scalar object that controls its accuracy.
- **Conceptual connection:** Connects correlation design to an exact finite mode representation, without treating a numerical Fourier discretization as the proof.
- **Source pointers:** [finite bath, Section 1](../science/finite_bath.md#1-a-finite-positive-covariance); [resource theorem, “Proof of the approximation”](../science/resource_theorem.md#proof-of-the-approximation).

### M15 — An autonomous commuting-field reference

- **Phase:** Narrative/innovation.
- **Central question:** How do signed oscillator frequencies realize the Gaussian phase process with a time-independent Hamiltonian?
- **Understanding target:** Explain how symmetric positive and negative frequencies produce commuting field observables with covariance $`K_m`$. Distinguish this infinite Fock-space proof reference from the final finite device, and stationarity of its vacuum under the free bath Hamiltonian from being a ground state.
- **Dependencies and story role:** Depends on M02, M10, M11, and M14. Realizes the designed covariance as a microscopic autonomous model.
- **Conceptual connection:** Connects the microscopic perspective of [RH5] with an exact controlled Gaussian representation; the signed-mode construction and its mathematical justification are supplied locally.
- **Source pointers:** [finite bath, Section 2](../science/finite_bath.md#2-the-gaussian-oscillator-reference); [bridge](bridge.md).

### M16 — One phase circuit for an adaptive timing tree

- **Phase:** Narrative/innovation.
- **Central question:** How can many possible contact schedules be represented without charging every possible time as a contact?
- **Understanding target:** Form the union grid of a finite policy's candidate times while retaining the actual contact set on each history. Explain why memory-only maps commute with the system's interval rotation and why each phase occurs once in the resulting circuit.
- **Dependencies and story role:** Depends on M05, M06, M07, and M15. Establishes the local representation needed for the adaptive comparison.
- **Conceptual connection:** Connects classically adaptive timing with a fixed operator-valued function of interval phases, without giving the tester access to hidden history copies.
- **Source pointers:** [adaptive comparison, Section 2](../science/adaptive_comparison.md#2-one-deterministic-grid-represents-a-finite-timing-tree); [model, “Testers and the contact budget”](../science/model.md#testers-and-the-contact-budget).

### M17 — Covariance differences as contact-spanning terms

- **Phase:** Narrative/innovation.
- **Central question:** Which structure in the colored-versus-white covariance difference makes a contact-based bound possible?
- **Understanding target:** Explain the decomposition into a negative weighted graph Laplacian and nonnegative boundary deficits. Recognize why an off-diagonal covariance connects two intervals and why the first moment bounds the total covariance crossing one time cut.
- **Dependencies and story role:** Depends on M10, M14, and M16. Converts the kernel's scalar positivity into the algebra used to compare entire experiments.
- **Conceptual connection:** Connects covariance cancellation to the temporal placement of interventions; bounding the two covariances separately would lose this structure.
- **Source pointers:** [adaptive comparison, Section 3](../science/adaptive_comparison.md#3-positive-covariances-have-a-useful-difference-decomposition); [finite bath, “First moment and integrated covariance”](../science/finite_bath.md#first-moment-and-integrated-covariance).

### M18 — The causal first-contact event

- **Phase:** Narrative/innovation.
- **Central question:** Why is the probability of making a first contact independent of phases that have not yet been observed through system access?
- **Understanding target:** Define the event of a policy-declared contact between two phase intervals. Explain why its probability is independent of the first distinguished phase by memory-only commutation, and of the second by causality. Distinguish this event from postselection on a system-measurement outcome.
- **Dependencies and story role:** Depends on M03, M05, M06, and M16. Supplies the load-bearing causal statement behind the adaptive error estimate.
- **Conceptual connection:** Connects no signalling to protected memory with a quantitative bound that remains valid on entangled inputs and feedback-dependent timing trees.
- **Source pointers:** [adaptive comparison, Section 4](../science/adaptive_comparison.md#4-a-first-contact-event-has-phase-independent-probability); [interpretation, “How classical timing enters the result”](../science/interpretation.md#how-classical-timing-enters-the-result).

### M19 — A Gaussian error charged to actual contacts

- **Phase:** Narrative/innovation.
- **Central question:** How do local phase derivatives become a global error proportional to $`N`$ rather than the timing tree's size?
- **Understanding target:** Connect the inactive phase-sum identity, positive active branches, parameter shifts, and Gaussian covariance interpolation. Explain why all activity probabilities come from one interpolated experiment and why their weighted sum is charged to contacts on each actual history.
- **Dependencies and story role:** Depends on M17 and M18. Completes the first uniform estimate: finite-tree Gaussian-versus-Markov error at most $`(2N+1)\mu_m`$.
- **Conceptual connection:** Connects a causal event probability with a trace-norm derivative bound and then with the complete experimental output.
- **Source pointers:** [adaptive comparison, Sections 5–7](../science/adaptive_comparison.md); [resource theorem, “Proof of the approximation”](../science/resource_theorem.md#proof-of-the-approximation).

### M20 — The actual finite Hamiltonian

- **Phase:** Narrative/innovation.
- **Central question:** What finite physical device replaces the infinite Gaussian reference?
- **Understanding target:** Define the bath as the subspace of total occupation at most $`k`$ and its Hamiltonian using $`P_kH_EP_k`$ and $`P_kBP_k`$. Explain why there is no measurement or projection during operation and why number-preserving free motion gives the correct compressed interaction picture.
- **Dependencies and story role:** Depends on M09, M12, and M15. Specifies the autonomous device whose resources will be counted.
- **Conceptual connection:** Connects an analytical reference model to a finite Hermitian matrix initialized once, without a supply of fresh bath systems.
- **Source pointers:** [finite bath, Section 4](../science/finite_bath.md#4-compressing-the-hamiltonian-to-a-fixed-occupation-sector); [model, “Target and simulator”](../science/model.md#target-and-simulator).

### M21 — Deleted paths and positive Wick contractions

- **Phase:** Narrative/innovation.
- **Central question:** What makes the difference between full and compressed evolution controllable?
- **Understanding target:** Explain how total-number compression deletes precisely creation–annihilation patterns that exceed $`k`$ at an intermediate step. Understand why their vacuum overlaps form a subset of nonnegative Wick contributions when $`K_m`$ is real and pointwise nonnegative.
- **Dependencies and story role:** Depends on M10, M12, M15, and M20. Identifies the local positivity mechanism for the second approximation estimate.
- **Conceptual connection:** Connects excursions in occupation space with scalar overlap inequalities; the argument does not assume operator monotonicity of projected Hamiltonians.
- **Source pointers:** [finite bath, “Deleted ladder paths have positive overlaps”](../science/finite_bath.md#deleted-ladder-paths-have-positive-overlaps); [interpretation, “Why the finite projection needs a dynamical proof”](../science/interpretation.md#why-the-finite-projection-needs-a-dynamical-proof).

### M22 — A truncation error independent of bandwidth

- **Phase:** Narrative/innovation.
- **Central question:** Why can the occupation cutoff remain fixed while the number and bandwidth of modes grow?
- **Understanding target:** Follow how the positive Wick moment and ordered-time integrals bound the Dyson tail by $`E_k(J)`$, with $`J\le\gamma T`$. Explain why a fixed error at $`\gamma T=1`$ permits a cutoff depending on accuracy but not on $`N`$, mode count, or the tester's memory.
- **Dependencies and story role:** Depends on M16 and M21. Completes the dynamical comparison between the Gaussian reference and the actual finite device.
- **Conceptual connection:** Connects local deleted-path positivity to a uniform full-output error bound that includes returning excursions and arbitrary finite adaptive controls.
- **Source pointers:** [finite bath, “The excursion error is independent of bandwidth” and Section 5](../science/finite_bath.md); [resource theorem, “Explicit upper parameters”](../science/resource_theorem.md#explicit-upper-parameters).

### M23 — Combining errors and counting one device

- **Phase:** Narrative/innovation.
- **Central question:** How do the two uniform estimates produce the three resource bounds for the same autonomous bath?
- **Understanding target:** Choose $`k`$ for the occupation error and $`m`$ proportional to $`N/\epsilon`$ for the Gaussian comparison. Relate $`M=4m-3`$ and $`D=\binom{M+k}{k}`$ to encoded memory, interaction norm, and free-bath width. Combine the finite-tree bounds before passing final-event inequalities to the operational closure.
- **Dependencies and story role:** Depends on M14, M19, M20, and M22. Integrates the construction into a global upper theorem.
- **Conceptual connection:** Connects separate analytical comparisons to simultaneous physical resources, without assuming convergence for the infinite reference in the closure definition.
- **Source pointers:** [resource theorem, “Explicit upper parameters” and “Proof of the approximation”](../science/resource_theorem.md); [finite bath, Section 5](../science/finite_bath.md#5-explicit-choices-and-finite-resources); [adaptive comparison, Section 8](../science/adaptive_comparison.md#8-passing-the-finite-device-result-to-the-operational-closure).

### M24 — Why a closed bath needs growing memory

- **Phase:** Narrative/innovation.
- **Central question:** What can stored weak-noise outputs reveal about the bath's dimension?
- **Understanding target:** Explain the tester with $`N`$ swaps and $`N+1`$ Bell outputs. Track the pre-readout output rank bound $`Dr`$, where $`r`$ is initial bath rank, and hence $`D^2`$ for a general mixed bath. Relate it to the ideal product spectrum and a permitted device-dependent final support measurement.
- **Dependencies and story role:** Depends on M03, M04, M07, M09, and M23. Supplies the first converse for the global resource claim.
- **Conceptual connection:** Connects system–bath entanglement and mixedness to an operational memory lower bound while retaining every tester register.
- **Source pointers:** [memory bound](../science/memory_bound.md); [resource theorem, “Memory necessity”](../science/resource_theorem.md#memory-necessity).

### M25 — Why the interaction must strengthen

- **Phase:** Narrative/innovation.
- **Central question:** How do repeated survival measurements distinguish bounded microscopic motion from the target's short-time noise?
- **Understanding target:** Compare quadratic survival loss under a bounded Hamiltonian with the Markovian linear short-time loss. Explain the complete all-success record, its contact count, and the resulting square-root interaction lower bound, which allows arbitrary conditional bath states.
- **Dependencies and story role:** Depends on M04, M06, M07, and M23. Supplies the interaction converse and identifies it as inherited rather than a new mechanism.
- **Conceptual connection:** Connects time resolution with the norm of system-affecting dynamics; the witness applies to a broader class than autonomous pure-dephasing baths.
- **Source pointers:** [dynamical bounds, Section 1](../science/dynamical_bounds.md#1-coupling-the-inherited-survival-witness); [related work, Section 1](../references/RELATED_WORK.md#1-intervention-resolution-and-the-strength-converse).

### M26 — Why bandwidth matters at small interaction strength

- **Phase:** Narrative/innovation.
- **Central question:** Why does a slowly varying autonomous bath fail under sufficiently many sign-reversal pulses?
- **Understanding target:** Explain why $`X`$ pulses reverse the microscopic $`Z\otimes B`$ interaction while preserving the Markov dephasing generator. Connect the inherited UDD remainder bound, spectrum centering, and the sum obstruction
  $`W_E/2+\Lambda\gt\gamma(N+1)/(4e)`$ in the stated accuracy range.
- **Dependencies and story role:** Depends on M04, M06, M09, and M25. Supplies the third converse with its required interaction-class restriction.
- **Conceptual connection:** Connects bath spectral variation to resistance against control. A separate linear lower bound on $`W_E`$ follows at square-root coupling; it is not established for unrestricted coupling.
- **Source pointers:** [dynamical bounds, Section 2](../science/dynamical_bounds.md#2-autonomous-bath-width-from-an-existing-udd-theorem); [resource theorem, “Interaction and spectral necessity”](../science/resource_theorem.md#interaction-and-spectral-necessity).

### M27 — The joint resource hierarchy

- **Phase:** Narrative/innovation.
- **Central question:** In what precise sense does the construction attain the necessary resource orders simultaneously?
- **Understanding target:** Combine the upper theorem and the three converses at fixed accuracy and $`\gamma T=1`$. Explain logarithmic encoded memory and square-root coupling, then the conditional linear width requirement at that coupling scale. Keep a device family indexed by $`N`$ distinct from one fixed device serving unbounded contact budgets.
- **Dependencies and story role:** Integrates M23–M26. States the complete mathematical result after both sufficiency and necessity have been established.
- **Conceptual connection:** Connects economical storage, rapid system response, and bath frequency range as different resources of the same physical simulator.
- **Source pointers:** [resource theorem](../science/resource_theorem.md); [interpretation, “Why bath width is an additional resource”](../science/interpretation.md#why-bath-width-is-an-additional-resource).

### M28 — Foundations, imported results, and the contribution

- **Phase:** Narrative/innovation.
- **Central question:** Which parts of the argument are established ingredients, and what combination is the project's supported contribution?
- **Understanding target:** Distinguish the selected textbook foundations from research-level proof dependencies. Attribute the survival and UDD converses, Gaussian representations, and earlier occupation/projection bounds appropriately. Locate the role of the actual-contact comparison and bandwidth-independent projection estimate in the joint autonomous result.
- **Dependencies and story role:** Depends on M19, M22, and M27. Places the assembled theorem in its scientific context.
- **Conceptual connection:** Connects the mathematical proof with an accurate account of prior work, including the stated full-text limits for recent comparisons; a textbook bridge is not a priority argument.
- **Source pointers:** [related work](../references/RELATED_WORK.md); [bibliography](../references/references.bib); [bridge](bridge.md).

### M29 — What the finite calculations establish

- **Phase:** Narrative/innovation.
- **Central question:** What does successful numerical reproduction support, and what remains an analytical claim?
- **Understanding target:** Identify the projected-Hamiltonian versus exact-Gaussian comparisons, retained references and outcomes, and feedback-dependent times. Recognize the examples' $`\gamma T=0.8`$ as a mechanism check rather than the conservative main-theorem parameter choice. Distinguish numerical error margins from a proof of the supremum over all testers.
- **Dependencies and story role:** Depends on M19, M22, M23, and M27. Connects the global proof with its reproducible finite evidence.
- **Conceptual connection:** Connects concrete controlled experiments to the two estimates without replacing universal quantifiers or lower bounds by sampled examples.
- **Source pointers:** [verification guide](../verification/README.md); [fixed-time calculation](../verification/check_autonomous_bath.py); [adaptive-time calculation](../verification/check_autonomous_adaptive_times.py).

### M30 — The physical meaning of the complete result

- **Phase:** Narrative/innovation.
- **Central question:** What does this theorem establish about autonomous noise, and which physical boundaries define that conclusion?
- **Understanding target:** Give one connected account of the target, tester, constructed device, approximation mechanisms, and conditional optimality statement. Explain why encoded qubit memory is not a local implementation cost, why the construction's stationary vacuum is nonpassive after energy shifting, and why the guarantee concerns a designed finite horizon with classical timing.
- **Dependencies and story role:** Integrates M13 and M27–M29, drawing on the mechanisms developed throughout the narrative. Completes the local-to-global account.
- **Conceptual connection:** Connects the theorem's resource hierarchy to its physical interpretation while preserving the open questions about thermal/passive alternatives, locality, coherent timing, and sharp joint accuracy dependence.
- **Source pointers:** [interpretation](../science/interpretation.md); [resource theorem, “Quantifiers and limitations”](../science/resource_theorem.md#quantifiers-and-limitations); [bridge](bridge.md).

[RH]: https://link.springer.com/book/10.1007/978-3-642-23354-8
[RH3]: https://link.springer.com/chapter/10.1007/978-3-642-23354-8_3
[RH4]: https://link.springer.com/chapter/10.1007/978-3-642-23354-8_4
[RH5]: https://link.springer.com/chapter/10.1007/978-3-642-23354-8_5
