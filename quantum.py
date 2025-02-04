from qiskit import QuantumCircuit

# set up a circuit with two qubits
entangled_circuit = QuantumCircuit(2)

# apply the H gate to the first qubit, then the CNOT gate with the first qubit as control
entangled_circuit.h(0)
entangled_circuit.cx(0, 1)
print(entangled_circuit.draw())
