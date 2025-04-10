a = input("Enter two number: ").split()
try:
    c = int(a[0]) + int(a[1])
    c = int(a[0]) / int(a[1])
    K = "kali" + int(a[0])
    print(c)
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except ZeroDivisionError:
    print("ZeroDivisionError")
print("Thank you for using this program")
