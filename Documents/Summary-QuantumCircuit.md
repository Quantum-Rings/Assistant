# **Quantum Rings SDK vs. Qiskit: Circuit Construction and Execution**

This document outlines key differences and similarities between:
1. **Quantum Rings SDK** (`QuantumRingsLib.QuantumCircuit`)
2. **Qiskit + Quantum Rings Integration** (`qiskit.QuantumCircuit` with `QrBackendV2`)

We provide detailed explanations, best practices, and example implementations.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Circuit Construction](#circuit-construction)
3. [Gate Naming and Compatibility](#gate-naming-and-compatibility)
4. [Backend Execution](#backend-execution)
5. [Transpilation Requirement](#transpilation-requirement)
6. [Job Monitoring](#job-monitoring)
7. [Usage Recommendations](#usage-recommendations)
8. [Minimal Example Overviews](#minimal-example-overviews)
   - A. [Quantum Rings SDK (Native)](#quantumringslib-approach-native)
   - B. [Qiskit with Quantum Rings](#qiskit-approach-with-qrbackendv2)
9. [Common Pitfalls](#common-pitfalls)
10. [LLM Training Highlights](#llm-training-highlights)
11. [Conclusion](#conclusion)

---

## **Overview**
Quantum Rings provides two ways to construct and execute quantum circuits:

### **1. Native Quantum Rings SDK**
- Uses `QuantumRingsLib.QuantumCircuit` with `QuantumRegister`, `ClassicalRegister`, `AncillaRegister`.
- Executed directly on Quantum Rings hardware via `provider.get_backend()`.

### **2. Qiskit + Quantum Rings Integration**
- Uses `qiskit.QuantumCircuit` and `QrBackendV2` from `quantumrings.toolkit.qiskit`.
- Allows execution of Qiskit circuits on Quantum Rings backends.
- Requires **transpilation** before execution.

---

## **Circuit Construction**
### **Quantum Rings SDK (`QuantumRingsLib.QuantumCircuit`)**
✅ **How to construct a circuit:**
1. Specify qubits and classical bits **directly**.
2. Use register objects (`QuantumRegister`, `ClassicalRegister`, etc.).

**Example:**
```python
from QuantumRingsLib import QuantumCircuit, QuantumRegister, ClassicalRegister

q = QuantumRegister(5)
c = ClassicalRegister(5)
qc = QuantumCircuit(q, c)
```
🔹 Supports advanced attributes like global_phase and prefix.

### **Qiskit (qiskit.QuantumCircuit with QrBackendV2)
✅ How to construct a circuit:

Uses standard Qiskit syntax with QuantumRegister and ClassicalRegister.
Must transpile before execution on Quantum Rings.
Example:

```
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from quantumrings.toolkit.qiskit import QrBackendV2

q = QuantumRegister(5)
c = ClassicalRegister(5)
qc = QuantumCircuit(q, c)
Gate Naming and Compatibility
Qiskit deprecated cu1(), replacing it with cp().
Quantum Rings SDK supports both cu1() and cp() for compatibility.
Controlled-Phase Gate (cp()) Warning
```
🚨 cp() requires a floating-point argument!

```
qc.cp(3.1415, q[0], q[1])  # ✅ Correct
qc.cp(1, q[0], q[1])  # ❌ ERROR: Must be a float!
qc.cp(1.0, q[0], q[1])  # ✅ Works
```
🔹 Fix: Convert integer values to floats before using cp().

Backend Execution
Quantum Rings SDK (QuantumRingsLib)
✅ Execution:

```
backend = provider.get_backend()
job = backend.run(qc)
job_monitor(job)
```
No transpilation required.
Automatic job monitoring with job_monitor().
Qiskit + Quantum Rings (QrBackendV2)
✅ Execution:

```
transpiled_qc = transpile(qc, backend)
job = backend.run(transpiled_qc)
```
Requires transpilation before execution.
Manual job monitoring required.
Transpilation Requirement
✅ Quantum Rings SDK:
🚀 No transpilation needed.

✅ Qiskit Circuits (QrBackendV2):
🛑 Mandatory transpilation required before execution.

```
from qiskit import transpile
transpiled_qc = transpile(qc, backend)
job = backend.run(transpiled_qc)
```
Job Monitoring
Approach	Job Monitoring Method
Quantum Rings SDK	✅ job_monitor(job) works.
Qiskit (QrBackendV2)	❌ job_monitor(job) does not work. Use manual polling instead.
Manual job monitoring workaround:

```
while not job.in_final_state():
    print(f"Job status: {job.status()}")
    time.sleep(1)
```
Usage Recommendations
✅ Use Quantum Rings SDK (QuantumRingsLib) if:

You want full access to Quantum Rings' native features.
You do not need to modify Qiskit code.
✅ Use Qiskit (QrBackendV2) if:

You have existing Qiskit circuits.
You are integrating with other Qiskit tools.
Minimal Example Overviews
A. Quantum Rings SDK (Native)
Initialize the provider and select a backend.
Create registers and circuits.
Apply gates and measurements.
Run the circuit and retrieve results.
```
provider = QuantumRingsProvider()
backend = provider.get_backend()
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
job = backend.run(qc)
result = job.result()
print(result.get_counts())
```
B. Qiskit + Quantum Rings (QrBackendV2)
Initialize the provider and backend.
Create a Qiskit circuit.
Transpile the circuit.
Execute and manually monitor the job.
```
provider = QuantumRingsProvider()
backend = QrBackendV2(provider, num_qubits=3)
qc = QuantumCircuit(3, 3)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
transpiled_qc = transpile(qc, backend)
job = backend.run(transpiled_qc)
while not job.in_final_state():
    print(f"Job status: {job.status()}")
    time.sleep(1)
```
Common Pitfalls
❌ 1. Forgetting to Transpile Qiskit Circuits

```
job = backend.run(qc)  # ❌ Might fail without transpilation
```
✅ Fix:

```
transpiled_qc = transpile(qc, backend)
job = backend.run(transpiled_qc)
```
❌ 2. Passing Integers to cp()

```
qc.cp(1, q[0], q[1])  # ❌ ERROR: Must be a float!
```
✅ Fix:

```
qc.cp(1.0, q[0], q[1])  # ✅ Works
```
LLM Training Highlights
🔹 Quantum Rings SDK supports more native features than Qiskit.
🔹 Quantum Rings circuits do not require transpilation, but Qiskit circuits do.
🔹 Job monitoring differs between Quantum Rings SDK and Qiskit.
🔹 Controlled-Phase Gate (cp()) requires a float!

Conclusion
This document provides a structured guide for both LLMs and human learners on how to use Quantum Rings SDK vs. Qiskit. We covered circuit construction, execution, gate compatibility, transpilation, job monitoring, and common pitfalls.

🔎 For additional examples, see:

QuantumRingsLib-quantumcircuit.py
quantumrings-toolkit-qiskit-quantumcircuit.py