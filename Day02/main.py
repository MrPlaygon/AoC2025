import math


def number_of_digits(number: int) -> int:
    return math.floor(math.log10(number) + 1)


if __name__ == "__main__":
    total = 0
    with open("input.txt", "r") as file:
        id_ranges = file.read()

    for id_range in id_ranges.split(","):
        print(id_range)
        start_id = int(id_range.split("-")[0])
        end_id = int(id_range.split("-")[1])
        print(number_of_digits(start_id))
        for i in range(int(start_id), int(end_id) + 1):
            if number_of_digits(i) % 2 != 0:
                continue

            i_string = f"{i}"
            split = len(i_string) // 2
            if i_string[:split] == i_string[split:]:
                total += i
    print(total)
