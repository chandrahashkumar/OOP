import random
print(random.randint(1, 10))
print(random.random())
print(random.uniform(1,6))
print(random.randrange(0 , 20,2))
my_list = ["apple", "banana", "cherry","pineapple"]
print(random.choice(my_list))
random.shuffle(my_list)
print(my_list)
print(random.sample(my_list, k=2))
for i in range(0,20,2):
    print(i)