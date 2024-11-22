import numpy as np
from scipy.optimize import minimize

# Дано
expected_returns = np.array([0.6, 0.5, 0.4, 0.7])  # Очікувані доходності (в частках)
risks = np.array([0.4, 0.3, 0.25, 0.5])  # Ризики (стандартні відхилення)
correlations = np.array([
    [1.0, 0.2, -0.3, 0.9],
    [0.2, 1.0, -0.5, 0.7],
    [-0.3, -0.5, 1.0, -0.3],
    [0.9, 0.7, -0.3, 1.0]
])  # Матриця кореляцій

# Розрахунок коваріаційної матриці
cov_matrix = np.outer(risks, risks) * correlations

# Функція для обчислення ризику портфеля
def portfolio_risk(weights):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# Обмеження: сума ваг = 1
constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}

# Обмеження: ваги мають бути в межах [0, 1]
bounds = [(0, 1) for _ in range(len(expected_returns))]

# Початкові ваги
initial_weights = np.ones(len(expected_returns)) / len(expected_returns)

# Оптимізація
result = minimize(portfolio_risk, initial_weights, bounds=bounds, constraints=constraints)

# Результати
optimal_weights = result.x
portfolio_expected_return = np.dot(optimal_weights, expected_returns)
portfolio_min_risk = portfolio_risk(optimal_weights)

optimal_weights, portfolio_expected_return, portfolio_min_risk
print("Оптимальні ваги портфеля:")
for i, weight in enumerate(optimal_weights, start=1):
    print(f"A{i}: {weight:.2%}")

print(f"\nОчікувана доходність портфеля: {portfolio_expected_return:.2%}")
print(f"Мінімальний ризик портфеля: {portfolio_min_risk:.2%}")