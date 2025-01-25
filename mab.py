import numpy as np
import matplotlib.pyplot as plt

# Bandit class to simulate each slot machine
class Bandit():
    def __init__(self):
        self.mean = np.random.uniform(1, 10)  # Random mean reward
        self.var = 1  # Variance of the reward

    def play(self):
        return np.random.normal(self.mean, self.var)  # Generate a reward


# Player class to track scores and play counts
class Player():
    def __init__(self, num_bandits):
        self.num_bandits = num_bandits
        self.scores = [0] * num_bandits  # Total reward for each bandit
        self.play_counts = [0] * num_bandits  # Number of times each bandit was played


# Function to play a single game
def playGame(num_bandits, e, N, display):
    total_regret = 0
    bandits = [Bandit() for _ in range(num_bandits)]  # Initialize bandits
    best_bandit_score = max(b.mean for b in bandits)  # Best possible mean score
    player = Player(num_bandits)  # Initialize player

    for i in range(N):
        prob = np.random.uniform(0, 1)

        if prob <= e:
            # Exploration: randomly choose a bandit
            bandit_choice = np.random.randint(0, num_bandits)
        else:
            # Exploitation: choose the bandit with the highest average reward
            averages = [
                (player.scores[j] / player.play_counts[j]) if player.play_counts[j] > 0 else 0
                for j in range(num_bandits)
            ]
            bandit_choice = np.argmax(averages)

        # Play the chosen bandit
        result = bandits[bandit_choice].play()
        player.scores[bandit_choice] += result
        player.play_counts[bandit_choice] += 1

        # Calculate regret
        current_regret = best_bandit_score - result
        total_regret += current_regret

        # Display (optional)
        if display:
            print(f"Iteration {i + 1}")
            print("Current scores:", player.scores)
            print("Total regret:", total_regret)
            print("---")

    return total_regret


# Function to play multiple games and calculate mean regret
def playN_games(num_games, num_bandits, e, N, display):
    combined_game_regret = 0

    for game in range(num_games):
        total_regret = playGame(num_bandits, e, N, display)
        combined_game_regret += total_regret

    mean_regret = combined_game_regret / num_games
    print(f"Mean regret for epsilon {e:.4f}: {mean_regret}")

    return mean_regret


# Run the simulation
step_size = 0.005
e_values = np.arange(0.05, 0.3, step_size)
e_regrets = []

for e in e_values:
    e_regrets.append(playN_games(10000, 5, e, 100, False))  # 1000 games, 5 bandits, 1000 rounds per game

# Plotting the results
# plt.figure(figsize=(8, 6))
# plt.plot(e_values, e_regrets, marker='o', linestyle='-', label='Mean Regret')
# plt.title('Mean Regret vs. Epsilon (e)', fontsize=14)
# plt.xlabel('Epsilon (e)', fontsize=12)
# plt.ylabel('Mean Regret', fontsize=12)
# plt.grid(True, linestyle='--', alpha=0.6)
# plt.legend(fontsize=12)
# plt.show()

degree = 3  # You can try different degrees
coefficients = np.polyfit(e_values, e_regrets, degree)
print(coefficients)
polynomial = np.poly1d(coefficients)

# Generate values for the fitted polynomial
e_fitted = np.linspace(min(e_values), max(e_values), 500)
regret_fitted = polynomial(e_fitted)

# Plotting the results
plt.figure(figsize=(8, 6))
plt.plot(e_values, e_regrets, 'o', label='Mean Regret (Data)', markersize=5)  # Original data
plt.plot(e_fitted, regret_fitted, '-', label=f'Polynomial Fit (Degree {degree})', linewidth=2)  # Polynomial fit
plt.title('Mean Regret vs. Epsilon (e)', fontsize=14)
plt.xlabel('Epsilon (e)', fontsize=12)
plt.ylabel('Mean Regret', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.show()