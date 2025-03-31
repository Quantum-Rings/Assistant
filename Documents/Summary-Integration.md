# LLM Instructions for Summary-Integration.md

llm_guidelines:
  purpose: >
    This document provides guidance on integrating Quantum Rings with Qiskit, including when 
    to use QrBackendV2, QrEstimatorV1, and QrSamplerV2. It clarifies interoperability rules 
    and circuit compatibility constraints for LLM-based assistance.

  llm_expectations:
    - Treat the examples as canonical. Do not invent alternate import paths or usage styles.
    - Always match the circuit class to the expected backend or estimator type.
    - If using QrBackendV2 or QrEstimatorV1, always import circuits from 'qiskit', not 'QuantumRingsLib'.
    - Help users understand when mismatched imports or classes may cause runtime exceptions.
    - Encourage use of at least 2 qubits in QrBackendV2 initialization to avoid cx-related errors.
    - Add clear notes about when and why certain APIs require Qiskit circuits.
    - Recommend starting from a working example and modifying it gradually.
    - For QrSamplerV1, use only the documented method of accessing results via 'quasi_dists[0]'.
    - Do not invent or infer alternate result access methods for QrSamplerV1.

  mistake_avoidance:
    - Do not suggest using QuantumRingsLib.QuantumCircuit with QrBackendV2 or Estimators.
    - Avoid using unsupported circuit formats, inputs, or argument types.
    - Warn when using fewer qubits than required for default gate registration in QrBackendV2.
    - Do not apply result access patterns from QrSamplerV2 or Qiskit to QrSamplerV1.

# Extended API Reference for Quantum Rings and Qiskit Integration

This document lists the available modules and classes for the Quantum Rings API, covering both native functionality and Qiskit integration. Use this summary as a guide for understanding the API structure and for generating examples or answering questions. Some sections (e.g., parts of the Qiskit integration) may be redundant with earlier summaries but are included here for completeness.

---

## 1. Quantumrings Toolkit for Qiskit Integration

These modules enable integration with Qiskit, allowing users to run Qiskit circuits on Quantum Rings hardware and leverage additional machine-learning tools.

### QrBackendV2 Module
- **Classes/Methods:**
  - `QrBackendV2` (constructor, target, max_circuits, num_qubits)
  - Internal methods: `_build_target()`, `_default_options()`
  - `run()`: Executes a Qiskit circuit.
- **Usage:**  
  Essential for running Qiskit circuits on Quantum Rings hardware.
  
### QrEstimator Modules
- **QrEstimatorV1 and QrEstimatorV2:**  
  - Both provide an `options` attribute, constructors, and a `run()` method.
- **Usage:**  
  For performing estimation tasks on Quantum Rings backends.

### QrJobV1 Module
- **Classes/Methods:**
  - `QrJobV1` (constructor, `cancel()`, `submit()`, `get_counts()`, `get_probabilities()`, `result()`, `status()`)
- **Usage:**  
  Manages job submission and retrieval for Qiskit circuits.

### QrSampler Modules
- **QrSamplerV1 and QrSamplerV2:**
  - Include an `options` attribute, constructors, and a `run()` method.
- **Usage:**  
  For sampling outcomes from quantum circuits.

### QrStatevector Modules
- **QrStatevector and QrStatevectorSampler:**
  - `QrStatevector`: Provides `data()` and `sample_memory()`.
  - `QrStatevectorSampler`: Offers a `run()` method.
- **Usage:**  
  For retrieving state vector data and sampling.

### Qiskit Machine Learning Integration
- **Modules:**
  - `QrEstimatorQNN`
  - `QrSamplerQNN`
  - `QrFidelityQuantumKernel`
  - `QrTrainableFidelityQuantumKernel`
- **Usage:**  
  These modules integrate Quantum Rings capabilities into Qiskit's machine learning package.

> **LLM Note:**  
> When training, emphasize that these Qiskit integration modules are designed to bridge familiar Qiskit workflows with Quantum Rings hardware, and they follow similar design patterns (e.g., options, run methods) across estimator, sampler, and statevector functionalities.

---

## 2. QuantumRingsLib Native API

These modules are part of the core Quantum Rings SDK and provide native functionality for building, executing, and manipulating quantum circuits.

### AncillaRegister Module
- **Class:** `AncillaRegister`
- **Constructor:** `AncillaRegister(size, name='')`
  - *Parameters:*  
    - `size`: Number of ancilla qubits.
    - `name`: (Optional) Register name (default: `"a_"`).
- **Key Methods:**  
  - `size()`, `name()`, `prefix()`

### BackendV2 Module (Native)
- **Class:** `BackendV2`
- **Attributes:**  
  - `version`, `dt`, `dtm`, `max_circuits`, `num_qubits`, `name`, `description`, `online_date`, `backend_version`
- **Methods:**  
  - Constructor and `run()`
- **Usage:**  
  Executes native QuantumRingsLib circuits via `provider.get_backend()`.

### ClassicalRegister Module
- **Class:** `ClassicalRegister`
- **Constructor:** `ClassicalRegister(size, name='')`
- **Key Methods:**  
  - `size()`, `name()`, `prefix()`

### Job Monitor Module
- **Function:** `job_monitor(job, interval=1, quiet=False)`
- **Usage:**  
  Waits until a job reaches a terminal status (DONE, CANCELLED, ERROR).

### JobV1 Module
- **Class:** `JobV1`
- **Key Methods:**  
  - `job_id()`, `done()`, `running()`, `cancelled()`, `in_final_state()`, `wait_for_final_state()`, `result()`, `cancel()`, `status()`, `backend()`
