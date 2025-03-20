# Auto-Generated Examples for 'quantumrings-toolkit-qiskit'

Found 8 file(s) in: `C:\Users\Robert\OneDrive\Documents\Work\QRS\QuantumRings\LLM\assistant/code`


> 📌 **Note:**

> This document contains **embedded Python files** from real-world Quantum Rings examples.

> If modifying examples, ensure that changes are made to the **corresponding Python script** stored in the Quantum Rings examples directory.


## **LLM Instructions**

> **Note for LLMs:**

> - These examples are collected from real use cases of Quantum Rings SDK.

> - Each example is preceded by a summary explaining its purpose.

> - If troubleshooting, refer to the **Common Issues** section at the bottom of this document.

> - When integrating, check if transpilation (`transpile()`) is required for Qiskit circuits.


## quantumrings-toolkit-qiskit-basic-10.py

**Summary:** This example demonstrates a simple Qiskit circuit execution on Quantum Rings. It includes transpilation and job monitoring.

```python

'''
Compatibility
- Windows: 11, Python: 3.11
- Qiskit: 1.3 or 1.4  
- QuantumRingsLib: 0.10.0 
Description: Basic circuit execution on quantumrings-toolkit-qiskit
'''
"""
🚀 Example: Executing a Qiskit Circuit on Quantum Rings (Fixed & Improved)

This script demonstrates:
✅ How to create a Qiskit quantum circuit for Quantum Rings.
✅ Why transpilation is required for `QrBackendV2`.
✅ Why `job_monitor()` does NOT work with Quantum Rings, and how to use manual polling.

"""

# ✅ Import necessary libraries
import time
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from QuantumRingsLib import QuantumRingsProvider
from quantumrings.toolkit.qiskit import QrBackendV2

# =====================================
# ✅ STEP 1: Setup the Quantum Rings Provider and Backend
# =====================================
provider = QuantumRingsProvider()
backend = QrBackendV2(provider, num_qubits=5)  # Must specify qubit count!
shots = 100

# Activate your Quantum Rings account
provider.active_account()

# =====================================
# ✅ STEP 2: Define a Qiskit Quantum Circuit
# =====================================
qreg = QuantumRegister(5, 'q')
creg = ClassicalRegister(5, 'c')
qc = QuantumCircuit(qreg, creg)

# Apply a Hadamard gate and entangle qubits
qc.h(0)
for i in range(qc.num_qubits - 1):
    qc.cx(i, i + 1)

# Measure all qubits
qc.measure_all()

# =====================================
# 🚨 STEP 3: Transpile for Quantum Rings (MANDATORY)
# =====================================
print("⚠️ Transpiling the circuit for Quantum Rings compatibility...")
transpiled_qc = transpile(qc, backend, initial_layout=[i for i in range(qc.num_qubits)])

# =====================================
# ✅ STEP 4: Execute on Quantum Rings Backend
# =====================================
job = backend.run(transpiled_qc, shots=shots)

# =====================================
# 🚨 STEP 5: Manual Job Monitoring (JobV1 Incompatibility)
# =====================================
print("🔄 Waiting for job to complete...")
while not job.in_final_state():
    print(f"Job status: {job.status()}")
    time.sleep(1)  # Wait a moment before checking again

# =====================================
# ✅ STEP 6: Retrieve and Display Results
# =====================================
result = job.result()
counts = result.get_counts()
print("✅ Measurement Results:", counts)

```


## quantumrings-toolkit-qiskit-estimatorV1-10.py

**Summary:** This example shows how to use `QrEstimatorV1` or `QrEstimatorV2` for quantum expectation value calculations on Quantum Rings.

