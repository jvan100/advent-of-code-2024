def main():
    with open("puzzle_input.txt", "r") as file:
        lines = file.readlines()

    list1 = []
    list2_counts = {}

    for line in lines:
        [num1, num2] = line.split()

        list1.append(int(num1))

        num2 = int(num2)
        list2_counts[num2] = list2_counts.get(num2, 0) + 1

    total = 0

    for num in list1:
        total += num * list2_counts.get(num, 0)

    print(total)

if __name__ == "__main__":
    main()