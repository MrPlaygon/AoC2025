import math
dial_position = 50
password = 0  # Count number of times dial_position == 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()  # remove whitespaces, line breaks, etc.
        print(f"Current position: {dial_position}")
        print(f"Instruction: {line}")
        if line[0] == "R":  # multiplier if rotate left or right
            multiplier = 1
        else:
            multiplier = -1

        number_of_steps = line[1:]  # strip rotation indicator
        steps = int(number_of_steps)  # convert integer

        if steps >= 100:  # multiple revolutions
            print(f"Multiple rotations: {steps} : {math.floor(steps/100)}")
            password += math.floor(steps/100)
            steps = steps % 100

        old_dial = dial_position  # prevent count when rotation left and starting at 0
        dial_position = dial_position + multiplier * steps  # rotate
        if (old_dial != 0 and dial_position < 0) or dial_position > 100:
            password += 1
            print("Passed zero")
        dial_position = dial_position % 100
        print(f"New Position: {dial_position}")
        if dial_position == 0:
            print("Is at zero")
            password += 1
        print("---")

print(password)
