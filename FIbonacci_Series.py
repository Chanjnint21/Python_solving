# Write  aprogram that print FIbonacci Series

Sequence = int(input("Number of sequence you want to know: "))
Seq = 0
for i in range (Sequence):
    i = i + Seq
    Seq += i
    print(i)
