#creating a list = we can mix may data types
list1 = [1,2,'three',4,5.5]
print(list1)

#accessing elments in list


print(list1[-1])

#modify,add,remove elements

list1[0] = 45

list1.insert(0,126)

# add at list end
list1.append("cute") 

# remove specific
list1.remove(126)

# remove last
list1.pop()


print(list1)

list2 = [10,30,20,1,2,4,567]
#for aseding simple sort
# for decending order
list2.sort(reverse = True)

list2.reverse()

print(len(list2))

#for loop

for num in list2:
    print(num)

#range function = when we want index wise iteration

for i in range(5):
    print (i)

for i in range(1,6,3):
    print(i)
print(list2)

#slicing

print(list2[:3])  #three not included
print(list2[0:])  #0 included
print(list2[2:5])
print(list2[::]) # as it is full list