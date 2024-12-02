def main():
    with open("puzzle_input.txt", "r") as file:
        reports = file.readlines()

    num_safe_reports = 0

    for report in reports:
        levels = [int(level) for level in report.split()]

        is_safe = all(1 <= levels[i] - levels[i - 1] <= 3 for i in range(1, len(levels)))

        if not is_safe:
            is_safe = all(1 <= levels[i - 1] - levels[i] <= 3 for i in range(1, len(levels)))

        if is_safe:
            num_safe_reports += 1

    print(num_safe_reports)

if __name__ == "__main__":
    main()