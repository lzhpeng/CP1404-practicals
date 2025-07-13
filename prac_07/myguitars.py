import csv
from guitar import Guitar


def main():
    """Load guitars from CSV and display them"""
    languages = []
    in_file = open('guitar.csv', 'r')
    in_file.readline()  # Skip header
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        language = Guitar(parts[0], parts[1], reflection)
        languages.append(language)
    in_file.close()

    for language in languages:
        print(language)


def using_csv():
    """Alternative method using CSV reader"""
    in_file = open('guitar.csv', 'r', newline='')
    in_file.readline()  # Skip header
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()


main()