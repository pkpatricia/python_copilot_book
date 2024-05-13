def rainfall_recorder():
    total_rainfall = 0
    max_rainfall = 0
    num_rainy_days = 0
    num_valid_days = 0
    
    while True:
        # Get rainfall input from user
        try:
            rainfall = float(input("Enter the amount of rainfall for the day (9999 to stop): "))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
            continue
        
        # Check for sentinel value to terminate
        if rainfall == 9999:
            break
        
        # Reject negative values as they are invalid
        if rainfall < 0:
            print("Negative rainfall amount is invalid. Please enter a positive value or zero.")
            continue
        
        # Update counters and totals
        num_valid_days += 1
        total_rainfall += rainfall
        
        # Check for rainy day
        if rainfall > 0:
            num_rainy_days += 1
        
        # Update maximum rainfall
        if rainfall > max_rainfall:
            max_rainfall = rainfall
    
    # Print results
    print("\n--- Rainfall Statistics ---")
    print(f"Number of valid recorded days: {num_valid_days}")
    print(f"Number of rainy days: {num_rainy_days}")
    print(f"Total rainfall over the period: {total_rainfall} units")
    print(f"Maximum rainfall on a single day: {max_rainfall} units")

# Run the rainfall recorder
rainfall_recorder()
