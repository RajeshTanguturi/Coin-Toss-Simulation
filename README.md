# Coin Toss Elimination Simulator

A statistical Python simulation that models a geometric distribution tournament. Starting with a large population of players, every player flips a fair coin each round. Only those who flip **Heads** advance to the next round. The simulation dynamically narrows down the pool until exactly one final winner remains.

The project records execution data sequentially and generates high-resolution, multi-run comparison visualizations.

---

## Features

* **Dynamic Population Architecture:** Simulates massive coin flips efficiently using batch execution vectoring.
* **Smart Population Alignment (`utils.py`):** Automatically sanitizes user input into valid mathematical bounds using custom power-of-2 rounding constraints:
  * Absolute nearest power of 2.
  * Largest nearest power of 2 (ceiling).
  * Smallest nearest power of 2 (floor).
* **Persistent CSV Storage:** Automatically tracks and appends data records across unique sequential execution runs.
* **Multi-Run Visualization:** Reads historical datasets to overlay multiple simulation runs on a single chart to highlight statistical variance.

---

## Project Structure

```text
coin_toss_game/
│
├── data/
│   ├── simulation_results.csv   # Raw numerical historical data
│   └── population_decay.png     # Saved visualization plot
│
├── src/
│   ├── __init__.py              # Package initializer
│   ├── simulator.py             # Core game-loop & edge-case logic
│   ├── storage.py               # CSV creation & data appending
│   ├── utils.py                 # Bitwise / Math rounding helpers
│   └── visualize.py             # Matplotlib multi-line graph engine
│
├── main.py                      # Application entry point
└── requirements.txt             # Third-party dependencies
```
<img width="3300" height="1800" alt="image" src="https://github.com/user-attachments/assets/f524c5fb-adc6-46d4-90ab-13c0f9b65ce3" />
