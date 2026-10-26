
name = input("ENTER YOUR NAME: ")
reg = input("ENTER YOUR REG-ID: ")
subject = input("ENTER SUBJECT NAME: ")
obtain_marks = int(input("ENTER OBTAIN MARKS: "))
total_marks = int(input("ENTER TOTAL MARKS: "))

percentage = (obtain_marks / total_marks ) * 100

print(f"""

NAME : {name}
REG-ID: {reg}
SUBJECT: {subject}
PERCENTAGE: {percentage} %
OBTAIN MARKS: {obtain_marks}
TOTAL MARKS: {total_marks}
""")