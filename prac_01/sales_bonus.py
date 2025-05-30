SALES_THRESHOLD = 1000
LOW_BONUS_RATE = 0.1
HIGH_BONUS_RATE = 0.15

def calculate_bonus(sales):
    if sales < SALES_THRESHOLD:
        return sales * LOW_BONUS_RATE
    return sales * HIGH_BONUS_RATE

def main():
    sales = float(input("Enter your sales: "))
    while sales >= 0:
        bonus = calculate_bonus(sales)
        print(f"Bonus: ${bonus:.2f}")
        sales = float(input("Enter your sales: "))

if __name__ == "__main__":
    main() 