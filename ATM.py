def atm():
    balance = float(input("What is your current balance: "))

    while True:
        try:
            op = int(input("""\nSelect an option:
1. DEPOSIT
2. WITHDRAW
3. CHECK BALANCE
Your choice: """))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if op == 1:
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    balance += amount
                    print("Deposit successful. Current balance:", balance)
            except ValueError:
                print("Invalid input. Enter a valid number.")
        
        elif op == 2:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be positive.")
                elif amount % 10 != 0:
                    print("Please enter amount in multiples of 10.")
                elif amount > balance:
                    print("Insufficient balance.")
                else:
                    balance -= amount
                    print("Withdrawal successful. Current balance:", balance)
            except ValueError:
                print("Invalid input. Enter a valid number.")
        
        elif op == 3:
            print("Your current balance is:", balance)
        
        else:
            print("Invalid option selected.")

        again = input("\nDo you want to use ATM again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the ATM :)")
            break

atm()
