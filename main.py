from energy_model import calculate_demand, calculate_solar_production
from battery_model import simulate_battery

print("=== SMART CITY ENERGY SIMULATOR ===\n")

# User Inputs
population = float(input("Enter city population: "))
industries = float(input("Enter number of industrial units: "))
solar_area = float(input("Enter total solar panel area (m^2): "))
battery_capacity = float(input("Enter battery capacity (kWh): "))

# Energy Calculations
demand = calculate_demand(population, industries)
solar_production = calculate_solar_production(solar_area)

energy_balance = solar_production - demand

# Battery Simulation
stored, used, remaining_deficit, remaining_surplus = simulate_battery(
    energy_balance, battery_capacity
)

# Report
print("\n--- ENERGY REPORT ---")
print(f"Total Daily Energy Demand: {demand:.2f} kWh")
print(f"Total Daily Solar Production: {solar_production:.2f} kWh")

if energy_balance >= 0:
    print(f"Initial Energy Surplus: {energy_balance:.2f} kWh")
else:
    print(f"Initial Energy Deficit: {abs(energy_balance):.2f} kWh")

print("\n--- BATTERY REPORT ---")
print(f"Energy Stored in Battery: {stored:.2f} kWh")
print(f"Energy Used from Battery: {used:.2f} kWh")
print(f"Remaining Deficit After Battery: {remaining_deficit:.2f} kWh")
print(f"Remaining Surplus After Battery: {remaining_surplus:.2f} kWh")

print("\nSimulation Complete.")
# Recommendation System
if remaining_deficit > 0:
    additional_solar_needed = remaining_deficit  # since 1 m² = 1 kWh

    print("\n--- SYSTEM RECOMMENDATION ---")
    print(f"To eliminate the remaining deficit, increase solar area by at least {additional_solar_needed:.2f} m².")

elif remaining_surplus > 0:
    print("\n--- SYSTEM RECOMMENDATION ---")
    print("System is producing excess energy.")
    print("Consider reducing solar area or exporting energy to the grid.")

else:
    print("\n--- SYSTEM RECOMMENDATION ---")
    print("System is perfectly balanced. No adjustments needed.")