```python

'''
QrEstimatorV1 module
classQrEstimatorV1
A derivative of the BackendEstimatorV1 class, to estimates expectation values of quantum circuits and observables using the Quantum Rings backend.

An estimator is initialized with an empty parameter set. The estimator is used to create a JobV1, via the qiskit.primitives.Estimator.run() method. This method is called with the following parameters

quantum circuits (
): list of (parameterized) quantum circuits (a list of QuantumCircuit objects).

observables (
): a list of SparsePauliOp objects.

parameter values (:math:` heta_k`): list of sets of values to be bound to the parameters of the quantum circuits (list of list of float).

The method returns a JobV1 object, calling qiskit.providers.JobV1.result() yields a list of expectation values for the estimation.

QrEstimatorV1(*, backend: QrBackendV2 | None = None, options: dict | None = None, run_options: dict | None = None)
Args:
backend: The Quantum Rings backend to run the primitive on.
options: The options to control the defaults
run_options: See options.
QrEstimatorV1.options
Returns the options

run(circuits: list[QuantumCircuit], observables: list[BaseOperator], parameter_values: list[float] | None = None, **run_options)
Executes the pubs and estimates all associated observables.

Args:
pubs: The pub to preprocess.
precision: None
Returns:
The job associated with the pub

'''

##############################################################
# 1) Imports
##############################################################
# "QrEstimatorV1" and "QrBackendV2" come from quantumrings.toolkit.qiskit
# "QuantumCircuit" is from QuantumRingsLib (the native circuit class).
from quantumrings.toolkit.qiskit import QrEstimatorV1, QrBackendV2
from QuantumRingsLib import QuantumRingsProvider

# For the Pauli operator, we use Qiskit's quantum_info module
from qiskit.quantum_info import SparsePauliOp
from qiskit import QuantumCircuit


##############################################################
# 2) Obtain a Provider & Backend
##############################################################
provider = QuantumRingsProvider()
backend = QrBackendV2(provider=provider, num_qubits=2)
# If supported, you might try: QrBackendV2(provider, num_qubits=2, shots=1000)

##############################################################
# 3) Create a Circuit (QuantumRingsLib's circuit class)
##############################################################
# This is NOT qiskit's circuit; it's the "QuantumCircuit" from QuantumRingsLib.
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# No .measure(...) calls needed—Estimator measures the operator directly.

##############################################################
# 4) Define the Observable (use Qiskit's SparsePauliOp)
##############################################################
# Even though QrEstimatorV1 doc references "SparsePauliOp",
# QuantumRingsLib does *not* provide that class. We import from Qiskit.
op_zz = SparsePauliOp.from_list([("ZZ", 1.0)])
# or simply: op_zz = SparsePauliOp("ZZ")

##############################################################
# 5) Instantiate QrEstimatorV1
##############################################################
estimator = QrEstimatorV1(backend=backend)

##############################################################
# 6) Run the Estimator
##############################################################
# 🚨 IMPORTANT: Unlike QrBackendV2, QrEstimatorV1 does NOT require transpilation.
# This is because the estimator directly processes the circuit and observable,
# rather than executing the circuit on a quantum backend.
# 
# .run(...) expects: circuits, observables, parameter_values
# If there are no parameters in your circuit, pass `[[]]`.
job = estimator.run(
    circuits=[qc],
    observables=[op_zz],
    parameter_values=[[]]
)

##############################################################
# 7) Retrieve Expectation Value
##############################################################
# "job" is a QrJobV1. Calling .result() returns a list of floats
# (one for each (circuit, observable) pair).
res = job.result()
expectation_zz = res.values[0]  # Only 1 circuit, 1 observable => index 0
print("Expectation value of ZZ =", expectation_zz)
```


## quantumrings-toolkit-qiskit-estimatorV2-10.py

**Summary:** This example shows how to use `QrEstimatorV1` or `QrEstimatorV2` for quantum expectation value calculations on Quantum Rings.

