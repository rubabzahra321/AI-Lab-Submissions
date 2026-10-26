#example no 01

data = {
    "students": [
        {"name": "Ali"},
        {"name": "Sara"}
    ]
}

print(data["students"][1]["name"])

#example no 2

data = {
    "students": [
        {
            "subjects": [
                {"name": "AI"},
                {"name": "Python"}
            ]
        }
    ]
}

print(data["students"][0]["subjects"][1]["name"])

#example no 3

data = [
    {"name": "Ali"},
    {"name": "Sara"}
]

print(data[1]["name"])

#example no 4

data = {
    "students": [
        {"name": "Ali", "age": 20},
        {"name": "Sara", "age": 21}
    ]
}

print(data["students"][1]["age"])

#example no 5

data = {
    "subjects": {
        "CS": ["Python", "Java", "C++"],
        "AI": ["ML", "Deep Learning"]
    }
}

print(data["subjects"]["AI"][1])

#example no 5

data = {
    "school": {
        "students": [
            {"name": "Ali", "subjects": ["Math", "AI"]},
            {"name": "Sara", "subjects": ["English", "Python"]}
        ]
    }
}

print(data["school"]["students"][1]["subjects"][1])

#example no 6

data = [
    {
        "student": {
            "name": "Ali",
            "skills": ["Python", "Java", "React"]
        }
    }
]

print(data[0]["student"]["skills"][2])

# example no 7

data = {
    "classes": [
        {
            "students": [
                {"name": "Ali", "marks": [70, 80]},
                {"name": "Sara", "marks": [85, 95]}
            ]
        }
    ]
}

print(data["classes"][0]["students"][1]["marks"][1])

# example no 8

data = {
    "company": {
        "departments": [
            {
                "name": "IT",
                "employees": [
                    {"name": "Ali", "skills": ["Python", "SQL"]},
                    {"name": "Sara", "skills": ["Java", "React"]}
                ]
            }
        ]
    }
}

print(data["company"]["departments"][0]["employees"][1]["skills"][1])

# exmple no 9

data = {
    "university": [
        {
            "department": {
                "students": [
                    {"name": "Ali", "courses": ["AI", "DB"]},
                    {"name": "Sara", "courses": ["Web", "Python"]}
                ]
            }
        }
    ]
}

print(data["university"][0]["department"]["students"][1]["courses"][1])