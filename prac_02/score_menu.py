MENU = " G = Get a valid score (must be 0-100 inclusive)\n P = Print result\n S = Show stars\n Q = Quit"


def main():
    score = get_valid_score()
    choice = ''
    while choice != 'Q':
        print(MENU)
        choice = input("Enter your choice: ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Thank you!")
        else:
            print("Invalid choice. Please try again.")


def get_valid_score():
    score = int(input("Enter a score (0-100): "))
    if 0 <= score <= 100:
        return score
    else:
        print("Score must be between 0 and 100.")
        return get_valid_score()


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score > 90:
            return "Excellent"
        elif score > 50:
            return "Passable"
        else:
            return "Bad"


def print_result(score):
    status = determine_score_status(score)
    print(f"The status of the score is: {score} so it is {status}")


def show_stars(score):
    print('*' * score)


if __name__ == '__main__':
    main() 