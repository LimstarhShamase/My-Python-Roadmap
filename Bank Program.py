
username = ""
password = ""
balance = 1000.00

def register():
    global username, password 
    # Register a new user
    newUser = input("Enter your username: ")
    passw = input("Enter new password: ")
    passConfirm = input("Confirm password: ")
    if passw == passConfirm:
        username = newUser
        password = passw
        log = input("Sign up successful, proceed to login? Y/N: ")
        if log.upper() == "Y":
            return True
        else:
            print("Exiting program")
            exit()
    else:
        print("Passwords do not match, try again!")
        return False

def login():
    for _ in range(3):
        usernamer = input("Enter username to login: ")
        passwords = input("Enter password to login: ")
        if usernamer == username and passwords == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Try again.")
    print("Too many login attempts. Exiting program.")
    exit()

def deposit(balance):
    amount = float(input("Enter amount to deposit: $"))
    if amount > 0:
        balance += amount
        print("Deposit successful. Your new balance is:", balance)
    else:
        print("Invalid amount. Please enter a positive number.")
    return balance

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: $"))
    if amount > 0 and amount <= balance:
        balance -= amount
        print("Withdrawal successful. Your new balance is:", balance)
    else:
        print("Invalid amount. Please enter a positive number that is less than or equal to your balance.")
    return balance

if register():
    if login():
        while True:
            print("****Welcome to Shamase Bank Ltd****")
            print("How may we be of service to you today")
            print("Your balance:", balance)
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            options = int(input("Enter choice from 1-3: "))
            
            if options == 1:
                balance = deposit(balance) 
            elif options == 2:
                balance = withdraw(balance)  
            elif options == 3:
                print("Exiting program")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
