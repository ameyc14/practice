
# def rotateString(s,goal) :
#     for i in range(1, len(s)):
#         if s[i:] + s[i - 1] == goal:
#             return True
#     return False
#
# print(rotateString('abcs','bsc'))
s="abcde"
goal="bcdea"

for i in range(1, len(s)):
        if s[i:] + s[i - 1] == goal:
            print("equal")
        print("unequal")