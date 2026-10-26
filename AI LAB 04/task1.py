atm_pin = ""

while atm_pin != "4521":
    atm_pin = input("Enter the pin for the ATM (Type cancle to end transaction!) : ")

    if atm_pin == "4521":

        print("PIN: " , atm_pin)

        print("Access Granted!")

    elif atm_pin == "cancle":

        print("Transaction Cancelled")

        break

    elif atm_pin != "4521":

        print("PIN: " , atm_pin)
        
        print("Incorrect PIN, try again.")

