# a=[1,2,3,3,4]
# b={}
# for i in a:
#     b[i]=True
# # print(b)
# for i in b.items():
#

class enc:
    def __init__(self,name=None,age=None):
        if name is None or age is None:
            print("default object created")
        else:
            self.name=name
            self.__age=age
    def accessAge(self):
        return self.__age

e1=enc("ac",33)
e2=enc()
# print()
print(e1.name)
print(e1.accessAge())