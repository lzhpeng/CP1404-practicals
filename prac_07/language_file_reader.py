import csv
from programming_language import ProgrammingLanguage


def main():
    """Load languages from CSV using basic file reading"""
    languages = []
    in_file = open('languages.csv', 'r')
    in_file.readline()  # Skip header
    for line in in_file:
        parts = line.strip().split(',')
        reflection = parts[2] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]))
        languages.append(language)
    in_file.close()

    for language in languages:
        print(language)


def using_csv():
    """Read CSV using csv.reader"""
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()  # Skip header
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()