class Constant:

    def __init__(self,name=None,marks=None):
        if name is None and marks :

            self.marks=marks
            print(self.marks)
        else:
            self.name=name
            self.marks=marks
            print(self.name,self.marks)

c1=Constant(3000)
c2=Constant('Amey',33)