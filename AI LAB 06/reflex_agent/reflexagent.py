

percept_sequence = ["Dark", "Dim", "Bright", "Dark","Very Bright"]


def room_light_agent(percept):
    if percept == "Dark":
        return "Turn Light ON"
    elif percept == "Bright":
        return "Turn Light OFF"
    elif percept == "Dim":
        return "Leave Light As Is"
    elif percept == "Very Bright":
        return "Turn Light OFF and Close Curtains"
    else:
        return "Unknown brightness"


print("Percept\tAction")
for percept in percept_sequence:
    action = room_light_agent(percept)
    print(percept, "\t" ,action)
