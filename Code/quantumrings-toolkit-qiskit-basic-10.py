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
