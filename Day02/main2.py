import math


def check_valid(number: str) -> bool:
    # print(f"------------------{number}")
    number_of_digits = len(number)
    max_len_to_check = number_of_digits // 2
    # print(f"Max length to check is {max_len_to_check}")
    for j in range(1, max_len_to_check + 1):
        if number_of_digits % j != 0:
            # print(f"Continue on {j}")
            continue

        parts = [number[k:k+j] for k in range(0, len(number), j)]
        # print(f"Parts on {j}: {parts}")
        if len(set(parts)) == 1:
            return False
    return True


if __name__ == "__main__":
    # check_valid(str(111))
    # exit()
    total = 0
    with open("input.txt", "r") as file:
        id_ranges = file.read()

    for id_range in id_ranges.split(","):
        # print(id_range)
        start_id = int(id_range.split("-")[0])
        end_id = int(id_range.split("-")[1])
        for i in range(int(start_id), int(end_id) + 1):
            i_string = f"{i}"
            if not check_valid(i_string):
                total += i
    print(total)
