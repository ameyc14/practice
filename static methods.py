# methods don't use self parameter
# work at class level
#Decorator allow us to wrap another function in order to extend the behaviour of the wrapped function without permanantely modifying it

# import re
# class Student:
#     @staticmethod
#     def Hello():
#
#         print("hello")
#
# # s1=Student()
# # s1.Hello()
# Student.Hello()
#
# a=[45,454,34,2,1,2,1]
# b=set(a)
# c=()
# print(type(c))
# print(b)
# builtin_names = dir(__builtins__)
# for name in builtin_names:
#     print(name)


# def revereslist(l):
#     return [l[0]+ revereslist(l[1:])]
#
# l=[1,2,3,4,5,6]
# print(revereslist(l))



# write a function to balance paranthesis
# test cases:

# ([]{}) is balanced.
# ({[]}) is balanced.
# (} is not balanced.
# ([..]{33})
# wap to


def is_balanced(s):
    def cleaned(s):
        string = ''
        clean = '{}[]()'
        for char in s:
            if char in clean:
                string += char
        return string
    s=cleaned(s)
    a=[]
    for char in s:
        if char=='(':
            a.append(char)
        elif char==')':
            if not a:
                return False
            a.pop()
    return len(a)==0
print(is_balanced('(4r3)42()(34)'))








