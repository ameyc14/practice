from collections import Counter
# Input: "I love programming in Python"
# Output: "programming"
Input= "I love programming in Python"

# approach 1
# l2=[char for char in Input.split()]
# d={}
# for i in l2:
#     d[i]=len(i)
# print(max(d,key=d.get))

# approach 2

# l1 = Input.split()
# longest_word = max(l1, key=len)
# print(longest_word)

l=Input.split()
d={}
for i in l:
    d[i]=len(i)
print(d)
print(max(d,key=d.get))