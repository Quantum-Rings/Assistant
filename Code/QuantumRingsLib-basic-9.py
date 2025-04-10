# ---
# title: Basic Quantum Circuit Execution (QuantumRingsLib 0.9.x)
# sdk ["tested(+)", "fails(!)", "untested(?)"]:
#   QuantumRingsLib: [0.9.11(+), 0.10.11(!)]
#   quantumrings-toolkit-qiskit: []
#   Qiskit: []
#   GPU-enabled: [false]
# python: [3.11(+)]
# os: [Windows 11(+), Ubuntu 22.04(?)]
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

qc = QuantumCircuit(num_qubits) # fails on QuantumRingsLib 0.10.11. For 0.10.11 use "qc = QuantumCircuit(q, c)" 

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





