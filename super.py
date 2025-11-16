class parent:
    def salary(self,salary):
        self.salary=salary

        print("salary is ",self.salary)
class child(parent):
    def salary(self):
        print("I am not earning right now . mY parent salary is my salary")
        super().salary(49999)

c1=child()
c1.salary()
