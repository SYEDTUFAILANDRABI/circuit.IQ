import numpy as np

def solve_series_circuit(voltage, resistors):
    total_resistance = sum(resistors)
    current = voltage / total_resistance
    return current

def verify_kvl(voltage_source, resistors, current):
    drops = [current * r for r in resistors]
    total_drop = sum(drops)
    passes = abs(total_drop - voltage_source) < 0.0001
    return {
        "drops": drops,
        "total_drop": total_drop,
        "passes": passes
    }

def verify_kcl(currents_in, currents_out):
    total_in = sum(currents_in)
    total_out = sum(currents_out)
    passes = abs(total_in - total_out) < 0.0001
    return {
        "total_in": total_in,
        "total_out": total_out,
        "passes": passes
    }

def calculate_power(voltage, current):
    power = voltage * current
    return power