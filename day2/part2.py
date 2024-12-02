def is_safe(levels):
    if all(1 <= levels[i] - levels[i - 1] <= 3 for i in range(1, len(levels))):
        return True

    return all(1 <= levels[i - 1] - levels[i] <= 3 for i in range(1, len(levels)))

def main():
    with open("puzzle_input.txt", "r") as file:
        reports = file.readlines()

    num_safe_reports = 0

    for report in reports:
        levels = [int(level) for level in report.split()]

        if is_safe(levels):
            num_safe_reports += 1
            continue

        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i+1:]):
                num_safe_reports += 1
                break

    print(num_safe_reports)

if __name__ == "__main__":
    main()