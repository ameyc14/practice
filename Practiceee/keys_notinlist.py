d = {"apples": 17, "bananas": 9, "grapes": 8}
required_keys = ["apples", "bananas", "oranges", "mangoes"]
# output= [oranges,mangoes]



for i,j in d.items():
    if i not in required_keys:
        print(i,end= " ")


for i in required_keys:
    if i not in d:
        print(i)

print([i for i in required_keys if i not in d])