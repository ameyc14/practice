# arr = [1, 2, 4, 6, 3, 7, 8]
# Output: 5 (since 5 is missing)

arr = [1, 2, 4, 6, 3, 7, 8]
n=len(arr)+1
lost= n*(n+1)/2-sum(arr)
print(int(lost))

# approach 1
# arr.sort()
# for i in range(0,len(arr)-1):
#     if arr[i+1]-arr[i]!=1:
#         print(arr[i]+1)
#         break

# approach 2

# n=len(arr)+1 # as one is missing
# total_sum=n*(n+1)/2
# arr_sum=sum(arr)
# desired_no=int(total_sum-arr_sum)
# print(desired_no)
#

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

for val in fib(10):
    print(val, end=" ")
