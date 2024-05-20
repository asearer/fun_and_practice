# cicada_emergence_calculator.py

def calculate_next_emergence(last_emergence_year, period):
    """
    Calculate the next emergence year for cicadas based on the last emergence year and the period.
    
    Args:
    last_emergence_year (int): The year when cicadas last emerged.
    period (int): The emergence period in years (typically 13 or 17).
    
    Returns:
    int: The next emergence year.
    
    Raises:
    ValueError: If the period is not 13 or 17 years.
    """
    if period not in [13, 17]:
        raise ValueError("Period must be 13 or 17 years.")
    
    next_emergence_year = last_emergence_year + period
    return next_emergence_year

def main():
    print("Cicada Emergence Calculator")
    
    try:
        last_emergence_year = int(input("Enter the last known emergence year: "))
        period = int(input("Enter the emergence period (13 or 17 years): "))
        
        if period not in [13, 17]:
            raise ValueError("Period must be 13 or 17 years.")
        
        next_emergence_year = calculate_next_emergence(last_emergence_year, period)
        print(f"The next cicada emergence year will be: {next_emergence_year}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
