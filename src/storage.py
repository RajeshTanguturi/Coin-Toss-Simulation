import csv
import os 

def save_to_csv(history: list[int] , filename="data/simulation_results.csv"):
    """
    Takes the history list from the simulator and saves it 
    as a structured CSV file for visualization.
    """

    # Ensure the 'data' directory exists before writing
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Check if the file already exists so we know if we need to write headers
    file_exists = os.path.isfile(filename)

    run_id = 1
    if file_exists:
        with open(filename, mode='r') as f:
            # plus one for header line
            run_id = len(f.readlines()) // 10 + 1
    with open(filename, mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # If it's a brand new file, write the column names first
        if not file_exists:
            writer.writerow(['run_id', 'round', 'players_remaining'])
        
        # Loop through your history list and write each round as a row
        for round_num, players in enumerate(history):
            writer.writerow([run_id, round_num, players])

    print(f"Successfully saved Run #{run_id} to {filename}!")