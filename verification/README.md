# Reproduce the finite calculations

[Project overview](../README.md) · [Resource theorem](../science/resource_theorem.md)

These checks compare finite autonomous bath dynamics with the exact Gaussian reference for concrete controlled experiments. They test the two approximation mechanisms, including an outcome-dependent timing policy. They do not prove the supremum over all testers or the asymptotic lower bounds.

## Run

From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The reference results were reproduced with Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. The dependencies record the inspected runtime. The runner checks numerical inequalities and normalization, then compares against the committed reference JSON with absolute tolerance $`2\times10^{-10}`$ and relative tolerance $`2\times10^{-8}`$. Run without Python's optimization flag, because the scientific scripts use assertions for their inequality checks. A discrepancy raises an error; the runner does not overwrite reference outputs.

Expected terminal summary:

```text
PASS: fixed-time; analytic inequalities, trace and reference output checked
PASS: adaptive-time; analytic inequalities, trace and reference output checked
```

Each script can also print its complete result to standard output:

```bash
python3 verification/check_autonomous_bath.py
python3 verification/check_autonomous_adaptive_times.py
```

## What is compared

Both examples use horizon $`T=1`$, rate $`\gamma=0.8`$ and kernel period $`L=4`$. Thus $`\gamma T=0.8`$, within the range of the construction's intermediate estimates. These small examples test the mechanisms; they are not the conservative theorem parameter choice at a prescribed target accuracy.

The finite bath uses the exact Jackson Fourier weights. A basis enumerates every occupation vector with total number at most $`k`$. Sparse matrix exponentiation evolves the single projected Hamiltonian between contacts. The accessible density matrix is obtained by tracing out the bath.

For the reference, a finite sum over forward and backward Pauli paths evaluates the Gaussian characteristic function exactly. This removes Monte Carlo sampling error. Numerical error remains in floating-point arithmetic, quadrature and matrix exponentiation.

| Check | Tested features | Cutoff-six distance to the Gaussian output |
|---|---|---:|
| Fixed-time experiment | Three contacts, Bell reference, noncommuting rotations, recorded measurement and feedback | approximately $`3.76\times10^{-7}`$ |
| Adaptive-time experiment | A recorded Y measurement determines two later contact times; protected reference; every outcome retained | approximately $`3.97\times10^{-7}`$ |

The fixed-time contacts are at 0.13, 0.39 and 0.74. The adaptive experiment first measures at 0.12 and then uses times (0.28, 0.76) or (0.47, 0.89), depending on the recorded outcome. Its initial state has an X component, so outcome probabilities depend on the phase history. Branch states remain subnormalized and are summed with their actual weights; no postselection is used.

## Inequalities tested

For $`m=2,4,8,16,32,64`$, the scripts compare colored and white Gaussian outputs with the first-moment bounds. The fixed-time calculation also checks covariance positivity and an entrywise covariance comparison. The adaptive-time script checks the actual-contact bound $`(2N+1)\mu_m`$ for $`N=3`$.

For the five-mode kernel $`m=2`$, cutoff values up to six are checked against the Dyson-tail estimate. The fixed-time calculation uses its integrated covariance $`J`$; the adaptive example uses the common upper bound $`J\le\gamma T`$. The 300-term positive numerical tail sum is adequate at these parameters; it is a floating-point evaluation of the analytic tail, not an interval-arithmetic proof certificate. The general convergent tail and geometric remainder certificate are established in [the construction](../science/finite_bath.md).

The committed outputs are [fixed-time results](check_autonomous_bath_results.json) and [adaptive-time results](check_autonomous_adaptive_times_results.json). The strict trace and error margins are much larger than the stated numerical tolerances. Exact memory-rank and dynamical-decoupling converses are analytical and are not replaced by these finite examples.

## Hosted mathematical display

The [rendering check](rendering/README.md) independently compares the actual GitHub equations with the exact committed source at wide and narrow viewports. The pull-request workflow retains its report and screenshots for visual review. This checks mathematical presentation; it does not substitute for the scientific calculations or proofs above.
