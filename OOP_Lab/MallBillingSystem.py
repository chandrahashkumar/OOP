class Mall:
    mall_name="Paramount"
    Total_bill=0
    def __init__(self,p_name,p_price,quantity):
        self.p_name=p_name
        self.p_price=p_price
        self.quantity=quantity
    def calculate_bill(self):
        self.bill=self.p_price*self.quantity
        Mall.Total_bill=Mall.Total_bill+self.bill
    def greet():
        print("Welcome to Paramount Mall\n")
    def display(self):
        print(f"Product Name :- {self.p_name}\nPrice Per Unit :- {self.p_price}\nQuantity :- {self.quantity}\nCost :- {self.bill}")
    def thank():
        print("Thank you for shopping with us")
        print("Please visit us again!")
    @classmethod
    def totalbill(cls):
        print("Total bill : " , cls.Total_bill)
item=[]

print("press any character and then press enter to calculate bill")
n=input("")
total_item=int(input("How many different items: "))
for i in range(total_item):
    print(f"Product {i+1} :- ")
    p_name=input("Enter product name: ")
    p_price=float(input("Enter price per unit: "))
    quantity=int(input("Enter total quantity: "))
    product=Mall(p_name,p_price,quantity)
    product.calculate_bill()
    item.append(product)
print("**********************")
print("All items inserted")
print("Now generating Bill")
print("**********************")
Mall.greet()
print("**********************")
for i in range(total_item):
    item[i].display()
Mall.totalbill()
Mall.thank()