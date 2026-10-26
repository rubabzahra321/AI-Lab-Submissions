shopping_list = [
    {"item": "Notebook", "price": 150, "purchased": True},
    {"item": "Pen", "price": 30, "purchased": True},
    {"item": "USB Drive", "price": 900, "purchased": False}
]


items_to_buy = [item["item"] for item in shopping_list if item["purchased"] == False]


remaining_cost = sum(
    [item["price"] for item in shopping_list if item["purchased"] == False]
)

print("Still need to buy:", items_to_buy)
print("Remaining cost:", remaining_cost)