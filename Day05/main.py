class MyRangeCollection:
    def __init__(self):
        self.ranges = []

    def add_range(self, new_range: range):
        self.ranges.append(new_range)

    def check_value(self, value: int):
        for r in self.ranges:
            if value in r:
                return True
        return False

if __name__ == '__main__':
    range_collection = MyRangeCollection()

    with open("input.txt", "r") as file:
        process_ranges = True
        fresh_items = 0
        for line in file:
            line = line.strip()
            if line == "":
                process_ranges = False
                continue

            if process_ranges:
                start = int(line.split("-")[0])
                end = int(line.split("-")[1])
                range_collection.add_range(range(start, end + 1))

            if not process_ranges:
                value_to_check = int(line)
                if range_collection.check_value(value_to_check):
                    fresh_items += 1

        print(f"Part one, fresh items: {fresh_items}")
