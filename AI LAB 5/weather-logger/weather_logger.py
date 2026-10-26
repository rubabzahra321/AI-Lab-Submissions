def summarize(temps):
    return {
        "minimum": min(temps),
        "maximum": max(temps),
        "average": sum(temps) / len(temps)
    }


temps = []

while True:
    temp = input("Enter temperature ('done' to stop): ")

    if temp == "done":
        break

    temps.append(float(temp))

result = summarize(temps)
print(result)