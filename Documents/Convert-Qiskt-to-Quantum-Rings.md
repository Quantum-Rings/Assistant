Step-by-step guide for converting Qiskit code to Quantum Rings

Convert: Qiskit Statevector to Quantum Rings QrStatevector
# from qiskit.quantum_info import Statevector
from quantumrings.toolkit.qiskit import QrStatevector as Statevector

Convert: Qiskit StatevectorSampler to Quantum Rings QrStatevectorSampler
# from qiskit.primitives import StatevectorSampler as Sampler
from quantumrings.toolkit.qiskit import QrStatevectorSampler as Sampler

Convert: Qiskit Sampler to Quantum Rings QrSamplerV1
# from qiskit.primitives import Sampler
from quantumrings.toolkit.qiskit import QrSamplerV1 as Sampler
sampler = Sampler()

Convert: Qiskit Estimator to Quantum Rings QrEstimatorV1
# from qiskit.primitives import Estimator
from quantumrings.toolkit.qiskit import QrEstimatorV1 as Estimator

Convert: Qiskit SamplerQNN to Quantum Rings QrSamplerQNN
# from qiskit_machine_learning.neural_networks import SamplerQNN
from quantumrings.toolkit.qiskit.machine_learning import QrSamplerQNN as SamplerQNN

Convert: Qiskit EstimatorQNN to Quantum Rings QrEstimatorQNN
# from qiskit_machine_learning.neural_networks import EstimatorQNN
from quantumrings.toolkit.qiskit.machine_learning import QrEstimatorQNN as EstimatorQNN

Convert: Qiskit FidelityQuantumKernel to Quantum Rings FidelityQuantumKernel
# from qiskit_machine_learning.kernels import FidelityQuantumKernel
from quantumrings.toolkit.qiskit.machine_learning import QrFidelityQuantumKernel

Convert: Qiskit TrainableFidelityQuantumKernel to Quantum Rings QrTrainableFidelityQuantumKernel
# from qiskit_machine_learning.kernels import TrainableFidelityQuantumKernel
from quantumrings.toolkit.qiskit.machine_learning import QrTrainableFidelityQuantumKernel

Note that when using quantumrings.toolkit.qiskit, you should use Qiskit functions, such as these from qiskit.circuit:
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.circuit.library import TwoLocal, QAOAAnsatz, QFT
from qiskit.quantum_info import Pauli, SparsePauliOp

Convert from Pennylane or Cirq or Q# to QuantumRings
Convert native code to QASM and then read the QASM into QuantumRings


How can I contribute to improving and updating this Quantum Rings help file?
Go to https://github.com/Quantum-Rings