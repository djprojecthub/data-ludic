t = int(input())

for i in range(t):
    a = input()
    b = input()
    count = 0

    if len(a) <= len(b):
        for i in a:
            if i in b:
                count = count+1
        count = len(a) + len(b) - (count*2)

    else:

        for i in b:
            if i in a:
                count = count + 1
        count = len(a) + len(b) - (count*2)

print(count)        

#***Test Cases***#

# tttttttttttttttttttttttttttttttttttttsssssssssssssssss
# sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
# pqwerteetlp
# dedfghwv

# abcxe
# eabrt

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb