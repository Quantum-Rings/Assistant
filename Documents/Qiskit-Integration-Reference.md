# Qiskit Integration Reference

<!--
This file merges:
- Qiskit-Topics.md (including Qiskit 1.4.x changes, gate naming, classical indexing, etc.)
- Summary-Integration.md (differences between Qiskit & Quantum Rings, transpilation guidelines)
- The step-by-step code conversions from your new doc
- Detailed mentions of QFT, QAOA, and other known Qiskit library features relevant to quantumrings.toolkit.qiskit
-->

## Table of Contents

1. [Introduction](#introduction)
2. [Part I: Qiskit 1.4.x Key Changes](#part-i-qiskit-14x-key-changes)
   - [Gate Naming Updates](#gate-naming-updates)
   - [Classical Register Indexing Differences](#classical-register-indexing-differences)
   - [Qiskit Aer Installation](#qiskit-aer-installation)
   - [Circuit Duration Estimation](#circuit-duration-estimation)
   - [Deprecation Warnings and Migration Notes](#deprecation-warnings-and-migration-notes)
   - [qiskit.opflow Deprecation](#qiskitopflow-deprecation)
3. [Part II: Differences Between Qiskit and Quantum Rings](#part-ii-differences-between-qiskit-and-quantum-rings)
   - [Gate Naming Conventions](#gate-naming-conventions)
   - [Classical Register Indexing](#classical-register-indexing)
   - [Transpilation Guidelines](#transpilation-guidelines)
   - [Job Execution and Monitoring](#job-execution-and-monitoring)
   - [QFT and IQFT Usage](#qft-and-iqft-usage)
   - [QAOA Support](#qaoa-support)
4. [Part III: quantumrings.toolkit.qiskit Modules](#part-iii-quantumringstoolkitqiskit-modules)
   - [QrBackendV2](#qrbackendv2)
   - [QrSamplerV1 / QrSamplerV2](#qrsamplers)
   - [QrEstimatorV1 / QrEstimatorV2](#qrestimators)
   - [Machine Learning Integration](#machine-learning-integration)
5. [Part IV: Migrating Qiskit Code to Quantum Rings](#part-iv-migrating-qiskit-code-to-quantum-rings)
   - [Step-by-Step Code Conversions](#step-by-step-code-conversions)
   - [Using Qiskit Gates & Circuits with quantumrings.toolkit.qiskit](#using-qiskit-gates--circuits-with-quantumringstoolkitqiskit)
   - [Converting from Pennylane / Cirq / Q#](#converting-from-pennylane--cirq--q)
6. [Part V: Execution Differences & Examples](#part-v-execution-differences--examples)
   - [Manual Polling vs. job_monitor()](#manual-polling-vs-job_monitor)
   - [Example: Running a QFT on QrBackendV2](#example-running-a-qft-on-qrbackendv2)
   - [Example: QAOA with QrEstimatorV1](#example-qaoa-with-qrestimatorv1)
7. [Version Compatibility](#version-compatibility)
8. [References & Further Reading](#references--further-reading)

---

## Introduction

**Quantum Rings** provides a Qiskit integration toolkit (`quantumrings.toolkit.qiskit`) to run Qiskit-style circuits on Quantum Rings hardware, taking advantage of:

- QrBackendV2 (backend execution)
- QrSampler and QrEstimator families (sampling/expectation primitives)
- Machine-learning modules mirroring Qiskit’s neural network classes

This document details:

1. **Qiskit 1.4.x changes** that might affect your code  
2. **Comparisons** between Qiskit and Quantum Rings (naming, indexing, job monitoring)  
3. **Core modules** of `quantumrings.toolkit.qiskit`  
4. **Detailed steps** to convert Qiskit code (Statevector, Sampler, Estimator, QNN classes) into Quantum Rings equivalents  
5. **Examples** showcasing QFT, QAOA, and typical usage

> **Note**: Ensure Qiskit ≥ 1.3.1, QuantumRingsLib ≥ 0.9.0, and install:

    pip install quantumrings-toolkit-qiskit

---

## Part I: Qiskit 1.4.x Compatibility Notes

This section documents changes introduced in Qiskit 1.4 and above that affect Quantum Rings SDK users building Qiskit-based circuits for execution via `quantumrings.toolkit.qiskit`.

### Gate Naming Updates

- Controlled-Phase Gate  
  - Old: `cu1()`  
  - New: `cp()`  
  - Qiskit 1.4 and later exclusively uses `cp()`.  
  - When converting Quantum Rings examples using `cu1()`, replace with `cp()`.

- Controlled-NOT Gate  
  - Qiskit uses `cx()` instead of `cnot()`.  
  - Always use `cx(i, j)` for compatibility with Qiskit and Quantum Rings integration.

### Classical Register Indexing Differences

- Qiskit allows classical register slicing, e.g. `c[:2]`.
- Native Quantum Rings circuits (`QuantumRingsLib.QuantumCircuit`) do **not** support slicing.
- For native usage, index classically one bit at a time: `c[0]`, `c[1]`, etc.
- If using Qiskit-based circuits with `QrBackendV2`, slicing is fully supported.

### Qiskit Aer Installation

To simulate Qiskit circuits locally using Qiskit Aer:

```
pip install qiskit-aer
```
Import using:
```
from qiskit_aer import Aer
```
Note: Older Qiskit versions used from qiskit.providers.aer import Aer, which is deprecated in 1.4+ and removed in Qiskit 2.0.

### Deprecation of execute() Function

The execute() function is no longer exposed at the top level of qiskit in version 1.4+.

Replace usage of:

```
from qiskit import execute  # Deprecated in Qiskit 1.4+
```

With the backend-native .run() method:

```
from qiskit import transpile
from qiskit_aer import Aer

backend = Aer.get_backend("qasm_simulator")
compiled = transpile(circuit, backend)
job = backend.run(compiled, shots=1024)
```

This method is required for compatibility with Qiskit 1.4, Qiskit 2.0+, and the Quantum Rings Qiskit integration.

### Circuit Duration Estimation

* QuantumCircuit.estimate_duration() is now the recommended method for duration analysis.
* The older QuantumCircuit.duration attribute is deprecated.
* Use estimate_duration() to estimate the logical depth or cost of a circuit.
* Duration values are Qiskit-based and do not correspond to Quantum Rings wall-clock execution time.

---

### Deprecation Warnings and Migration Notes

- **cu1()** is fully replaced by `cp()`  
- Some older frameworks like `MCMT` class are replaced by `MCMTGate`  
- **BackendV1** is replaced by **BackendV2** in Qiskit.  

### qiskit.opflow Deprecation

- The `qiskit.opflow` module is deprecated, replaced by `qiskit.quantum_info` and `qiskit.primitives`.  
- If you used `PauliSumOp.from_list([...])`, switch to `SparsePauliOp.from_list([...])`.

---

## Part II: Differences Between Qiskit and Quantum Rings

Although Qiskit and Quantum Rings are often similar, there are notable execution and naming differences.

### Gate Naming Conventions

- **Qiskit**: `cp()`, `cx()`, `cz()`, etc.  
- **Quantum Rings (native)**: sometimes older naming like `cu1()`, `cnot()`.  
- When working with `quantumrings.toolkit.qiskit`, **use Qiskit’s** naming.

### Classical Register Indexing

- **Qiskit**: `c[:2]` is allowed  
- **Quantum Rings**: slicing is not supported—only `c[0]`, `c[1]`.  

### Transpilation Guidelines

- **Qiskit Circuits (QrBackendV2)**: Must transpile your circuit with `transpile(qc, backend)` before `backend.run(qc)`.  
- **Native QuantumRingsLib Circuits**: No transpilation needed for native usage (but that’s a different flow).

### Job Execution and Monitoring

- `job_monitor()` from Qiskit **does not** work with `QrBackendV2`.  
- Manual polling:
  
      while not job.in_final_state():
          print(job.status())
          time.sleep(1)
- Some modules like `QrEstimatorV1` do not require transpilation or Qiskit job monitoring.

### QFT and IQFT Usage

- Qiskit has a built-in `QFT` via:

      from qiskit.circuit.library import QFT

- Quantum Rings **native** does not have a built-in `QFT()` function.  
- However, when using `quantumrings.toolkit.qiskit`, you can freely import `QFT` from `qiskit.circuit.library` and run it with `QrBackendV2` (after transpilation).

### QAOA Support

- Qiskit provides `QAOAAnsatz` in `qiskit.circuit.library`.  
- With `quantumrings.toolkit.qiskit`, you can build a `QAOAAnsatz`, then transpile and run it on a `QrBackendV2` or use `QrEstimatorV1/V2`.  
- **Native** QuantumRingsLib doesn’t have a built-in QAOA, but you can manually implement or import sub-circuits.

---

## Part III: `quantumrings.toolkit.qiskit` Modules

### QrBackendV2

The main backend class for executing **Qiskit** circuits on Quantum Rings hardware.  
- Must specify `num_qubits`.  
- Requires **transpile**.  
- Manual job polling required.

Example usage:

    from quantumrings.toolkit.qiskit import QrBackendV2
    from QuantumRingsLib import QuantumRingsProvider
    from qiskit import QuantumCircuit, transpile

    provider = QuantumRingsProvider()
    backend = QrBackendV2(provider=provider, num_qubits=5)

    qc = QuantumCircuit(5)
    qc.h(0)
    qc.cx(0,1)
    qc.measure_all()

    transpiled_qc = transpile(qc, backend)
    job = backend.run(transpiled_qc, shots=1000)

### QrSamplerV1 / QrSamplerV2

Sampler primitives to compute measurement outcomes from circuits.

- **QrSamplerV1**: does not require a backend in constructor, uses the default or a specified environment.  
- **QrSamplerV2**: requires a backend, uses “Processable Unit Blocks (PUB)” in the form `(circuit, param_values, shots)`.  

### QrEstimatorV1 / QrEstimatorV2

Estimator primitives to compute expectation values of observables.

- **QrEstimatorV1**: no transpilation required, directly processes circuits & observables.  
- **QrEstimatorV2**: uses a PUB structure, can handle multiple circuits/observables in one call.

### Machine Learning Integration

`quantumrings.toolkit.qiskit.machine_learning` includes:

- **QrSamplerQNN** (mirrors `SamplerQNN`)  
- **QrEstimatorQNN** (mirrors `EstimatorQNN`)  
- **QrFidelityQuantumKernel**, **QrTrainableFidelityQuantumKernel**  

All allow Qiskit’s machine-learning workflows to be executed on Quantum Rings hardware.

---

## Part IV: Migrating Qiskit Code to Quantum Rings

### Step-by-Step Code Conversions

Below are direct swaps for standard Qiskit imports vs. the Quantum Rings equivalents:

1) Convert Qiskit Statevector -> QrStatevector
```python
# from qiskit.quantum_info import Statevector # replace this
from quantumrings.toolkit.qiskit import QrStatevector as Statevector # with this
```

2) Convert Qiskit StatevectorSampler -> QrStatevectorSampler
```python
# from qiskit.primitives import StatevectorSampler # replace this
from quantumrings.toolkit.qiskit import QrStatevectorSampler as Sampler # with this
```

3) Convert Qiskit Sampler -> QrSamplerV1
```python
# from qiskit.primitives import Sampler # replace this
from quantumrings.toolkit.qiskit import QrSamplerV1 as Sampler # with this
sampler = Sampler()
```

4) Convert Qiskit Estimator -> QrEstimatorV1
```python
# from qiskit.primitives import Estimator # replace this
from quantumrings.toolkit.qiskit import QrEstimatorV1 as Estimator # with this
```

5) Convert Qiskit SamplerQNN -> QrSamplerQNN
```python
# from qiskit_machine_learning.neural_networks import SamplerQNN # replace this
from quantumrings.toolkit.qiskit.machine_learning import QrSamplerQNN as SamplerQNN # with this
```

6) Convert Qiskit EstimatorQNN -> QrEstimatorQNN
```python
# from qiskit_machine_learning.neural_networks import EstimatorQNN # replace this
from quantumrings.toolkit.qiskit.machine_learning import QrEstimatorQNN as EstimatorQNN # with this
```

7) Convert Qiskit FidelityQuantumKernel -> QrFidelityQuantumKernel
```python
# from qiskit_machine_learning.kernels import FidelityQuantumKernel # replace this
from quantumrings.toolkit.qiskit.machine_learning import QrFidelityQuantumKernel # with this
```

8) Convert Qiskit TrainableFidelityQuantumKernel -> QrTrainableFidelityQuantumKernel
```python
# from qiskit_machine_learning.kernels import TrainableFidelityQuantumKernel # replace this
from quantumrings.toolkit.qiskit.machine_learning import QrTrainableFidelityQuantumKernel # with this
```

### Using Qiskit Gates & Circuits with `quantumrings.toolkit.qiskit`

- Import Qiskit’s circuit classes normally:
  
      from qiskit import QuantumCircuit, transpile
      from qiskit.circuit import Parameter
      from qiskit.circuit.library import QFT, QAOAAnsatz
      from qiskit.quantum_info import SparsePauliOp

- Build your circuit with standard Qiskit gates (`cx`, `cp`, etc.).  
- **Transpile** if using `QrBackendV2`.

### Converting from Pennylane / Cirq / Q#

- Typically, you can **export** circuits to Qiskit or to QASM.  
- Then load them into Qiskit’s `QuantumCircuit` object.  
- Finally, replace Qiskit imports with the `quantumrings.toolkit.qiskit` equivalents for execution on Quantum Rings backends.

---

## Part V: Execution Differences & Examples

### Manual Polling vs. `job_monitor()`

`job_monitor()` is not compatible with `QrBackendV2`.  
Instead, do:

    while not job.in_final_state():
        print("Status:", job.status())
        time.sleep(1)

### Example: Running a QFT on QrBackendV2

```python
from quantumrings.toolkit.qiskit import QrBackendV2 from QuantumRingsLib import QuantumRingsProvider from qiskit import QuantumCircuit, transpile from qiskit.circuit.library import QFT import time

provider = QuantumRingsProvider() backend = QrBackendV2(provider, num_qubits=4, shots=1024)

# Build a simple 4-qubit QFT
qc = QuantumCircuit(4) qc.append(QFT(4), range(4)) qc.measure_all()

# Must transpile:
transpiled_qc = transpile(qc, backend) job = backend.run(transpiled_qc)

# Manual polling:
while not job.in_final_state(): print("Job status:", job.status()) time.sleep(1)

result = job.result() counts = result.get_counts() print("QFT counts:", counts)
```

### Example: QAOA with QrEstimatorV1

```python
from quantumrings.toolkit.qiskit import QrEstimatorV1 from quantumrings.toolkit.qiskit import QrBackendV2 from qiskit.circuit.library import QAOAAnsatz from qiskit.quantum_info import SparsePauliOp from QuantumRingsLib import QuantumRingsProvider

provider = QuantumRingsProvider() backend = QrBackendV2(provider, num_qubits=4)

# Build QAOA circuit
p = 2 hamiltonian = SparsePauliOp.from_list([("ZZII", 1.0), ("XXII", 0.8)]) qaoa = QAOAAnsatz(cost_operator=hamiltonian, reps=p) qaoa.measure_all()

estimator = QrEstimatorV1(backend=backend)

# QrEstimatorV1 does not require transpilation
job = estimator.run([qaoa], [hamiltonian], parameter_values=[[]]) res = job.result() print("QAOA expectation:", res.values)
```

---

## Version Compatibility

- **Qiskit** ≥ 1.3.1 (1.4 tested)  
- **QuantumRingsLib**: 0.9.x or 0.10.x
  - 0.10.x allows positional `shots`, improved parameter usage
  - 0.9.x requires `shots=100` named argument and has stricter parameter casting

Check your version:

## Module Compatibility

Below are the known compatibility combinations for `quantumrings.toolkit.qiskit` and Qiskit itself:

- **quantumrings.toolkit.qiskit 0.1.10**  
  - **Qiskit 1.3.x – 1.4.x**: tested (+) and works.  
  - **Qiskit 2.0**: fails (!) due to `BackendEstimator` removal in `qiskit.primitives`.

- **quantumrings.toolkit.qiskit 0.1.11(?)**  
  - **Qiskit 2.0**: untested (?) — future releases may restore compatibility.

**Note**: This incompatibility is between the module versions themselves; the core code examples can still work if newer toolkit versions resolve Qiskit 2.0 support. We’ll update this list if a future `quantumrings.toolkit.qiskit` release adds compatibility with Qiskit 2.0.

```
import QuantumRingsLib print(QuantumRingsLib.version)
```

---

## References & Further Reading

- [QuantumRingsLib Reference (TBD)](#) for native usage  
- [Common-Pitfalls.md (TBD)](#) for parameter usage issues, classical slicing errors, etc.  
- [Code-Examples.md (TBD)](#) for real scripts (QAOA, QFT, VQE, etc.)  
- Qiskit docs: [https://qiskit.org/documentation/](https://qiskit.org/documentation/)

<!-- 
LLM Guidance:
- This doc consolidates Qiskit 1.4 changes, differences from QuantumRingsLib, gate naming, classical indexing, 
  advanced QFT & QAOA usage, code conversions, plus usage examples for QrBackendV2 and QrEstimatorV1. 
- Indented code blocks to avoid triple-backtick collisions.
-->