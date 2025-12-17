class MyRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __str__(self):
        return f"Range({self.start}-{self.end})"

    def __repr__(self):
        return self.__str__()

    def overlaps(self, other: "MyRange") -> bool:
        if other.start > self.end or other.end < self.start:
            return False
        return True


    def extend_range(self, other: "MyRange"):
        if not self.overlaps(other):
            raise Exception("Cannot extend range without overlap")
        self.start = min(self.start, other.start)
        self.end = max(self.end, other.end)


    def get_number_of_ids(self):
        return self.end - self.start + 1


if __name__ == '__main__':
#     input_data = """3-5
# 10-14
# 16-20
# 12-18"""
    with open("input.txt", "r") as f:
        input_data = f.read()

    ranges = []
    for line in input_data.split("\n"):
        line = line.strip()
        if line == "":
            break
        print(f"Working on range {line}")
        start = int(line.split("-")[0])
        end = int(line.split("-")[1])
        new_range = MyRange(start, end)
        merged = True
        while merged:
            merged = False
            for r in ranges:
                if new_range.overlaps(r):
                    new_range.extend_range(r)
                    ranges.remove(r)
                    merged = True
        ranges.append(new_range)
    print(ranges)

    sum_of_ids = 0
    for r in ranges:
        sum_of_ids += r.get_number_of_ids()
    print(f"Sum of ids: {sum_of_ids}")