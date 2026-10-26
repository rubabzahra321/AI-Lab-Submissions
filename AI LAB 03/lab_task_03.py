library = [
{"title": "Introduction to AI", "author": "Stuart Russell",
"copies_available": 3, "rating": 4.8},
{"title": "Python Crash Course", "author": "Eric Matthes",
"copies_available": 0},
{"title": "Deep Learning", "author": "Ian Goodfellow",
"copies_available": 5, "rating": 4.6}
]

print("------book with title author----------")

for name in library:
    print("Title of the book: ",name["title"] )
    print("Author of the book: ",name["author"] )

print("----------------------------------------")


print("------book with specific count----------")

book_list = [book["title"] for book in library if book["copies_available"] >= 3]
print(book_list)

print("----------------------------------------")


print("------display rating----------")

for name in library:
    print("Title of the book: ",name.get("rating","Not Rated") )

print("----------------------------------------")


print("------update copies available count----------")
    

for name in library:
    if name["title"] == "Introduction to AI":
        name["copies_available"] -= 1
        print(name["title"], name["copies_available"], " copies available!")
    else:
        pass



print("------update library list----------")


for name in library:
    print(name)