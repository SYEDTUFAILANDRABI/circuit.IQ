import numpy as np
import matplotlib.pyplot as plt

def ohms_law_simulation(resistance, max_current_mA=100):
    current_mA = np.linspace(0, max_current_mA, 100)
    current_A = current_mA / 1000
    voltage = current_A * resistance
    
    print(f"Ohm's Law Simulation — R = {resistance}Ω")
    print(f"{'Current (mA)':<15} {'Voltage (V)':<15}")
    print("-" * 30)
    for i in [0, 25, 50, 75, 100]:
        v = (i/1000) * resistance
        print(f"{i:<15} {v:<15.2f}")
    
    plt.figure(figsize=(8, 5))
    plt.plot(current_mA, voltage, color='#06B6D4', linewidth=2.5)
    plt.title(f"Ohm's Law — V vs I (R = {resistance}Ω)")
    plt.xlabel("Current (mA)")
    plt.ylabel("Voltage (V)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    return current_mA, voltage

ohms_law_simulation(100)