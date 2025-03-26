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
