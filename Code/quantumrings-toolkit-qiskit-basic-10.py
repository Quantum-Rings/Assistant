# ---
# title: Qiskit Toolkit Basic 10
# synergy: |
#   - quantumrings.toolkit.qiskit 0.1.10 fails(!) with Qiskit 2.0
#   - A future version (0.1.11?) may resolve Qiskit 2.0 compatibility
# sdk ["tested(+)", "fails(!)", "untested(?)"]:
#   QuantumRingsLib: [0.9.11(+), 0.10.11(+)]
#   quantumrings-toolkit-qiskit: [0.1.10(+)]
#   Qiskit: [1.3.1(+), 1.4.1(+), 2.0(?)]
#   GPU-enabled: [false]
# python: [3.11(+)]
# os: [Windows 11(+), Ubuntu 22.04(?)]
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
