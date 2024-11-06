'''
Encapsulation: 
1. Data Protection.
2. Code simplicity.
3. Data Hiding.
''' 

class BankAccount: 
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance
        print(f"Congrats! Your {self.account_number} Account is Created, And Balance have {self.__balance}TK")

    #! method to deposit balance: 
    def deposit(self, amount): 
        if amount > 0: 
            self.__balance += amount
            print(f"{amount}TK added to Account {self.account_number}")
        else: 
            ("Invalid deposit account")
    
    #! method to withdraw balance: 
    def withdraw(self, amount): 
        if 0 < amount <= self.__balance: 
            self.__balance -= amount
            print(f"{amount}TK withdraw from account {self.account_number}")

        else: 
            print("Insufficient Balance or invalid amount")
        
    #! method to get balance: 
    def get_balance(self): 
        return self.__balance

#! Creating an instance of Bank account: 
account_of_shakib = BankAccount("26676", 5000)

#! Using method to interact with private data: 
account_of_shakib.deposit(2000)
account_of_shakib.withdraw(1000)
print(f"Current Balance {account_of_shakib.get_balance()}TK")