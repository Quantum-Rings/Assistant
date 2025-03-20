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