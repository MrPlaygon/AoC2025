#Grausam
DEBUG = False

def my_print(text):
    if DEBUG:
        print(text)

def calculate_adjacent(y, x, lageplan):
    y_start = y-1
    y_end = y+1
    x_start = x-1
    x_end = x+1
    summe = 0
    for y1 in range(y_start, y_end+1):
        my_print(f"Checking row {y1}")
        if y1 not in range(0, len(lageplan)):
            my_print(f"Row not in range")
            continue
        for x1 in range(x_start, x_end+1):
            my_print(f"Checking column {x1}")
            if x1 not in range(0, len(lageplan[0])):
                my_print(f"Column not in range")
                continue
            if x1 == x and y1 == y:
                my_print("Is at original position, not adjacent")
                continue
            my_print(f"Checking ({x1}, {y1})")
            if lageplan[y1][x1] == "@":
                my_print(f"Increase because of cell {x1}, {y1}")
                summe += 1
    return summe


def zeige_matrix(lageplan, matrix):
    for l in lageplan:
        print(l)
    print()
    for x in matrix:
        print(x)
    print("---------------------------------------------------")


if __name__ == "__main__":
    # lageplan = [["@", "@", "@", "."], ["@", "@", "@", "."], ["@", "@", "@", "."], [".", ".", ".", "."]]
    # zeige_matrix(lageplan, [])
    # print(calculate_adjacent(1, 1, lageplan))
    # exit()

    lageplan = []

    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            lageplan.append(list(line))

    old_summe = -1
    summe = 0

    while old_summe != summe:
        old_summe = summe
        matrix = [([0]*len(lageplan)).copy() for i in range(len(lageplan[0]))]
        # matrix = [[0] * len(lageplan)] * len(lageplan[0])
        for y, row in enumerate(lageplan):
            for x, cell in enumerate(row):
                adj = calculate_adjacent(y, x, lageplan)
                my_print(f"Got adjacency number {adj} for cell {x}, {y}")
                matrix[y][x] = adj

        # zeige_matrix(lageplan, matrix)

        for y, row in enumerate(lageplan):
            for x, cell in enumerate(row):
                if lageplan[y][x] == "@" and matrix[y][x] < 4:
                    summe += 1
                    lageplan[y][x] = "x"

    print(summe)