# ---
# title: Quantumringslib Parameter Binding Test
# sdk:
#   QuantumRingsLib: [0.9.x, 0.10.x]
#   quantumrings-toolkit-qiskit: []
#   GPU-enabled: [false]
# python: [3.11]
# os: [Windows 11, Ubuntu 22.04]
# tags: ['parameter binding', 'Parameter', 'ParameterVector', 'QuantumRingsLib', 'diagnostic']
# description: >
#   Diagnostic script for testing parameter binding compatibility in QuantumRingsLib 0.9 and 0.10.
#   Verifies valid and invalid usage patterns involving Parameters and ParameterVectors.
#   Includes checks for type consistency, correct dictionary key usage, and inplace parameter assignment.
#   Helps identify common user mistakes and SDK version differences.
# ---

import math
from QuantumRingsLib import (
    QuantumRegister, ClassicalRegister, QuantumCircuit,
    Parameter, ParameterVector, QuantumRingsProvider
)

# =========================================================
# ✅ STEP 0: Activate Provider
# Required to construct circuits or registers in QuantumRingsLib
# =========================================================
provider = QuantumRingsProvider()  # Uses saved credentials if available
# provider = QuantumRingsProvider(token="YOUR_TOKEN", name="YOUR_EMAIL")
provider.active_account()

# =========================================================
# ✅ STEP 1: Create Registers and Circuit
# =========================================================
q = QuantumRegister(2, "q")
c = ClassicalRegister(2, "c")
qc = QuantumCircuit(q, c)

# Define parameters
theta = Parameter("theta")
phi = Parameter("phi")
lam = Parameter("lambda")
vec = ParameterVector("p", 2)

# =========================================================
# ✅ TEST 1: All Parameters of Same Type — WORKS
# =========================================================
print("\n✅ TEST 1: u() gate with all parameters (compatible types)")

try:
    qc.rx(theta, q[0])
    qc.ry(vec[0], q[0])
    qc.rz(phi, q[1])
    qc.u(theta, phi, lam, q[1])  # ✅ All args are Parameters

    param_dict = {
        "theta": math.pi / 2,
        "phi": math.pi / 3,
        "lambda": math.pi / 4,
        "p[0]": math.pi / 5
    }

    qc.assign_parameters(param_dict, inplace=True)
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])
    print("✅ assign_parameters + u() succeeded")
    print(qc.draw())
except Exception as e:
    print("❌ Unexpected failure:", e)

# =========================================================
# ❌ TEST 2: Mixed Parameter + Float — FAILS
# =========================================================
print("\n❌ TEST 2: u() with mixed Parameter + float (should fail)")

try:
    qc2 = QuantumCircuit(q, c)
    qc2.u(theta, math.pi / 2, math.pi / 3, q[1])  # ❌ Mixed types
    print("❌ ERROR: This should have failed due to type mismatch!")
except TypeError as e:
    print("✅ Correctly failed with TypeError:", e)
except Exception as e:
    print("❌ Unexpected error type:", e)

# =========================================================
# ❌ TEST 3: assign_parameters with Parameter keys — FAILS
# =========================================================
print("\n❌ TEST 3: assign_parameters() with Parameter keys (not strings)")

try:
    qc3 = QuantumCircuit(q, c)
    qc3.rx(theta, q[0])
    bad_keys = {theta: math.pi}
    qc3.assign_parameters(bad_keys, inplace=True)
    print("❌ ERROR: Should not accept Parameter objects as keys!")
except Exception as e:
    print("✅ Correctly failed:", e)

# =========================================================
# ❌ TEST 4: assign_parameters without inplace=True — Returns None
# =========================================================
print("\n❌ TEST 4: assign_parameters without inplace=True")

try:
    qc4 = QuantumCircuit(q, c)
    qc4.rx(theta, q[0])
    qc4.rz(phi, q[1])
    qc4.measure(q[0], c[0])
    qc4.measure(q[1], c[1])

    new_qc = qc4.assign_parameters({"theta": math.pi, "phi": math.pi / 2})
    if new_qc is None:
        print("✅ assign_parameters returned None (as expected)")
    else:
        print("❌ Unexpected: assign_parameters returned a circuit:", new_qc.draw())
except Exception as e:
    print("✅ Correctly failed or returned None:", e)

# =========================================================
# END
# =========================================================
print("\n✅ All tests completed.")
