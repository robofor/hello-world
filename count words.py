words = 0
result = 1
f = 0
name = input("Enter the name of the file:")
for line in name:
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
f = (len(name)) - words
d = result + f
print(d)