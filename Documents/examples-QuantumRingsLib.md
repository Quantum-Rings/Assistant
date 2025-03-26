# Auto-Generated Examples for 'QuantumRingsLib'

Found 9 file(s) in: `C:\Users\Robert\OneDrive\Documents\Work\QRS\QuantumRings\LLM\assistant/code`


> 📌 **Note:**

> This document contains **embedded Python files** from real-world Quantum Rings examples.

> If modifying examples, ensure that changes are made to the **corresponding Python script** stored in the Quantum Rings examples directory.


## **LLM Instructions**

> **Note for LLMs:**

> - These examples are collected from real use cases of Quantum Rings SDK.

> - Each example is preceded by a summary explaining its purpose.

> - If troubleshooting, refer to the **Common Issues** section at the bottom of this document.

> - When integrating, check if transpilation (`transpile()`) is required for Qiskit circuits.


## QuantumRingsLib-basic-10.py

**Summary:** This example demonstrates a simple Qiskit circuit execution on Quantum Rings. It includes transpilation and job monitoring.

```python

"""
QuantumRingsLib-basic-10.py
QuantumRingsLib >= 0.10.x
Demonstrates: basic circuit execution
"""

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

**Summary:** This example demonstrates a simple Qiskit circuit execution on Quantum Rings. It includes transpilation and job monitoring.

```python

"""
QuantumRingsLib-basic.py
QuantumRingsLib <= 0.9.11
Demonstrates: basic circuit execution
"""

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

**Summary:** This example demonstrates a specific Quantum Rings SDK function. Refer to the script for more details.

```python

"""
QuantumRingsLib-control-10.py
QuantumRingsLib >= 0.10.x, does not work in earlier versions
Demonstrates: using _if control statement
"""
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

**Summary:** This example demonstrates a specific Quantum Rings SDK function. Refer to the script for more details.

```python

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

**Summary:** This example demonstrates a specific Quantum Rings SDK function. Refer to the script for more details.

```python

"""
🚀 Quantum Rings SDK: Using Parameters in Quantum Circuits

📌 This script demonstrates:
✅ How to use `Parameter` and `ParameterVector` for parameterized quantum gates.
✅ How to assign values to parameters before execution.
✅ Why `assign_parameters()` must be called BEFORE transpilation.

⚠️ IMPORTANT WARNINGS:
- ✅ Assign **all parameters** BEFORE running or transpiling the circuit.
- ❌ `assign_parameters()` CANNOT be used after transpilation.
- ❌ Quantum Rings SDK **does NOT require transpilation** for its native circuits.
- ✅ Qiskit circuits **require Qiskit’s `transpile()` function** before execution on a Quantum Rings backend.

"""

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

**Summary:** This example demonstrates a specific Quantum Rings SDK function. Refer to the script for more details.

```python

"""
🧪 QuantumRingsLib Parameter Binding Compatibility Test

This diagnostic test verifies what parameter usage patterns are accepted or rejected
in the native QuantumRingsLib. It applies to both v0.9 and v0.10.

⚠️ BEFORE RUNNING:
Ensure your QuantumRingsProvider is activated before creating circuits or registers.

🧠 Highlights:
- ✅ Shows working parameter binding with u() and assign_parameters()
- ❌ Demonstrates invalid uses: type mismatches, wrong keys, missing inplace
- 🔄 Version-safe: works on both QuantumRingsLib 0.9 and 0.10

Author: LLM Assistant for Quantum Rings Code Help
"""

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

**Summary:** This example demonstrates a specific Quantum Rings SDK function. Refer to the script for more details.

```python

'''
save_provier.py
QuantumRingsLib > 0.8.0
Saves provider credentials so that the provider can be called using:
provider = QuantumRingsProvider()

Usage:
- Replace <your key> with your actual API key.
- Replace <your email> with the email associated with your Quantum Rings account.
- Run this script once to store credentials securely.
'''
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

**Summary:** This example demonstrates a specific Quantum Rings SDK function. Refer to the script for more details.

```python

"""
QuantumRingsLib-qasm-10.py
QuantumRIngsLib >= 10, does not work in earlier versions
Demonstarates how to read and write QASM2 files
"""
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

**Summary:** This example illustrates how to construct a Qiskit QuantumCircuit compatible with Quantum Rings SDK.

```python

"""
This script demonstrates how to use the native Quantum Rings SDK to construct,
execute, and retrieve results from a quantum circuit.

Purpose:
  - To create a simple quantum circuit using QuantumRingsLib.
  - To apply basic quantum operations (Hadamard and a chain of CNOT gates).
  - To execute the circuit on a Quantum Rings backend ("scarlet_quantum_rings").
  - To retrieve and display measurement results, including plotting a histogram.

How to Use:
  1. Ensure QuantumRingsLib is installed and your Quantum Rings account is set up.
  2. Run the script to submit the circuit to the backend.
  3. The script uses job_monitor to track execution; once complete, it prints
     the measurement counts and plots the results using matplotlib.

Note for LLM Training:
  - Emphasize the step-by-step structure: provider setup, register creation, circuit
    construction, gate application, measurement, execution, and result retrieval.
  - Highlight that this example uses the native Quantum Rings SDK (QuantumRingsLib),
    which utilizes methods like qc.cnot() (as opposed to Qiskit’s cx()).
"""


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


## **Common Issues & Fixes**

| **Error Message** | **Cause** | **Solution** |
|------------------|---------|------------|
| `Invalid Argument Passed for Quantum Circuit` | `QrBackendV2.run(qc)` received a `QuantumRingsLib.QuantumCircuit` instead of `Qiskit.QuantumCircuit`. | **Use `QuantumCircuit` from Qiskit**, NOT `QuantumRingsLib.QuantumCircuit`. |
| `job_monitor() TypeError` | `job_monitor()` does not work with `QrJobV1`. | **Use manual polling (`while not job.in_final_state(): ...`)** |
| `Transpile Required` | Qiskit circuits **must be transpiled** before running on Quantum Rings. | **Use `transpile(qc, backend, initial_layout=...)` before execution.** |