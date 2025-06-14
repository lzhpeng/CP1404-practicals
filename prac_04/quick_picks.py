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
        quick_picks = random.sample(range(NUMBERS_MINIMUM, NUMBERS_MAXIMUM + 1), LINE_NUMBERS)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))

main() 