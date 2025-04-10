# Quantum Rings SDK Overview and Setup

## Table of Contents

1. [Introduction](#introduction)  
2. [System Requirements](#system-requirements)  
   - [Supported OS](#supported-os)  
   - [Hardware](#hardware)  
   - [Python Versions](#python-versions)  
3. [Installation Steps](#installation-steps)  
   - [Windows](#windows)  
   - [macOS Sequoia](#macos-sequoia)  
   - [Google Colab](#google-colab)  
   - [Linux](#linux)  
   - [Qiskit Integration Toolkit](#qiskit-integration-toolkit)  
4. [Plans & Pricing](#plans--pricing)  
5. [License Reference](#license-reference)  
6. [Contact & Official Resources](#contact--official-resources)  
7. [Further Reading](#further-reading)  
8. [Revision Notes](#revision-notes)

---

## Introduction

**Quantum Rings** is a comprehensive SDK for developing, simulating, and optimizing quantum circuits.  
It supports:

- **Native QuantumRingsLib** features (direct circuit construction).  
- **Qiskit Integration** (via `quantumrings-toolkit-qiskit` to run Qiskit circuits on Quantum Rings).

This guide covers **installation**, **pricing**, and **basic references** to get started.  
For deeper usage details, refer to:

- [QuantumRingsLib Reference (TBD)](#)
- [Qiskit Integration Reference (TBD)](#)

---

## System Requirements

### Supported OS

- Windows 11 Pro  
- Google Colab  
- Debian GNU/Linux 12 (bookworm)  
- OpenSUSE Tumbleweed (Version 20240415)  
- Oracle Linux 9.3  
- Ubuntu 22.04.4 LTS  
- macOS Sequoia

### Hardware

- **Windows/Linux CPU**: 64-bit x86 (14 cores / 20 logical processors recommended)  
- **macOS CPU**: 64-bit Intel or Apple Silicon  
- **Memory**: 32 GB installed (18 GB free recommended)

### Python Versions

- **Windows**: 3.11 (64-bit)  
- **Linux**: 3.6, 3.10, 3.11, 3.12  
- **macOS**: 3.13  

> **Note**: A higher-end system helps simulate more qubits more efficiently.

---

## Installation Steps

Below are consolidated instructions for each major platform.

### Windows

1. Install [Anaconda](https://www.anaconda.com/) or ensure you have Python 3.11 (64-bit).  
2. Open a terminal/Anaconda prompt and run:

```
pip install QuantumRingsLib
```

3. If pip cannot find the latest version:

```
pip install --extra-index-url https://pypi.python.org/pypi QuantumRingsLib
```

4. A system restart might be required in some cases.

### macOS Sequoia

1. Install Python 3.13 from [python.org](https://www.python.org/).  
2. Create & activate a virtual environment:

```
python3.13 -m venv myenv
source myenv/bin/activate
```

3. Install Quantum Rings:

```
pip install QuantumRingsLib
```

4. **Note**: Conda-based installs are not supported on macOS yet.

### Google Colab

In a Colab notebook cell:

```
!pip install QuantumRingsLib
```

Then **restart** the runtime to complete setup.

### Linux

1. **Check** platform compatibility (`manylinux_2_34_x86_64`, `glibc >= 2.34`).  
2. **Install/Update** packages:

```
sudo apt update && sudo apt upgrade
```

3. **Install** Python 3.11 (or another supported version).  
4. **Create & Activate** a virtual environment:

```
python3.11 -m venv myenv
source myenv/bin/activate
```

5. **Optional**: Install Jupyter Notebook/ipykernel for dev use.  
6. **Install** QuantumRingsLib:

```
pip install QuantumRingsLib
```

> Some distributions may need `curl` or `gcc` to fix missing libraries.

### Qiskit Integration Toolkit

**Requirements**:
- Qiskit ≥ 1.3.1  
- QuantumRingsLib ≥ 0.9.0

```
pip install quantumrings-toolkit-qiskit
```

After installation, you can run Qiskit circuits on Quantum Rings backends.  
For usage details, see [Qiskit Integration Reference (TBD)](#).

### Module Compatibility:
Currently, quantumrings.toolkit.qiskit 0.1.10 is tested with Qiskit ≤ 1.4.1. Attempting Qiskit 2.0 will result in an import error (ImportError: cannot import name 'BackendEstimator'). Future versions of quantumrings.toolkit.qiskit may address Qiskit 2.0 compatibility.

---

## Optional: Setting Up a Local Provider

While you can run Quantum Rings with default settings, we **strongly recommend** configuring a **local provider** for your environment. This ensures:

1. **Faster** job submission (reduced overhead).
2. **Consistent** authentication for advanced features.
3. **Easier** offline or private cluster usage if available.

An example of local provider setup:

```
from QuantumRingsLib import QuantumRingsProvider
```

# Acquire a local or saved provider instance.
# This can store your credentials locally for repeated usage.
provider = QuantumRingsProvider(token="<YOUR_TOKEN>", name="<YOUR_EMAIL>")

# Optionally, you can save the account for future sessions:
provider.save_account(token="<YOUR_TOKEN>", name="<YOUR_EMAIL>")

# Then confirm the provider is active
provider.active_account()

### Note: If you choose not to set up a local provider, you can still create one on the fly each session. However, we recommend this approach for streamlined development.

## Best Practices for the LLM

1. **Confirm Version Synergy**  
   - If the user requests Qiskit-based usage, **always** ask for both the `quantumrings.toolkit.qiskit` version and the Qiskit version.
   - If they mention “Qiskit 2.0” + “quantumrings.toolkit.qiskit 0.1.10,” warn them of the known incompatibility.

2. **Provider & Backend Placement**  
   - After the user’s import statements, **immediately** define the provider and backend (e.g., `provider = QuantumRingsProvider()`, `backend = provider.get_backend("...")`).
   - **Do not** place provider or backend creation inside a function if they intend to run multiple circuits or rely on persistent credentials.

3. **No Native/Qiskit Mixing**  
   - If the user says they’re using native `QuantumRingsLib.QuantumCircuit`, do **not** use Qiskit methods like `.transpile()` or gates like `.mcp(...)` with `Parameter`.
   - If they use `qiskit.QuantumCircuit`, provide Qiskit-based references (`QrBackendV2`), etc.

4. **Check Code Examples**  
   - Before giving final code, scan the relevant tested code examples (marked `(+)`) for the user’s environment. If no example matches their version synergy, disclaim or provide a fallback.

5. **Ask for Clarification**  
   - If uncertain which version or approach the user has, politely ask. This avoids mixing modules or referencing unsupported methods.

## Plans & Pricing

- **Academic (Free)**  
  - Up to 128 qubits  
  - Non-commercial, academic usage  
  - Community support  

- **Starter (Free)**  
  - Up to 64 qubits  
  - Ideal for learning and evaluation (non-commercial)  
  - Community support  

- **Personal/Startup ($35/month)**  
  - Up to 128 qubits  
  - Email support  
  - Intended for small teams (<25 employees, <$1M annual revenue)

- **Enterprise (Custom)**  
  - Unlimited qubits (hardware permitting)  
  - Professional support  
  - Commercial usage at any scale  

> **Tip**: You can upgrade/downgrade or request extra qubits anytime.  
> Email [info@quantumrings.com](mailto:info@quantumrings.com) for details.

---

## License Reference

By installing or using Quantum Rings SDK, you agree to our **Evaluation Agreement**.  
For the full legal text, see:

- [License.md](./License.md)

**Key Points** (non-exhaustive):
- **Beta/Evaluation**: The SDK may contain bugs; usage is for evaluation unless otherwise stated.  
- **Intellectual Property**: All proprietary rights remain with Quantum Rings, Inc.  
- **Disclaimer**: Provided “AS IS”; liability capped at \$50.  
- **Confidentiality**: Non-public info about the SDK must not be disclosed.

---

## Contact & Official Resources

- **Website**: [https://www.quantumrings.com](https://www.quantumrings.com)  
- **Email**: [info@quantumrings.com](mailto:info@quantumrings.com)  
- **Address**: 2000 Central Ave, Suite 100, Boulder CO, 80301  
- **GitHub**: [https://github.com/Quantum-Rings](https://github.com/Quantum-Rings)  
  - **Contribute**: [https://github.com/Quantum-Rings/Assistant](https://github.com/Quantum-Rings/Assistant)  
  - **Bug Reports**: [https://github.com/Quantum-Rings/Assistant/Bugs](https://github.com/Quantum-Rings/Assistant/Bugs)

---

## Further Reading

- **Best Practices**: See [QuantumRingsLib Reference (TBD)](#) for native circuit creation, provider setup, and performance optimizations.  
- **Qiskit Integration**: Check [Qiskit Integration Reference (TBD)](#) for instructions on `QrBackendV2`, `QrEstimatorV1/V2`, `QrSamplerV1/V2`, and transpilation workflows.  
- **Code Examples**: Refer to [Code-Examples.md (TBD)](#) for real-world usage scenarios.

---

## Revision Notes

- **2024-XX-XX**: Initial merged overview from `Qiskit.md`, `Pricing.md`, partial `Miscellaneous.md`, referencing `License.md`.  


