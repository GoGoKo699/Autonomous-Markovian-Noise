# Memory, interaction and spectral width

[Model](model.md) · [Resource theorem](resource_theorem.md)

## What repeated access detects

Under Markovian dephasing, each interval has a fresh phase increment. Earlier measurements can inform the tester about its system, but they do not reveal a bath state that changes the statistics of subsequent increments. A finite closed simulator must reproduce that behavior while retaining every piece of information in its own finite joint evolution.

An unrestricted one-time channel dilation does not answer this question. The tester may swap in fresh entangled probes, measure in noncommuting bases, and move later contact times according to earlier outcomes. The relevant approximation therefore concerns the controlled process, including its records and protected references.

## Why logarithmic encoded memory can suffice

Over the fixed horizon $`\gamma T=1`$, the total noise strength is fixed. Increasing the tester's time resolution increases the number of distinguishable locations in which the bath may store relevant activity, without increasing the observation horizon. The construction captures this separation with many modes and a fixed total-occupation cutoff.

For $`M`$ modes and cutoff $`k`$, the finite bath dimension is

```math
D=\binom{M+k}{k}.
```

At fixed accuracy, $`k`$ is fixed and $`M`$ grows linearly with $`N`$. Thus $`D`$ is polynomial in $`N`$, and its encoded qubit cost is logarithmic. This does not mean that the proposed mode realization literally contains only logarithmically many native oscillators. It means the retained finite subspace can be represented using that many qubits if arbitrary encoded Hamiltonian matrices are permitted.

The memory converse has a different physical form. A tester stores $`N+1`$ weakly dephased Bell outputs. Their joint state distributes a fixed amount of weight over a growing collection of distinguishable records. A closed bath of bounded dimension cannot supply the required accessible output rank. Even an initially mixed bath only changes the rank allowance from $`D`$ to at most $`D^2`$.

## Why faster access needs stronger coupling

Bounded Hamiltonian evolution initially produces quadratic survival loss, whereas the target semigroup has a linear short-time dissipative term. Repeated interventions can expose that discrepancy. The inherited interaction-resolution bound makes this operational: holding error fixed while increasing the number of contacts requires coupling strength of order $`\gamma\sqrt N`$.

The construction reaches that order because a covariance peak of width of order $`T/N`$ and fixed integrated mass has height of order $`\gamma^2N`$. The field amplitude therefore has square-root order. The finite occupation cutoff contributes a constant depending on accuracy.

## Why bath width is an additional resource

A strong interaction alone does not specify how rapidly the bath field changes. The free bath Hamiltonian supplies that variation. With a sufficiently narrow free spectrum, a sequence of instantaneous sign reversals can average the microscopic dephasing interaction away. The ideal Markovian generator is invariant under those sign reversals, so it continues to dephase.

This operational mismatch yields

```math
\frac{W_E}{2}+\Lambda=\Omega(\gamma N).
```

At square-root coupling, the bath width must provide the linear term. The construction does so using frequencies spanning a range of order $`\gamma N`$. The result identifies two different dynamical requirements: enough interaction strength to create short-time noise and enough bath frequency range to resist increasingly fine intervention sequences.

The sum bound leaves open other allocations when the interaction is allowed to grow linearly or faster. It is therefore a conditional bandwidth optimum, not a complete resource frontier.

## Why the finite projection needs a dynamical proof

A small high-occupation probability at a final time does not by itself show that deleting high-occupation states leaves the evolution unchanged. A path can leave the retained subspace and later return, changing amplitudes inside it. Postselecting or renormalizing a restricted trajectory ensemble would also alter the operational process.

Here the finite Hamiltonian is defined directly on the total-occupation subspace. The proof compares its Dyson paths with the full Gaussian reference. The particular covariance is pointwise nonnegative, so deleted-path overlaps are bounded by positive Wick sums. This controls all excursions and gives an error bound independent of the growing bandwidth. Pointwise nonnegativity is a substantive property of the chosen kernel; positive definiteness alone would not justify the termwise comparison.

## How classical timing enters the result

A finite policy tree can contain many candidate times although only $`N`$ contacts occur along any realized record. Bounding every potential branch separately would pay for that larger tree. Instead, the Gaussian interpolation proof uses the event that an actual contact separates two phase intervals. Before the first such contact, operations on protected memory cannot detect a local system phase. That causal fact bounds phase derivatives by the probability of the contact event. Summing those probabilities charges only actual contacts.

The theorem allows feedback-dependent real times and arbitrarily close contacts. It does not treat a clock kept in a coherent superposition of distinct interaction schedules. The operational closure is applied only after the two approximation estimates have been combined for the finite device.

## Physical boundaries

The bath reference contains positive and negative mode frequencies. After truncation its spectrum is finite and can be shifted above zero without affecting dynamics. That shift does not make the initial vacuum a ground state: it remains an excited stationary state. The construction therefore uses a nonpassive resource and makes no thermal or equilibrium claim.

The total-occupation constraint is global. Locality, preparation, robustness to imperfect control and efficient compilation are separate implementation questions. The upper constants are conservative, and the theorem does not optimize the joint limit in which accuracy vanishes while $`N`$ grows. Finally, the guarantee covers the designed horizon $`T`$; a finite autonomous bath need not imitate irreversible noise indefinitely.
