class BillingSystem:
    totalBill = 0
    def __init__(self,name_of_product,quantity,unit_price):
        self.name_of_product = name_of_product
        self.quantity = quantity
        self.unit_price = unit_price

    def cal_price(self):
        self.bill = self.unit_price * self.quantity
        BillingSystem.totalBill = BillingSystem.totalBill + self.bill
        return self.bill
    @classmethod
    def totalbill(cls):
        print(f"Total Bill: {BillingSystem.totalBill}")
    def generate_bill(self):
        print(f"Product Name: {self.name_of_product}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Price: {self.cal_price()}")
        print("Thank you for shopping!")

product_list = []
product_n = int(input("Enter the number of products: "))
for i in  range(product_n):
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product per unit price: "))
    product_quantity = int(input("Enter product quantity: "))
    product = BillingSystem(product_name,product_price,product_quantity)
    product_list.append(product)

for product in range(product_n):
    product_list[product].generate_bill()
BillingSystem.totalbill()

