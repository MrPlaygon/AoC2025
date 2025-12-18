import math


def int_or_zero(s: str) -> int:
    if s == " ":
        return 0
    else:
        return int(s)

if __name__ == "__main__":
#     data = []
#     text = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """
#     for line in text.splitlines():
#         l = line.split()
#         data.append(l)
#         print(l)

    data = []
    with open("input.txt", "r") as f:
        for line in f:
            l = list(line.split())
            data.append(l)
            print(l)

    ### Part 1
    print("### Part 1 ###")
    DEPTH = 3
    summe = 0
    for i in range(len(data[0])):
        numbers = [row[i] for row in data[:DEPTH]]
        print(numbers)
        numbers = map(int, numbers)
        if data[DEPTH][i] == "*":
            summe += math.prod(numbers)
        elif data[DEPTH][i] == "+":
            summe += sum(numbers)
    print(summe)

    ### Part 2
    print("### Part 2 ###")
    DEPTH = 4

    # data = []
    # for line in text.splitlines():
    #     l = list(line)
    #     data.append(l)
    #     print(l)

    data = []
    with open("input.txt", "r") as f:
        for line in f:
            l = list(line.replace("\n", ""))
            data.append(l)
            print(l)

    print(data)
    operation = ""
    result_so_far = 0
    summe = 0
    for column in range(len(data[0])):
        print("### Working on column ", column)

        # load operation
        if data[DEPTH][column] == "*":
            operation = "*"
        elif data[DEPTH][column] == "+":
            operation = "+"
        print(f"Operation: {operation}")

        # assemble number
        numbers = []
        for row in range(DEPTH):
            if data[row][column] != " ":
                numbers.append(data[row][column])
        print(f"Numbers: {numbers}")
        number = 0
        numbers.reverse()  # lol
        for i in range(len(numbers) - 1, -1, -1):
            number += int(numbers[i]) * pow(10, i)
        print(f"Number: {number}")


        # reset for next calculation
        if number == 0:
            summe += result_so_far
            print(f"End of Column, updating Sum: {summe}")
            result_so_far = 0
            continue

        if operation == "*":
            if result_so_far == 0:
                result_so_far = number
            else:
                result_so_far *= number
        elif operation == "+":
            result_so_far += number
        print(f"Updated Result: {result_so_far}")

    summe += result_so_far
    print(summe)

