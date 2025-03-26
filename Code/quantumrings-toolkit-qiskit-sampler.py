# ---
# title: Qiskit Toolkit Sampler V1 Example
# sdk:
#   QuantumRingsLib: [0.10.x]
#   quantumrings-toolkit-qiskit: [1.3.1, 1.4.0]
#   Qiskit: [1.4.0]
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['Qiskit', 'QrSamplerV1', 'sampling', 'measurement', 'shots', 'circuit execution']
# description: >
#   Demonstrates use of QrSamplerV1 to run a parameterized Qiskit QuantumCircuit on a Quantum Rings backend.
#   Includes parameter definition using qiskit.circuit.Parameter, binding of values, and execution to retrieve 
#   measurement outcomes. Highlights how QrSamplerV1 integrates with Qiskit primitives for lightweight sampling 
#   tasks without requiring manual job polling.
# ---


"""
🚀 Example: Correct Usage of QrSamplerV1, QrSamplerV2, and QrBackendV2

This script ensures **proper Quantum Rings SDK usage**, covering:
   - `QrSamplerV1`: For basic & parameterized circuits (no backend required).
   - `QrSamplerV2`: Uses **Processable Unit Blocks (PUB)** for execution.
   - `QrBackendV2`: Direct backend execution with **correct transpilation**.

📌 **Key Fixes & Best Practices:**
   ✅ **Run circuits individually** to avoid batch execution issues.
   ✅ **Ensure correct circuit input format** for each API.
   ✅ **Transpile circuits properly** before running them on the backend.
   ✅ **Temporarily remove `performance="highestaccuracy"`** if execution fails.
   ✅ **Use explicit basis gate transpilation** to avoid unsupported operations.
"""

# ===============================
# 📌 Import Required Modules
# ===============================
from qiskit import QuantumCircuit, transpile
from QuantumRingsLib import QuantumRingsProvider
from quantumrings.toolkit.qiskit import QrBackendV2, QrSamplerV2, QrSamplerV1
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import BasisTranslator
from qiskit.circuit.equivalence_library import SessionEquivalenceLibrary

# ===============================
# 🔹 Initialize Quantum Rings Backend
# ===============================
provider = QuantumRingsProvider()
shots = 1000
backend = QrBackendV2(provider=provider, num_qubits=2)

# ===============================
# 🔹 Construct Circuits
# ===============================
print("\n✅ Constructing quantum circuits...")

circuits = []
for _ in range(3):  # Three test circuits
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    circuits.append(qc)

# ===============================
# 🔹 Debug Circuit Depth Before Transpilation
# ===============================
print("\n✅ Pre-Transpilation Debugging:")
for i, circuit in enumerate(circuits):
    print(f"🔹 Circuit {i} Depth Before Transpilation: {circuit.depth()}")

# ===============================
# 🔹 Transpile Circuits for Quantum Rings Backend
# ===============================
print("\n🚀 Transpiling circuits for Quantum Rings backend...")

# ✅ Force basis gate transpilation for compatibility
basis_gates = ["cx", "h", "measure"]
pass_manager = PassManager(BasisTranslator(SessionEquivalenceLibrary, basis_gates))

try:
    transpiled_circuits = [pass_manager.run(transpile(circuit, backend)) for circuit in circuits]
except Exception as e:
    print(f"❌ Transpilation Error: {e}")
    exit(1)

# ===============================
# 🔹 Debug Circuit Depth After Transpilation
# ===============================
print("\n✅ Post-Transpilation Debugging:")
for i, transpiled in enumerate(transpiled_circuits):
    print(f"🔹 Circuit {i} Depth After Transpilation: {transpiled.depth()}")
    print(transpiled.draw())  # Show circuit structure after transpilation

# ===============================
# 🔹 Run Circuits on Quantum Rings Backend (Individual Execution)
# ===============================
print("\n🚀 Running circuits on Quantum Rings backend...")

try:
    results = []  # Store results for each individual job

    for i, circuit in enumerate(transpiled_circuits):
        print(f"▶ Running Circuit {i}...")
        
        # ✅ Run each circuit **individually** instead of as a batch
        job = backend.run(circuit, shots=shots)  # Removing `performance="highestaccuracy"` for now
        
        results.append(job.result())

    # ✅ Process and print results
    for i, res in enumerate(results):
        counts = res.get_counts()
        print(f"✅ QrBackendV2 Counts for Circuit {i}:", counts)

except Exception as e:
    print(f"❌ Error executing on Quantum Rings backend: {e}")
    exit(1)


# ===============================
# ✅ `QrSamplerV1` Usage: Running Parameterized Circuits
# ===============================
print("\n🚀 Running parameterized circuits with QrSamplerV1...")

# ✅ Construct a parameterized circuit
pqc = QuantumCircuit(2)
pqc.h(0)
pqc.cx(0, 1)
pqc.measure_all()
theta_values = [0, 1, 1, 2, 3, 5]  # Example parameter values

# ✅ Correct usage of QrSamplerV1 (No backend required)
# ✅ QrSamplerV1 - requires circuits, parameter_values, and parameters explicitly.
# ❌ Do NOT use tuple format (e.g., (circuit, values, shots)) — that is only for QrSamplerV2.
sampler_v1 = QrSamplerV1()
job_v1 = sampler_v1.run(circuits=[pqc], parameter_values=[theta_values], parameters=[pqc.parameters])
result_v1 = job_v1.result()

print("✅ QrSamplerV1 Probabilities:", result_v1.quasi_dists)


# ===============================
# ✅ `QrSamplerV2` Usage: Running Circuits Using PUB Format
# ===============================
print("\n🚀 Running circuits with QrSamplerV2...")

# ✅ Define a PUB (Processable Unit Block)
# PUB Format: (QuantumCircuit, ParameterValues, Shots)
# ✅ QrSamplerV2 - requires Processable Unit Blocks (PUBs) in the form of tuples.
# Each tuple must be: (QuantumCircuit, parameter_values, shots)
# ❌ This format does NOT work with QrSamplerV1.
pub = (circuits[0], [], 1000)  # No parameters, 1000 shots

# ✅ Correct instantiation of QrSamplerV2 (Backend required)
sampler_v2 = QrSamplerV2(backend=backend)
job_v2 = sampler_v2.run([pub])  # Must be a **list of PUBs**
result_v2 = job_v2.result()

print("✅ QrSamplerV2 Counts:", result_v2[0].data.meas.get_counts())
