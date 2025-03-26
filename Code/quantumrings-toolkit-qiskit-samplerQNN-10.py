# ---
# title: Qiskit Toolkit Sampler QNN 10
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: [1.3.1, 1.4.0]
#   Qiskit: [1.4.0]
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['Qiskit', 'SamplerQNN', 'machine learning', 'neural network', 'QrSamplerQNN']
# description: >
#   Demonstrates how to create and evaluate a SamplerQNN using the Quantum Rings QrSamplerQNN interface 
#   for Qiskit machine learning integration. Builds a Qiskit TwoLocal circuit as the model, sets up 
#   input-to-output mappings using input_gradients=False, and executes sampling across different input encodings.
#   Suitable for hybrid classical-quantum ML workflows.
# ---


'''
QrSamplerQNN module
classQrSamplerQNN(*, circuit, sampler, input_params, weight_params, sparse, interpret, 
output_shape, gradient, input_gradients, pass_manager)
A neural network implementation based on the Sampler primitive.

This class is a derivative of the Qiskit Machine Learning Package class SamplerQNN. 
Please refer to the class for more documentation.

The QrSamplerQNN is a neural network that takes in a parametrized quantum circuit with 
designated parameters for input data and/or weights and translates the quasi-probabilities 
estimated by the Sampler primitive into predicted classes. Quite often, a combined quantum 
circuit is used. Such a circuit is built from two circuits: a feature map, it provides 
input parameters for the network, and an ansatz (weight parameters). In this case a 
QNNCircuit can be passed as circuit to simplify the composition of a feature map and ansatz. 
If a QNNCircuit is passed as circuit, the input and weight parameters do not have to be provided, 
because these two properties are taken from the QNNCircuit.

The output can be set up in different formats, and an optional post-processing step 
can be used to interpret the sampler’s output in a particular context (e.g. mapping the 
resulting bitstring to match the number of classes).

In this example the network maps the output of the quantum circuit to two classes via a custom 
interpret function:

'''

from qiskit import QuantumCircuit
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_machine_learning.circuit.library import QNNCircuit

from quantumrings.toolkit.qiskit.machine_learning import QrSamplerQNN as SamplerQNN

num_qubits = 2

def parity(x):
    return f"{bin(x)}".count("1") % 2

# Using the QNNCircuit:
# Create a parameterized 2 qubit circuit composed of the default ZZFeatureMap feature map
# and RealAmplitudes ansatz.
qnn_qc = QNNCircuit(num_qubits)

qnn = SamplerQNN(
    circuit=qnn_qc,
    interpret=parity,
    output_shape=2
)

qnn.forward(input_data=[1, 2], weights=[1, 2, 3, 4, 5, 6, 7, 8])

# Explicitly specifying the ansatz and feature map:
feature_map = ZZFeatureMap(feature_dimension=num_qubits)
ansatz = RealAmplitudes(num_qubits=num_qubits)

qc = QuantumCircuit(num_qubits)
qc.compose(feature_map, inplace=True)
qc.compose(ansatz, inplace=True)

qnn = SamplerQNN(
    circuit=qc,
    input_params=feature_map.parameters,
    weight_params=ansatz.parameters,
    interpret=parity,
    output_shape=2
)

qnn.forward(input_data=[1, 2], weights=[1, 2, 3, 4, 5, 6, 7, 8])

'''
The following attributes can be set via the constructor but can also be read and 
updated once the SamplerQNN object has been constructed.

Attributes:

sampler (BaseSampler): The sampler primitive used to compute the neural network’s 
results. gradient (BaseSamplerGradient): A sampler gradient to be used for the backward pass.

__init__(self, *, circuit, sampler, input_params, weight_params, sparse, interpret, 
output_shape, gradient, input_gradients, pass_manager)
Args:
circuit: The parametrized quantum circuit that generates the samples of this network. If a
QNNCircuit is passed,
the input_params and weight_params do not have to be provided, because these two
properties are taken from the QNNCircuit.
sampler: Not used.
input_params: The parameters of the circuit corresponding to the input. If a
QNNCircuit is provided the input_params value here is ignored. Instead, the value is taken from the
QNNCircuit input_parameters.
weight_params: The parameters of the circuit corresponding to the trainable weights. If a
QNNCircuit is provided the weight_params value here is ignored. Instead, the value is taken from the
QNNCircuit weight_parameters.
sparse: Returns whether the output is sparse or not.
interpret: A callable that maps the measured integer to another unsigned integer or tuple
of unsigned integers. These are used as new indices for the (potentially sparse)
output array. If no interpret function is passed, then an identity function will be
used by this neural network.
output_shape: The output shape of the custom interpretation. For SamplerV1, it is ignored
if no custom interpret method is provided where the shape is taken to be
2^circuit.num_qubits.
gradient: An optional sampler gradient to be used for the backward pass. If None is
given, a default instance of ParamShiftSamplerGradient will be used.
input_gradients: Determines whether to compute gradients with respect to input data. Note
that this parameter is False by default, and must be explicitly set to True
for a proper gradient computation when using TorchConnector.
pass_manager: The pass manager to transpile the circuits, if necessary.
Defaults to None, as some primitives do not need transpiled circuits.

'''