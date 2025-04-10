# ---
# title: Quantumringslib Control 10
# sdk ["tested(+)", "fails(!)", "untested(?)"]:
#   QuantumRingsLib: [0.9.11(!), 0.10.11(+)]
#   quantumrings-toolkit-qiskit: []
#   Qiskit: []
#   GPU-enabled: [false]
# python: [3.11(+)]
# os: [Windows 11(+), Ubuntu 22.04(?)]
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
qc = QuantumCircuit(q, c) # fails on QuantumRingsLib 0.9.11. For 0.9.11 use "qc = QuantumCircuit(num_qubits)"
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