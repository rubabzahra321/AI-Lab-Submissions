habits = [
    ("Drink water", True),
    ("Read 10 pages", False),
    ("Exercise", True),
    ("Sleep 8 hours", True),
    ("Study Python", True),
    ("Walk 20 minutes", True)
]

for habit, status in habits:
    if status:
        print(habit + ": Done")
    else:
        print(habit + ": Not done")


def habit_report(habits):
    completed = 0

    for habit, status in habits:
        if status:
            completed += 1

    return {
        "completed": completed,
        "total": len(habits)
    }


print(habit_report(habits))