students = ["rubab","rida","zuhaib","alishba","minahil","Laiba"]

print( "list of students: " , students)


print( "Postivive index Print first student: " , students[0])

print("Postivive index print last student: " ,students[5])

print("Negative index first student: " , students[-6])

print("Negative index last student: ", students[-1])

students.append("Samrana")

students.insert(2, "Rabeeca")

students.remove("zuhaib")

print("|----------Final list printed-------|")

print(students)

print("length of the list is: " , len(students))