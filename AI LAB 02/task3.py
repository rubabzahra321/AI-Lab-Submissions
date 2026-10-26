Attendance_list = [
    "Present", "Present", "Absent", "Present", "Absent",
    "Present", "Present", "Absent", "Present", "Present"
]

print ("|---Full attendance list displayed---|")

for i in Attendance_list:
    print(i)

print ("|------------------------------------|")

present_std = 0

absent_std = 0

for j in Attendance_list:

    if j == "Present":
        present_std += 1

    else:
        absent_std += 1

print("Total Present: " , present_std)

print("Total Absent: " , absent_std) 

print ("First Five Students: " , Attendance_list[:5])
print ("last Five Students: " , Attendance_list[5:])

Attendance_list.reverse()

print ("|---Reversed attendance list displayed---|")

print(Attendance_list)

print ("|----------------------------------------|")


print("Attendance Percentage: " , (present_std / len(Attendance_list))*100 , "%" )