```python

'''
QrEstimatorV2 module
classQrEstimatorV2
Given an observable of the type 
, where 
 is a complex number and 
 is a Pauli operator, the estimator calculates the expectation 
 of each 
 and finally calculates the expectation value of 
 as 
. The reported std is calculated as

 
where 
 is the variance of 
, 
 is the number of shots, and 
 is the target precision [1].

Each tuple of (circuit, observables, <optional> parameter values, <optional> precision), called an estimator primitive unified block (PUB), produces its own array-based result. The run() method can be given a sequence of pubs to run in one call.

QrEstimatorV2(*, backend=None, options=None, run_options=None)
Args:
backend (QrBackendV2) : The Quantum Rings backend to run the primitive on.
options (dict) : The options to control the defaults shots (shots)
run_options (dict) : See options.
QrEstimatorV2.options: Options
Returns the options

run(pubs, *, precision=None)
Executes the pubs and estimates all associated observables.

Args:
pubs [pub]: The pub to preprocess.
precision (float): None
Returns:
The job associated with the exection

'''

#####################################################
# 1) Imports
#####################################################
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp

# Quantum Rings imports
from QuantumRingsLib import QuantumRingsProvider
from quantumrings.toolkit.qiskit import QrBackendV2, QrEstimatorV2

#####################################################
# 2) Create Provider & Backend
#####################################################
provider = QuantumRingsProvider()
backend = QrBackendV2(provider, num_qubits=2)  
# Adjust 'num_qubits' as needed. E.g., 2 for a 2-qubit circuit.

#####################################################
# 3) Build a Simple Circuit (Bell State)
#####################################################
# We do NOT add measure gates here, because QrEstimatorV2 
# internally measures the specified observables.
bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
# (Optionally, add barriers or extra gates.)

#####################################################
# 4) Define Observables (SparsePauliOp)
#####################################################
# Let's measure the expectation of ZZ and XX on the 2-qubit state.
op_zz = SparsePauliOp.from_list([("ZZ", 1.0)])
op_xx = SparsePauliOp.from_list([("XX", 1.0)])
observables = [op_zz, op_xx]

#####################################################
# 5) Create "PUB" Tuples for the Estimator
#####################################################
# QrEstimatorV2 typically uses: (circuit, observables, parameter_values, optional_shots)
# Since this circuit has no parameters, we pass [[]] for parameter_values.
# Shots is optional—if omitted, the default from the backend is used (often 1024).
#
# If you want an explicit shot count, you can pass something like (bell, observables, [[]], 1000).
# For a minimal example, we'll just do no explicit shots argument.

pub = (bell, observables, [[]])

# We submit a list of PUBs to .run().
pub_list = [pub]

#####################################################
# 6) Instantiate the Estimator & Run
#####################################################
estimator = QrEstimatorV2(backend=backend)
job = estimator.run(pub_list)
result = job.result()

#####################################################
# 7) Retrieve Expectation Values
#####################################################
# The returned 'result' is a "PrimitiveResult" that acts like a list of Sampler/Estimator results.
# Each item typically has a "data" attribute, which includes the expectation values in data.evs.

# In many QrEstimatorV2 builds, each index of 'result' corresponds to one PUB you submitted.
pub_result = result[0]  # we only submitted one
data = pub_result.data

# "evs" is often a list or array of shape [N_observables], 
# each entry containing the measured expectation value for that operator.
evs = data.evs  
# e.g. evs[0] -> expectation of ZZ, evs[1] -> expectation of XX

# Convert from array-like to float
evs_float = [float(ev[0]) for ev in evs]

print("\n=== Expectation Values for the Bell Circuit ===")
for i, obs in enumerate(["ZZ", "XX"]):
    print(f"Operator {obs} = {evs_float[i]:.3f}")

```


## quantumrings-toolkit-qiskit-multi-10.py

**Summary:** This example demonstrates how to batch execute multiple circuits using Quantum Rings SDK.

