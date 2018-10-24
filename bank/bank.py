maxbalance = 100
maxbalanceaccount = -1
class bank:
    __accno = -1
    __balance = -1
    def __init__(self,accno,balance=100):
        self.__accno = accno
        self.__balance = balance
        print("Account created successfully")
    def withdraw(self,amt):
        if(self.__balance-amt < 100):
            print("withdraw unsuccessful")
        else:
            self.__balance -= amt
            print("withdraw suceessful")
    def deposit(self,amt):
        global maxbalance,maxbalanceaccount
        self.__balance += amt
        print("amount added successfully")
    def getBalance(self):
        return self.__balance

accounts = {}
flag = True
while(flag):
    option = int(input("""
    Enter any option
       1) New Account
       2) Withdraw from an account
       3) Deposit to an account
       4) Show details of maximum deposit
    :"""))
    if option is 1: 
        accno = int(input("Enter the account no of the new account : "))
        if accno in accounts:
            print("Account already exists")
        else: 
            accounts[accno] = bank(accno)
    elif option is 2:
        accno = int(input("Enter the account no of the account you want to withdraw from :"))
        if accno not in accounts:
            print("Account doesn't exist")
        else:
            accounts[accno].withdraw(int(input("Enter the amount you want to withdraw : ")))
    elif option is 3:
        accno = int(input("Enter the account no of the account you want to deposit money : "))
        if accno not in accounts:
            print("Account doesn't exist")
        else: 
            accounts[accno].deposit(int(input("Enter the amount you want to deposit : ")))
    elif option is 4:
        if len(accounts) is 0:
            print("No accounts exist")
        else:
            max = -1
            acc = -1
            for key, value in accounts.items():
                if value.getBalance() > max:
                    max = value.getBalance()
                    acc = key
            print("Accno : %d \nBalance : %d" % (acc,max))
    else:
        print("Invalid option")
        flag = False


