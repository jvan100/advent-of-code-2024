import re

PATTERN = r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)"

def main():
    with open("puzzle_input.txt", "r") as file:
        text = file.read()

    enabled = True
    total = 0

    for match in re.finditer(PATTERN, text):
        if match.group(1):
            enabled = True
        elif match.group(2):
            enabled = False
        elif enabled:
            operand1 = int(match.group(3))
            operand2 = int(match.group(4))

            total += operand1 * operand2

    print(total)

if __name__ == "__main__":
    main()