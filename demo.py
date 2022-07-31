# Comments - in C //

# Declare variables in C -> int num = 7
num = 4
height = int(input("Height: "))
name = 'Greg'

# print statements - in C -> printf("Hello, %s", name)
print("Hello, " + name + ". Nice to meet you!")
print(f"Hello, {name}. Nice to meet you!")

# while loops - in C -> while (num > 7) {}
# while (height < 8):
#     print("Error")
#     break

# while (num < 9):
#     print(num)
#     num = num + 1

# for loops in C -> for(int i = 0; i < 4; i++)
people = ['Joe', 'Ralf', 'Larry']
for person in people:
    print(person)

ns = range(0, num + 1)
for n in ns:
    print(n)

# conditionals - in C -> if, else if, else
if (height < 2):
    print("low")
elif (height == 2):
    print("exact")
else:
    print("high")
