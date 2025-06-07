# question 1
with open("name.txt", "w") as out_file:
    name = input("What is your name? ")
    print(name, file=out_file)

# question 2
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)

# question 3
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# question 4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number
print(total) 