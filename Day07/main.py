# Recursive approach
# def count_splits(row, column, machine) -> int:
#     pass
def print_tree(machine):
    for line in machine:
        text = ""
        for character in line:
            text += character
        print(text)

if __name__ == '__main__':
    machine = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            machine.append(list(line))
    print(machine)
    
    starting_position = machine[0].index('S')
    # splits = count_splits(1, starting_position, machine)
    # print(splits)
    
    WIDTH = len(machine[0])
    splits = 0
    machine[1][starting_position] = "|"
    for i in range(2, len(machine)):
        print(f"Working on line {i}")
        print(machine[i])
        for j in range(WIDTH):
            if machine[i][j] == "." and machine[i - 1][j] == "|":
                machine[i][j] = "|"
                continue
            if machine[i][j] == "^" and machine[i - 1][j] == "|":
                splits += 1
                # if j+1 < WIDTH:
                machine[i][j + 1] = "|"
                # if j-1 >= 0:
                machine[i][j - 1] = "|"
        print_tree(machine)
        print(splits)
        