correct = ["A", "C", "B", "D", "A"]
users= []

user_input = ""
question_no = 1
while user_input != "quit":

    user_input = input(f"Question {question_no} answer (or 'quit' to stop): ")

    if user_input != "quit":
        question_no += 1
        users.append(user_input)
        if question_no == 6:
            break

def grade_quiz(user_answers, correct_answers):
    correct = 0
    attempted = 0

    for ans in user_answers:
        if ans in ["A", "B", "C", "D"]:
            attempted += 1

    for index in range(len(user_answers)):
        if user_answers[index] == correct_answers[index]:
            correct += 1

        percentage = correct / attempted * 100

    return {
        "Score": correct,
        "Attempted": attempted,
        "Percentage": percentage
    }


OUTPUT = grade_quiz(users, correct)

print("SCORE -> " , OUTPUT["Score"])
print("ATTEMPTED -> " , OUTPUT["Attempted"])
print("PERCENTAGE -> " , OUTPUT["Percentage"])