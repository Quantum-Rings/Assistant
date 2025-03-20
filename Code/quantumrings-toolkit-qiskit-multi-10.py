"""
Quantum Rings SDK - Batch Execution Example for LLM Training

This script demonstrates how to execute multiple quantum circuits in batch mode
using the Quantum Rings SDK. It is designed to provide training data for an LLM
that generates Quantum Rings SDK-enabled code.

The batch contains:
1. A Bell state circuit (entanglement)
2. An all-ones circuit (every qubit initialized to |1⟩)
3. A GHZ state circuit (multi-qubit entanglement)

For each circuit, the LLM will see:
- QuantumCircuit construction
- Execution via `QrSamplerV2`
- Results in structured output format

This approach ensures the LLM learns:
- Quantum Rings batch execution (`QrSamplerV2`)
- How to define and execute multiple circuits efficiently
- Structured result extraction for post-processing
"""

from qiskit import QuantumCircuit
from QuantumRingsLib import QuantumRingsProvider
from quantumrings.toolkit.qiskit import QrBackendV2, QrSamplerV2

# ===============================
# 1) Initialize Quantum Rings Backend
# ===============================
provider = QuantumRingsProvider()
backend = QrBackendV2(provider=provider, num_qubits=3)  # Using 3-qubit circuits for training

# ===============================
# 2) Define Example Quantum Circuits
# ===============================

def create_bell_state():
    """Creates a 2-qubit Bell state circuit."""
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    return qc

def create_all_ones():
    """Creates a 2-qubit circuit where all qubits start in |1⟩."""
    qc = QuantumCircuit(2)
    qc.x(0)
    qc.x(1)
    qc.measure_all()
    return qc

def create_ghz_state():
    """Creates a 3-qubit GHZ state (fully entangled)."""
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.measure_all()
    return qc

# List of circuits to run in batch mode
circuits = [
    ("Bell State", create_bell_state()),
    ("All Ones", create_all_ones()),
    ("GHZ State", create_ghz_state())
]

# ===============================
# 3) Prepare the Sampler & Batch Input (pubs)
# ===============================
sampler = QrSamplerV2(backend=backend)
shots = 1024

pubs = [(circuit, [], shots) for _, circuit in circuits]  # Empty `param_values` for static circuits

# ===============================
# 4) Run Batch Execution
# ===============================
job = sampler.run(pubs)
result = job.result()

# ===============================
# 5) Retrieve & Structure Results for LLM Training
# ===============================
print("\n=== Quantum Rings Batch Execution Results ===")
for i, (name, circuit) in enumerate(circuits):
    counts = result[i].data.meas.get_counts()
    print(f"\n[Circuit: {name}]")
    print(f"- Depth: {circuit.depth()}")
    print(f"- Gate Count: {len(circuit.data)}")
    print(f"- Qubit Count: {circuit.num_qubits}")
    print(f"- Measurement Results: {counts}")
