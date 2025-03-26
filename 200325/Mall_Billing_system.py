class BillingSystem:
    def __init__(self,name_of_product,quantity,unit_price):
        self.name_of_product = name_of_product
        self.quantity = quantity
        self.unit_price = unit_price

    def cal_price(self):
        self.unit_price *= self.quantity
        return self.unit_price

    def generate_bill(self):
        print(f"Product Name: {self.name_of_product}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Price: {self.cal_price()}")
        print("Thank you for shopping!")

Ram = BillingSystem("Shoes",1, 1300)
Kal = BillingSystem("Footwear",1, 380)
Sita = BillingSystem("Hanky",2, 120)

Ram.generate_bill()
print("................")
Kal.generate_bill()
print("................")
Sita.generate_bill()