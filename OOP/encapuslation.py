class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance  #private variable
        
    def deposite(self , amount):
        self.__balance += amount
        print(f'Deposited{amount}.New balance{self.__balance}')
        
    def get_balance(self):
        return self.__balance#controlled access
    
account = BankAccount('122345',50000)

account.deposite(2000)
print(account.get_balance())
        