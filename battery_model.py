def simulate_battery(energy_balance, battery_capacity):
    """
    Simulates battery behavior.

    energy_balance:
        positive  → surplus energy
        negative  → deficit

    battery_capacity:
        max battery storage (kWh)
    """

    if energy_balance > 0:
        # Store surplus energy
        stored_energy = min(energy_balance, battery_capacity)
        remaining_surplus = energy_balance - stored_energy

        return stored_energy, 0, 0, remaining_surplus

    elif energy_balance < 0:
        # Use battery during deficit
        deficit = abs(energy_balance)
        used_energy = min(deficit, battery_capacity)
        remaining_deficit = deficit - used_energy

        return 0, used_energy, remaining_deficit, 0

    else:
        return 0, 0, 0, 0