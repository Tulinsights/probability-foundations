# probability-foundations
Exploring probability concepts using Python: Law of Large Numbers, Bayes' Theorem, and Simulations

The Goal
I am investigating how empirical probability approaches theoretical probability as the number of trials increases.

Key Concepts
Theoretical Probability: For a fair coin, P(H) = 0.5.
Law of Large Numbers: As n --> infinity , the sample mean will converge to the theoretical mean.




# Monty Hall Simulation
This script simulates the famous Monty Hall problem. It demonstrates that the probability of winning is significantly higher (66.6%) if the contestant chooses to switch doors after a goat is revealed, compared to staying with their initial choice (33.3%).

### The Mathematical Proof
Using Bayes' Theorem, we calculate the probability of winning by switching ($C_2$) given that Monty opened Door 3 ($M_3$):

$$P(C_2|M_3) = \frac{P(M_3|C_2)P(C_2)}{P(M_3)} = \frac{1 \cdot \frac{1}{3}}{\frac{1}{2}} = \frac{2}{3}$$

This confirms our simulation results!
