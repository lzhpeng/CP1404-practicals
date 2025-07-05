from prac_06.car import Car

MENU = "Menu:\nD) Drive\nR) Refuel\nQ) Quit"

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Value must be >= 0")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
