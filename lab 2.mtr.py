
table = {
    "1 корпорація": {"success": 0.6, "profit_success": 8, "failure": 0.4, "profit_failure": -0.5},
    "2 корпорація": {"success": 0.7, "profit_success": 12, "failure": 0.3, "profit_failure": -0.5},
    "Створення асоціації": {"success": 0.3, "profit_success": 25, "failure": 0.7, "profit_failure": -1}
}

def calculate_expected_profit(table):
    success = table["success"]
    profit_success = table["profit_success"]
    failure = table["failure"]
    profit_failure = table["profit_failure"]
    
    expected_profit = (success * profit_success) + (failure * profit_failure)
    return expected_profit

results = {}
for table_name, table_data in table.items():
    expected_profit = calculate_expected_profit(table_data)
    results[table_name] = expected_profit

for table_name, expected_profit in results.items():
    print(f"{table_name}: Очікуваний прибуток = {expected_profit} млн. грн.")

best_table = max(results, key=results.get)
print(f"\nНайкращий варіант злиття: {best_table}")
