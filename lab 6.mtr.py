import numpy as np

# Матриця прибутків (F+)
profits = np.array([
    [40, 30, 15],
    [65, 25, 30],
    [30, 70, 30],
    [35, 60, 50],
    [40, 80, 15],
    [80, 50, 45]
])

# Вагові коефіцієнти пропорційні складу груп (1/2, 1/3, 1/6)
weights = np.array([1/2, 1/3, 1/6])

# Ймовірності для першої групи експертів
P1 = np.array([0.3, 0.4, 0.3])

# Обчислюємо очікуваний прибуток для кожного варіанту рішення за кожною групою експертів
# Група 1: відомі ймовірності
expected_profits_P1 = profits @ P1

# Група 2: умови нерівності (P2 >= P1 + P3, P3 >= P2, де P2 = P1 + P3)
# Відсутність точної ймовірності потребує компромісу (середнє значення)
P2 = np.array([0.4, 0.4, 0.2])  # (наприклад, збалансоване припущення)

expected_profits_P2 = profits @ P2

# Група 3: рівномірний розподіл через невизначеність (всі ймовірності рівні)
P3 = np.array([1/3, 1/3, 1/3])

expected_profits_P3 = profits @ P3

# Загальний компромісний прибуток з урахуванням вагових коефіцієнтів
total_expected_profits = (weights[0] * expected_profits_P1 +
                          weights[1] * expected_profits_P2 +
                          weights[2] * expected_profits_P3)

# Знаходимо оптимальне рішення (максимальний прибуток)
optimal_decision_index = np.argmax(total_expected_profits) + 1
optimal_profit = total_expected_profits[optimal_decision_index - 1]

# Вивід результатів
print(f"Оптимальне рішення: {optimal_decision_index}")
print(f"Максимальний очікуваний прибуток: {optimal_profit:.2f} тис. у.о.")
