numbers = int(input("enter five digit number: "))

if numbers <= 0:
    print("Enter the number again!")

number_list = list(str(numbers))

number_list.reverse()

for i in number_list:
    print(i)