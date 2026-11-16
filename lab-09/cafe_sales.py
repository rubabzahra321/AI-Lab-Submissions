
import numpy as np

units = np.array([
    [30, 20, 10],
    [25, 30, 15],
    [40, 25, 20],
    [35, 15, 25]
])

price = np.array([100, 150, 200])

revenue = units * price

daily_revenue = revenue.sum(axis=1)

print("Revenue per day:", daily_revenue)

item_sales = units.sum(axis=0)

print("Units sold per item:", item_sales)

best_day = daily_revenue.argmax()

print("Best day index:", best_day)

coffee_last_two = units[-2:, 1]

print("Coffee, last two days:", coffee_last_two)

print("Total weekly revenue:", daily_revenue.sum())