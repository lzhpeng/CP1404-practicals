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