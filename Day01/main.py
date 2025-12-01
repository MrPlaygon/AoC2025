dial_position = 50
password = 0  # Count number of times dial_position == 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()  # remove whitespaces, line breaks, etc.
        print(line)
        if line[0] == "R":  # multiplier if rotate left or right
            multiplier = 1
        else:
            multiplier = -1

        number_of_steps = line[1:]  # strip rotation indicator
        steps = int(number_of_steps)  # cpmnvert integer
        dial_position = dial_position + multiplier * steps  # rotate
        dial_position = dial_position % 100
        if dial_position == 0:
            password += 1

print(password)
