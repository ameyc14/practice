# # # Input: "A man, a plan, a canal, Panama"
# # # Output: True
# # #
# # # Input: "hello"
# # # Output: False
# # #
# # import re
# # # def alpha(s):
# # #     s1=re.sub(r'[^A-Za-z0-9]','',s)
# # #     l1=list(s1.lower())
# # #     s1.lower()
# # #     return l1
# #
# # import re
# # def palindrome(s):
# #     s=re.sub(r'[^A-Z0-9a-z]','',s)
# #     s.lower()
# #     l1=list(s)
# #
# #     s2=''
# #
# #     for i in range(len(l1)-1,-1,-1):
# #         s2+=l1[i]
# #
# #     l2=list(s2)
# #     if l1==l2:
# #         print(l2)
# #         return True
# #     return False
# #
# import  re
# def palindrome(x):
#     # Convert the string to a list of characters
#     x1=list(re.sub(r'[^A-Za-z0-9]','',x))
#     # x1 = list(x)
#     print(x1)
#     x2 = ''
#     for i in x1:
#         x2 = i + x2  # Build the reversed string by prepending each character
#     x3 = list(x2)
#     return x1 == x3  # Compare original list to reversed list
#
# print(palindrome('ama/ chc ama'))
# #
# #
# #
# #
# # n=int(input("enter the range"))
# # a,b=0,1
# # print("fibonacci no's are",a,b,end=" ")
# # for i in range(2,n):
# #     c=a+b
# #     print(c,end=" ")
# #     a,b=b,c
# print(lambda x:x*2)(5)
from os import remove

from numpy.f2py.crackfortran import endifs


#Find a factorial
# def factorial(n):
#     if n==1 or n==0:
#         return 1
#         print(factorial(5))
#     else:
#         return n* factorial(n-1)

# Generate Fibonacci series up to n.
# def fibonacci(n):
#     a,b=0,1
#     print('fibonacci series:',a,b,end="")
#     for i in range(2,n+1):
#         c=a+b
#         print(c, end=" ")
#         a,b=b,c
# fibonacci(6)

# Write a function to flatten a nested list.
# Remove duplicates from a list.
# def remove_duplicates(l):
#     b=set()
#     for i in l:
#         b.add(i)
#     l1=list(b)
#     print(l1)
# remove_duplicates([1,2,2,3,4])

# Count frequency of each word in a string.
# def frequency_count(n):
#     d={}
#     for i in n:
#         d[i]=d.get(i,0)+1
#     print(d)
# frequency_count([1,2,2,3,4,55,55,55])

# Find the first non-repeating character in a string.
# aabbccde
# def first_nr(s):
#     d={}
#     for i in s:
#         d[i]=d.get(i,0)+1
#     for i,j in d.items():
#         if j==1:
#             print(i)
#             return
# first_nr('aabbdfs')

# Merge two sorted lists into one sorted list.
# l1=[1,3,5,6,7,9]
# l2=[2,3,4,6]
# def merge_sorted_lists(list1, list2):
#     merged = []
#     i, j = 0, 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged.append(list1[i])
#             i += 1
#         else:
#             merged.append(list2[j])
#             j += 1
#     merged.extend(list1[i:])
#     merged.extend(list2[j:])
#     return merged
#
# # Example usage:
# a = [1, 3, 5]
# b = [2, 4, 6]
# print(merge_sorted_lists(a, b))  # Output: [1, 2, 3, 4, 5,

# Find the largest and smallest number in a list without using min/max.

# def minmax(l):
#     l.sort()
#     print(f'min:{l[0]} , max:{l[-1]}')
# minmax([1,2,34,5,6,0])

# Sort a dictionary by its values.
# d={'a':12,'b':19,'c':1}
# def sortdict(n):
#     l=[]
#     a={}
#     for i,j in n.items():
#         l.append(j)
#     l.sort()
#     for i in l:
#        a[i]=a.get(i)

#
# d = {'a': 12, 'b': 19, 'c': 1}
# print(dict(sorted(d.items(),key=lambda x:x[1])))

# Use map() and filter() on a list of numbers.
l=[1,2,3,4,5,6]
a=list(map(lambda x: x*2,l))
b=list(filter(lambda x: x%2==0,l))

print(a,b)