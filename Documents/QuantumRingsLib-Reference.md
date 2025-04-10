# QuantumRingsLib Reference

<!--
This doc merges:
- Summary-Python.md (the module-by-module overview of the native Quantum Rings API)
- Summary-QuantumCircuit.md (native usage portions)
- Relevant “Miscellaneous.md” best practices for native circuits
- Differences between 0.9.x and 0.10.x (positional shots, parameter usage, etc.)
- Emphasis on *not* mixing these native classes with Qiskit-based ones
-->

## Table of Contents

1. [Introduction](#introduction)
2. [Core Modules and Classes](#core-modules-and-classes)
   1. [AncillaRegister](#ancillaregister)
   2. [BackendV2 (Native)](#backendv2-native)
   3. [ClassicalRegister](#classicalregister)
   4. [Job Monitor and JobV1](#job-monitor-and-jobv1)
   5. [OptimizeQuantumCircuit](#optimizequantumcircuit)
   6. [Parameter and ParameterVector](#parameter-and-parametervector)
   7. [qasm2 Module](#qasm2-module)
   8. [QuantumRegister](#quantumregister)
3. [Building and Executing Native Quantum Circuits](#building-and-executing-native-quantum-circuits)
4. [Best Practices and Version Differences](#best-practices-and-version-differences)
   - [Required Provider Initialization](#required-provider-initialization)
   - [QuantumRingsLib 0.9.x vs 0.10.x](#quantumringslib-09x-vs-010x)
   - [Parameterized Circuits (Native)](#parameterized-circuits-native)
   - [Classical Register Slicing (Native)](#classical-register-slicing-native)
   - [Common Pitfalls](#common-pitfalls)
5. [No Mixing with Qiskit Integration](#no-mixing-with-qiskit-integration)
6. [Usage Examples](#usage-examples)
7. [Conclusion](#conclusion)

---

## Introduction

This **QuantumRingsLib Reference** describes the **native** Quantum Rings SDK usage (i.e., **not** the Qiskit integration). Here, you’ll use:

- `QuantumRingsLib.QuantumCircuit`, `QuantumRegister`, `ClassicalRegister`, `AncillaRegister`
- Native `BackendV2` objects (different from `quantumrings.toolkit.qiskit.QrBackendV2`)
- `job_monitor`, `JobV1` for job handling
- `OptimizeQuantumCircuit` for in-place optimization
- `Parameter` and `ParameterVector` for parameterized circuits

**Important**: Do **not** mix these classes with Qiskit-based classes from `quantumrings.toolkit.qiskit`. If you want to use Qiskit’s `QuantumCircuit`, refer to the [Qiskit-Integration-Reference.md](#).

---

**Tested Versions**:  
- 0.9.11(+)  
- 0.10.11(+)

**Key Differences**:

1. **Job Execution & `job.result()` Behavior**  
   - **0.9.x**: `job.result()` may be **non-blocking**. You must manually wait for the job to finish. For example:
     ```python
     while not job.in_final_state():
         time.sleep(1)
     result = job.result()
     ```
   - **0.10.x**: `job.result()` is **blocking** by default, so an explicit waiting loop is not required.

2. **Measurement Methods**  
   - **`measure_all()`** is fully supported in 0.10.x.  
   - In 0.9.x, if `measure_all()` is not recognized, you may need to explicitly measure each qubit, e.g.:
     ```python
     for i in range(qc.num_qubits):
         qc.measure(i, i)
     ```

3. **Parameters & Shots**  
   - **Positional `shots`** in `backend.run(qc, 100)`:
     - 0.9.x: can fail or raise a `TypeError`; must do `shots=100`.  
     - 0.10.x: supports `backend.run(qc, 100)` or `backend.run(qc, shots=100)` interchangeably.

4. **Provider Initialization**  
   - In 0.9.x, `provider.active_account()` may be required.  
   - In 0.10.x, it’s **optional** (and in some releases, deprecated), since credentials can be auto-loaded or cached.

**Tip**: Always verify your QuantumRingsLib version with:
```
import QuantumRingsLib
print(QuantumRingsLib.version)
```

## Core Modules and Classes

### AncillaRegister

- **Class**: `AncillaRegister`
- **Purpose**:  
  Define a register for **ancilla qubits** (extra qubits used for intermediate computations).
- **Constructor**:
    
        ar = AncillaRegister(size, name='')

  Parameters:
  - `size (int)`: Number of ancilla qubits
  - `name (str, optional)`: Defaults to `"a_"`

  **Key Methods**:
  - `size()`: Returns number of qubits
  - `name()`: Returns register’s name
  - `prefix()`: Returns the prefix character

**Note**: Use ancilla registers when you need extra qubits for advanced algorithms (e.g., error correction, certain subroutines).

---

### BackendV2 (Native)

- **Class**: `BackendV2`
- **Purpose**:  
  Acts as the **main execution engine** for running **native** quantum circuits on Quantum Rings hardware (different from QrBackendV2, which is for Qiskit).
- **Constructor**:
    
        backend = BackendV2()

  **Key Attributes**:
  - `version`: Version number (currently 2)
  - `num_qubits`: Max qubits supported
  - `max_circuits`: Max circuits per run
  - `name`, `description`, `online_date`, `backend_version`

  **Key Method**:  
  - `run(run_input, **kwargs)`: Executes a **QuantumRingsLib.QuantumCircuit**
    - `run_input`: A `QuantumCircuit` object
    - `kwargs`: Execution parameters (shots, mode, performance, etc.)
    - Returns a `JobV1` object

When explaining backend execution natively, highlight that **transpilation is not needed**. Just pass the `QuantumCircuit`.

---

### ClassicalRegister

- **Class**: `ClassicalRegister`
- **Purpose**:  
  Define classical registers for storing measurement outcomes in **native** circuits.
- **Constructor**:
    
        cr = ClassicalRegister(size, name='')

  - `size (int)`: Number of classical bits
  - `name (str, optional)`: Defaults to `"c_"`

  **Key Methods**:
  - `size()`: # bits
  - `name()`: Register name
  - `prefix()`: Prefix character

**Note**: In **native** mode, **no slicing** is allowed (e.g., `c[:2]` will fail).

---

### Job Monitor and JobV1

- **`job_monitor(job, interval=1, quiet=False)`**:
  - Monitors the status of a submitted **native** job (`JobV1`) until completion.
  - Parameters:
    - `job`: The job object
    - `interval (int)`: # of seconds between checks
    - `quiet (bool)`: If `True`, suppress status messages

- **Class**: `JobV1`
  - **Represents** a submitted job for **native** execution.
  - Typically returned by `backend.run(qc)`
  - Attributes:
    - `version`, `_async`
  - Methods:
    - `job_id()`: Returns job ID
    - `done()`, `running()`, `cancelled()`: Check status
    - `in_final_state()`: True if job is finished
    - `wait_for_final_state(timeout, wait, callback)`
    - `result()`: Retrieves final result
    - `cancel()`: Cancels the job
    - `backend()`: Returns associated backend

Use `job_monitor(job)` or `job.wait_for_final_state()` to wait for job completion.

---

### OptimizeQuantumCircuit

- **Function**: `OptimizeQuantumCircuit(qc)`
- **Purpose**: Optimizes a **native** quantum circuit for better performance.
- **Returns**: `True` if optimization succeeded, `False` if not.
- **Important**:
  - **Modifies** `qc` in-place
  - Do **not** reassign it: `qc = OptimizeQuantumCircuit(qc)` is incorrect
  - Raises `RunTimeError` if something goes wrong

**Warning**: This function **cannot** be used with Qiskit-based circuits (`qiskit.QuantumCircuit`). For Qiskit, use `transpile()`.

Use `OptimizeQuantumCircuit` especially for **native** circuits that have multiple qubits, deep gate sequences, or repeated patterns.

---

### Parameter and ParameterVector

**Parameter (Class)**:  
- Creates symbolic parameters for parameterized quantum circuits in **native** usage.
- Example:
  
      from QuantumRingsLib import Parameter
      theta = Parameter("theta")

**ParameterVector (Class)**:  
- Manages a vector of named parameters.
- Example:
  
      from QuantumRingsLib import ParameterVector
      vec = ParameterVector("p", length=4)

**Key Points** (Native Only):
- Use `.assign_parameters(..., inplace=True)`
- All parameters in a gate must be either all `Parameter` or all `float`
- Use **string-based keys**: `{"theta": 3.14}`, **not** `{theta: 3.14}`
- Omitting `inplace=True` returns `None`

---

### qasm2 Module

- **Class**: `qasm2`
- **Purpose**: Build quantum circuits from QASM 2.0 code.
- **Methods**:
  - `load(filename, ...)`: Load a circuit from QASM file
  - `loads(qasm2string, ...)`: Load from QASM string

Useful for importing circuits from external tools into **native** `QuantumRingsLib.QuantumCircuit`.

---

### QuantumRegister

- **Class**: `QuantumRegister`
- **Purpose**: Define the quantum registers for a **native** circuit.
- **Constructor**:
    
        qr = QuantumRegister(size, name='q')

  - `size (int)`: # qubits
  - `name (str, optional)`: Defaults to `"q_"`

**Use**:  
```
from QuantumRingsLib import QuantumRegister, QuantumCircuit
q = QuantumRegister(3, "q")
qc = QuantumCircuit(q)
```

## Building and Executing Native Quantum Circuits

**Steps**:

1. **Provider & Backend**  
    ```
    from QuantumRingsLib import QuantumRingsProvider
    provider = QuantumRingsProvider(token="YOUR_API", name="YOUR_EMAIL")
    provider.active_account()
    backend = provider.get_backend("some_native_backend")
    ```

2. **Create Registers** (`QuantumRegister`, `ClassicalRegister`, `AncillaRegister`)

3. **Construct** a `QuantumCircuit`:

    ```
    from QuantumRingsLib import QuantumCircuit
    qc = QuantumCircuit(q, c)
    qc.h(0)
    qc.cx(0,1)
    qc.measure_all()
    ```

4. **(Optional) Optimize**:

    ```
    from QuantumRingsLib import OptimizeQuantumCircuit
    success = OptimizeQuantumCircuit(qc)
    # modifies qc in place
    ```

5. **Execute**:

    ```
    job = backend.run(qc, shots=100)
    from QuantumRingsLib import job_monitor
    job_monitor(job)
    result = job.result()
    counts = result.get_counts()
    print(counts)
    ```

No transpilation required. **Use** `OptimizeQuantumCircuit` if you want circuit optimizations in native mode.

---

## Best Practices and Version Differences

### Required Provider Initialization

Before creating **any** `QuantumCircuit`, `QuantumRegister`, or `ClassicalRegister`, you **must** initialize and activate a `QuantumRingsProvider`. This authenticates your account and allocates qubits. Even if you’re not immediately executing the circuit, do:

```
from QuantumRingsLib import QuantumRingsProvider
provider = QuantumRingsProvider(token="...", name="...") provider.active_account()
```

You do **not** need a backend unless you plan on `backend.run(qc)`.

### QuantumRingsLib 0.9.x vs 0.10.x

- **Positional shots** in `backend.run(qc, 100)`:
  - 0.9.x: raises `TypeError`
  - 0.10.x: works
- Always safer to do `backend.run(qc, shots=100)` to avoid version issues.

### Parameterized Circuits (Native)

- 0.9.x and 0.10.x both support `Parameter`, `ParameterVector`.
- Must use `.assign_parameters({...}, inplace=True)` with string keys only.
- **No mixing** float and `Parameter` in the same gate call.

### Classical Register Slicing (Native)

- **Expressions** like `c[:2]` fail with `TypeError`.
- Only individual indexing: `c[0]`, `c[1]`, etc.

### Common Pitfalls

- Don’t assume Qiskit’s `.assign_parameters()` or `.bind_parameters()` works in **native**. Use the native approach described above.
- If you see a **pybind11 casting** error, it’s often a parameter usage mismatch.
- If a user tries `backend.run(qc, 100)` on 0.9.x, it fails.
- `OptimizeQuantumCircuit` modifies circuits in-place, be careful not to reassign `qc`.

---

## No Mixing with Qiskit Integration

**Important**: The classes in this doc (`QuantumRingsLib.QuantumCircuit`, `BackendV2`, `OptimizeQuantumCircuit`) are **not** compatible with Qiskit-based modules like `QrBackendV2`. If you want to use Qiskit circuits, see [Qiskit-Integration-Reference.md](#). Don’t combine them:

- `QuantumRingsLib.QuantumCircuit` + `QrBackendV2` → **Error**  
- `qiskit.QuantumCircuit` + `OptimizeQuantumCircuit` → **Error**

Always keep them separate.

---

## Usage Examples

### Example 1: Basic 2-Qubit Circuit

    from QuantumRingsLib import QuantumRingsProvider, QuantumCircuit, QuantumRegister, ClassicalRegister, job_monitor

    # Provider
    provider = QuantumRingsProvider(token="YOUR_API", name="YOUR_EMAIL")
    provider.active_account()

    # Registers
    q = QuantumRegister(2, "q")
    c = ClassicalRegister(2, "c")
    qc = QuantumCircuit(q, c)

    qc.h(0)
    qc.cx(0,1)
    qc.measure_all()

    # Backend
    backend = provider.get_backend("native_backend")
    job = backend.run(qc, shots=200)
    job_monitor(job)
    result = job.result()
    counts = result.get_counts()
    print(counts)

### Example 2: Parameterized Circuit + Optimize

    from QuantumRingsLib import (QuantumRingsProvider, QuantumCircuit, QuantumRegister, ClassicalRegister, 
                                 Parameter, OptimizeQuantumCircuit, job_monitor)

    provider = QuantumRingsProvider()
    provider.active_account()
    backend = provider.get_backend("native_backend")

    q = QuantumRegister(2, "q")
    c = ClassicalRegister(2, "c")
    qc = QuantumCircuit(q, c)

    theta = Parameter("theta")
    qc.rx(theta, q[0])
    qc.cx(q[0], q[1])
    qc.measure(q[0], c[0])
    qc.measure(q[1], c[1])

    # Assign parameter
    qc.assign_parameters({"theta": 3.14}, inplace=True)

    # Optimize
    success = OptimizeQuantumCircuit(qc)

    job = backend.run(qc, shots=100)
    job_monitor(job)
    res = job.result()
    print("Counts:", res.get_counts())
