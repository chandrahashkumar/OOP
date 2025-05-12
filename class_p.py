class Account:
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc

    def credit(self,amount = 0):
        self.bal += amount
        print(f"{amount} was credited")
        print("Your total balance is",self.get_balance())
    def debit(self,amount):
        self.bal -= amount
        print(f"{amount} was debited")
        print("Your total balance is = ", self.get_balance())

    def get_balance(self):
        return self.bal


acc1 = Account(5000,4562)
acc1.credit(500) #5500
acc1.debit(4690)
print(acc1.bal)
print(acc1.acc)








