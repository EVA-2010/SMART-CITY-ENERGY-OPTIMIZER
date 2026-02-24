def calculate_solar_output(area, sunlight_hours, panel_efficiency):
    """
    Calculate daily solar energy production in kWh.
    
    area: total solar panel area in square meters
    sunlight_hours: average daily sunlight hours
    panel_efficiency: efficiency as decimal (e.g., 0.20 for 20%)
    """

    solar_irradiance = 1  # kW per square meter (average approximation)

    raw_energy = area * solar_irradiance * sunlight_hours
    actual_energy = raw_energy * panel_efficiency

    return actual_energy