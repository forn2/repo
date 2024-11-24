salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_savings_needed = 0  # Начальная сумма подушки безопасности

for month in range(months):
    total_savings_needed += round(spend - salary)
    spend *= 1 + increase  # Увеличение трат на следующий месяц

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", total_savings_needed)

