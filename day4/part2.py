def main():
    with open("puzzle_input.txt", "r") as file:
        chars = []

        for line in file.readlines():
            chars.append(list(line.strip()))

    def check_xmas(x, y):
        patterns = [
            [(-1, -1, "M"), (1, 1, "S")],
            [(-1, 1, "M"), (1, -1, "S")],
            [(1, -1, "M"), (-1, 1, "S")],
            [(1, 1, "M"), (-1, -1, "S")]
        ]

        matched_pattern_count = 0

        for (pattern1, pattern2) in patterns:
            new_y1 = y + pattern1[0]
            new_y2 = y + pattern2[0]
            new_x1 = x + pattern1[1]
            new_x2 = x + pattern2[1]

            if 0 <= new_y1 < len(chars) and 0 <= new_y2 < len(chars) and 0 <= new_x1 < len(chars[0]) and 0 <= new_x2 < len(chars[0]):
                if chars[new_y1][new_x1] == pattern1[2] and chars[new_y2][new_x2] == pattern2[2]:
                    matched_pattern_count += 1

            if matched_pattern_count == 2:
                return True

        return False

    count = 0

    for y in range(len(chars)):
        for x in range(len(chars[0])):
            if chars[y][x] == "A" and check_xmas(x, y):
                count += 1

    print(count)

if __name__ == "__main__":
    main()