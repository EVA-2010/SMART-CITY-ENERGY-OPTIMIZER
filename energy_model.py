def calculate_demand(population, industries):
    """
    Calculates total daily energy demand (kWh)
    """

    household_demand = population * 2
    industrial_demand = industries * 1500

    return household_demand + industrial_demand


def calculate_solar_production(solar_area):
    """
    Calculates daily solar energy production (kWh)
    """

    solar_efficiency = 1
    return solar_area * solar_efficiency