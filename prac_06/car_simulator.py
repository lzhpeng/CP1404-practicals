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

def main():
    print("Let's drive!")
    name = input("Enter your car name: ")
    car = Car(name, 100)  # Initial fuel of 100
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").strip().lower()
    while choice != "q":
        if choice == "d":
            distance_to_drive = get_positive_integer("How many km do you wish to drive? ")
            distance_driven = car.drive(distance_to_drive)
            print(f"The car drove {distance_driven} km", end="")
            if car.fuel == 0:
                print(" and ran out of fuel", end="")
            print(".")
        elif choice == "r":
            fuel_to_add = get_positive_integer("How many units of fuel do you want to add to the car? ")
            car.add_fuel(fuel_to_add)
            print(f"Added {fuel_to_add} units of fuel.")
        else:
            print("Invalid choice")
        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").strip().lower()
    print(f"\nGoodbye, {car.name}'s driver.")

if __name__ == "__main__":
    main()