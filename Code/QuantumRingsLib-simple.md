# Qiskit Sampler Example (Qiskit 1.4)

**Compatibility**  
- **Windows**: 11
- **Python**: 3.11  
- **Qiskit**: 1.4  
- **QuantumRingsLib**: 0.9.0 

**Description**  
This snippet demonstrates local Aer simulator usage in Qiskit 1.4 style 
(e.g. using `AerSimulator.run(...)`). If you are on an older Qiskit 
version (pre-1.4), you might need to use `execute(transpiled_qc, backend=simulator)`.
see [release notes](https://qiskit.org/documentation/release-notes/) for any 
minor changes.

```python
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit, transpile

# Build a simple 2-qubit circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Initialize Qiskit Aer simulator
simulator = AerSimulator()

# Transpile for the simulator
t_qc = transpile(qc, simulator)

# Run the circuit
job = simulator.run(t_qc, shots=1024)
result = job.result()

# Retrieve measurement counts
counts = result.get_counts()
print("Local Qiskit counts =>", counts)
