# ---
# title: Quantumringslib Basic 10
# sdk ["tested(+)", "fails(!)", "untested(?)"]:
#   QuantumRingsLib: [0.9.11(!), 0.10.11(+)]
#   quantumrings-toolkit-qiskit: []
#   Qiskit: []
#   GPU-enabled: [false]
# python: [3.11(+)]
# os: [Windows 11(+), Ubuntu 22.04(?)]
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
qc = QuantumCircuit(q, c) # fails on QuantumRingsLib 0.9.11. For 0.9.11 use "qc = QuantumCircuit(num_qubits)"

# construct the quantum circuit

qc.h(0);
for i in range (qc.num_qubits - 1):
    qc.cnot(i, i + 1);

qc.measure_all();

# Executing the Code

job = backend.run(qc, shots)
job_monitor(job)
result = job.result()
print(result)