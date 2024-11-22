import numpy as np

# Матриця виграшів (прибутків)
payoff_matrix = np.array([
    [6.0, 3.5, 0.5],  # x1
    [6.5, 3.0, 2.5],  # x2
    [3.5, 3.5, 3.5]   # x3
])

# Критерій Вальда (максимізація мінімального виграшу)
wald_criterion = payoff_matrix.min(axis=1)
wald_strategy = np.argmax(wald_criterion) + 1

# Критерій Севіджа (мінімізація максимального ризику)
max_values = payoff_matrix.max(axis=0)
risk_matrix = max_values - payoff_matrix
savage_criterion = risk_matrix.max(axis=1)
savage_strategy = np.argmin(savage_criterion) + 1

# Критерій Гурвіца (зважений підхід, беремо коефіцієнт оптимізму α = 0.5)
alpha = 0.5
hurwicz_criterion = alpha * payoff_matrix.max(axis=1) + (1 - alpha) * payoff_matrix.min(axis=1)
hurwicz_strategy = np.argmax(hurwicz_criterion) + 1

print("Результати прийняття рішень:")
print(f"1. Критерій Вальда: обрати стратегію x{wald_strategy}")
print(f"2. Критерій Севіджа: обрати стратегію x{savage_strategy}")
print(f"3. Критерій Гурвіца: обрати стратегію x{hurwicz_strategy} (при α = 0.5)")