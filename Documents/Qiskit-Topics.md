Guide to Using Qiskit 1.4.x and Comparison with Quantum Rings
This guide summarizes important updates and best practices for using Qiskit 1.4.x, along with a comparison to the Quantum Rings framework. It highlights changes from previous Qiskit versions, common pitfalls, deprecations, and critical execution differences between Qiskit and Quantum Rings.

# 📌 Part I: Qiskit 1.4.x – Key Changes and Best Practices
## 1. Gate Naming Updates
Controlled-Phase Gate
Old: cu1()
New: cp()
Note: Qiskit now exclusively uses cp() for the controlled-phase gate.
🔹 Replace all instances of cu1() with cp().
Controlled-NOT Gate
Qiskit Syntax: Use cx() (not cnot()).
Tip: When converting from other frameworks (e.g., Quantum Rings), note that Quantum Rings might still use cnot(), while Qiskit strictly uses cx().

## 2. Classical Register Indexing Differences
Qiskit: Classical registers can be accessed using slicing, e.g., c[:2].
Quantum Rings: ❌ Classical registers do NOT support slicing. Instead, use explicit indexing:

```
c[0]  # ✅ Allowed in Quantum Rings
c[:2] # ❌ Not supported
```

Implication: When porting code, adjust classical register indexing accordingly.

## 3. Qiskit Aer Installation
To install the Qiskit Aer simulator, use:

```
pip install qiskit-aer
```

## 4. Circuit Duration Estimation
Qiskit 1.4 introduces:

```
QuantumCircuit.estimate_duration()
```

🔹 Purpose: Computes the estimated duration of a circuit post-transpilation.
🚀 Benefit: Helps optimize circuit runtime and replaces the deprecated QuantumCircuit.duration attribute.

## 5. Deprecation Warnings and Migration Notes (Qiskit 1.4.x)
Qiskit 1.4.x is the final minor version before Qiskit v2.0.
🔹 Expect deprecations before the Qiskit v2.0 release.

Deprecated Feature	Qiskit v1.4.x	Qiskit v2.0 Replacement
Controlled-Phase Gate	cu1()	cp()
Register Subclassing	QuantumRegister, Qubit subclassing	❌ Deprecated
MCMT Class	MCMT	MCMTGate
BackendV1 Inputs	BackendV1	BackendV2
ClassicalFunction Module	PhaseOracle, BitFlipOracle	🔹 Alternative functions required
📌 Migration Tip: Upgrade to Qiskit 1.4.x first to see deprecation warnings before transitioning to Qiskit v2.0.

## 6. Deprecation of qiskit.opflow and Migration to qiskit.quantum_info
### 📌 Important Update
The qiskit.opflow module has been deprecated and replaced by qiskit.quantum_info and qiskit.primitives. Users should update their code to avoid errors in newer versions of Qiskit.

### Migration Guide
* If you previously used PauliSumOp.from_list([...]), replace it with SparsePauliOp.from_list([...]) from qiskit.quantum_info.
* If you used StateFn(operator, is_measurement=True), switch to using Estimator().run(circuit, observable).
* If you relied on CircuitSampler(backend).convert(operator), replace it with Sampler().run(circuits, parameter_values).
* If you used Trotter(mode="suzuki") for Trotterization, switch to SuzukiTrotter().
* If you applied PauliExpectation(), now use Estimator() instead.

### Example Fix
Before (Using qiskit.opflow)
This code will fail in Qiskit 1.4 and later:

```
from qiskit.opflow import PauliSumOp
hamiltonian = PauliSumOp.from_list([("ZZ", 1.0), ("XX", 0.5)])
```
❌ This results in an ImportError.

After (Using qiskit.quantum_info)
Use this instead:

