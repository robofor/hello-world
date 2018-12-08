sum = 0
letter = input("enter letter:")
line = input("Enter the line:")
for i in range(len(line)):
   if line[i] == letter:
        sum += 1
        print(i, line[i])
print("result")
print(sum)