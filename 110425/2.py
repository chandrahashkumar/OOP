# How to print, which type of error generate
try:
    n = int(input())
    print(n)
except:
    print("Error")

finally:
    print("OK")