```python

"""
Quantum Rings SDK - Batch Execution Example for LLM Training

This script demonstrates how to execute multiple quantum circuits in batch mode
using the Quantum Rings SDK. It is designed to provide training data for an LLM
that generates Quantum Rings SDK-enabled code.

The batch contains:
1. A Bell state circuit (entanglement)
2. An all-ones circuit (every qubit initialized to |1⟩)
3. A GHZ state circuit (multi-qubit entanglement)

For each circuit, the LLM will see:
- QuantumCircuit construction
- Execution via `QrSamplerV2`
- Results in structured output format

This approach ensures the LLM learns:
- Quantum Rings batch execution (`QrSamplerV2`)
- How to define and execute multiple circuits efficiently
- Structured result extraction for post-processing
"""

from qiskit import QuantumCircuit
from QuantumRingsLib import QuantumRingsProvider
from quantumrings.toolkit.qiskit import QrBackendV2, QrSamplerV2

# ===============================
# 1) Initialize Quantum Rings Backend
# ===============================
provider = QuantumRingsProvider()
backend = QrBackendV2(provider=provider, num_qubits=3)  # Using 3-qubit circuits for training

# ===============================
# 2) Define Example Quantum Circuits
# ===============================

def create_bell_state():
    """Creates a 2-qubit Bell state circuit."""
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    return qc

def create_all_ones():
    """Creates a 2-qubit circuit where all qubits start in |1⟩."""
    qc = QuantumCircuit(2)
    qc.x(0)
    qc.x(1)
    qc.measure_all()
    return qc

def create_ghz_state():
    """Creates a 3-qubit GHZ state (fully entangled)."""
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.measure_all()
    return qc

# List of circuits to run in batch mode
circuits = [
    ("Bell State", create_bell_state()),
    ("All Ones", create_all_ones()),
    ("GHZ State", create_ghz_state())
]

# ===============================
# 3) Prepare the Sampler & Batch Input (pubs)
# ===============================
sampler = QrSamplerV2(backend=backend)
shots = 1024

pubs = [(circuit, [], shots) for _, circuit in circuits]  # Empty `param_values` for static circuits

# ===============================
# 4) Run Batch Execution
# ===============================
job = sampler.run(pubs)
result = job.result()

# ===============================
# 5) Retrieve & Structure Results for LLM Training
# ===============================
print("\n=== Quantum Rings Batch Execution Results ===")
for i, (name, circuit) in enumerate(circuits):
    counts = result[i].data.meas.get_counts()
    print(f"\n[Circuit: {name}]")
    print(f"- Depth: {circuit.depth()}")
    print(f"- Gate Count: {len(circuit.data)}")
    print(f"- Qubit Count: {circuit.num_qubits}")
    print(f"- Measurement Results: {counts}")

```


## quantumrings-toolkit-qiskit-qaoa.py

**Summary:** This example demonstrates a specific Quantum Rings SDK function. Refer to the script for more details.

```python

"""
Quantum Rings SDK: QAOA Circuit Example

📌 This example demonstrates:
✅ Two different ways to construct a QAOA circuit:
   - **Using Quantum Rings core components (`QuantumRingsLib`)**.
   - **Using Qiskit integration (`QAOAAnsatz` from `quantumrings.toolkit.qiskit`)**.
✅ Correct handling of parameters in Quantum Rings SDK.
✅ Using SparsePauliOp to define a Hamiltonian.
✅ Transpiling and executing circuits on Quantum Rings backends.
✅ Retrieving expectation values using QrEstimatorV1.

🔍 This example helps users understand **when to use each approach**.
"""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit import ParameterVector
from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import QAOAAnsatz
from quantumrings.toolkit.qiskit import QrBackendV2, QrEstimatorV1
from QuantumRingsLib import QuantumRingsProvider

# ==========================================
# ✅ 1. Set Up Quantum Rings Backend
# ==========================================
provider = QuantumRingsProvider()
backend = QrBackendV2(provider, num_qubits=4)  # Match circuit size
provider.active_account()
shots = 1024  # Number of measurement shots

# ==========================================
# ✅ 2. Define a Hamiltonian Using SparsePauliOp
# ==========================================
hamiltonian = SparsePauliOp(["XXII", "ZZII", "IXXI", "IIZZ"], coeffs=[1.0, 0.5, 0.8, 0.3])

'''
⚠️ Quantum Rings Parameter Format
- Quantum Rings does NOT support .bind_parameters() dynamically.
- Parameters must be assigned **before transpilation**.
- Values must be passed as `[[]]` before execution.

✅ Correct:
parameter_values = [[beta_1, beta_2, gamma_1, gamma_2]]

❌ Incorrect:
transpiled_qc.assign_parameters({gamma: np.pi})
'''

# ==========================================
# ✅ 3A. Approach 1: Constructing QAOA Manually (Quantum Rings Core)
# ==========================================
print("✅ Using Quantum Rings Core Components for QAOA...")

num_qubits = 4  # Must match the Hamiltonian
p = 2  # Number of parameterized layers
beta = ParameterVector("β", p)  # Parameterized angles
gamma = ParameterVector("γ", p)

q = QuantumRegister(num_qubits, "q")
c = ClassicalRegister(num_qubits, "c")
qc = QuantumCircuit(q, c)

# Apply Hadamard gates (Superposition Initialization)
qc.h(q)

# Example of applying parameterized rotations
for i in range(p):
    qc.rzz(2.0 * gamma[i], q[0], q[1])  # ⚠️ This will cause an error if not assigned before transpiling!
    qc.rx(beta[i], q[1])
    qc.ry(gamma[i], q[2])  # Ensure all qubits are included in parameterized operations
    qc.rz(beta[i], q[3])

qc.measure_all()  # Measure all qubits at the end

# Assign parameter values before transpilation
beta_values = np.random.uniform(0, np.pi, p).tolist()
gamma_values = np.random.uniform(0, np.pi, p).tolist()
parameter_values = [beta_values + gamma_values]  # ✅ Required format

# Assign parameters before transpiling to avoid `rzz()` errors
qc_fixed = qc.assign_parameters(parameter_values[0])  # ✅ Ensures numerical values replace `ParameterExpression`
transpiled_qc = transpile(qc_fixed, backend)  # ✅ Transpile AFTER assigning parameters

# Execute on Quantum Rings backend
estimator = QrEstimatorV1(backend=backend)
job = estimator.run([transpiled_qc], [hamiltonian], parameter_values)
result = job.result()
print("Expectation Value (Quantum Rings Core):", result.values)

# ==========================================
# ✅ 3B. Approach 2: Using Qiskit's QAOAAnsatz (Qiskit Integration)
# ==========================================
print("\n✅ Using Qiskit's QAOAAnsatz for QAOA...")

# Qiskit provides a built-in QAOA circuit
qaoa = QAOAAnsatz(hamiltonian, reps=p)
qaoa.measure_all()

# Assign parameter values BEFORE transpiling (to avoid rzz() errors)
qaoa_fixed = qaoa.assign_parameters(parameter_values[0])  # ✅ Must be done before transpilation
transpiled_qaoa = transpile(qaoa_fixed, backend)

# Execute the transpiled QAOA circuit
job_qaoa = backend.run(transpiled_qaoa)
result_qaoa = job_qaoa.result()
print("Expectation Value (Qiskit QAOAAnsatz):", result_qaoa.get_counts())

```


