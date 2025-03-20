'''
save_provier.py
QuantumRingsLib > 0.8.0
Saves provider credentials so that the provider can be called using:
provider = QuantumRingsProvider()

Usage:
- Replace <your key> with your actual API key.
- Replace <your email> with the email associated with your Quantum Rings account.
- Run this script once to store credentials securely.
'''
import QuantumRingsLib
from QuantumRingsLib import QuantumRingsProvider

#Acquire the Quantum Rings Provider
provider = QuantumRingsProvider(token ='<your key>', name='<your email>')
print("Account Name: ", provider.active_account()["name"], "\nMax Qubits: ", provider.active_account()["max_qubits"])

#Save the account locally.
provider.save_account(token ='<your key>', name='<your email>')
print(provider.saved_accounts(False, "default"))