```
from qiskit.quantum_info import SparsePauliOp
hamiltonian = SparsePauliOp.from_list([("ZZ", 1.0), ("XX", 0.5)])
```
⚠️ Important Note:
SparsePauliOp requires full-length Pauli strings where all qubits are specified.
❌ Incorrect: SparsePauliOp(["Z0", "Z1Z2"], coeffs=[1.0, 0.5]) (Missing "I" placeholders).
✅ Correct: SparsePauliOp(["IZII", "IIZZ"], coeffs=[1.0, 0.5]).
✅ This works correctly in the latest Qiskit versions.

# 📌 Part II: Differences Between Qiskit and Quantum Rings
While Qiskit and Quantum Rings share many similarities, there are important execution differences that users must be aware of.

## 1. Gate Naming Conventions
Qiskit: Uses cp() for controlled-phase and cx() for CNOT.
Quantum Rings: Often retains older naming conventions (cu1(), cnot()).
Implication:
✅ When writing Quantum Rings code, cnot() is accepted.
⚠️ When converting from Quantum Rings to Qiskit, replace cnot() with cx() and cu1() with cp().

## 2. Classical Register Indexing
Feature	Qiskit	Quantum Rings
Register Slicing	✅ c[:2] allowed	❌ Not supported
Explicit Indexing	✅ c[0], c[1]	✅ Use this method

## 3. Transpilation: When It Is and Isn't Needed
### When Transpilation is Required
In Quantum Rings, some execution backends require transpilation, while others do not. Understanding when to apply transpilation is critical to avoid errors and improve performance.

### ✅ When You MUST Transpile (QrBackendV2)
* If you are using QrBackendV2.run(qc), you must transpile your circuit first.
* QrBackendV2 is designed to execute Qiskit circuits on Quantum Rings hardware, which requires mapping the circuit to the appropriate qubits and gate set.
* Correct usage:
```
from qiskit import transpile
transpiled_qc = transpile(qc, backend)  # REQUIRED before running QrBackendV2
job = backend.run(transpiled_qc)
```
* Common Error:
```
job = backend.run(qc)  # ❌ This will likely fail unless `qc` is already mapped.
```
## ❌ When You Should NOT Transpile (QrEstimatorV1)
* If you are using QrEstimatorV1.run(), DO NOT transpile your circuit before execution.
* QrEstimatorV1 directly processes quantum circuits and observables without requiring transpilation.
* Correct usage:
```
job = estimator.run([qc], [observable], parameter_values=[[1.2, 0.5]])
```
* Common Mistake:
```
transpiled_qc = transpile(qc, backend)  
job = estimator.run([transpiled_qc], [observable], parameter_values=[[1.2, 0.5]])  
```
⚠️ Incorrect! QrEstimatorV1 does NOT need a transpiled circuit.
## ✅ When You MAY Need to Transpile (QrSamplerV2)
* If you are using QrSamplerV2.run(), transpilation is usually required.
* QrSamplerV2 is designed for sampling multiple circuits, similar to QrBackendV2, and needs the circuit to be mapped to the Quantum Rings backend.
* Best practice:
```
transpiled_qc = transpile(qc, backend)
job = sampler.run([(transpiled_qc, [], shots)])
```
🔹 Final Key Takeaways
1. Always transpile when using QrBackendV2.run(qc).
2. Never transpile when using QrEstimatorV1.run().
2. For QrSamplerV2, transpile before execution unless otherwise specified.
4. If you see an error related to qubit mapping, check whether your circuit was correctly transpiled.

## 4. Job Execution: job_monitor() Incompatibility
Qiskit Standard	Quantum Rings (QrBackendV2)
✅ Uses job_monitor(job)	❌ job_monitor() does NOT work
✅ Automatic job polling	✅ Manual polling required
Fix: Use Manual Job Monitoring

```
while not job.in_final_state():
    print(f"Job status: {job.status()}")
    time.sleep(1)
```