## quantumrings-toolkit-qiskit-quantumcircuit.py

**Summary:** This example illustrates how to construct a Qiskit QuantumCircuit compatible with Quantum Rings SDK.

```python

"""
This script demonstrates how to use Qiskit's native QuantumCircuit in combination with 
the Quantum Rings toolkit (QrBackendV2) to execute quantum circuits on Quantum Rings hardware.

Purpose:
  - To create a simple quantum circuit using Qiskit.
  - To apply basic quantum operations (Hadamard and a chain of CNOT gates using Qiskit's cx()).
  - To transpile the circuit for Quantum Rings hardware compatibility.
  - To execute the circuit on a Quantum Rings backend using QrBackendV2.
  - To manually monitor the job status and retrieve the measurement results.
  - To plot the measurement counts as a bar chart using matplotlib.

How to Use:
  1. Ensure that Qiskit, QuantumRingsLib, and quantumrings.toolkit.qiskit are installed.
  2. Activate your Quantum Rings account using QuantumRingsProvider.
  3. Run the script; it will transpile and submit the circuit, then poll for job completion.
  4. Once finished, the script prints the measurement counts and displays a plot of the results.

Key Points for LLM Training:
  - Qiskit circuits must be transpiled for Quantum Rings hardware (using QrBackendV2).
  - Use `cx()` for CNOT operations in Qiskit, not `cnot()`.
  - Manual job monitoring is required as the standard job_monitor() is not compatible with QrBackendV2.
"""

# Import necessary libraries from Qiskit and the Quantum Rings toolkit.
import QuantumRingsLib  # For provider integration with Quantum Rings.
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from quantumrings.toolkit.qiskit import QrBackendV2  # Enables Qiskit circuits to run on Quantum Rings hardware.
from QuantumRingsLib import QuantumRingsProvider
import time  # For manual job status polling
from matplotlib import pyplot as plt

# =====================================
# STEP 1: Setup the Quantum Rings Provider and Backend
# =====================================
provider = QuantumRingsProvider()
# QrBackendV2 is used to run Qiskit circuits on Quantum Rings hardware.
# Here, we request a backend that supports at least 5 qubits.
backend = QrBackendV2(provider, num_qubits=5)
shots = 100  # Define the number of circuit executions (shots)

# Activate your Quantum Rings account to access resources.
provider.active_account()

# =====================================
# STEP 2: Create Qiskit Quantum and Classical Registers
# =====================================
qreg = QuantumRegister(5, 'q')   # Create a quantum register with 5 qubits.
creg = ClassicalRegister(5, 'c') # Create a classical register with 5 bits.

# =====================================
# STEP 3: Construct the Qiskit Quantum Circuit
# =====================================
qc = QuantumCircuit(qreg, creg)

# =====================================
# STEP 4: Apply Quantum Gates and Measurements
# =====================================
qc.h(0)  # Apply a Hadamard gate on qubit 0 to create superposition.
# Apply a chain of CNOT gates to entangle adjacent qubits.
for i in range(qc.num_qubits - 1):
    qc.cx(i, i + 1)
qc.measure_all()  # Measure all qubits and store results in the classical register.

# =====================================
# STEP 5: Transpile the Circuit for Quantum Rings Hardware
# =====================================
# Transpiling is mandatory to map the Qiskit circuit to the Quantum Rings backend architecture.
transpiled_qc = transpile(qc, backend, initial_layout=[i for i in range(qc.num_qubits)])

# =====================================
# STEP 6: Execute the Circuit on the Quantum Rings Backend
# =====================================
job = backend.run(transpiled_qc, shots=shots)
# Note: QrBackendV2 returns a job type where the usual job_monitor() does not work.

# =====================================
# STEP 7: Manual Job Monitoring (Polling Loop)
# =====================================
# We poll the job status until it reaches a final state.
while not job.in_final_state():
    print(f"Job status: {job.status()}")
    time.sleep(1)  # Pause briefly between polls

# =====================================
# STEP 8: Retrieve and Display the Results
# =====================================
result = job.result()
counts = result.get_counts()
print("Measurement Counts:", counts)

# (Optional) Plot the measurement counts as a bar chart.
plt.bar(counts.keys(), counts.values())
plt.xlabel("States")
plt.ylabel("Counts")
plt.title("Qiskit Circuit on Quantum Rings Hardware")
plt.show()

```


