import random

LINE_NUMBERS = 6
NUMBERS_MINIMUM = 1
NUMBERS_MAXIMUM = 45

def main():
    numbers = int(input("How many quick picks:"))
    while numbers < 0:
        print("Error")
        numbers = int(input("How many quick picks:"))
    for i in range(numbers):
        quick_picks = []
        for j in range(LINE_NUMBERS):
            numbers = random.randint(NUMBERS_MINIMUM, NUMBERS_MAXIMUM)
            while numbers in quick_picks:
                numbers = random.randint(NUMBERS_MINIMUM, NUMBERS_MAXIMUM)
            quick_picks.append(numbers)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))

main() 