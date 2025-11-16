class Constant:

    def __init__(self,name=None,marks=None):
        if name is None and marks is None:
            print("No parameters")
        else:
            self.name=name
            self.marks=marks
            print(self.name,self.marks)

c1=Constant()
c2=Constant('Amey',33)