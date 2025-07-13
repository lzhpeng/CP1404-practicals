import csv
from collections import namedtuple
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


def using_namedtuple():
    """Read CSV using namedtuple for structured data"""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    Language = namedtuple('Language', 'name, typing, reflection, year')
    reader = csv.reader(in_file)

    for row in reader:
        language = Language._make(row)
        print(repr(language))
    in_file.close()


def using_csv_namedtuple():

    """Read CSV using namedtuple with map function"""
    Language = namedtuple('Language', 'name, typing, reflection, year')
    in_file = open("languages.csv", "r")
    in_file.readline()  # Skip header
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))


if __name__ == "__main__":
    main()