# src/visualize.py
import csv
import os
import matplotlib.pyplot as plt
from collections import defaultdict

def generate_line_plot(csv_filename="data/simulation_results.csv", output_filename="data/population_decay.png"):
    """
    Reads the simulation CSV data, groups data by run_id, 
    and plots all runs together to compare the population decay.
    """
    if not os.path.exists(csv_filename):
        print(f"Error: {csv_filename} not found. Run the simulation first!")
        return

    # 1. Structure to organize data by Run ID: { run_id: { 'rounds': [], 'players': [] } }
    runs_data = defaultdict(lambda: {'rounds': [], 'players': []})
    
    with open(csv_filename, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            run_id = row['run_id']
            runs_data[run_id]['rounds'].append(int(row['round']))
            runs_data[run_id]['players'].append(int(row['players_remaining']))

    if not runs_data:
        print("The data file is empty!")
        return

    # 2. Create the multi-line plot
    plt.figure(figsize=(11, 6))
    
    # Loop through each run and plot its individual line
    for run_id, data in runs_data.items():
        plt.plot(
            data['rounds'], 
            data['players'], 
            marker='o', 
            linewidth=1.8, 
            markersize=4, 
            label=f"Run #{run_id}"
        )
    
    # Add title and labels
    plt.title("Coin Toss Simulation Comparison - Population Decay", fontsize=14, fontweight='bold')
    plt.xlabel("Round Number", fontsize=12)
    plt.ylabel("Number of Players Remaining", fontsize=12)
    
    # Add a clean grid style
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Place a legend on the side so it doesn't cover up the data lines
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    
    # Adjust layout so the legend fits cleanly inside the saved image file
    plt.tight_layout()
    
    # 3. Save the final visualization image
    plt.savefig(output_filename, dpi=300)
    plt.close()
    
    print(f"📊 Updated visualization with {len(runs_data)} run(s) saved to {output_filename}!")