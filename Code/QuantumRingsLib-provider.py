# ---
# title: Quantumringslib Provider Setup
# sdk ["tested(+)", "fails(!)", "untested(?)"]:
#   QuantumRingsLib: [0.9.11(+), 0.10.11(+)]
#   quantumrings-toolkit-qiskit: []
#   Qiskit: []
#   GPU-enabled: [false]
# python: [3.11(+)]
# os: [Windows 11(+), Ubuntu 22.04(?)]
# tags: ['provider', 'authentication', 'QuantumRingsProvider', 'setup']
# description: >
#   Demonstrates how to initialize and activate a QuantumRingsProvider using saved credentials 
#   or manual API token entry. Essential setup step for accessing Quantum Rings backends and 
#   executing circuits. Suitable for both persistent and interactive session management.
# ---

import QuantumRingsLib
from QuantumRingsLib import QuantumRingsProvider

#Acquire the Quantum Rings Provider
provider = QuantumRingsProvider(token ='<your key>', name='<your email>')
print("Account Name: ", provider.active_account()["name"], "\nMax Qubits: ", provider.active_account()["max_qubits"])

#Save the account locally.
provider.save_account(token ='<your key>', name='<your email>')
print(provider.saved_accounts(False, "default"))