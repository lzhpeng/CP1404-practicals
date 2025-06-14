def main():
    number_of_months = int(input("How many months? "))
    incomes = [float(input(f"Enter income for month {month}: ")) for month in range(1, number_of_months + 1)]
    print_report(incomes)

def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main() 