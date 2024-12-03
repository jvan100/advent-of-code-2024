import re

PATTERN = r"mul\((\d+),(\d+)\)"

def main():
    with open("puzzle_input.txt", "r") as file:
        text = file.read()

    total = 0

    for match in re.finditer(PATTERN, text):
        operand1 = int(match.group(1))
        operand2 = int(match.group(2))

        total += operand1 * operand2

    print(total)

if __name__ == "__main__":
    main()