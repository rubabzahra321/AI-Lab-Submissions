Personal_detail = {

    "name": "Rubab",
    "Phone": "03104314276",
    "city": "Kamra"
}


print(f"""
Name: {Personal_detail["name"]}
Phone: {Personal_detail["Phone"]}
City: {Personal_detail["city"]}  
    """)

Personal_detail["Email"] = "rubabzahra@gmail.com"

Personal_detail["city"] = "Islamabad"

Phone_number = Personal_detail.pop("Phone")

print("Phone removed was: " , Phone_number)

print(Personal_detail.get("company","Freelancer"))

for key, value in Personal_detail.items():
 print(key, "->", value)