## 5. Quantum Fourier Transform (QFT)
Feature	Qiskit	Quantum Rings
Built-in qft() Function	✅ Yes	⚠️ Depends on Library
Manual QFT Implementation Required	❌ No	⚠️ Only if using QuantumRingsLib alone
* 📌 QuantumRingsLib does NOT include a built-in QFT function, meaning users must manually implement QFT if working only with QuantumRingsLib.
* Qiskit’s qiskit.circuit.library.QFT CAN be used when working with quantumrings.toolkit.qiskit, and it is fully compatible with QrBackendV2 and QrSamplerV2 backends.
* If using Quantum Rings with Qiskit, the correct way to add QFT to a circuit is:
```
from qiskit.circuit.library import QFT
qc.append(QFT(num_qubits=4), range(4))
```
* Common Mistake: Assuming QuantumRingsLib has a built-in QFT() function—it does not.  But the toolkit supports it.

## 🧠 Using Qiskit Circuit Features with quantumrings.toolkit.qiskit

The `quantumrings.toolkit.qiskit` module is built to work seamlessly with standard Qiskit constructs. You are encouraged to use:

- `qiskit.QuantumCircuit`
- `qiskit.Parameter` and `ParameterVector`
- Circuit templates from `qiskit.circuit.library` (e.g., `QFT`, `TwoLocal`, `EfficientSU2`)

These circuits should be transpiled before execution on Quantum Rings backends using:
```
from qiskit import transpile
qc = transpile(qc, backend)
```

## 6. Inverse Quantum Fourier Transform (IQFT or qft_inverse)
Feature	Qiskit	Quantum Rings
Built-in iqft() Function	✅ Yes	⚠️ Depends on Library
Manual IQFT Implementation Required	❌ No	⚠️ Only if using QuantumRingsLib alone
📌 QuantumRingsLib (core library) does not include a built-in iqft() or qft_inverse() function.
🔹 If working only with QuantumRingsLib, users must manually construct IQFT circuits.
✅ However, when using quantumrings.toolkit.qiskit, users can import QFT from qiskit.circuit.library.QFT, apply .inverse(), and execute the circuit on Quantum Rings hardware.

## 7. QrSamplerV2 Initialization and Batch Execution
### Feature	Qiskit	Quantum Rings
Sampler Initialization	Sampler() (no backend required)	QrSamplerV2(backend=backend) (backend required)

Batch Execution Format	sampler.run([circuits], shots=1024)	sampler.run([(qc1, [], shots), (qc2, [], shots)])

### Important Notes:
Unlike Qiskit’s Sampler(), Quantum Rings requires a backend when initializing QrSamplerV2:
```
sampler = QrSamplerV2(backend=backend)  # ✅ Required backend
```

### Incorrect Usage:
```
sampler = QrSamplerV2()  # ❌ This will fail
```

### Batch Execution Requires PUB Format
When running multiple circuits, use a list of tuples (Processable Unit Blocks - PUBs):
```
pub_list = [(qc1, [], shots), (qc2, [], shots)]  # ✅ Correct
job = sampler.run(pub_list)
result = job.result()
```

Common Mistake: Passing circuits directly without PUB formatting will cause an error.
Troubleshooting: If you get a TypeError: __init__() takes 1 positional argument but 2 were given, ensure:
You have the latest Quantum Rings SDK:
```
pip install --upgrade QuantumRingsLib
```

You are using backend=backend explicitly:
```
sampler = QrSamplerV2(backend=backend)  # ✅ Correct
```

## 8. Parameter Handling in Quantum Rings SDK

### 📌 Quantum Rings SDK vs. Qiskit: Parameter Assignment

Quantum Rings and Qiskit both support parameterized circuits, but their workflows differ significantly—especially between native QuantumRingsLib usage and Qiskit-based integration via `quantumrings.toolkit.qiskit`.

---

### ✅ Native SDK: Using QuantumRingsLib.QuantumCircuit

The native SDK supports `.assign_parameters()` if you follow these rules:

- You must use `inplace=True` when calling `.assign_parameters()`.
- Parameter dictionary keys must be strings matching the parameter names, not Parameter objects.
- All arguments to parameterized gates like `u()` must be of the same type. You cannot mix a `Parameter` with a `float`.
- Omitting `inplace=True` will cause `.assign_parameters()` to return `None`, which may cause confusion.

