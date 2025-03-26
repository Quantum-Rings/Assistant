# Auto-Generated Code Examples


> 📌 **Note:**
> This document contains **embedded Python files** from the code examples directory.
> If modifying examples, ensure that changes are made to the **corresponding Python script** stored in the repository.

## **LLM Instructions**

> **Note for LLMs:**
> - These examples are collected from real-world use cases.
> - Each example is preceded by a summary explaining its purpose.
> - If troubleshooting, refer to the **Common Issues** section at the bottom of this document.
> - When integrating, check if transpilation (`transpile()`) is required.


## QuantumRingsLib-basic-10.py

**Summary:** This example demonstrates a simple circuit execution with proper job monitoring.

```python
# ---
# title: Quantumringslib Basic 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['basic', 'execution', 'job_monitor', 'backend.run']
# description: >
#   This example demonstrates a simple Qiskit circuit execution on Quantum Rings. 
#   It includes transpilation and job monitoring using QuantumRingsLib version 0.10.x. 
#   The circuit uses a Hadamard gate followed by a cascade of CNOT gates, and measures all qubits.
# ---

import QuantumRingsLib
from QuantumRingsLib import QuantumRegister, ClassicalRegister, QuantumCircuit
from QuantumRingsLib import QuantumRingsProvider
from QuantumRingsLib import job_monitor

# provision the provier and define the backend

# This is the standard way to provision the provider, replace your token and email addrss
# provider = QuantumRingsProvider(token =<YOUR_TOKEN_HERE>, name=<YOUR_ACCOUNT_NAME_HERE>)

# This is a way to provision the provider if you've saved your credentials
# see QuantumRingsLib-provider.py
provider = QuantumRingsProvider()
backend = provider.get_backend("scarlet_quantum_rings")
shots = 100
num_qubits=2

# activate credentials

provider.active_account()

# define registers

q = QuantumRegister(num_qubits)
c = ClassicalRegister(num_qubits)
qc = QuantumCircuit(q, c)

# construct the quantum circuit

qc.h(0);
for i in range (qc.num_qubits - 1):
    qc.cnot(i, i + 1);

qc.measure_all();

# Executing the Code

qc.measure_all();

job = backend.run(qc, shots)
job_monitor(job)
result = job.result()
print(result)
```


## QuantumRingsLib-basic-9.py

**Summary:** This example demonstrates a simple circuit execution with proper job monitoring.

```python
# ---
# title: Basic Quantum Circuit Execution (QuantumRingsLib 0.9.x)
# sdk:
#   QuantumRingsLib: [0.9.11]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: [basic, execution, QuantumRingsLib, backend.run, job_monitor]
# description: >
#   Demonstrates how to execute a simple quantum circuit using QuantumRingsLib <= 0.9.11.
#   Shows how to construct a circuit, execute it on the backend, and monitor job status.
#   Includes use of QuantumRegister, ClassicalRegister, and QuantumRingsProvider.
# ---

import QuantumRingsLib
from QuantumRingsLib import QuantumRegister, ClassicalRegister, QuantumCircuit
from QuantumRingsLib import QuantumRingsProvider
from QuantumRingsLib import job_monitor

# provision the provier and define the backend

# This is the standard way to provision the provider, replace your token and email addrss
# provider = QuantumRingsProvider(token =<YOUR_TOKEN_HERE>, name=<YOUR_ACCOUNT_NAME_HERE>)

# This is a way to provision the provider if you've saved your credentials
# see QuantumRingsLib-provider.py
provider = QuantumRingsProvider()
backend = provider.get_backend("scarlet_quantum_rings")
shots = 100
num_qubits = 2

# activate provider

provider.active_account()

# create circuit

qc = QuantumCircuit(num_qubits)

# construct the quantum circuit

qc.h(0);
for i in range (qc.num_qubits - 1):
    qc.cnot(i, i + 1);

qc.measure_all()

# Executing the Code

job = backend.run(qc, shots=shots)
job_monitor(job)
result = job.result()
counts = result.get_counts()
print(counts)






```


## QuantumRingsLib-control-10.py

**Summary:** This example demonstrates a specific function. Refer to the script for more details.

