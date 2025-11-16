from numpy.ma.extras import average

students = {
    "Alice": [85, 78, 92],
    "Bob": [79, 74, 88],
    "Charlie": [92, 90, 85]
}

# output: {'Alice': 85.0, 'Bob': 80.33, 'Charlie': 89.0}

# print(students["Alice"][0])
output={}
a=39
for i,j in students.items():
    # print(i,average(j))
    output[i]=round(sum(j)/len(j),2)
print(output)
print(a)

print(students.get('Alice'))
print(students.values())



