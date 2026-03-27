class BankAccount:

    def __init__(account_holder, balance, amount, amount2):
        account_holder.account_holder = account_holder
        account_holder.balance = balance
        account_holder.amount = amount
        account_holder.amount2 = amount2
        

    def deposit(account_holder, amount, balance):
        amount = input("How much money would you like to deposit?")
        balance + amount == balance
    
    def withdraw(account_holder, amount2, balance):
        amount2 = input("How much money would you like to withdraw?")
        account_holder.balance - amount2 == balance
        if account_holder.balance < amount2:
            print("Insufficient Funds!")

    def check_balance(balance):
        print("You have $" + balance + " in your account")
        
John = BankAccount("John", "$1000", 300)
John.check_balance()

print(John.withdraw())
John.withdraw(1500)
John.check_balance()

Steve = BankAccount("Steve", "$2500")
Steve.check_balance()
Steve.deposit(500)
Steve.check_balance



        