```python
# ---
# title: Quantumringslib Control 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['c_if', 'conditional', 'control-flow', 'job_monitor']
# description: >
#   Demonstrates use of conditional quantum logic in QuantumRingsLib version 0.10.x, 
#   specifically the `.c_if()` method for classical control over quantum gates.
#   Initializes qubits, measures into classical bits, then applies conditional operations 
#   based on classical register values. Executes the circuit using backend.run() 
#   and retrieves results after monitoring job completion.
# ---

import QuantumRingsLib
from QuantumRingsLib import QuantumRegister, ClassicalRegister, QuantumCircuit
from QuantumRingsLib import QuantumRingsProvider
from QuantumRingsLib import job_monitor

provider = QuantumRingsProvider()
backend = provider.get_backend("scarlet_quantum_rings")
shots = 100
num_qubits=4
provider.active_account()
q = QuantumRegister(num_qubits)
c = ClassicalRegister(num_qubits)
qc = QuantumCircuit(q, c)
qc.x([q[0],q[1]])
qc.measure(0, 0)
qc.measure(1, 1)
qc.reset(0)
qc.reset(1)
qc.x(q[1]).c_if(c[0],1)
qc.x(q[2]).c_if(c[1],1)
qc.measure_all();
# Executing the Code
job = backend.run(qc, shots)
job_monitor(job)
result = job.result()
counts = result.get_counts()
print(counts)
```


## QuantumRingsLib-no-slicing-10.py

**Summary:** This example demonstrates a specific function. Refer to the script for more details.

```python
# ---
# title: Quantumringslib No Slicing 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['compatibility', 'classical register', 'indexing', 'QuantumRingsLib']
# description: >
#   Compares classical register indexing behavior between Qiskit and QuantumRingsLib. 
#   Demonstrates that Quantum Rings does not support slicing of classical registers (e.g., c[:2]), 
#   and enforces explicit indexing (e.g., c[0], c[1]). 
#   Includes working and failing examples to clarify compatibility differences in classical measurement.
# ---

# Qiskit Test: ClassicalRegister Slicing vs Individual Indexing
try:
    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    print("\n=== QISKIT TEST ===")
    
    # Qiskit Classical Register
    c_qiskit = ClassicalRegister(4, "c_qiskit")

    # ✅ Works in Qiskit: ClassicalRegister allows slicing
    print("[Qiskit] c_qiskit[:2]:", c_qiskit[:2])  

    # ✅ Explicit indexing also works
    print("[Qiskit] c_qiskit[0]:", c_qiskit[0])  
    print("[Qiskit] c_qiskit[1]:", c_qiskit[1])  
    
except Exception as e:
    print("[Qiskit] ERROR:", e)

# Quantum Rings Test: ClassicalRegister Slicing vs Individual Indexing
try:
    import QuantumRingsLib
    from QuantumRingsLib import QuantumRegister, ClassicalRegister, QuantumCircuit

    print("\n=== QUANTUM RINGS TEST ===")
    
    # Quantum Rings Classical Register
    c_qr = ClassicalRegister(4, "c_qr")

    # ❌ Expected to FAIL in Quantum Rings: ClassicalRegister does not allow slicing
    try:
        print("[Quantum Rings] c_qr[:2]:", c_qr[:2])  
    except Exception as e:
        print("[Quantum Rings] ERROR (expected):", e)

    # ✅ Works in Quantum Rings: Explicit indexing
    print("[Quantum Rings] c_qr[0]:", c_qr[0])  
    print("[Quantum Rings] c_qr[1]:", c_qr[1])  

    # ✅ Test measurement with explicit indexing (no slicing)
    q = QuantumRegister(2, "q")
    qc = QuantumCircuit(q, c_qr)
    
    qc.measure(q[0], c_qr[0])  # ✅ Should work
    qc.measure(q[1], c_qr[1])  # ✅ Should work
    print("[Quantum Rings] Measurement assigned without slicing.")

except Exception as e:
    print("[Quantum Rings] ERROR:", e)

```


## QuantumRingsLib-param-10.py

**Summary:** This example demonstrates a specific function. Refer to the script for more details.

