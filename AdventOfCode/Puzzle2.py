import re


def open_input(filename):
    with open(f"PuzzleInputs/{filename}") as file:
        text = file.readlines()

    text = list(map(lambda x: x.strip('\n'), text))
    return text


def parse_row(row):
    regex = re.compile("^(\d+)-(\d+) ([a-z]): (\w+)$")
    matches = regex.match(row)
    (minimum, maximum, character, password) = (int(matches.group(1)), int(matches.group(2)), matches.group(3), matches.group(4))
    return (minimum, maximum, character, password)


def row_valid(tuple):
    min, max, char, password = tuple
    num = password.count(char)

    return num >= min and num <= max


def row_valid_b(tuple):
    first, second, char, password = tuple

    firstEqual = password[first-1] == char
    secondEqual = password[second-1] == char

    return firstEqual ^ secondEqual


def puzzle2A(file_input):
    parsed = list(map(parse_row, file_input))
    valid_passwords = list(filter(row_valid, parsed))
    return len(valid_passwords)


def puzzle2B(file_input):
    parsed = list(map(parse_row, file_input))
    valid_passwords = list(filter(row_valid_b, parsed))
    return len(valid_passwords)


def main():
    file_input = open_input("Puzzle2")
    outputA = puzzle2A(file_input)
    outputB = puzzle2B(file_input)

    print(f"Puzzle 2A: {outputA}, Puzzle 2B: {outputB}")


if __name__ == "__main__":
    main()
