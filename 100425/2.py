a = input("Enter two number: ").split()
try:
    c = int(a[0]) + int(a[1])
    print(c)
except ValueError:
    print("Invalid input")
print("Thank you for using this program")