```python
# ---
# title: Quantumringslib Param 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['parameters', 'assign_parameters', 'ParameterVector', 'QuantumRingsLib']
# description: >
#   Demonstrates parameterized quantum circuit construction using QuantumRingsLib 0.10.x.
#   Shows how to use `Parameter` and `ParameterVector` for gates like `u()` and `mcp()`, 
#   and correctly assign values using `.assign_parameters(..., inplace=True)`.
#   Highlights best practices and pitfalls, such as avoiding mixed parameter types and 
#   ensuring all keys in assignment dictionaries are strings.
# ---

# ✅ Import necessary libraries
import QuantumRingsLib
from QuantumRingsLib import QuantumRegister, ClassicalRegister, QuantumCircuit, QuantumRingsProvider
from QuantumRingsLib import Parameter, ParameterVector
from qiskit import transpile  # ✅ Qiskit's transpile function (only for Qiskit circuits)
from math import pi

# =====================================
# ✅ STEP 1: Setup Quantum Rings Provider and Backend
# =====================================
provider = QuantumRingsProvider()
backend = provider.get_backend("scarlet_quantum_rings")  # Example backend
shots = 100  # Number of circuit executions (shots)
total_qubits = 5  # Define the total number of qubits for the circuit

# =====================================
# ✅ STEP 2: Create Quantum and Classical Registers
# =====================================
q = QuantumRegister(total_qubits, "q")
c = ClassicalRegister(total_qubits, "c")
qc = QuantumCircuit(q, c)

# =====================================
# ✅ STEP 3: Define Parameters for Parameterized Gates
# =====================================
# 🚨 WARNING: Always assign parameters BEFORE execution.

myparamvec = ParameterVector("test", 6)  # ✅ Safe for Quantum Rings SDK
theta = Parameter("theta")  # ✅ Safe for Quantum Rings SDK
phi = Parameter("phi")
lam = Parameter("lambda")
gamma = Parameter("gamma")

# =====================================
# ✅ STEP 4: Build the Quantum Circuit with Parameters
# =====================================
qc.h(q[0])  # Hadamard gate
qc.x(q[1])
qc.x(q[2])
qc.h(q[3])
qc.x(q[4])
qc.h(q[4])

# ✅ Safe use of parameters BEFORE execution
qc.mcp(theta, [q[0], q[1], q[3]], q[2])  
qc.rx(phi, 3)
qc.ry(pi / 2, 4)  
qc.rz(myparamvec[5], 0)
qc.u(myparamvec[0], myparamvec[1], myparamvec[2], 1)

# =====================================
# ✅ STEP 5: Assign Parameter Values BEFORE Execution
# =====================================
# 🚨 WARNING: Assigning parameters AFTER transpilation will FAIL.
myparam = {
    "test[0]": pi,
    "test[1]": pi / 2,
    "test[2]": pi / 3,
    "test[3]": pi / 4,
    "test[4]": pi / 6,
    "test[5]": pi / 7,
    "theta": pi / 8,
    "phi": pi / 9,
    "lambda": pi / 11,
    "gamma": pi / 13,
}

# ✅ Assign parameters BEFORE execution (SAFE)
qc.assign_parameters(myparam, inplace=True)  # ✅ Works correctly

# =====================================
# ✅ STEP 6: EXECUTE ON QUANTUM RINGS BACKEND (NO TRANSPILATION NEEDED)
# =====================================
print("\n🚀 Executing the Quantum Rings circuit...")
job = backend.run(qc, shots=shots)

# ✅ Monitor Job Execution
print("🔄 Waiting for job to complete...")
while not job.in_final_state():
    print(f"Job status: {job.status()}")
    time.sleep(1)

# ✅ Retrieve and Display Results
result = job.result()
counts = result.get_counts()
print("✅ Measurement Results:", counts)

# =====================================
# ✅ STEP 7: QISKIT CIRCUITS REQUIRE TRANSPILATION
# =====================================
# 🚨 WARNING: Quantum Rings SDK does NOT require transpilation for native circuits.
# ✅ If using a Qiskit circuit, use `transpile()` before execution.

# Example (ONLY for Qiskit circuits, not needed for Quantum Rings SDK):
# transpiled_qc = transpile(qc, backend)
# job = backend.run(transpiled_qc)  # ✅ Works for Qiskit circuits

print("\n🎉 SCRIPT COMPLETE: Follow best practices to avoid parameter assignment errors!")

```


