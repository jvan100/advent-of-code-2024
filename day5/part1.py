from collections import defaultdict

def main():
    with open("puzzle_input.txt", "r") as file:
        reading_rules = True

        ordering_rules = defaultdict(set)
        updates = []

        for line in file.readlines():
            line = line.strip()

            if reading_rules:
                if line == "":
                    reading_rules = False
                    continue

                [before, after] = line.split("|")
                ordering_rules[int(before)].add(int(after))
            else:
                updates.append([int(page) for page in line.split(",")])

    def is_valid_update(update):
        pages_seen = set()

        for page in update:
            if not pages_seen.isdisjoint(ordering_rules[page]):
                return False

            pages_seen.add(page)

        return True

    middle_total = 0

    for update in updates:
        if is_valid_update(update):
            middle_total += update[len(update) // 2]

    print(middle_total)

if __name__ == "__main__":
    main()