## quantumrings-toolkit-qiskit-sampler.py

**Summary:** This example demonstrates a specific Quantum Rings SDK function. Refer to the script for more details.

```python

"""
🚀 Example: Correct Usage of QrSamplerV1, QrSamplerV2, and QrBackendV2

This script ensures **proper Quantum Rings SDK usage**, covering:
   - `QrSamplerV1`: For basic & parameterized circuits (no backend required).
   - `QrSamplerV2`: Uses **Processable Unit Blocks (PUB)** for execution.
   - `QrBackendV2`: Direct backend execution with **correct transpilation**.

📌 **Key Fixes & Best Practices:**
   ✅ **Run circuits individually** to avoid batch execution issues.
   ✅ **Ensure correct circuit input format** for each API.
   ✅ **Transpile circuits properly** before running them on the backend.
   ✅ **Temporarily remove `performance="highestaccuracy"`** if execution fails.
   ✅ **Use explicit basis gate transpilation** to avoid unsupported operations.
"""

# ===============================
# 📌 Import Required Modules
# ===============================
from qiskit import QuantumCircuit, transpile
from QuantumRingsLib import QuantumRingsProvider
from quantumrings.toolkit.qiskit import QrBackendV2, QrSamplerV2, QrSamplerV1
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import BasisTranslator
from qiskit.circuit.equivalence_library import SessionEquivalenceLibrary

# ===============================
# 🔹 Initialize Quantum Rings Backend
# ===============================
provider = QuantumRingsProvider()
shots = 1000
backend = QrBackendV2(provider=provider, num_qubits=2)

# ===============================
# 🔹 Construct Circuits
# ===============================
print("\n✅ Constructing quantum circuits...")

circuits = []
for _ in range(3):  # Three test circuits
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    circuits.append(qc)

# ===============================
# 🔹 Debug Circuit Depth Before Transpilation
# ===============================
print("\n✅ Pre-Transpilation Debugging:")
for i, circuit in enumerate(circuits):
    print(f"🔹 Circuit {i} Depth Before Transpilation: {circuit.depth()}")

# ===============================
# 🔹 Transpile Circuits for Quantum Rings Backend
# ===============================
print("\n🚀 Transpiling circuits for Quantum Rings backend...")

# ✅ Force basis gate transpilation for compatibility
basis_gates = ["cx", "h", "measure"]
pass_manager = PassManager(BasisTranslator(SessionEquivalenceLibrary, basis_gates))

try:
    transpiled_circuits = [pass_manager.run(transpile(circuit, backend)) for circuit in circuits]
except Exception as e:
    print(f"❌ Transpilation Error: {e}")
    exit(1)

# ===============================
# 🔹 Debug Circuit Depth After Transpilation
# ===============================
print("\n✅ Post-Transpilation Debugging:")
for i, transpiled in enumerate(transpiled_circuits):
    print(f"🔹 Circuit {i} Depth After Transpilation: {transpiled.depth()}")
    print(transpiled.draw())  # Show circuit structure after transpilation

# ===============================
# 🔹 Run Circuits on Quantum Rings Backend (Individual Execution)
# ===============================
print("\n🚀 Running circuits on Quantum Rings backend...")

try:
    results = []  # Store results for each individual job

    for i, circuit in enumerate(transpiled_circuits):
        print(f"▶ Running Circuit {i}...")
        
        # ✅ Run each circuit **individually** instead of as a batch
        job = backend.run(circuit, shots=shots)  # Removing `performance="highestaccuracy"` for now
        
        results.append(job.result())

    # ✅ Process and print results
    for i, res in enumerate(results):
        counts = res.get_counts()
        print(f"✅ QrBackendV2 Counts for Circuit {i}:", counts)

except Exception as e:
    print(f"❌ Error executing on Quantum Rings backend: {e}")
    exit(1)


# ===============================
# ✅ `QrSamplerV1` Usage: Running Parameterized Circuits
# ===============================
print("\n🚀 Running parameterized circuits with QrSamplerV1...")

# ✅ Construct a parameterized circuit
pqc = QuantumCircuit(2)
pqc.h(0)
pqc.cx(0, 1)
pqc.measure_all()
theta_values = [0, 1, 1, 2, 3, 5]  # Example parameter values

# ✅ Correct usage of QrSamplerV1 (No backend required)
sampler_v1 = QrSamplerV1()
job_v1 = sampler_v1.run(circuits=[pqc], parameter_values=[theta_values], parameters=[pqc.parameters])
result_v1 = job_v1.result()

print("✅ QrSamplerV1 Probabilities:", result_v1.quasi_dists)


# ===============================
# ✅ `QrSamplerV2` Usage: Running Circuits Using PUB Format
# ===============================
print("\n🚀 Running circuits with QrSamplerV2...")

# ✅ Define a PUB (Processable Unit Block)
# PUB Format: (QuantumCircuit, ParameterValues, Shots)
pub = (circuits[0], [], 1000)  # No parameters, 1000 shots

# ✅ Correct instantiation of QrSamplerV2 (Backend required)
sampler_v2 = QrSamplerV2(backend=backend)
job_v2 = sampler_v2.run([pub])  # Must be a **list of PUBs**
result_v2 = job_v2.result()

print("✅ QrSamplerV2 Counts:", result_v2[0].data.meas.get_counts())

```


