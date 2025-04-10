# ---
# title: Quantumringslib Param 10
# sdk ["tested(+)", "fails(!)", "untested(?)"]:
#   QuantumRingsLib: [0.9.11(!), 0.10.11(+)]
#   quantumrings-toolkit-qiskit: []
#   Qiskit: []
#   GPU-enabled: [false]
# python: [3.11(+)]
# os: [Windows 11(+), Ubuntu 22.04(?)]
# tags: ['parameters', 'assign_parameters', 'ParameterVector', 'QuantumRingsLib']
# description: >
#   Demonstrates parameterized quantum circuit construction using QuantumRingsLib 0.10.x.
#   Shows how to use `Parameter` and `ParameterVector` for gates like `u()` and `mcp()`, 
#   and correctly assign values using `.assign_parameters(..., inplace=True)`.
#   Highlights best practices and pitfalls, such as avoiding mixed parameter types and 
#   ensuring all keys in assignment dictionaries are strings.
# ---

# ✅ Import necessary libraries
import QuantumRingsLib
from QuantumRingsLib import QuantumRegister, ClassicalRegister, QuantumCircuit, QuantumRingsProvider
from QuantumRingsLib import Parameter, ParameterVector
from math import pi

# =====================================
# ✅ STEP 1: Setup Quantum Rings Provider and Backend
# =====================================
provider = QuantumRingsProvider()
backend = provider.get_backend("scarlet_quantum_rings")  # Example backend
shots = 100  # Number of circuit executions (shots)
total_qubits = 5  # Define the total number of qubits for the circuit

# =====================================
# ✅ STEP 2: Create Quantum and Classical Registers
# =====================================
q = QuantumRegister(total_qubits, "q")
c = ClassicalRegister(total_qubits, "c")
qc = QuantumCircuit(q, c)

# =====================================
# ✅ STEP 3: Define Parameters for Parameterized Gates
# =====================================
# 🚨 WARNING: Always assign parameters BEFORE execution.

myparamvec = ParameterVector("test", 6)  # ✅ Safe for Quantum Rings SDK
theta = Parameter("theta")  # ✅ Safe for Quantum Rings SDK
phi = Parameter("phi")
lam = Parameter("lambda")
gamma = Parameter("gamma")

# =====================================
# ✅ STEP 4: Build the Quantum Circuit with Parameters
# =====================================
qc.h(q[0])  # Hadamard gate
qc.x(q[1])
qc.x(q[2])
qc.h(q[3])
qc.x(q[4])
qc.h(q[4])

# ✅ Safe use of parameters BEFORE execution
#qc.mcp(theta, [q[0], q[1], q[3]], q[2])  
qc.mcp(0.3, [0, 1, 3], 2)
qc.rx(phi, 3)
qc.ry(pi / 2, 4)  
qc.rz(myparamvec[5], 0)
qc.u(myparamvec[0], myparamvec[1], myparamvec[2], 1)

# Add measurement
qc.measure_all()

# =====================================
# ✅ STEP 5: Assign Parameter Values BEFORE Execution
# =====================================
# 🚨 WARNING: Assigning parameters AFTER transpilation will FAIL.
myparam = {
    "test[0]": pi,
    "test[1]": pi / 2,
    "test[2]": pi / 3,
    "test[3]": pi / 4,
    "test[4]": pi / 6,
    "test[5]": pi / 7,
    "theta": pi / 8,
    "phi": pi / 9,
    "lambda": pi / 11,
    "gamma": pi / 13,
}

# ✅ Assign parameters BEFORE execution (SAFE)
qc.assign_parameters(myparam, inplace=True)  # ✅ Works correctly

# =====================================
# ✅ STEP 6: EXECUTE ON QUANTUM RINGS BACKEND (NO TRANSPILATION NEEDED)
# =====================================
print("\n🚀 Executing the Quantum Rings circuit...")
job = backend.run(qc, shots=shots)



# ✅ Retrieve and Display Results
result = job.result()
counts = result.get_counts()
print("✅ Measurement Results:", counts)

# =====================================
# ✅ STEP 7: QISKIT CIRCUITS REQUIRE TRANSPILATION
# =====================================
# 🚨 WARNING: Quantum Rings SDK does NOT require transpilation for native circuits.
# ✅ If using a Qiskit circuit, use `transpile()` before execution.

# Example (ONLY for Qiskit circuits, not needed for Quantum Rings SDK):
# transpiled_qc = transpile(qc, backend)
# job = backend.run(transpiled_qc)  # ✅ Works for Qiskit circuits

print("\n🎉 SCRIPT COMPLETE: Follow best practices to avoid parameter assignment errors!")
