# class Account:
#     def __init__(self,bal,acc):
#         self.bal = bal
#         self.acc = acc
#
#     def credit(self,amount = 0):
#         self.bal += amount
#         print(f"{amount} was credited")
#         print("Your total balance is",self.get_balance())
#     def debit(self,amount):
#         self.bal -= amount
#         print(f"{amount} was debited")
#         print("Your total balance is = ", self.get_balance())
#
#     def get_balance(self):
#         return self.bal
#
#
# acc1 = Account(5000,4562)
# acc1.credit(500) #5500
# acc1.debit(4690)
# print(acc1.bal)
# print(acc1.acc)








class hunam_body:
    def __init__(self,eye,mouth,nose):
        self.eye = eye
        self.mouth = mouth
        self.nose = nose
    def show(self):
        print(f"Eye: {self.eye} Mouth: {self.mouth} Nose: {self.nose}")
Ankit=hunam_body(2,3,9)
ayush=hunam_body(6,6,9)
abhay=hunam_body(6,6,8)
Ankit.show()
ayush.show()
abhay.show()