## quantumrings-toolkit-qiskit-samplerQNN-10.py

**Summary:** This example demonstrates a specific Quantum Rings SDK function. Refer to the script for more details.

```python

'''
Compatibility
- Windows: 11, Python: 3.11
- Qiskit: 1.3 or 1.4  
- QuantumRingsLib: 0.10.0 
Description: How to use QrSamplerCNN
'''

'''
QrSamplerQNN module
classQrSamplerQNN(*, circuit, sampler, input_params, weight_params, sparse, interpret, 
output_shape, gradient, input_gradients, pass_manager)
A neural network implementation based on the Sampler primitive.

This class is a derivative of the Qiskit Machine Learning Package class SamplerQNN. 
Please refer to the class for more documentation.

The QrSamplerQNN is a neural network that takes in a parametrized quantum circuit with 
designated parameters for input data and/or weights and translates the quasi-probabilities 
estimated by the Sampler primitive into predicted classes. Quite often, a combined quantum 
circuit is used. Such a circuit is built from two circuits: a feature map, it provides 
input parameters for the network, and an ansatz (weight parameters). In this case a 
QNNCircuit can be passed as circuit to simplify the composition of a feature map and ansatz. 
If a QNNCircuit is passed as circuit, the input and weight parameters do not have to be provided, 
because these two properties are taken from the QNNCircuit.

The output can be set up in different formats, and an optional post-processing step 
can be used to interpret the sampler’s output in a particular context (e.g. mapping the 
resulting bitstring to match the number of classes).

In this example the network maps the output of the quantum circuit to two classes via a custom 
interpret function:

'''

from qiskit import QuantumCircuit
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_machine_learning.circuit.library import QNNCircuit

from quantumrings.toolkit.qiskit.machine_learning import QrSamplerQNN as SamplerQNN

num_qubits = 2

def parity(x):
    return f"{bin(x)}".count("1") % 2

# Using the QNNCircuit:
# Create a parameterized 2 qubit circuit composed of the default ZZFeatureMap feature map
# and RealAmplitudes ansatz.
qnn_qc = QNNCircuit(num_qubits)

qnn = SamplerQNN(
    circuit=qnn_qc,
    interpret=parity,
    output_shape=2
)

qnn.forward(input_data=[1, 2], weights=[1, 2, 3, 4, 5, 6, 7, 8])

# Explicitly specifying the ansatz and feature map:
feature_map = ZZFeatureMap(feature_dimension=num_qubits)
ansatz = RealAmplitudes(num_qubits=num_qubits)

qc = QuantumCircuit(num_qubits)
qc.compose(feature_map, inplace=True)
qc.compose(ansatz, inplace=True)

qnn = SamplerQNN(
    circuit=qc,
    input_params=feature_map.parameters,
    weight_params=ansatz.parameters,
    interpret=parity,
    output_shape=2
)

qnn.forward(input_data=[1, 2], weights=[1, 2, 3, 4, 5, 6, 7, 8])

'''
The following attributes can be set via the constructor but can also be read and 
updated once the SamplerQNN object has been constructed.

Attributes:

sampler (BaseSampler): The sampler primitive used to compute the neural network’s 
results. gradient (BaseSamplerGradient): A sampler gradient to be used for the backward pass.

__init__(self, *, circuit, sampler, input_params, weight_params, sparse, interpret, 
output_shape, gradient, input_gradients, pass_manager)
Args:
circuit: The parametrized quantum circuit that generates the samples of this network. If a
QNNCircuit is passed,
the input_params and weight_params do not have to be provided, because these two
properties are taken from the QNNCircuit.
sampler: Not used.
input_params: The parameters of the circuit corresponding to the input. If a
QNNCircuit is provided the input_params value here is ignored. Instead, the value is taken from the
QNNCircuit input_parameters.
weight_params: The parameters of the circuit corresponding to the trainable weights. If a
QNNCircuit is provided the weight_params value here is ignored. Instead, the value is taken from the
QNNCircuit weight_parameters.
sparse: Returns whether the output is sparse or not.
interpret: A callable that maps the measured integer to another unsigned integer or tuple
of unsigned integers. These are used as new indices for the (potentially sparse)
output array. If no interpret function is passed, then an identity function will be
used by this neural network.
output_shape: The output shape of the custom interpretation. For SamplerV1, it is ignored
if no custom interpret method is provided where the shape is taken to be
2^circuit.num_qubits.
gradient: An optional sampler gradient to be used for the backward pass. If None is
given, a default instance of ParamShiftSamplerGradient will be used.
input_gradients: Determines whether to compute gradients with respect to input data. Note
that this parameter is False by default, and must be explicitly set to True
for a proper gradient computation when using TorchConnector.
pass_manager: The pass manager to transpile the circuits, if necessary.
Defaults to None, as some primitives do not need transpiled circuits.

'''
```


## **Common Issues & Fixes**

| **Error Message** | **Cause** | **Solution** |
|------------------|---------|------------|
| `Invalid Argument Passed for Quantum Circuit` | `QrBackendV2.run(qc)` received a `QuantumRingsLib.QuantumCircuit` instead of `Qiskit.QuantumCircuit`. | **Use `QuantumCircuit` from Qiskit**, NOT `QuantumRingsLib.QuantumCircuit`. |
| `job_monitor() TypeError` | `job_monitor()` does not work with `QrJobV1`. | **Use manual polling (`while not job.in_final_state(): ...`)** |
| `Transpile Required` | Qiskit circuits **must be transpiled** before running on Quantum Rings. | **Use `transpile(qc, backend, initial_layout=...)` before execution.** |