## QuantumRingsLib-parameter-binding-test.py

**Summary:** This example demonstrates a specific function. Refer to the script for more details.

```python
# ---
# title: Quantumringslib Parameter Binding Test
# sdk:
#   QuantumRingsLib: [0.9.x, 0.10.x]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['parameter binding', 'Parameter', 'ParameterVector', 'QuantumRingsLib', 'diagnostic']
# description: >
#   Diagnostic script for testing parameter binding compatibility in QuantumRingsLib 0.9 and 0.10.
#   Verifies valid and invalid usage patterns involving Parameters and ParameterVectors.
#   Includes checks for type consistency, correct dictionary key usage, and inplace parameter assignment.
#   Helps identify common user mistakes and SDK version differences.
# ---

import math
from QuantumRingsLib import (
    QuantumRegister, ClassicalRegister, QuantumCircuit,
    Parameter, ParameterVector, QuantumRingsProvider
)

# =========================================================
# ✅ STEP 0: Activate Provider
# Required to construct circuits or registers in QuantumRingsLib
# =========================================================
provider = QuantumRingsProvider()  # Uses saved credentials if available
# provider = QuantumRingsProvider(token="YOUR_TOKEN", name="YOUR_EMAIL")
provider.active_account()

# =========================================================
# ✅ STEP 1: Create Registers and Circuit
# =========================================================
q = QuantumRegister(2, "q")
c = ClassicalRegister(2, "c")
qc = QuantumCircuit(q, c)

# Define parameters
theta = Parameter("theta")
phi = Parameter("phi")
lam = Parameter("lambda")
vec = ParameterVector("p", 2)

# =========================================================
# ✅ TEST 1: All Parameters of Same Type — WORKS
# =========================================================
print("\n✅ TEST 1: u() gate with all parameters (compatible types)")

try:
    qc.rx(theta, q[0])
    qc.ry(vec[0], q[0])
    qc.rz(phi, q[1])
    qc.u(theta, phi, lam, q[1])  # ✅ All args are Parameters

    param_dict = {
        "theta": math.pi / 2,
        "phi": math.pi / 3,
        "lambda": math.pi / 4,
        "p[0]": math.pi / 5
    }

    qc.assign_parameters(param_dict, inplace=True)
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])
    print("✅ assign_parameters + u() succeeded")
    print(qc.draw())
except Exception as e:
    print("❌ Unexpected failure:", e)

# =========================================================
# ❌ TEST 2: Mixed Parameter + Float — FAILS
# =========================================================
print("\n❌ TEST 2: u() with mixed Parameter + float (should fail)")

try:
    qc2 = QuantumCircuit(q, c)
    qc2.u(theta, math.pi / 2, math.pi / 3, q[1])  # ❌ Mixed types
    print("❌ ERROR: This should have failed due to type mismatch!")
except TypeError as e:
    print("✅ Correctly failed with TypeError:", e)
except Exception as e:
    print("❌ Unexpected error type:", e)

# =========================================================
# ❌ TEST 3: assign_parameters with Parameter keys — FAILS
# =========================================================
print("\n❌ TEST 3: assign_parameters() with Parameter keys (not strings)")

try:
    qc3 = QuantumCircuit(q, c)
    qc3.rx(theta, q[0])
    bad_keys = {theta: math.pi}
    qc3.assign_parameters(bad_keys, inplace=True)
    print("❌ ERROR: Should not accept Parameter objects as keys!")
except Exception as e:
    print("✅ Correctly failed:", e)

# =========================================================
# ❌ TEST 4: assign_parameters without inplace=True — Returns None
# =========================================================
print("\n❌ TEST 4: assign_parameters without inplace=True")

try:
    qc4 = QuantumCircuit(q, c)
    qc4.rx(theta, q[0])
    qc4.rz(phi, q[1])
    qc4.measure(q[0], c[0])
    qc4.measure(q[1], c[1])

    new_qc = qc4.assign_parameters({"theta": math.pi, "phi": math.pi / 2})
    if new_qc is None:
        print("✅ assign_parameters returned None (as expected)")
    else:
        print("❌ Unexpected: assign_parameters returned a circuit:", new_qc.draw())
except Exception as e:
    print("✅ Correctly failed or returned None:", e)

# =========================================================
# END
# =========================================================
print("\n✅ All tests completed.")

```


