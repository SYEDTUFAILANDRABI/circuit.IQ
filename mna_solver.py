import numpy as np

def solve_circuit(components):
    nodes = set()
    voltage_sources = []
    resistors = []
    
    for comp in components:
        if comp[0] == 'R':
            _, n1, n2, val = comp
            nodes.add(n1)
            nodes.add(n2)
            resistors.append((n1, n2, val))
        elif comp[0] == 'V':
            _, n1, n2, val = comp
            nodes.add(n1)
            nodes.add(n2)
            voltage_sources.append((n1, n2, val))
    
    nodes.discard(0)
    nodes = sorted(nodes)
    n = len(nodes)
    m = len(voltage_sources)
    size = n + m
    
    A = np.zeros((size, size))
    b = np.zeros(size)
    
    node_index = {node: i for i, node in enumerate(nodes)}
    
    for n1, n2, r in resistors:
        g = 1.0 / r
        if n1 != 0:
            A[node_index[n1]][node_index[n1]] += g
        if n2 != 0:
            A[node_index[n2]][node_index[n2]] += g
        if n1 != 0 and n2 != 0:
            A[node_index[n1]][node_index[n2]] -= g
            A[node_index[n2]][node_index[n1]] -= g
    
    for i, (n1, n2, val) in enumerate(voltage_sources):
        vi = n + i
        if n1 != 0:
            A[node_index[n1]][vi] += 1
            A[vi][node_index[n1]] += 1
        if n2 != 0:
            A[node_index[n2]][vi] -= 1
            A[vi][node_index[n2]] -= 1
        b[vi] = val
    
    x = np.linalg.solve(A, b)
    
    node_voltages = {node: x[node_index[node]] for node in nodes}
    source_currents = {f"V{i+1}": x[n+i] for i in range(m)}
    
    return node_voltages, source_currents


def verify_kvl(loop_voltages):
    total = sum(loop_voltages)
    passes = abs(total) < 0.0001
    explanation = "Voltages around the loop sum to zero ✅" if passes else f"KVL failed — sum is {total:.4f}V ❌"
    return {"sum": total, "passes": passes, "explanation": explanation}


def verify_kcl(currents_in, currents_out):
    total_in = sum(currents_in)
    total_out = sum(currents_out)
    diff = abs(total_in - total_out)
    passes = diff < 0.0001
    explanation = "Currents at node balance ✅" if passes else f"KCL failed — difference is {diff:.4f}A ❌"
    return {"sum_in": total_in, "sum_out": total_out, "passes": passes, "explanation": explanation}


def calculate_power(voltage, current):
    power = voltage * current
    return {"watts": power, "milliwatts": power * 1000}