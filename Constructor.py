from webcolors import names


class Constant:

    def __init__(self,name=None,marks=None):
        if name is None and marks is None:
            print("No parameters")
        # elif name is None :
        #     print("just marks are given",self.marks)

        else:
            self.name=name
            self.marks=marks
            print(self.name,self.marks)

c1=Constant()
# c3=Constant(name=None,marks=22)
c2=Constant('Amey',33)

class args:
    def __init__(self,*args):
        if len(args)==0:
            print("no parameters")
        elif len(args)==1:
            self.name=args
            print(self.name)
        elif len(args)==2:
            self.name,self.age=args
            print(self.name,self.age)
        else:
            print("Invalid arguments")

a1=args()
a2=args("amey")
a3=args("AMey",43)
a4=args(4,5,56)


class check:
    def __init__(self,name,age):
        print(self.name,self.age)
    def __init__(self):
        print('no parameters')

c1=check()