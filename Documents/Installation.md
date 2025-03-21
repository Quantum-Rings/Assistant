# Quantum Rings SDK Installation & Setup

Below is an overview of how to install and configure the Quantum Rings SDK on various platforms, along with notes on requirements and optional toolkit installations.

---

## Minimum System Requirements

- **Supported OS:**
  - Windows 11 Pro
  - Google Colab
  - Debian GNU/Linux 12 (bookworm)
  - OpenSUSE Tumbleweed (Version 20240415)
  - Oracle Linux 9.3
  - Ubuntu 22.04.4 LTS
  - macOS Sequoia

- **CPU:**  
  - Windows/Linux: 64-bit x86 (14 cores / 20 logical processors recommended)  
  - macOS: 64-bit Intel or Apple Silicon

- **Memory:** 32 GB installed, 18 GB free recommended  
- **Python Versions:**  
  - **Windows:** 3.11 (64-bit)  
  - **Linux:** 3.6, 3.10, 3.11, 3.12 (64-bit)  
  - **macOS:** 3.13 (64-bit)  

 A more capable system is advised for better performance and higher qubit counts.

---

## Windows Installation

1. **Recommended:** Use [Anaconda](https://www.anaconda.com/) with a Python 3.11 environment.  
2. **Install via Pip:**  
```
   pip install QuantumRingsLib
```

If pip cannot find the latest version, try:

```
pip install –-extra-index-url https://pypi.python.org/pypi QuantumRingsLib
```
Note: A system restart may be required on some installations.
macOS Sequoia Installation
Supported Python: 3.13 from python.org.
## Create and activate a virtual environment:
```
python3.13 -m venv myenv
source myenv/bin/activate
```
## Install Quantum Rings SDK:
```
pip install QuantumRingsLib
```
Important: No Conda-based installs are supported on macOS yet; only the official Python 3.13 distribution.
Google Colab
Install via Pip in a Colab notebook cell:
```
!pip install QuantumRingsLib
```
Restart the kernel to complete setup.
Linux Installation
Check Platform Compatibility:
Manylinux_2_34_x86_64 and glibc >= 2.34.
Run platform.platform() in Python to verify.
Install/Update System Packages:
sudo apt update && sudo apt upgrade (or equivalent in your distro).
Install Python 3.11 (e.g., sudo apt install python3.11).
## Create & Activate a Virtual Environment:
```
virtualenv --python=/usr/bin/python3.11 myenv
source myenv/bin/activate
```
(On some distros: python3.11 -m venv myenv)
Install Jupyter Notebook (Optional):
```
pip install notebook
```
If needed, install ipykernel to ensure the correct Python version is used:
```
python -m pip install ipykernel
python -m ipykernel install --user
```
## Install Quantum Rings SDK:
```
pip install QuantumRingsLib
```
## Troubleshooting Dependencies
Some systems may require curl (sudo apt install curl) or gcc (zypper install gcc) to resolve libgomp.so not found errors.
Installing the Toolkit for Qiskit Integration
Check Qiskit Version: Must be 1.3.1 (earlier versions not supported).
```
import qiskit
print(qiskit.__version__)
```
Check QuantumRingsLib Version: Must be 0.9.0 or later.
```
import QuantumRingsLib
print(QuantumRingsLib.__version__)
```
If needed, upgrade:
```
pip install QuantumRingsLib --upgrade
```
## Install the Toolkit:
```
pip install quantumrings-toolkit-qiskit
```
This toolkit allows seamless integration with Qiskit once the correct versions of both Qiskit and QuantumRingsLib are installed.

That’s it! You’re now ready to develop and experiment with quantum circuits using the Quantum Rings SDK. For specific troubleshooting or advanced configurations, refer to detailed documentation or contact technical support.