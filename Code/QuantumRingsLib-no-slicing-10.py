# Qiskit Test: ClassicalRegister Slicing vs Individual Indexing
try:
    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    print("\n=== QISKIT TEST ===")
    
    # Qiskit Classical Register
    c_qiskit = ClassicalRegister(4, "c_qiskit")

    # ✅ Works in Qiskit: ClassicalRegister allows slicing
    print("[Qiskit] c_qiskit[:2]:", c_qiskit[:2])  

    # ✅ Explicit indexing also works
    print("[Qiskit] c_qiskit[0]:", c_qiskit[0])  
    print("[Qiskit] c_qiskit[1]:", c_qiskit[1])  
    
except Exception as e:
    print("[Qiskit] ERROR:", e)

# Quantum Rings Test: ClassicalRegister Slicing vs Individual Indexing
try:
    import QuantumRingsLib
    from QuantumRingsLib import QuantumRegister, ClassicalRegister, QuantumCircuit

    print("\n=== QUANTUM RINGS TEST ===")
    
    # Quantum Rings Classical Register
    c_qr = ClassicalRegister(4, "c_qr")

    # ❌ Expected to FAIL in Quantum Rings: ClassicalRegister does not allow slicing
    try:
        print("[Quantum Rings] c_qr[:2]:", c_qr[:2])  
    except Exception as e:
        print("[Quantum Rings] ERROR (expected):", e)

    # ✅ Works in Quantum Rings: Explicit indexing
    print("[Quantum Rings] c_qr[0]:", c_qr[0])  
    print("[Quantum Rings] c_qr[1]:", c_qr[1])  

    # ✅ Test measurement with explicit indexing (no slicing)
    q = QuantumRegister(2, "q")
    qc = QuantumCircuit(q, c_qr)
    
    qc.measure(q[0], c_qr[0])  # ✅ Should work
    qc.measure(q[1], c_qr[1])  # ✅ Should work
    print("[Quantum Rings] Measurement assigned without slicing.")

except Exception as e:
    print("[Quantum Rings] ERROR:", e)
