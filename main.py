# main.py
from src.simulator import run_simulation
from src.storage import save_to_csv
from src.utils import get_powers_2
from src.visualize import generate_line_plot

def main():
    print("Starting coin toss simulation...")
    user_input = int(input("Enter the starting population: "))
    lower, upper, nearest = get_powers_2(user_input)
    n = upper
    print(f"Population adjusted to largest nearest  power of 2: {n}")
    
    # 1. Run the simulation starting with 1024 players
    history_data = run_simulation(n)
    # 2. Save the results into the data folder
    save_to_csv(history_data)
    generate_line_plot()

if __name__ == "__main__":
    main()