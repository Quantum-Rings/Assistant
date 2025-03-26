# ---
# title: Quantumringslib Quantumcircuit
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['QuantumCircuit', 'construction', 'registers', 'QuantumRingsLib']
# description: >
#   Illustrates how to construct a quantum circuit using the native QuantumRingsLib QuantumCircuit class.
#   Includes manual instantiation of QuantumRegister and ClassicalRegister objects, as well as
#   usage of basic gates and circuit attributes. Intended to familiarize users with low-level
#   circuit building in the Quantum Rings SDK.
# ---



# Import the necessary modules from the Quantum Rings SDK.
import QuantumRingsLib
from QuantumRingsLib import QuantumRegister, ClassicalRegister, QuantumCircuit
from QuantumRingsLib import QuantumRingsProvider
from QuantumRingsLib import job_monitor
from matplotlib import pyplot as plt

# STEP 1: Setup the Quantum Rings provider and select a backend.
provider = QuantumRingsProvider()
# Select a backend; in this case, we use "scarlet_quantum_rings" as an example.
backend = provider.get_backend("scarlet_quantum_rings")
shots = 100  # Number of shots (circuit executions)

# Activate your account to enable resource access.
provider.active_account()

# STEP 2: Create Quantum and Classical Registers.
# Create a quantum register with 5 qubits and a classical register with 5 bits.
q = QuantumRegister(5, 'q')
c = ClassicalRegister(5, 'c')

# STEP 3: Construct the Quantum Circuit.
# Instantiate the circuit using the created registers.
qc = QuantumCircuit(q, c)

# STEP 4: Apply Quantum Gates.
# Apply a Hadamard gate on qubit 0 to put it in superposition.
qc.h(0)
# Apply a chain of CNOT gates to entangle adjacent qubits.
for i in range(qc.num_qubits - 1):
    qc.cnot(i, i + 1)

# STEP 5: Add Measurements.
# Measure all qubits; this maps each qubit to its corresponding classical bit.
qc.measure_all()

# STEP 6: Execute the Circuit.
# Run the circuit on the selected backend with the specified number of shots.
job = backend.run(qc, shots)
# Monitor the job status using the provided job_monitor utility.
job_monitor(job)

# STEP 7: Retrieve and Display the Results.
# Get the results once the job is complete.
result = job.result()
# Extract the measurement counts from the result.
counts = result.get_counts()
print("Measurement Counts:", counts)

# (Optional) Plot the results using matplotlib.
plt.bar(counts.keys(), counts.values())
plt.xlabel("States")
plt.ylabel("Counts")
plt.title("Quantum Rings Circuit Results")
plt.show()
