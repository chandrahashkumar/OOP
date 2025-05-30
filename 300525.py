# Encapsulation
class Bank:
    def __init__(self):
        self.__Name = "Kali"
        self.__account_no = 45785
        self.__customerID = 56
    def display(self):
        print(f"Account Number {self.__account_no}")
    def __change_name(self,Name):
        self.__Name =Name
        print(self.__Name)

c = Bank()
# print(c.Name) # AttributeError
print(c._Bank__customerID)
c._Bank__customerID = 78
print(c._Bank__customerID)
c.display()
# c.__change_name  # AttributeError
c._Bank__change_name("KAL")
print(c._Bank__Name)