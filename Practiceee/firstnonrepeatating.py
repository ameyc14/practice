s='swiwss'
# output:w
d={}
# l=[]
for i in s:
    d[i]=d.get(i,0)+1

for i in s:
    if d[i]==1:
        print(i)
        break
print("most_counted:",max(d,key=d.get))
# for i,j in d.items():
    # if j==1:
    #     l.append(i)
# print(l[0])

# print(d)

# approach 2

from collections import Counter
def counter1():
    t='swissss'
    count=Counter(t)
    for i in t:
        if count[i]==1:
            return i
    return None
print(counter1())
