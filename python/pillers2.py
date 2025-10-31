# encapsulation ✅
# abstraction

class BankAccount:
    def __init__(self, account_holder, pin):
        self.__balance = 0 # private attribute
        self.account_holder = account_holder # public attribute
        self.__pin = pin # private attribute

    def deposit(self, amount): # public method // setter 
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount, pin): # public method // getter
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Incorrect PIN.")

    def get_balance(self, pin): # public method // getter
        if pin == self.__pin:
            return self.__balance
        else:
            return "Incorrect PIN."
        
meraAccount = BankAccount("Arman", 1234)
print(meraAccount.account_holder)  # Accessing public attribute
# print(meraAccount.__balance)  # Accessing public attribute
print(meraAccount.get_balance(1234))
meraAccount.deposit(500)
print(meraAccount.get_balance(1234))
meraAccount.withdraw(200, 1234)
print(meraAccount.get_balance(1234))