**Working Example (Native SDK):**

```python
from QuantumRingsLib import Parameter, QuantumCircuit, QuantumRegister

theta = Parameter("theta")
phi = Parameter("phi")
lam = Parameter("lambda")

q = QuantumRegister(1, "q")
qc = QuantumCircuit(q)

qc.u(theta, phi, lam, q[0])  # All parameters are symbolic

qc.assign_parameters({
    "theta": 3.14,
    "phi": 1.57,
    "lambda": 0.785
}, inplace=True)
```

### Common Mistakes That Will Fail:
```
qc.u(theta, 0, 0, q[0])  # ❌ Mixing Parameter and float types

qc.assign_parameters({theta: 3.14}, inplace=True)  # ❌ Key must be a string

qc.assign_parameters({"theta": 3.14})  # ❌ Missing inplace=True returns None
```
Refer to examples/tests/QuantumRingsLib-parameter-binding-test.py for a complete working and failing test.

* ⚠️ Qiskit-Based Integration: Using quantumrings.toolkit.qiskit
If you are using Qiskit circuits with the Quantum Rings Toolkit (e.g., QrEstimatorV1, QrBackendV2, or QrSamplerV1), parameter handling is different:

Qiskit circuits should not use .assign_parameters() after transpilation.

Instead, you must provide parameter values directly using the parameter_values argument in a nested list format: [[]].

Transpiling a circuit will remove symbolic parameters, so assigning parameters after transpilation will usually fail silently.

### Incorrect (Fails in Toolkit):
```
transpiled_qc = transpile(qc, backend)
transpiled_qc.assign_parameters({gamma: np.pi})  # ❌ May not work
```

Correct (Toolkit Execution with Parameters):
```
parameter_values = [[np.pi / 2, np.pi / 3]]
job = estimator.run([transpiled_qc], [hamiltonian], parameter_values)
result = job.result()
print("Expectation value:", result.values)
```

### ✅ Best Practices Summary
* For native QuantumRingsLib circuits, use .assign_parameters() with inplace=True and string-based keys.
* For Qiskit circuits using the Quantum Rings toolkit, always pass parameter values via parameter_values=[[...]].
* Never mix Parameter and float in multi-argument gates like u().
* Always assign parameter values before transpilation if you plan to remove symbolic expressions.


# 📌 Part III: Common Issues & Fixes
Error Message	Cause	Solution
Invalid Argument Passed for Quantum Circuit	QrBackendV2.run(qc) received a QuantumRingsLib.QuantumCircuit instead of Qiskit.QuantumCircuit.	
* ✅ Use QuantumCircuit from Qiskit, NOT QuantumRingsLib.QuantumCircuit.
job_monitor() TypeError	job_monitor() is not compatible with QrBackendV2.	
* ✅ Use manual polling (while not job.in_final_state(): ...).
Transpile Required	Qiskit circuits must be transpiled before running on Quantum Rings.	
* ✅ Use transpile(qc, backend, initial_layout=...) before execution.
### 📌 Conclusion
This guide provides a concise yet comprehensive summary of important changes in Qiskit 1.4.x while detailing key differences between Qiskit and Quantum Rings.

### 🚀 Key Takeaways
* ✅ Use cx() (not cnot()) in Qiskit
* ✅ Transpile Qiskit circuits for QrBackendV2, but NOT for QrEstimatorV1
* ✅ Manually monitor jobs when using Quantum Rings (QrBackendV2)
* ✅ Quantum Rings does NOT support register slicing (c[:2]), use explicit indexing (c[0]) instead
* ✅ No built-in qft() or iqft or qft_inverse() in Quantum Rings – must be implemented manually

By following these guidelines, both human developers and LLMs can effectively write, debug, and optimize quantum circuits using Qiskit 1.4.x while understanding the differences in Quantum Rings execution.

🚀 End of Guide 🚀