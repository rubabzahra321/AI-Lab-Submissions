current_users = ["rubab","ali","alishba","minahil","zaib"]
new_users = ["rubab","ali","khan","faraz","zaib"]

current_users_upper = []

for user in current_users:
    current_users_upper.append(user.upper())

for newuser in new_users:
    if newuser.upper() in current_users_upper:
        print("enter new user name")

    else:
        print("user name available")