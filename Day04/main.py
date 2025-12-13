matrix = []
lageplan = []


def calculate_adjacent(y, x, lageplan):
    y_start = y-1
    y_end = y+1
    x_start = x-1
    x_end = x+1
    summe = 0
    for y1 in range(y_start, y_end+1):
        print(f"Checking Y {y1}")
        if y1 not in range(0, len(lageplan)):
            print(f"Y1 not in range: {y1}")
            continue
        for x1 in range(x_start, x_end+1):
            print(f"Checking X {x1}")
            if x1 not in range(0, len(lageplan[0])):
                print(f"X1 not in range: {x1}")
                continue
            if x1 == x and y1 == y:
                print("Is at original position, not adjacent")
                continue
            print(f"Checking {x1}, {y1}")
            if lageplan[y1][x1] == "@":
                summe += 1
    return summe

def build_matrix(lageplan):
    matrix = []
    for y, row in enumerate(lageplan):
        for x, cell in enumerate(row):
            matrix[y][x] = calculate_adjacent(y, x, lageplan)

if __name__ == "__main__":
    # test = [["@", ".", ".", "."], ["@", ".", ".", "."], [".", ".", ".", "."], [".", ".", ".", "."]]
    # print(calculate_adjacent(0, 2, test))
    # exit()
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            lageplan.append(list(line))
            matrix.append([0] * len(line))

    print(lageplan)
    print(matrix)

    for y, row in enumerate(lageplan):
        for x, cell in enumerate(row):
            matrix[y][x] = calculate_adjacent(y, x, lageplan)

    print(matrix)

    summe = 0
    for y, row in enumerate(lageplan):
        for x, cell in enumerate(row):
            if lageplan[y][x] == "@" and matrix[y][x] < 4:
                summe += 1

    print(summe)