## QuantumRingsLib-provider.py

**Summary:** This example demonstrates a specific function. Refer to the script for more details.

```python
# ---
# title: Quantumringslib Provider Setup
# sdk:
#   QuantumRingsLib: [0.9.x, 0.10.x]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['provider', 'authentication', 'QuantumRingsProvider', 'setup']
# description: >
#   Demonstrates how to initialize and activate a QuantumRingsProvider using saved credentials 
#   or manual API token entry. Essential setup step for accessing Quantum Rings backends and 
#   executing circuits. Suitable for both persistent and interactive session management.
# ---

import QuantumRingsLib
from QuantumRingsLib import QuantumRingsProvider

#Acquire the Quantum Rings Provider
provider = QuantumRingsProvider(token ='<your key>', name='<your email>')
print("Account Name: ", provider.active_account()["name"], "\nMax Qubits: ", provider.active_account()["max_qubits"])

#Save the account locally.
provider.save_account(token ='<your key>', name='<your email>')
print(provider.saved_accounts(False, "default"))
```


## QuantumRingsLib-qasm-10.py

**Summary:** This example demonstrates a specific function. Refer to the script for more details.

```python
# ---
# title: Quantumringslib Qasm 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['qasm', 'qasm2', 'load', 'QuantumRingsLib', 'circuit loading']
# description: >
#   Demonstrates how to load and parse QASM 2.0 content into a QuantumRingsLib QuantumCircuit 
#   using the `qasm2.loads()` method. Highlights options for include paths, strict parsing, 
#   and error handling. Useful for importing circuits from external tools or text representations.
# ---

import QuantumRingsLib
from QuantumRingsLib import QuantumRingsProvider
from QuantumRingsLib import QuantumCircuit
provider = QuantumRingsProvider()
# to import QASM2 code:
qc = QuantumCircuit.from_qasm_file("test.qasm")
# to output QASM2 code use this:
qc.qasm(True)
```


## QuantumRingsLib-quantumcircuit.py

**Summary:** This example illustrates how to construct a quantum circuit compatible with the framework.

```python
# ---
# title: Quantumringslib Quantumcircuit
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['QuantumCircuit', 'construction', 'registers', 'QuantumRingsLib']
# description: >
#   Illustrates how to construct a quantum circuit using the native QuantumRingsLib QuantumCircuit class.
#   Includes manual instantiation of QuantumRegister and ClassicalRegister objects, as well as
#   usage of basic gates and circuit attributes. Intended to familiarize users with low-level
#   circuit building in the Quantum Rings SDK.
# ---



# Import the necessary modules from the Quantum Rings SDK.
import QuantumRingsLib
from QuantumRingsLib import QuantumRegister, ClassicalRegister, QuantumCircuit
from QuantumRingsLib import QuantumRingsProvider
from QuantumRingsLib import job_monitor
from matplotlib import pyplot as plt

# STEP 1: Setup the Quantum Rings provider and select a backend.
provider = QuantumRingsProvider()
# Select a backend; in this case, we use "scarlet_quantum_rings" as an example.
backend = provider.get_backend("scarlet_quantum_rings")
shots = 100  # Number of shots (circuit executions)

# Activate your account to enable resource access.
provider.active_account()

# STEP 2: Create Quantum and Classical Registers.
# Create a quantum register with 5 qubits and a classical register with 5 bits.
q = QuantumRegister(5, 'q')
c = ClassicalRegister(5, 'c')

# STEP 3: Construct the Quantum Circuit.
# Instantiate the circuit using the created registers.
qc = QuantumCircuit(q, c)

# STEP 4: Apply Quantum Gates.
# Apply a Hadamard gate on qubit 0 to put it in superposition.
qc.h(0)
# Apply a chain of CNOT gates to entangle adjacent qubits.
for i in range(qc.num_qubits - 1):
    qc.cnot(i, i + 1)

# STEP 5: Add Measurements.
# Measure all qubits; this maps each qubit to its corresponding classical bit.
qc.measure_all()

# STEP 6: Execute the Circuit.
# Run the circuit on the selected backend with the specified number of shots.
job = backend.run(qc, shots)
# Monitor the job status using the provided job_monitor utility.
job_monitor(job)

# STEP 7: Retrieve and Display the Results.
# Get the results once the job is complete.
result = job.result()
# Extract the measurement counts from the result.
counts = result.get_counts()
print("Measurement Counts:", counts)

# (Optional) Plot the results using matplotlib.
plt.bar(counts.keys(), counts.values())
plt.xlabel("States")
plt.ylabel("Counts")
plt.title("Quantum Rings Circuit Results")
plt.show()

```


