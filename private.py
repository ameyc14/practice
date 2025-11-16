#  private defined by __
#
# class privatee:
#     __name="amey"
#
#     def name(self):
#         print(self.__name)
#
# p1=privatee()
# p1.name()



# class privatee:
#     __name="amey"
#
#     def __whatisurname(self):
#         print(self.__name)
#
#     def callprivate(self):
#         self.__whatisurname()
#
# p1=privatee()
# p1.callprivate()
# p1.__whatisurname() # this will throw error

class encapsule:
    __name="Private hu mai"

    # def priv(self):
    #     return self.__name
    def set_name(self2, name1):
        self2.__name=name1
    def get_name(self):
        return self.__name
e1=encapsule()
e1.set_name("Samir")
print(e1.get_name())