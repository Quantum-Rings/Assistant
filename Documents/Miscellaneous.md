Quantum Rings' official website at https://www.quantumrings.com/

Quantum Rings Email: info@quantumrings.com

Quantum Rings Address:
2000 Central Ave,
Suite 100,

Quantum Rings GitHub: https://github.com/Quantum-Rings

How can users contribute to improving and updating this Quantum Rings help file?
Go to https://github.com/Quantum-Rings/Assistant

How can users submit bugs?
Go to https://github.com/Quantum-Rings/Assistant/Bugs

## Best Practices

* Convert from Pennylane or Cirq or Q# to QuantumRings
* Convert native code to QASM and then read the QASM into QuantumRings
* Always place the provider authentication and backend definition before they are needed in the code.  
* A good practice is to define the provider and backend directly following the import section.
* It is good practice to include the provider and backend outside of a def, unless they are being strategically localized. 

### ⚠️ Required FOR ALL CIRCUIT CREATION IN QuantumRingsLib
Before constructing any QuantumCircuit, QuantumRegister, or ClassicalRegister objects, you MUST initialize and activate a QuantumRingsProvider. This step authenticates your access and allocates qubits, even if you're not executing the circuit.

```
from QuantumRingsLib import QuantumRingsProvider

provider = QuantumRingsProvider(token="YOUR_API_KEY", name="YOUR_EMAIL")
provider.active_account()
```
✅ You do not need to define a backend unless you plan to execute the circuit using backend.run(qc) or other backend-specific functions.

### 🧠 Optimization Strategy for Native QuantumRingsLib Circuits
When working with QuantumRingsLib-native circuits, the LLM should automatically consider using:

```
from QuantumRingsLib import OptimizeQuantumCircuit
```
Use OptimizeQuantumCircuit(qc) when:

* The circuit is part of a core algorithm or non-trivial computation.
* The circuit has multiple qubits, deep gate sequences, or repeated patterns.
* The goal is to improve performance before execution or reduce circuit complexity.
⚠️ The function modifies qc in-place and returns a bool indicating success:

```
success = OptimizeQuantumCircuit(qc)  # ✅ Never assign result back to `qc`
```
❌ Do not use this function with qiskit.QuantumCircuit objects or within quantumrings.toolkit.qiskit workflows.
Use transpile() instead for Qiskit circuits.

✅ If generating circuits for variational algorithms, QAOA, QFT, or similar native SDK workflows, the LLM should add this optimization step before execution.

# QuantumRingsLib 0.9.x vs 0.10.x
Use this guide to debug code based on the SDK version in use. If a user reports an error, ask them to run this version check and paste the result into chat:
```
from QuantumRingsLib import __version__
print("QuantumRingsLib version:", __version__)
```
## ✅ What Works and What Fails

### Positional shots in backend.run():

* In 0.9.x, calling backend.run(qc, 100) raises a TypeError.
* In 0.10.x, this positional form works.
* In both versions, using shots=100 always works and is safest.

### ✅ Parameterized Circuits (Parameter, ParameterVector)

QuantumRingsLib 0.9 and 0.10 both define `Parameter` and `ParameterVector`,
and contrary to earlier notes, parameter binding **is supported** if used correctly.

#### ✅ What Works:

- Use `.assign_parameters(my_dict, inplace=True)`
- Ensure that all parameters passed to a multi-argument gate (like `u(...)`) are either all `Parameter` or all `float`
- Use **string-based keys** in the parameter dictionary, e.g., `"theta"` or `"p[0]"`

**Example (WORKS):**
```
from QuantumRingsLib import Parameter, ParameterVector

theta = Parameter("theta")
phi = Parameter("phi")
lam = Parameter("lambda")
vec = ParameterVector("p", 2)

qc.u(theta, phi, lam, q[0])  # All parameters are valid
qc.assign_parameters({
    "theta": 3.14,
    "phi": 1.57,
    "lambda": 0.785,
}, inplace=True)
```
**❌ What Fails:**
* Mixing float and Parameter in the same gate call:
```
qc.u(theta, 0, 0, q[0])  # ❌ fails — mixed types
```

* Using Parameter objects as dictionary keys:
```
qc.assign_parameters({theta: 3.14})  # ❌ fails — keys must be strings
```