- **Usage:**  
  Represents a submitted job for native circuit execution.

### OptimizeQuantumCircuit Module
- **Function:** `OptimizeQuantumCircuit(qc)`
- **Usage:**  
  Optimizes a quantum circuit for performance (returns `True` if successful).

### Parameter and ParameterVector Modules
- **Parameter Module:**
  - **Class:** `Parameter`
  - **Constructor:** `Parameter(name)`
  - **Key Method:** `name()`
- **ParameterVector Module:**
  - **Class:** `ParameterVector`
  - **Constructor:** `ParameterVector(name, length)`
  - **Key Methods:** `name()`, `resize()`, `params()`, `index()`

### qasm2 Module
- **Class:** `qasm2`
- **Key Methods:**  
  - `load(filename, include_path, include_input_directory, strict)`
  - `loads(qasm2string, include_path, include_input_directory, strict)`
- **Usage:**  
  Convert QASM 2.0 files or strings into quantum circuits.

### QuantumCircuit Module
- **Class:** `QuantumCircuit`
- **Attributes:**  
  - `num_qubits`, `num_ancillas`, `num_clbits`, `header`, `instances`, `global_phase`, `prefix`, `op_start_times`, etc.
- **Key Methods:**  
  - Single-qubit gates: `h()`, `x()`, `i()`, `t()`, `s()`, `tdg()`, `sx()`, `sxdg()`, etc.
  - Rotation gates: `rx()`, `ry()`, `rz()`, `u()`, etc.
  - Controlled gates: `cx()`/`cnot()`, `cp()`, `cu1()`, `cu3()`, etc.
  - Multi-qubit operations: `ccx()`, `ccz()`, `cswap()`, `fredkin()`, etc.
  - Circuit management: `clear()`, `compose()`, `copy()`, `measure()`, `measure_all()`, `qasm()`, `draw()`, etc.
- **Usage:**  
  Core interface for constructing and manipulating quantum circuits in the native SDK.

### QuantumRegister Module
- **Class:** `QuantumRegister`
- **Constructor:** `QuantumRegister(size, name='')`
- **Key Methods:**  
  - `size()`, `name()`, `prefix()`
- **Usage:**  
  Defines quantum registers for circuits.

### QuantumRingsProvider Module
- **Class:** `QuantumRingsProvider`
- **Key Methods:**  
  - Constructor, `get_backend()`, `backends()`, `active_account()`, `delete_account()`, `save_account()`, `saved_accounts()`
- **Usage:**  
  Provides access to available Quantum Rings backends and manages account credentials.

### Result Module
- **Class:** `Result`
- **Attributes:**  
  - `backend_name`, `backend_version`, `qobj_id`, `job_id`, `success`, `results`, `date`, `status`, `header`
- **Key Methods:**  
  - Constructor, `to_dict()`, `data()`, `get_memory()`, `get_counts()`, `get_statevector()`, `get_unitary()`, `from_dict()`, `get_probabilities()`, `get_densitymatrix()`, `get_classicalregister()`
- **Usage:**  
  Holds the outcome of a quantum circuit execution.

> **LLM Instruction:**  
> Use these sections to help generate detailed examples and to answer questions about native circuit construction, job handling, and result processing.

---

## 3. Categorizing and Avoiding Redundancy

- **Redundancy Note:**  
  Some modules (e.g., parts of `quantumrings.toolkit.qiskit`) appear in both this document and previous API summaries. When training, emphasize that the Quantum Rings toolkit for Qiskit integration is a subset of the overall API and is meant to extend the native functionality for Qiskit users.

- **Categorization Strategy:**  
  - **Integration Modules:**  
    Group all modules under `quantumrings.toolkit.qiskit` and its machine-learning submodules.
  - **Native Quantum Rings Modules:**  
    Group all modules under `QuantumRingsLib` (AncillaRegister, BackendV2, ClassicalRegister, JobV1, OptimizeQuantumCircuit, Parameter, qasm2, QuantumCircuit, QuantumRegister, QuantumRingsProvider, Result).
  - **Instruction and Utility Functions:**  
    Include modules like `job_monitor` and `OptimizeQuantumCircuit` that assist in execution and performance tuning.

> **LLM Instruction:**  
> When encountering redundant content, the LLM should be able to cross-reference the integration modules with the native modules, noting that the Qiskit integration is built on top of the native API and shares many common functionalities.

---

## 4. Usage Instructions and Best Practices

- **When to Use Each Category:**  
  - Use the **Qiskit Integration modules** if you have an existing Qiskit codebase or prefer Qiskit's API, but want to run circuits on Quantum Rings hardware.
  - Use the **Native QuantumRingsLib modules** for full access to advanced features, such as additional circuit attributes and native execution without transpilation.

- **Generating Examples:**  
  - Show how to create registers (quantum, classical, ancilla) using the native constructors.
  - Demonstrate how to build a circuit, add gates, and measure.
  - Include examples of submitting circuits via both `BackendV2.run()` (native) and `QrBackendV2.run()` (Qiskit integration).
  - Illustrate job monitoring with `job_monitor` and manual polling using `JobV1` methods.

> **LLM Instruction:**  
> Provide clear, step-by-step examples in generated responses that reflect these best practices, ensuring that users understand the distinctions and integration points.

---

## 5. Conclusion

This extended API document covers both the Quantum Rings native SDK and its Qiskit integration modules. The categorization into integration and native sections, along with detailed summaries and usage instructions, is designed to help an LLM generate accurate, context-aware examples and answers about constructing and running quantum circuits using Quantum Rings. Use this guide as a foundation for training the LLM to understand the complete API landscape.

---

# End of Document
