import random

def monty_hall_trial(switch_door):
    # 1. Setup doors: 0 and 1 are goats, 2 is the car
    doors = [0, 1, 2]
    car_door = random.choice(doors)
    
    # 2. Contestant makes a choice
    my_pick = random.choice(doors)
    
    # 3. Monty opens a door that isn't the car and isn't the contestant's pick
    remaining_doors = [d for d in doors if d != my_pick and d != car_door]
    monty_opens = random.choice(remaining_doors)
    
    # 4. If we switch, our new pick is the door that isn't our original and isn't Monty's
    if switch_door:
        final_pick = [d for d in doors if d != my_pick and d != monty_opens][0]
    else:
        final_pick = my_pick
        
    return final_pick == car_door

# Run the simulation 10,000 times
n = 10000
switch_wins = sum(monty_hall_trial(True) for _ in range(n))
stay_wins = sum(monty_hall_trial(False) for _ in range(n))

print(f"Results after {n} trials:")
print(f"Win rate when switching: {switch_wins/n:.2%}")
print(f"Win rate when staying:   {stay_wins/n:.2%}")
