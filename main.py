import getpass

users = [
    {"username": "Rhoda", "pin": "1234", "balance": {"KSh": 73000, "USD": 550}},
    {"username": "Joan", "pin": "4321", "balance": {"KSh": 52005, "USD": 490}},
    {"username": "Francis", "pin": "9876", "balance": {"KSh": 120387, "USD": 1000}},
    {"username": "Oliver", "pin": "6789", "balance": {"KSh": 300456, "USD": 1700}},
]


def main():
    logged_in = False
    attempts = 0
    another_transaction = True

    while logged_in == False and attempts < 3:
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        for user in users:
            if username == user["username"] and password == user["pin"]:
                print("Welcome to Convenience ATM Machine. How can we help you?")
                logged_in = True
                break
        else:

            if attempts < 2:

                attempts = attempts + 1
                print("Incorrect username/password. Try again.")

            else:
                attempts = attempts + 1
                print("Incorrect username/password. Blocked!")

    if logged_in:
        print("a. Check balance\nb. Withdraw")

        service = input("Enter a/b: ")
        if service == "a":
            print("Kenya Shillings: ", user["balance"]["KSh"])
        elif service == "b":
            initial_balance = user["balance"]["KSh"]
            amount = int(input("Enter amount to withdraw: "))

            if amount > initial_balance:
                print("Insufficient funds. Balance: Kes", initial_balance)
            else:
                current_balance = initial_balance - amount
                print("Successful!\nBalance: Kes", current_balance)
                while another_transaction == True:
                    print("a. Another transaction\nb. Receipt")
                    option = input("Enter a/b: ")

                    final_balance = current_balance

                    if option == "a":
                        another_amount = int(input("Enter amount to withdraw: "))
                        if another_amount > current_balance:
                            print("Insufficient funds. Balance: Kes", current_balance)
                        else:
                            final_balance = current_balance - another_amount
                            print("Successful!\nBalance: Kes", final_balance)

                    elif option == "b":
                        another_transaction = False
                        print(
                            "*****RECEIPT*****\nName: "
                            + user["username"]
                            + "\nBalance: "
                            + str(final_balance)
                            + "\n*****Thank you for banking with us*****",
                        )
                    else:
                        print("Invalid input")

        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
