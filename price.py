# class quantity:
#     def __init__(self,price,quantity):
#         self.price=price
#         self.quantity=quantity
#     def fun(self):
#        # print(self.price*self.quantity)
#         return self.price*self.quantity
# q1=quantity(30,4)
# print(q1.fun())

# import re
# a="9"
# if  re.search(r'^\d',a):
#     print("it is a digit")
# else:
#     print('not a digit')
# import re
# a = "cats"
# result = re.search(r'^\d', a)
# if result:
#     print("Starts with a digit")
# else:
#     print("Does not start with a digit")

d={}
l=['eat','tea','attte']

for i in l:
    t=tuple(sorted(i))
    if t in d:
        d[t].append(i)
    else:
        d[t]=[i]

for i , j in d.items():
    print(d)

# nums=[4,1,-1,2,-1,2,3]
# # nums.sort()
# k=2
# d = {}
#
# for i in nums:
#     d[i] = d.get(i, 0) + 1
#
# sorted_dict=sorted(d.items(), key=lambda item:item[1],reverse=True)
#
# # print(sorted_dict)
#
# result=[item[0] for item in sorted_dict[:k]]
# print(result)
# l=["bete","neet"]
# t=''
# for i in l:
#     t+=''.join(tuple(i))
#
# print(list(t))

a=[1,2,3,3,4,4,4,5,5]
b=set(a)
c={}
for i in a:
    c[i]=c.get(i,0)+1

print(c)

# import pandas as pd
# df=pd.DataFrame({"ac":[1,2,3,4],"Bc":[1,2,2,2]},index=['a','b','c','d'])
# print(df)
#





