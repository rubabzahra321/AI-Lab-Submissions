numbers_list = []

for i in range(1,16):
   numbers_list.append(i)

even_list = []

odd_list = []

for num in numbers_list:
    if num % 2 == 0:
        even_list.append(num)

    else:
        odd_list.append(num)

print("Numbers: " , numbers_list)

numbers_list.sort(reverse= True)

print("Even Number:" , even_list)
print("Odd Number: ", odd_list)
print("Descending Order: " , numbers_list)
print("Middle Five: ", numbers_list[5:10])