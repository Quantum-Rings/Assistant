'''
QrEstimatorV1 module
classQrEstimatorV1
A derivative of the BackendEstimatorV1 class, to estimates expectation values of quantum circuits and observables using the Quantum Rings backend.

An estimator is initialized with an empty parameter set. The estimator is used to create a JobV1, via the qiskit.primitives.Estimator.run() method. This method is called with the following parameters

quantum circuits (
): list of (parameterized) quantum circuits (a list of QuantumCircuit objects).

observables (
): a list of SparsePauliOp objects.

parameter values (:math:` heta_k`): list of sets of values to be bound to the parameters of the quantum circuits (list of list of float).

The method returns a JobV1 object, calling qiskit.providers.JobV1.result() yields a list of expectation values for the estimation.

QrEstimatorV1(*, backend: QrBackendV2 | None = None, options: dict | None = None, run_options: dict | None = None)
Args:
backend: The Quantum Rings backend to run the primitive on.
options: The options to control the defaults
run_options: See options.
QrEstimatorV1.options
Returns the options

run(circuits: list[QuantumCircuit], observables: list[BaseOperator], parameter_values: list[float] | None = None, **run_options)
Executes the pubs and estimates all associated observables.

Args:
pubs: The pub to preprocess.
precision: None
Returns:
The job associated with the pub

'''

##############################################################
# 1) Imports
##############################################################
# "QrEstimatorV1" and "QrBackendV2" come from quantumrings.toolkit.qiskit
# "QuantumCircuit" is from QuantumRingsLib (the native circuit class).
from quantumrings.toolkit.qiskit import QrEstimatorV1, QrBackendV2
from QuantumRingsLib import QuantumRingsProvider

# For the Pauli operator, we use Qiskit's quantum_info module
from qiskit.quantum_info import SparsePauliOp
from qiskit import QuantumCircuit


##############################################################
# 2) Obtain a Provider & Backend
##############################################################
provider = QuantumRingsProvider()
backend = QrBackendV2(provider=provider, num_qubits=2)
# If supported, you might try: QrBackendV2(provider, num_qubits=2, shots=1000)

##############################################################
# 3) Create a Circuit (QuantumRingsLib's circuit class)
##############################################################
# This is NOT qiskit's circuit; it's the "QuantumCircuit" from QuantumRingsLib.
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
# No .measure(...) calls needed—Estimator measures the operator directly.

##############################################################
# 4) Define the Observable (use Qiskit's SparsePauliOp)
##############################################################
# Even though QrEstimatorV1 doc references "SparsePauliOp",
# QuantumRingsLib does *not* provide that class. We import from Qiskit.
op_zz = SparsePauliOp.from_list([("ZZ", 1.0)])
# or simply: op_zz = SparsePauliOp("ZZ")

##############################################################
# 5) Instantiate QrEstimatorV1
##############################################################
estimator = QrEstimatorV1(backend=backend)

##############################################################
# 6) Run the Estimator
##############################################################
# 🚨 IMPORTANT: Unlike QrBackendV2, QrEstimatorV1 does NOT require transpilation.
# This is because the estimator directly processes the circuit and observable,
# rather than executing the circuit on a quantum backend.
# 
# .run(...) expects: circuits, observables, parameter_values
# If there are no parameters in your circuit, pass `[[]]`.
job = estimator.run(
    circuits=[qc],
    observables=[op_zz],
    parameter_values=[[]]
)

##############################################################
# 7) Retrieve Expectation Value
##############################################################
# "job" is a QrJobV1. Calling .result() returns a list of floats
# (one for each (circuit, observable) pair).
res = job.result()
expectation_zz = res.values[0]  # Only 1 circuit, 1 observable => index 0
print("Expectation value of ZZ =", expectation_zz)