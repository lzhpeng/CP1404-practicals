numbers = [int(input("Number:")) for _ in range(5)]
print(numbers)
print("the first number is", numbers[0])
print("the last number is", numbers[-1])
print("the smallest number is", min(numbers))
print("the biggest number is", max(numbers))
print("the average of the number is", sum(numbers)/len(numbers))

# 2. Woefully inadequate security checker...
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
'ExecState', 'InteractiveConsole', 'InterpreterInterface',
'StartServer', 'bob']
username = input("Enter username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied") 