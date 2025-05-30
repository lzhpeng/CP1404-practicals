import random


def main():
    score = float(input("Enter score: "))
    print(determine_status(score))
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    random_status = determine_status(random_score)
    print(f"Random score status: {random_status}")


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main() 