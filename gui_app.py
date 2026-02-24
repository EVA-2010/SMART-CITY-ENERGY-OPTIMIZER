import tkinter as tk
from tkinter import messagebox

from energy_model import calculate_demand, calculate_solar_production
from battery_model import simulate_battery


def run_simulation():
    try:
        population = float(population_entry.get())
        industries = float(industries_entry.get())
        solar_area = float(solar_entry.get())
        battery_capacity = float(battery_entry.get())

        demand = calculate_demand(population, industries)
        solar_production = calculate_solar_production(solar_area)
        energy_balance = solar_production - demand

        stored, used, remaining_deficit, remaining_surplus = simulate_battery(
            energy_balance, battery_capacity
        )

        result_text.set(
            f"ENERGY REPORT\n"
            f"--------------------------\n"
            f"Total Demand: {demand:.2f} kWh\n"
            f"Solar Production: {solar_production:.2f} kWh\n\n"
            f"BATTERY REPORT\n"
            f"Energy Stored: {stored:.2f} kWh\n"
            f"Energy Used: {used:.2f} kWh\n"
            f"Remaining Deficit: {remaining_deficit:.2f} kWh\n"
            f"Remaining Surplus: {remaining_surplus:.2f} kWh\n\n"
            f"RECOMMENDATION\n"
        )

        if remaining_deficit > 0:
            result_text.set(
                result_text.get()
                + f"Increase solar area by at least {remaining_deficit:.2f} m²."
            )
        elif remaining_surplus > 0:
            result_text.set(
                result_text.get()
                + "System produces excess energy. Consider exporting to grid."
            )
        else:
            result_text.set(
                result_text.get()
                + "System is perfectly balanced."
            )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


# Window setup
root = tk.Tk()
root.title("Smart City Energy Optimizer")
root.geometry("600x550")
root.configure(bg="#f4f6f9")

title = tk.Label(
    root,
    text="SMART CITY ENERGY OPTIMIZER",
    font=("Helvetica", 18, "bold"),
    bg="#f4f6f9",
    fg="#1f2937"
)
title.pack(pady=20)

frame = tk.Frame(root, bg="#f4f6f9")
frame.pack(pady=10)

def create_input(label_text):
    label = tk.Label(frame, text=label_text, font=("Helvetica", 12), bg="#f4f6f9")
    label.pack()
    entry = tk.Entry(frame, font=("Helvetica", 12), width=25)
    entry.pack(pady=5)
    return entry

population_entry = create_input("City Population")
industries_entry = create_input("Number of Industrial Units")
solar_entry = create_input("Total Solar Panel Area (m²)")
battery_entry = create_input("Battery Capacity (kWh)")

run_button = tk.Button(
    root,
    text="Run Simulation",
    font=("Helvetica", 12, "bold"),
    bg="#2563eb",
    fg="white",
    padx=10,
    pady=5,
    command=run_simulation
)
run_button.pack(pady=20)

result_text = tk.StringVar()
result_label = tk.Label(
    root,
    textvariable=result_text,
    font=("Courier", 11),
    bg="white",
    width=60,
    height=15,
    anchor="nw",
    justify="left",
    relief="solid",
    padx=10,
    pady=10
)
result_label.pack(pady=10)

root.mainloop()