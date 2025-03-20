"""
QuantumRingsLib-qasm-10.py
QuantumRIngsLib >= 10, does not work in earlier versions
Demonstarates how to read and write QASM2 files
"""
import QuantumRingsLib
from QuantumRingsLib import QuantumRingsProvider
from QuantumRingsLib import QuantumCircuit
provider = QuantumRingsProvider()
# to import QASM2 code:
qc = QuantumCircuit.from_qasm_file("test.qasm")
# to output QASM2 code use this:
qc.qasm(True)