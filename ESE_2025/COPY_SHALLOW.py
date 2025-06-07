import copy

l = [4,6,5,[8,6,9]]
shallow_copy = l.copy()
deep_copy = copy.deepcopy(l)

shallow_copy[3][2] = 50
shallow_copy[2] = 50 # not effect original list without nested list
deep_copy[1] = 80
print(f"original list: {l}")
print(f"Shallow copy: {shallow_copy}")
print(f"Deepcopy : {deep_copy}")


