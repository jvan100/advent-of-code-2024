def main():
    with open("puzzle_input.txt", "r") as file:
        lines = file.readlines()

    list1 = []
    list2 = []

    for line in lines:
        [num1, num2] = line.split()

        list1.append(int(num1))
        list2.append(int(num2))

    list1.sort()
    list2.sort()

    total = 0

    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])

    print(total)

if __name__ == "__main__":
    main()