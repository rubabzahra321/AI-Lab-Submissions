fruits = [("Apple",150) , ("banana",80),("avacado",200),("mango",500),("grapes",450),("watermelon",390)]

print("-----------------------")
for fruit in fruits:
    print(fruit[0] ,":",fruit[1])
    print("Price: " , fruit[1])

print("-----------------------")

new_fruits_name_list = [fruit[0] for fruit in fruits ]
print("Fruits List: " , new_fruits_name_list)

print("-----------------------")

new_fruits_price_list = [sum(fruit[1] for fruit in fruits) ]
print("Fruit Price: " , new_fruits_price_list)

print("-----------------------")

fruits = [("Papaya",150) , ("Melon",80),("avacado",200),("mango",500),("grapes",450),("watermelon",390)]

print("-----------------------")

for fruit in fruits:
    print("Name: " , fruit[0])
    print("Price: " , fruit[1])

print("-----------------------")