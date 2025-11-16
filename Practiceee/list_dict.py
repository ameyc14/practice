dicts = [
    {"apples": 10, "bananas": 5},
    {"apples": 7, "oranges": 3},
    {"bananas": 4, "grapes": 8}
]
# {'apples': 17, 'bananas': 9, 'oranges': 3, 'grapes': 8}
d={}
for l in dicts:
    for i,j in l.items():
        d[i]=d.get(i,0)+j
print(dict(sorted(d.items(),reverse=True)))
print(d)
print(i,j)