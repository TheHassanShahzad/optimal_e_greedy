
# Epsilon-Greedy Algorithm Optimization

This project implements a simulation of the epsilon-greedy algorithm to solve the multi-armed bandit problem. It aims to find the optimal value of epsilon (\( \epsilon \)) that minimizes regret in the exploration-exploitation tradeoff.

## Overview

The epsilon-greedy algorithm balances exploration (randomly selecting arms to discover new information) and exploitation (choosing the arm with the highest average reward so far). This project explores how the value of \( \epsilon \) affects the performance of the algorithm and uses polynomial fitting to find the optimal \( \epsilon \) value.

### Features

- Simulates multi-armed bandit machines with random rewards.
- Implements an epsilon-greedy player to balance exploration and exploitation.
- Computes and plots the mean regret for various values of \( \epsilon \).
- Fits a polynomial to the data to identify the optimal \( \epsilon \).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/TheHassanShahzad/epsilon-greedy-optimization.git
   cd epsilon-greedy-optimization
   ```

2. Install required dependencies:
   ```bash
   pip install matplotlib numpy
   ```

## How It Works

1. **Bandit Class**: Represents a slot machine with a randomly initialized reward mean and variance.
2. **Player Class**: Keeps track of the scores and the number of times each bandit is played.
3. **Simulation**:
   - The player explores with probability \( \epsilon \) or exploits the best-known bandit based on the highest average reward.
   - Regret (the difference between the best possible reward and the obtained reward) is calculated for each round.
4. **Polynomial Fit**: A polynomial is fitted to the mean regret data to identify the optimal \( \epsilon \).

## Usage

### Running the Simulation

The main script generates a range of \( \epsilon \) values, computes the mean regret for each, and plots the results along with a polynomial fit:

```python
# Simulation parameters
step_size = 0.005
e_values = np.arange(0.05, 0.3, step_size)

# Run the simulation
e_regrets = []
for e in e_values:
    e_regrets.append(playN_games(10000, 5, e, 100, False))

# Polynomial fitting
degree = 3
coefficients = np.polyfit(e_values, e_regrets, degree)
print("Polynomial coefficients:", coefficients)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(e_values, e_regrets, 'o', label='Mean Regret (Data)', markersize=5)
plt.plot(e_fitted, regret_fitted, '-', label=f'Polynomial Fit (Degree {degree})', linewidth=2)
plt.title('Mean Regret vs. Epsilon (e)', fontsize=14)
plt.xlabel('Epsilon (e)', fontsize=12)
plt.ylabel('Mean Regret', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)
plt.show()
```

### Outputs

- **Mean Regret vs. Epsilon Plot**: Shows the relationship between \( \epsilon \) and mean regret.
- **Polynomial Fit**: A smooth curve that highlights the optimal \( \epsilon \).

## Results

The project computes the coefficients of the polynomial that best fits the mean regret data. The optimal \( \epsilon \) (minimizing regret) can be identified by solving for the minimum of the polynomial.

## Customization

- **Change Parameters**:
  - Number of bandits: `num_bandits`
  - Number of games: `num_games`
  - Number of plays per game: `N`
- **Polynomial Degree**: Adjust the degree of the polynomial fit for a smoother or more precise curve.

## License

This project is licensed under the MIT License.

## Contributions

Feel free to fork this repository and submit pull requests for improvements or bug fixes!