def calculate_board_feet(length_ft, width_in, thickness_in, quantity=1):
    """
    Calculate board feet.
    Formula: (Thickness (in) x Width (in) x Length (ft)) / 12
    """
    try:
        bf = (float(thickness_in) * float(width_in) * float(length_ft)) / 12
        return round(bf * int(quantity), 2)
    except (ValueError, TypeError):
        return 0
