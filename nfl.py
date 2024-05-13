import csv

# Path to the CSV file
file_path = 'nfl_offensive_stats.csv'

# Open the CSV file
with open(file_path, mode='r', newline='') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Skip the header if necessary
    next(csv_reader)
    
    # Initialize a variable to store the total passing yards for Aaron Rodgers
    total_passing_yards = 0
    
    # Process each row in the CSV file
    for row in csv_reader:
        # Check if the player name in the fourth column (index 3) is 'Aaron Rodgers'
        if row[3] == 'Aaron Rodgers':
            # Add the passing yards from the eighth column (index 7) to the total
            # Ensure to convert the passing yards to an integer before adding
            total_passing_yards += int(row[7])
    
    # Print the total passing yards for Aaron Rodgers
    print(f"Total passing yards for Aaron Rodgers: {total_passing_yards}")
