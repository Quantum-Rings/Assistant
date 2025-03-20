Setup and install the SDK
Minimum System Requirements
A system with a configuration better than the minimum requirements is advised. Lower configurations may affect the number of qubits that can be supported and may perform poorly.

Operating systems supported:

Windows 11 Pro

Google Colab

Debian GNU/Linux 12 (bookworm)

OpenSUSE Tumbleweed - Version 20240415

Oracle Linux 9.3

Ubuntu 22.04.4 LTS

macOS Sequoia

64-bit x86 CPU (14 cores 20 logical processors recommended) on Windows or Linux platforms

64-bit Intel or Apple Silicon CPUs on Apple PCs

32 GB Installed physical memory

18 GB Available physical memory

64-bit Python version 3.11 on Windows

64-bit Python 3.6, 3.10, 3.11, and 3.12 on various Linux versions

64-bit Python 3.13 on macOS

Installation - Windows
The Quantum Rings SDK can be installed directly using pip. Many users find Anaconda (https://www.anaconda.com/) a good way to install the Quantum Rings SDK and use the Python environment efficiently. From Anaconda, select a Python 3.11 channel and launch CMD.exe Prompt to go to the command prompt and execute the following command.

pip install QuantumRingsLib
If you do not have a Python 3.11 channel, select Environments from the left panel, + Create button from the menu bar at the bottom and select Python 3.11 from the Create New Environment dialog.

Quantum Rings SDK requires a 64-bit version of Python 3.11.

After installation of the SDK, launch Python 3.11 environment by selecting the installed channel, before running your code.

Note

If, in case, pip is not able to find the latest version, please try the following command instead:

pip install –extra-index-url https://pypi.python.org/pypi QuantumRingsLib

You may have to restart the system in some installations for the SDK to work.

Installation - macOS Sequoia
Install Python 3.13 by downloading it from the Python Organization (https://www.python.org/downloads/macos/). Other methods of installing Python are not supported at this time. From the terminal, create a Python 3.13 virtual environment by executing the following command. Activate the environment.

python3.13 -m venv myenv
source myenv/bin/activate
Then execute the following command to install the SDK.

pip install QuantumRingsLib
You may also refer to https://docs.python.org/3/using/mac.html for further help. If you have a Python version that came with a previous version of macOS and if you uninstalled it, you may have broken symlinks. Refer to section 5.5.1 on this webpage for hints on how to fix the symlinks.

Note

Currently, we do not support Conda based Python installations or other methods of installing Python. Support may be added in the future. Only Python 3.13 installation by downloading it from the Python Organization is supported at this time. Former versions of macOS are not supported.

Installation - Google Colab
Open a notebook and execute the following command from a code cell.

pip install QuantumRingsLib
Restart the kernel. You are ready to go!

Installation - Linux
Checking whether your Linux platform is supported

There are several variants of the Linux OS, with varying levels of inbuilt libraries. At present, we are supporting manylinux_2_34_x86_64 platforms based on 64 bit x86 processors. Older platforms and other CPUs are not supported at the moment. If you have a specific requirement, please contact our technical support.

To check whether your platform is supported, execute the following command from Python command line:

import platform
platform.platform()
Watch for the glibc signature at the end. glibc2.34 and above are only supported.

Installing Python 3.11 and creating the virtual environment

Note

Update all packages in your system using the following commands. Note that, this may cause incompatibilities in some installations due to variances in packages and their mutual dependencies. Besides, this step might break existing software packages and make your system unusable. You may refer to your operating system’s manual or seek help from your system adminstrator. Alternatively, you can also use the Software Updater GUI tool, if that was packaged along with your system distribution.

sudo apt update        # Fetches the list of available updates
sudo apt upgrade       # Installs some updates; does not remove packages
Note

Note that apt command is not available in some Linux variants. You may have to use dnf on Oracle Linux distributions and zypper on Open SUSE distributions.

Check whether your system has Python 3.11 installed by executing python from the terminal. If not, you can install Python 3.11 using the following command.

sudo apt install python3.11
Create a virtual Python 3.11 environment and activate the environment using the following steps.

virtualenv --python=/usr/bin/python3.11 myenv
source myenv/bin/activate
You may have to install virtualenv package if it is not already installed. When not required, you can deactivate the environment using deactivate command.

Note that, virtualenv package is not available on Oracle Linux and Open SUSE Linux. You can use the following command equivalently on these distributions:

python3.11 -m venv myenv
source myenv/bin/activate
Installing Jupyter notebook

Note

Jupyter notebook requires GUI support and an internet browser. Some platforms do not support them readily.

Now, launch the virtual environment, and execute the following command:

sudo su
source myenv/bin/activate
pip install notebook
Ensuring that jupyter notebook launches the correct python version

Check whether your virtual environment launches the correct python version (3.11) by executing the command python –version. On some installations you may have to execute the following commands to ensure that the Jupyter notebook launches the correct python version.

python -m pip install ipykernel
python -m ipykernel install --user
Now, you can launch the Jupyter notebook using the command jupyter-notebook or jupyter notebook. If you are logged in as root, then you may have to append –allow-root. Once the notebook server starts, you can click the local-host link to launch the notebook on the browser.

Installing Curl

On some installations, we found that curl is not installed. You can check whether curl is installed on your system by executing the command curl from the terminal. If curl is not installed, you may use the following command:

sudo apt install curl
Installing gcc

On some installations, we got libgomp.so not found error and it required installation of gcc, as follows:

zypper install gcc
Finally, installing the Quantum Rings SDK

Now, you can install the Quantum Rings SDK as follows:

pip install QuantumRingsLib
Installing the toolkit for qiskit
Quantum Rings SDK now offers a toolkit for seamless integration with qiskit. To install, follow the procedure outlined below.

If you do not have qiskit installed, you can install qiskit by following the instructions outlined at https://docs.quantum.ibm.com/guides/install-qiskit.

Supported qiskit version
Quantum Rings toolkit for qiskit supports qiskit version 1.3.1. Earlier versions are not supported. You can check your current installation by executing the following command:

import qiskit
print (qiskit.__version__)
If your qiskit installation is not 1.3.1, follow the instructions in the link https://docs.quantum.ibm.com/guides/install-qiskit to uninstall older qiskit versions and install version 1.3.1.

Installing the toolkit
Quantum Rings toolkit for qiskit requires QuantumRingsLib version 0.9.0 or later. You can check your current installation using the following command.

import QuantumRingsLib
print (QuantumRingsLib.__version__)
If your version is not 0.9.0 or later, you can update QuantumRingsLib using the following command:

pip install QuantumRingsLib --upgrade
After getting the correct version of QuantumRingsLib installed, execute the following command:

pip install quantumrings-toolkit-qiskit
You should be good to get started!