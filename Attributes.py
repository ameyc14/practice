# class attr
# obj attr
# obj attr>class attr
class att:
    name="amey" #class attr
    def __init__(self,name=None):
        if name is None:
            pass
        else:
            self.name=name
            print(self.name)

a1=att()
print(a1.name)
