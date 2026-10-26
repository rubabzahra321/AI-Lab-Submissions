percept_sequence = [
    ("A", "Dirty"),
    ("A", "Clean"),
    ("B", "Dirty"),
    ("B", "Clean")
]


def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


print("Location\tStatus\tAction")

for location, status in percept_sequence:
    action = vacuum_agent(location, status)
    print(location, "\t\t", status, "\t", action)