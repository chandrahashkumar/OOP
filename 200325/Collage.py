# import Mall_Billing_system as ka
# print(ka.p(9))
# print(ka.pi)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter positive number: "))
    # Enter positive number: 7
print(f"The factorial of {num} is {factorial(num)}")
    #The factorial of 7 is 5040