## quantumrings-toolkit-qiskit-basic-10.py

**Summary:** This example demonstrates a simple circuit execution with proper job monitoring.

```python
# ---
# title: Qiskit Toolkit Basic 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: [1.3.1, 1.4.0]
#   Qiskit: [1.4.0]
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['Qiskit', 'QrBackendV2', 'transpile', 'manual job monitoring', 'execution']
# description: >
#   Demonstrates execution of a Qiskit-style quantum circuit on Quantum Rings hardware using QrBackendV2.
#   Includes required transpilation step, manual polling for job status (job_monitor not supported), 
#   and retrieval of measurement results. This is a canonical integration example for Qiskit users 
#   migrating to the Quantum Rings backend.
# ---

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

**Summary:** This example shows how to use an estimator for quantum expectation value calculations.

```python
# ---
# title: Qiskit Toolkit Estimator V1 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: [1.3.1, 1.4.0]
#   Qiskit: [1.4.0]
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['Qiskit', 'QrEstimatorV1', 'expectation value', 'SparsePauliOp', 'estimator']
# description: >
#   Demonstrates use of QrEstimatorV1 from the quantumrings-toolkit-qiskit package to compute 
#   expectation values of observables in Qiskit circuits using Quantum Rings hardware. 
#   Includes setup of SparsePauliOp observables and explains why transpilation is not needed. 
#   Returns a list of estimated values for the given observable and circuit pairs.
# ---

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

**Summary:** This example shows how to use an estimator for quantum expectation value calculations.

```python
# ---
# title: Qiskit Toolkit Estimator V2 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: [1.3.1, 1.4.0]
#   Qiskit: [1.4.0]
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['Qiskit', 'QrEstimatorV2', 'SparsePauliOp', 'expectation value', 'estimator', 'multi-observable']
# description: >
#   Demonstrates use of QrEstimatorV2 to compute expectation values over multiple observables 
#   for a given Qiskit circuit using Quantum Rings backends. Shows construction of a Bell state circuit, 
#   definition of observables like ZZ and XX, and interpretation of the resulting expectation values. 
#   Also explains how QrEstimatorV2 accepts structured input as a list of PUB tuples and does not require transpilation.
# ---

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

**Summary:** This example demonstrates how to batch execute multiple circuits.

```python
# ---
# title: Qiskit Toolkit Multi-Circuit Sampling 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: [1.3.1, 1.4.0]
#   Qiskit: [1.4.0]
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['Qiskit', 'QrSamplerV2', 'multi-circuit', 'sampling', 'batch execution', 'shots']
# description: >
#   Demonstrates batch execution of multiple Qiskit circuits using QrSamplerV2 in the Quantum Rings SDK.
#   Includes circuits for Bell state, all-ones initialization, and GHZ state. Highlights how to construct 
#   processable unit blocks (PUBs) for sampler input and retrieve structured measurement results for each 
#   individual circuit in the batch. Ideal for scenarios requiring scalable sampling or parallel circuit testing.
# ---


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
# ✅ QrSamplerV2 - requires Processable Unit Blocks (PUBs) in the form of tuples.
# Each tuple must be: (QuantumCircuit, parameter_values, shots)
# ❌ This format does NOT work with QrSamplerV1.
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

**Summary:** This example demonstrates a specific function. Refer to the script for more details.

