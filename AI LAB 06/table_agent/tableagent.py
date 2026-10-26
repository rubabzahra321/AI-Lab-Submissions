
percept_sequence = ["Red", "Green", "Yellow", "Red"]
percepts = []
table = {"Red": "Stop", "Yellow": "Slow Down", "Green": "Go","Flashing Red": "Stop and Proceed with Caution"}


def lookup_table(percept, table):
    return table.get(percept)


def table_driven_agent(percept):
    percepts.append(percept)
    return lookup_table(percept, table)


print("Percepts so far\t\t\tAction")
for current_percept in percept_sequence:
    action = table_driven_agent(current_percept)
    print(percepts, "\t\t", action)
