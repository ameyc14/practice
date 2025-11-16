l=[1,2,3,4,5,6,7]
target=5
l1=[]
s=set()
for i in l:
    t1=target-i
    if t1 in s:
        l1.append([i,t1])
    s.add(i)
print(l1)















