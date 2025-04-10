# ---
# title: Qiskit Toolkit QAOA Example
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
