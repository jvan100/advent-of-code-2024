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

    def sort_update(update):
        sorted_update = []
        remaining = set(update)

        while remaining:
            for page in remaining:
                if all(after not in remaining for after in ordering_rules[page]):
                    sorted_update.append(page)
                    remaining.remove(page)
                    break

        return sorted_update

    middle_total = 0

    for update in updates:
        if not is_valid_update(update):
            sorted_update = sort_update(update)
            middle_total += sorted_update[len(sorted_update) // 2]

    print(middle_total)

if __name__ == "__main__":
    main()