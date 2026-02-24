# Smart City Energy Optimizer

## Overview
The *Smart City Energy Optimizer* is a Python-based system that models and optimizes energy demand in urban areas.  
It integrates *population and industrial energy demand, **solar energy production, and **battery storage simulation* to provide actionable recommendations for a city’s energy planning.

This project includes a *Graphical User Interface (GUI)* for easy interaction and visualization of results.

---

## Features
- *Energy Demand Calculation*  
  Computes total energy demand based on city population and industrial units.

- *Solar Energy Simulation*  
  Calculates solar production based on available solar panel area.

- *Battery Storage Management*  
  Simulates battery usage to reduce energy deficits and store excess energy.

- *Deficit/Surplus Analysis*  
  Provides recommendations to increase solar capacity or utilize surplus efficiently.

- *GUI Interface*  
  Interactive interface built with Tkinter for inputting values and viewing results in real-time.

---

## Getting Started

### Prerequisites
- Python 3.10 or higher  
- Tkinter library (usually included with Python; if not, install via python -m pip install tk)  

### Running the GUI
1. Clone or download this repository  
2. Navigate to the project folder:  
```bash
cd smart-city-energy-optimizer

3. Run the GUI application:



python gui_app.py

4. Enter the following values in the GUI:

City Population

Number of Industrial Units

Solar Panel Area (m²)

Battery Capacity (kWh)



5. Click Run Simulation to see the results.



Optional: CLI Version

Run the command-line version of the project:

python main.py


---

Project Structure

smart-city-energy-optimizer/
├── gui_app.py          # Main GUI program
├── main.py             # Optional CLI version
├── energy_model.py     # Functions for energy and solar calculations
├── battery_model.py    # Battery simulation logic
├── README.md           # Project description
├── LICENSE             # MIT license
├── .gitignore          # Files ignored by Git


---

Technologies Used

Python 3.x

Tkinter for GUI

Git & GitHub for version control



---

Future Improvements

Include CO₂ emission calculations

Add cost and ROI optimization for solar + battery

Export simulation results to CSV or PDF

Web-based version with Flask or Django for online access



---

Author

Eva Likhi
GitHub Profile