* Omitting inplace=True in .assign_parameters():
```
new_qc = qc.assign_parameters({...})  # ❌ returns None — not supported
```
⚠️ Developer Tip:
If you're unsure, run parameter_binding_test.py in /examples/tests/ to validate your usage.

### Classical Register Slicing:
* Expressions like c[:2] raise a TypeError.
* Only individual access works: c[0], c[1], etc.
job_monitor() and wait_for_final_state():
* These are stable in both versions.
* They provide blocking job monitoring and callbacks as expected.

# 🔍 Confirmed Change in 0.10.x
The only confirmed API improvement in 0.10.x is:
* Positional arguments in backend.run() now work
Everything else — including parameter handling and classical register limitations — remains unchanged.

# ⚠️ Common Pitfalls to Avoid (LLM Guidance)
* Do not assume Qiskit’s assign_parameters() or bind_parameters() work in the native SDK
* If you see a pybind11 casting error, it’s likely related to parameter usage
* If a user gets a TypeError from backend.run(qc, 100), they are using 0.9.x
* Always use shots=... syntax for version-safe code

# 🧪 Additional Tests (For Future Enhancements)
If needed, consider testing:
* Chained use of parameters across multiple gates
* Assigning parameters during construction instead of post hoc
* Passing parameter values in batch-mode estimators
* Appending parameterized sub-circuits
These are not critical for day-to-day debugging but could matter in advanced workflows.


## LLM Instructions

This section provides structured guidance for LLMs and documentation tools when analyzing example code files in this SDK.

### ✅ Code Example Metadata Block

Each `.py` or `.ipynb` file should begin with a YAML-style metadata block. This block helps describe the context, version compatibility, and purpose of the example.

Use the following format:

```
# ---
# title: <Brief title of the example>
# sdk:
#   QuantumRingsLib: [<version(s)>]
#   quantumrings-toolkit-qiskit: [<version(s)>]
#   GPU-enabled: [true, false]
#   Qiskit: [<version(s)>]
# python: [<version(s)>]
# os: [<platform(s)>]
# tags: [<descriptive topics>]
# description: >
#   Multi-line summary of what the example tests, demonstrates, or explores.
#   Include parameter usage, expected inputs/outputs, and version-specific notes if needed.
# ---
```

All fields are optional, but inclusion is strongly encouraged.

### 📘 Version Status Annotations

Each version in a list may be annotated to describe its compatibility:

- `version` (e.g., `0.10`) — ✅ confirmed working (tested)
- `version?` (e.g., `1.2.0?`) — ❓ untested, but expected to work
- `version!` (e.g., `0.9!`) — ❌ known not to work or incompatible

Examples:

- `QuantumRingsLib: [0.9, 0.10]` — tested and works in both versions
- `quantumrings-toolkit-qiskit: [1.2.0, 1.3.0?]` — 1.2.0 confirmed, 1.3.0 untested
- `GPU-enabled: [true, false!]` — works on GPU, known to fail on CPU-only systems
- `python: [3.11, 3.10?]` — tested on 3.11, expected to work on 3.10
- `os: [windows-11, linux-ubuntu-22.04?]` — tested on Windows, untested on Linux

**Note:** The absence of a version does **not** imply incompatibility. It simply means the version has not been tested or declared.

### 🧠 Purpose

This metadata is intended to:

- Help LLMs determine which examples apply in specific runtime contexts
- Allow test harnesses to validate compatibility across SDK versions
- Support doc generators, search indexing, and structured filtering

Please include this header in any example where SDK, toolkit, or version behavior is relevant.

### 🚫 When Not to Use

- One-liner examples inside Markdown files
- Trivial print/test statements
- Docstring-only snippets with no runtime behavior

## Qiskit Integration Rule
Use qiskit.QuantumCircuit and related components only as supported through quantumrings.toolkit.qiskit.

✅ Preferred: Use QuantumCircuit, Parameter, SparsePauliOp, and similar classes from Qiskit when integrated via quantumrings.toolkit.qiskit.
❌ Avoid using Qiskit modules such as qiskit.algorithms, qiskit.opflow, or AerSimulator.

All execution must be routed through Quantum Rings backends, such as QrBackendV2, QrEstimatorV1/V2, or QrSamplerV1/V2.