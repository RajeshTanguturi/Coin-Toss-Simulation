# src/simulator.py
import random

def run_simulation(n: int):
    """
    Simulates a coin toss elimination tournament.
    Starts with 'n' players, loops until exactly 1 player remains,
    and returns a history of the population size at each round.
    """
    # Create a list to track the population size at each stage
    history = [n]
    
    while True:
        # Flip a coin for every remaining player all at once
        results = random.choices(['Heads', 'Tails'], k=n)
        
        # Count how many players advanced
        head_count = results.count('Heads')
        
        # Edge Case: Everyone flipped Tails! 
        # We ignore this "dead round" and make them re-flip.
        if head_count == 0:
            continue
            
        # Success Condition: Exactly one person got Heads. We have our winner!
        if head_count == 1:
            history.append(1)
            break
            
        # General Case: More than 1 player advanced.
        # Update 'n' for the next round and record the progress.
        n = head_count
        history.append(n)
        
    return history