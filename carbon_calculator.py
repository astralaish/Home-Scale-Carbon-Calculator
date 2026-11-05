def calculate_annual_emissions(daily_distance, monthly_electricity, weekly_waste, daily_meals, factors):
    """Calculates annual carbon emissions and returns a dictionary of results."""
    
    # Check for negative inputs to satisfy your test's ValueError assertion
    if daily_distance < 0 or monthly_electricity < 0 or weekly_waste < 0 or daily_meals < 0:
        raise ValueError("Inputs cannot be negative.")
        
    # Check for missing factors to satisfy your test's ValueError assertion
    required_keys = {"Transport", "Electricity", "Waste", "Diet"}
    if not required_keys.issubset(factors.keys()):
        raise ValueError("Missing required emission factors in the dictionary.")
        
    # Annualize the inputs and multiply by the emission factors
    transport_kg = (daily_distance * 365) * factors["Transport"]
    electricity_kg = (monthly_electricity * 12) * factors["Electricity"]
    waste_kg = (weekly_waste * 52) * factors["Waste"]
    diet_kg = (daily_meals * 365) * factors["Diet"]
    
    # Convert to tonnes for the total
    total_tonnes = round((transport_kg + electricity_kg + waste_kg + diet_kg) / 1000, 2)
    
    return {
        "total_tonnes": total_tonnes,
        "category_kg": {
            "transport": transport_kg,
            "electricity": electricity_kg,
            "waste": waste_kg,
            "diet": diet_kg
        }
    }