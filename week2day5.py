class bankacount:
    def __init__ (self,):
        self.balance=0.0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("insufficient balance")
    def getbalance(self):
        print(f"Current balance: {self.balance}")
def main():
        
        account = bankacount()
        while True:
            
            change = input("Enter 'd' to deposit, 'w' to withdraw, 'b' to check balance, or 'q' to quit: ")
            if change == 'd':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif change == 'w':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif change == 'b':
                account.getbalance()
            elif change == 'q':
                print("Thank you for using the bank account system. Goodbye!")
                break
            else:
                print("Invalid input. Please try again.")
main()            