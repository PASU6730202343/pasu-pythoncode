# Complete this ATM simulation

balance = 1000
pin = "1234"
entered_pin = input("Enter PIN: ")

if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            print('Your balance:', balance)
        elif choice == '2':
                withdraw = float(input("How much do you want withdraw "))
                if withdraw <= 0:
                    print("Invalid amount.")
                elif withdraw > balance:
                    print("Insufficient balance.")
                else:
                    balance =balance-withdraw
                    print('Withdrawal successful. New balance:', balance)
        elif choice == '3':
                deposit = float(input("How much do you want to deposit "))
                if deposit <= 0:
                    print("Invalid amount.")
                else:
                    balance += deposit
                    print('Deposit successful. New balance:', balance)
        elif choice == '4':
            print("Thank you.")
            break
        else:
            print("Invalid option. Please choose 1-4")
else:
    print("Invalid PIN")
     
            

