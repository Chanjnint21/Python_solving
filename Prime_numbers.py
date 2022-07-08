# Find prime number between two number

n1 = int(input("Input num 01: "))
n2 = int(input("Input num 02: "))
for i in range (n1, n2+1):
    for pm in range (2, i):
        if i%pm == 0:
            break
        else:
            print(i)
            break