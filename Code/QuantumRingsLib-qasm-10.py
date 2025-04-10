# ---
# title: Quantumringslib Qasm 10
# sdk ["tested(+)", "fails(!)", "untested(?)"]:
#   QuantumRingsLib: [0.9.11(+), 0.10.11(+)]
#   quantumrings-toolkit-qiskit: []
#   Qiskit: []
#   GPU-enabled: [false]
# python: [3.11(+)]
# os: [Windows 11(+), Ubuntu 22.04(?)]
# tags: ['qasm', 'qasm2', 'load', 'QuantumRingsLib', 'circuit loading']
# description: >
#   Demonstrates how to load and parse QASM 2.0 content into a QuantumRingsLib QuantumCircuit 
#   using the `qasm2.loads()` method. Highlights options for include paths, strict parsing, 
#   and error handling. Useful for importing circuits from external tools or text representations.
# ---

import QuantumRingsLib
from QuantumRingsLib import QuantumRingsProvider
from QuantumRingsLib import QuantumCircuit
provider = QuantumRingsProvider()
# to import QASM2 code:
qc = QuantumCircuit.from_qasm_file("test.qasm")
# to output QASM2 code use this:
qc.qasm(True)