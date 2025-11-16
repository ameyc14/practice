class Car:
    def __init__(self):
        self.brk=False
        print("Car is starting")
    def start(self):
        self.brk=True
        print("car started")
c1=Car()
c1.start()
