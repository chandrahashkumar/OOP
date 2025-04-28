try:
    # Code that might raise an exception
    result = 10 / u
except Exception as e:
    print("An error occurred:",type(e).__name__) #display name of the error