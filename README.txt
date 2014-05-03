Heuristic for dividing a horse race into n lots consisting of at least one horse such that the difference in probability of winning between all lots is minimized.

Methodology:

Given a list of horses and their odds (e.g. 8-1), first compute the probability implied by the odds for each horse. Rank the horses from highest implied probability to lowest.

Seed the solution space of n lots by adding the next available horse with the highest implied probability to the lot with lowest implied expectation of winning (the implied expectation of winning of a lot is found by summing the implied probability of the horses in that lot).

Compute the variance of expectation of winning between the lots.

For a set number of iterations, say 10000, randomly select two lots and randomly swap two horses. Recompute the variance. If the variance is lower, use these new lots. If not, use the lots with the lowest variance computed thus far.

To run:

generate_lots.py horses.txt