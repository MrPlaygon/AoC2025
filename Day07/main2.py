def print_tree(machine):
    for line in machine:
        text = ""
        for character in line:
            text += str(f"{character}".ljust(3))
        print(text)


if __name__ == '__main__':
    machine = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            new_line = [x if x != "." else 0 for x in line]
            machine.append(new_line)
    print(machine)
    
    starting_position = machine[0].index('S')
    
    WIDTH = len(machine[0])
    machine[1][starting_position] = 1
    for i in range(2, len(machine)):
        print(f"Working on line {i}")
        print(machine[i])
        for j in range(WIDTH):
            if machine[i][j] != "^" and machine[i - 1][j] != "^":
                machine[i][j] += machine[i - 1][j]
            elif machine[i][j] == "^":
                machine[i][j - 1] = machine[i - 1][j] + machine[i][j - 1]
                machine[i][j + 1] = machine[i - 1][j] + machine[i][j + 1]
        print_tree(machine)
    
    last_row = machine[len(machine)-1]
    print(last_row)
    print(sum(last_row))
        