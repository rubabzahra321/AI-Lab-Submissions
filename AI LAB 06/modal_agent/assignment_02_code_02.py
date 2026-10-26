model = {"A": None, "B": None}


def update_model(location, status):
    model[location] = status


def vacuum_agent(location, status):
    update_model(location, status)

    if status == "Dirty":
        return "Suck"

    elif model["A"] == "Clean" and model["B"] == "Clean":
        return "NoOp - Stop"

    elif location == "A":
        return "Move Right"

    else:
        return "Move Left"


percept_sequence = [
    ("A", "Dirty"),
    ("A", "Clean"),
    ("B", "Dirty"),
    ("B", "Clean")
]

print("Location Status Action Model")

for location, status in percept_sequence:
    action = vacuum_agent(location, status)
    print(location,"\t", status, "\t", action, "\t", model)

    if action == "NoOp - Stop":
        break