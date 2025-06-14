import random

MAX_INCREASE = 0.1
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
FILENAME = "stock_output.txt"

price = INITIAL_PRICE

day = 0

with open(FILENAME, 'w') as out_file:
    print(f"Starting price: ${price:,.2f}")
    out_file.write(f"Starting price: ${price:,.2f}\n")
    while MIN_PRICE <= price <= MAX_PRICE:
        price_change = 0
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)
        day += 1
        price *= (1 + price_change)
        print(f"On day {day} price is ${price:,.2f}")
        out_file.write(f"On day {day} price is ${price:,.2f}\n")
        
out_file.close()