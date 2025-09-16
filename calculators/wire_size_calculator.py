# wire_size_calculator.py
# Simple Wire Size Calculator (based on current and length)
# Reference: NEC Ampacity Tables
# Full interactive version: https://azadtechhub.com/wiring-size-calculator-a-comprehensive-guide/

def wire_size(current, length, voltage_drop=3, supply_voltage=230):
    """
    Estimate minimum wire size (in mm²) based on current and length.
    
    current: Load current in amperes
    length: One-way length of the conductor in meters
    voltage_drop: Allowed % voltage drop (default = 3%)
    supply_voltage: Supply voltage (default = 230V single-phase)
    """

    # Resistivity of copper (Ω·mm²/m)
    resistivity_copper = 0.0172  

    # Maximum allowable voltage drop
    max_vdrop = (voltage_drop / 100) * supply_voltage  

    # Total resistance allowed
    r_allowed = max_vdrop / current  

    # Required cross-sectional area (mm²)
    area = (resistivity_copper * (2 * length)) / r_allowed  

    return round(area, 2)


# Example usage
if __name__ == "__main__":
    current = 20   # amps
    length = 30    # meters
    size = wire_size(current, length)

    print(f"Required Wire Size ≈ {size} mm²")
    print("Note: Always verify with NEC tables for final selection.")

