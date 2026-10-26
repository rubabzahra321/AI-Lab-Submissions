sandwich_orders = ["chicken","beef","mutton","vegetables"]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich}  sandwich." )
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)