```python
# ---
# title: Qiskit Toolkit QAOA Example
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: [1.3.1, 1.4.0]
#   Qiskit: [1.4.0]
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['Qiskit', 'QAOA', 'variational circuit', 'sampler', 'optimization', 'quantum algorithm']
# description: >
#   Demonstrates how to build and execute a QAOA variational circuit using Qiskit with Quantum Rings integration.
#   Uses the QAOAAnsatz circuit from qiskit.circuit.library, constructs cost Hamiltonians using SparsePauliOp, 
#   and executes the circuit using QrSamplerV2. This example supports variational optimization workflows 
#   and highlights how to evaluate expectation values over a parameterized ansatz.
# ---

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

**Summary:** This example illustrates how to construct a quantum circuit compatible with the framework.

```python
# ---
# title: Qiskit Toolkit QuantumCircuit Construction
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: [1.3.1, 1.4.0]
#   Qiskit: [1.4.0]
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['Qiskit', 'QuantumCircuit', 'circuit construction', 'QrBackendV2', 'QrEstimatorV1']
# description: >
#   Shows how to construct a Qiskit QuantumCircuit compatible with Quantum Rings execution backends. 
#   Demonstrates interoperability of standard Qiskit registers and gates with Quantum Rings' QrBackendV2 
#   and QrEstimatorV1. Useful for integrating existing Qiskit code into the Quantum Rings SDK pipeline 
#   without rewriting circuit logic.
# ---


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

**Summary:** This example demonstrates a specific function. Refer to the script for more details.

```python
# ---
# title: Qiskit Toolkit Sampler V1 Example
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: [1.3.1, 1.4.0]
#   Qiskit: [1.4.0]
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['Qiskit', 'QrSamplerV1', 'sampling', 'measurement', 'shots', 'circuit execution']
# description: >
#   Demonstrates use of QrSamplerV1 to run a parameterized Qiskit QuantumCircuit on a Quantum Rings backend.
#   Includes parameter definition using qiskit.circuit.Parameter, binding of values, and execution to retrieve 
#   measurement outcomes. Highlights how QrSamplerV1 integrates with Qiskit primitives for lightweight sampling 
#   tasks without requiring manual job polling.
# ---


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
# ✅ QrSamplerV1 - requires circuits, parameter_values, and parameters explicitly.
# ❌ Do NOT use tuple format (e.g., (circuit, values, shots)) — that is only for QrSamplerV2.
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
# ✅ QrSamplerV2 - requires Processable Unit Blocks (PUBs) in the form of tuples.
# Each tuple must be: (QuantumCircuit, parameter_values, shots)
# ❌ This format does NOT work with QrSamplerV1.
pub = (circuits[0], [], 1000)  # No parameters, 1000 shots

# ✅ Correct instantiation of QrSamplerV2 (Backend required)
sampler_v2 = QrSamplerV2(backend=backend)
job_v2 = sampler_v2.run([pub])  # Must be a **list of PUBs**
result_v2 = job_v2.result()

print("✅ QrSamplerV2 Counts:", result_v2[0].data.meas.get_counts())

```


## quantumrings-toolkit-qiskit-samplerQNN-10.py

**Summary:** This example demonstrates a specific function. Refer to the script for more details.

```python
# ---
# title: Qiskit Toolkit Sampler QNN 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: [1.3.1, 1.4.0]
#   Qiskit: [1.4.0]
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['Qiskit', 'SamplerQNN', 'machine learning', 'neural network', 'QrSamplerQNN']
# description: >
#   Demonstrates how to create and evaluate a SamplerQNN using the Quantum Rings QrSamplerQNN interface 
#   for Qiskit machine learning integration. Builds a Qiskit TwoLocal circuit as the model, sets up 
#   input-to-output mappings using input_gradients=False, and executes sampling across different input encodings.
#   Suitable for hybrid classical-quantum ML workflows.
# ---


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
| `Invalid Argument Passed for Quantum Circuit` | Received a wrong type of circuit. | **Use the correct circuit type.** |
| `job_monitor() TypeError` | `job_monitor()` does not work with the provided job type. | **Use manual polling (`while not job.in_final_state(): ...`)** |
| `Transpile Required` | Circuits **must be transpiled** before running. | **Use `transpile(qc, backend, initial_layout=...)` before execution.** |