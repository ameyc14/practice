def reverse_string(s):
    revers=''
    for char in s:
        revers=char+revers
    return revers

print(reverse_string('abc'))
