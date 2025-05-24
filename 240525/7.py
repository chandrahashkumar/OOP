#  Static Variables in Python
"""
• Static variables retain their values across function calls.
• In Python, they are created using class attributes.
"""
# Useful for tracking shared data across multiple objects.
class Counter:
    count = 0
    def increment(self):
        Counter.count +=1
        print(f"Count {Counter.count}")

c = Counter()
c.increment() # 1
c2 = Counter()
c2.increment() # 2
