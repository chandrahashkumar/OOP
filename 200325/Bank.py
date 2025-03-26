class Bank:
    def __init__(self,Name,ID,accn,DOB,amount):
        self.Name = Name
        self.ID = ID
        self.accn = accn
        self.DOB = DOB
        self.amount = amount

    def withdraw(self,amount):
        if amount > 0:
            self.amount -= amount
        else:
            print("not enough money")
    def deposit(self,amount):
        self.amount += amount
    def display(self):
        print("Name:", self.Name)
        print("ID:", self.ID)
        print("Account Number:", self.accn)
        print("DOB:", self.DOB)
        print("amount:", self.amount)

person1 = Bank('Kali',45,45612,'10/12/2006',1000)
person1.withdraw(1500)
# person1.deposit(500)
person1.display()
