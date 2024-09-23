import math

def U(x):
    return 2 * math.sqrt(x)

capital_A = 100 * (1 + 0.15)  
utility_A = U(capital_A)


capital_B_gain = 100 * (1 + 0.50)  
capital_B_no_gain = 100            

prob_gain = 0.4
prob_no_gain = 0.6

utility_B = prob_gain * U(capital_B_gain) + prob_no_gain * U(capital_B_no_gain)

if utility_A > utility_B:
    decision = "Опція A (фіксована прибутковість) краща."
else:
    decision = "Опція B (ризиковані інвестиції) краща."

print(f"Корисність для Опції A: {utility_A}")
print(f"Корисність для Опції B: {utility_B}")
print(decision)
