class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car is started")

    @staticmethod
    def stop():
        print("car stopped")

    # def __init__(self):

class Toyota(Car):
    def __init__(self,name):
        self.name=name

# car1=Toyota("Fortuner")
# car2=Toyota("proist")
#
# print(car1.name)
# car1.start()

class   Fortuner(Toyota): #multilevel inheritence
    def __init__(self,price):
        self.price=price

F1=Fortuner(400000)

F1.start()

# multilevel Inheritence
class A:
    varA="wlcomA"
class B:
    varB="werB"
class C(A,B):
    vac="welcome to c"
c1=C()
print(c1.varA)
print(c1.varB)
print(c1.vac)

