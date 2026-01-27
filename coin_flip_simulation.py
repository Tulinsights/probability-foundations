import random

def simulate_coin_flips(n):
    heads = 0
    for _ in range(n):
        if random.random() < 0.5:
            heads += 1
    return heads / n

trials = [10, 100, 1000, 10000, 100000]

print("Probability of Heads as sample size increases:")
for n in trials:
    probability = simulate_coin_flips(n)
    print(f"n={n:7}: {probability:.4f}")
