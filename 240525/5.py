# Pass by Reference(Mutable type) [list,dictionaries,set]
def modify_list(lis):
    lis.append(10)


num_list = [4,9,2,5,8,2,2]
modify_list(num_list) #modify the list
print(num_list) #[4, 9, 2, 5, 8, 2, 2, 10]