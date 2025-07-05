from prac_06.guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    name = input("Name (leave blank to finish): ").strip()
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} added.")
        name = input("Name (leave blank to finish): ").strip()

    # Add sample guitars after user input
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
