class student:
    def __init__(self,name,age,major):
        self.name=name
        self.age =age 
        self.major=major
    def greet(self):
        print( f"Hello my name is {self.name} and Iam  {self.age} years old and major is {self.major}")  

s1=student("Ali",20,"cs")
s2=student("Bilal",22,"It")
#print(f"Hello my name is {s1.name} and Iam  {s1.age} years old and major is {s1.major}")        
#print(f"Hello my name is {s2.name} and Iam  {s2.age} years old and major is {s2.major}")        
s1.greet()
s2.greet()
#second code  
print("===============================")
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")        

    def show_balance(self):
        print(f"{self.owner}'s current balance is {self.balance}.")
acc1 = BankAccount("Ali", 100)

acc2 = BankAccount("Sara", 50)

acc1.deposit(50)
acc1.withdraw(100)
acc1.show_balance()

acc2.withdraw(100)  
acc2.show_balance(   )