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