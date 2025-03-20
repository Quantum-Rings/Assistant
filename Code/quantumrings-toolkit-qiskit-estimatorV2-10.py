'''
QrEstimatorV2 module
classQrEstimatorV2
Given an observable of the type 
, where 
 is a complex number and 
 is a Pauli operator, the estimator calculates the expectation 
 of each 
 and finally calculates the expectation value of 
 as 
. The reported std is calculated as

 
where 
 is the variance of 
, 
 is the number of shots, and 
 is the target precision [1].

Each tuple of (circuit, observables, <optional> parameter values, <optional> precision), called an estimator primitive unified block (PUB), produces its own array-based result. The run() method can be given a sequence of pubs to run in one call.

QrEstimatorV2(*, backend=None, options=None, run_options=None)
Args:
backend (QrBackendV2) : The Quantum Rings backend to run the primitive on.
options (dict) : The options to control the defaults shots (shots)
run_options (dict) : See options.
QrEstimatorV2.options: Options
Returns the options

run(pubs, *, precision=None)
Executes the pubs and estimates all associated observables.

Args:
pubs [pub]: The pub to preprocess.
precision (float): None
Returns:
The job associated with the exection

'''

#####################################################
# 1) Imports
#####################################################
from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp

# Quantum Rings imports
from QuantumRingsLib import QuantumRingsProvider
from quantumrings.toolkit.qiskit import QrBackendV2, QrEstimatorV2

#####################################################
# 2) Create Provider & Backend
#####################################################
provider = QuantumRingsProvider()
backend = QrBackendV2(provider, num_qubits=2)  
# Adjust 'num_qubits' as needed. E.g., 2 for a 2-qubit circuit.

#####################################################
# 3) Build a Simple Circuit (Bell State)
#####################################################
# We do NOT add measure gates here, because QrEstimatorV2 
# internally measures the specified observables.
bell = QuantumCircuit(2)
bell.h(0)
bell.cx(0, 1)
# (Optionally, add barriers or extra gates.)

#####################################################
# 4) Define Observables (SparsePauliOp)
#####################################################
# Let's measure the expectation of ZZ and XX on the 2-qubit state.
op_zz = SparsePauliOp.from_list([("ZZ", 1.0)])
op_xx = SparsePauliOp.from_list([("XX", 1.0)])
observables = [op_zz, op_xx]

#####################################################
# 5) Create "PUB" Tuples for the Estimator
#####################################################
# QrEstimatorV2 typically uses: (circuit, observables, parameter_values, optional_shots)
# Since this circuit has no parameters, we pass [[]] for parameter_values.
# Shots is optional—if omitted, the default from the backend is used (often 1024).
#
# If you want an explicit shot count, you can pass something like (bell, observables, [[]], 1000).
# For a minimal example, we'll just do no explicit shots argument.

pub = (bell, observables, [[]])

# We submit a list of PUBs to .run().
pub_list = [pub]

#####################################################
# 6) Instantiate the Estimator & Run
#####################################################
estimator = QrEstimatorV2(backend=backend)
job = estimator.run(pub_list)
result = job.result()

#####################################################
# 7) Retrieve Expectation Values
#####################################################
# The returned 'result' is a "PrimitiveResult" that acts like a list of Sampler/Estimator results.
# Each item typically has a "data" attribute, which includes the expectation values in data.evs.

# In many QrEstimatorV2 builds, each index of 'result' corresponds to one PUB you submitted.
pub_result = result[0]  # we only submitted one
data = pub_result.data

# "evs" is often a list or array of shape [N_observables], 
# each entry containing the measured expectation value for that operator.
evs = data.evs  
# e.g. evs[0] -> expectation of ZZ, evs[1] -> expectation of XX

# Convert from array-like to float
evs_float = [float(ev[0]) for ev in evs]

print("\n=== Expectation Values for the Bell Circuit ===")
for i, obs in enumerate(["ZZ", "XX"]):
    print(f"Operator {obs} = {evs_float[i]:.3f}")
