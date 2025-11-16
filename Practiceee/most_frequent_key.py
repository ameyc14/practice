data = [
    {"name": "Alice", "city": "New York"},
    {"name": "Bob", "city": "Los Angeles"},
    {"name": "Charlie", "city": "New York"},
    {"name": "David", "city": "Chicago"},
    {"name": "Eve", "city": "New York"}
]
d={}
for i in data:
    for j,k in i.items():
        if j=="city":
            d[k]=d.get(k,0)+1

print(d)

print(max(d,key=d.get))

