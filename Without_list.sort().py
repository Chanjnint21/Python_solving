# Sort list without using list.sort()

list = [1, 3, 2, 5, 8, 7, 4, 6]

for i in range(len(list)):
  for j in range(i+1, len(list)):              #len() returns the length of the given list
    if list[i] > list[j]:
      list[i], list[j] = list[j], list[i]

print(list)

