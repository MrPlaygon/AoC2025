def array_to_integer(arr: list) -> int:
    result = 0
    arr = arr[::-1]
    for i, value in enumerate(arr):
        # print(i, value)
        result += value * pow(10, i)
    return result


def process_line(line: str) -> int:
    biggest_line_number = [0] * 12  # Change for part 1 and 2
    print(f"Length of line: {len(line)}")
    for character_index, character in enumerate(line):
        print(f"######Processing character: {character} at position {character_index}")
        rest_of_line_character_count = len(line) - 1 - character_index
        print(f"Rest of line characters count: {rest_of_line_character_count}")
        for i in range(max(0, len(biggest_line_number) - 1 - rest_of_line_character_count), len(biggest_line_number), 1):
            print(f"Comparing {biggest_line_number[i]} to {character}")
            if biggest_line_number[i] < int(character):
                print(f"New Character is bigger")
                biggest_line_number[i] = int(character)
                for j in range(i + 1, len(biggest_line_number)):
                    biggest_line_number[j] = 0
                print(f"New Biggest Line: {biggest_line_number}")
                break
    print(f"Biggest line number: {biggest_line_number}")
    return array_to_integer(biggest_line_number)


if __name__ == '__main__':
    print(array_to_integer([5,2,3,4]))
    # print(process_line("3733444444337244341463452463644234493354144584433344425444453534454444343444324335454446423343444472"))
    # print(process_line("9937334444443372443414634524636442344333541445144333444254444535344544443434443243354544464233434472"))
    # print(process_line("1738344444433724434146345246364423443335414451443334442544445353445444434344433243354544464233434499"))
    # print(process_line("1738344444433724434146345246364423443335414451443334442544445353445444434344432433354544464233434419"))
    #
    # exit(0)
    summe = 0
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            summe += process_line(line)
    print(summe)
