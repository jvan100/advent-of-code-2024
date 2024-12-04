def main():
    with open("puzzle_input.txt", "r") as file:
        chars = []

        for line in file.readlines():
            chars.append(list(line.strip()))

    def check_direction(x, y, dx, dy):
        xmas_chars = ("X", "M", "A", "S")

        for i in range(4):
            if 0 <= y < len(chars) and 0 <= x < len(chars[0]):
                if chars[y][x] != xmas_chars[i]:
                    return False

                y += dy
                x += dx
            else:
                return False

        return True

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0

    for y in range(len(chars)):
        for x in range(len(chars[0])):
            if chars[y][x] != "X":
                continue

            for dy, dx in directions:
                if check_direction(x, y, dx, dy):
                    count += 1

    print(count)

if __name__ == "__main__":
    main()