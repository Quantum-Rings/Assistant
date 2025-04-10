# ---
# title: Qiskit Toolkit Multi-Circuit Sampling 10
# synergy: |
#   - quantumrings.toolkit.qiskit 0.1.10 fails(!) with Qiskit 2.0
#   - A future version (0.1.11?) may resolve Qiskit 2.0 compatibility
# sdk ["tested(+)", "fails(!)", "untested(?)"]:
#   QuantumRingsLib: [0.9.11(+), 0.10.11(+)]
#   quantumrings-toolkit-qiskit: [0.1.10(+)]
#   Qiskit: [1.3.1(+), 1.4.1(+), 2.0(?)]
#   GPU-enabled: [false]
# python: [3.11(+)]
# os: [Windows 11(+), Ubuntu 22.04(?)]
# tags: ['Qiskit', 'QrSamplerV2', 'multi-circuit', 'sampling', 'batch execution', 'shots']
# description: >
#   Demonstrates batch execution of multiple Qiskit circuits using QrSamplerV2 in the Quantum Rings SDK.
#   Includes circuits for Bell state, all-ones initialization, and GHZ state. Highlights how to construct 
#   processable unit blocks (PUBs) for sampler input and retrieve structured measurement results for each 
#   individual circuit in the batch. Ideal for scenarios requiring scalable sampling or parallel circuit testing.
# ---


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
# ✅ QrSamplerV2 - requires Processable Unit Blocks (PUBs) in the form of tuples.
# Each tuple must be: (QuantumCircuit, parameter_values, shots)
# ❌ This format does NOT work with QrSamplerV1.
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
