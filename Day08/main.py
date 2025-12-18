# Fully connected graph: n(n-1)/2
import math
import random


class Circuit:
    def __init__(self):
        self.boxes = []
        self.id = random.randint(1, 99999999)

    def add_box(self, box: "JunctionBox"):
        self.boxes.append(box)
        box.set_circuit(self)

    def __contains__(self, box: "JunctionBox"):
        return box in self.boxes

    def merge(self, other: "Circuit"):
        self.boxes.extend(other.boxes)
        for box in other.boxes:
            box.set_circuit(self)

    def __str__(self):
        return str(f"{self.id}")

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return len(self.boxes) < len(other.boxes)

class Connection:
    def __init__(self, box1: "JunctionBox", box2: "JunctionBox"):
        self.distance = box1.get_distance_to(box2)
        self.box1 = box1
        self.box2 = box2

    def __lt__(self, other: "Connection") -> bool:
        return self.distance < other.distance

    def __eq__(self, other: "Connection") -> bool:
        return self.distance == other.distance

    def __str__(self):
        return f"L: {self.distance:.1f} :: {self.box1} -> {self.box2}"

    def __repr__(self):
        return self.__str__()

class JunctionBox:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.circuit: "Circuit" = None

    def get_distance_to(self, other: "JunctionBox") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def set_circuit(self, circuit: "Circuit"):
        self.circuit = circuit

if __name__ == "__main__":

    # Creating JunctionBoxes and possible Connections
    connections = []
    boxes = []
    with open("input.txt") as f:
        for line in f:
            x,y,z = map(int,line.split(","))
            print(f"Creating box {x},{y},{z}")
            new_box = JunctionBox(x, y, z)
            for b in boxes:
                print(f"Creating possible connection with {b}")
                connections.append(Connection(new_box, b))
            boxes.append(new_box)
        print(f"Total number of boxes {len(boxes)}")
        print(f"Total number of connections {len(connections)}")

    connections.sort()
    print(connections)

    circuits = []
    for connection in connections[:1000]:
        print(f"Processing connection {connection}")
        box1 = connection.box1
        box2 = connection.box2
        if box1.circuit is not None and box1.circuit == box2.circuit:
            print(f"Box {box1} has same circuit as {box2}: {box1.circuit} == {box2.circuit}")
            continue
        if box1.circuit is not None and box2.circuit is not None:
            print(f"Box {box1} and {box2} are both in a circuit: {box1.circuit} and {box2.circuit}")
            print(f"Removing circuit {box2.circuit}")
            circuits.remove(box2.circuit)
            box1.circuit.merge(box2.circuit)
        elif box1.circuit is not None:
            print(f"Box1 {box1} has circuit")
            box1.circuit.add_box(box2)
        elif box2.circuit is not None:
            print(f"Box2 {box1} has circuit")
            box2.circuit.add_box(box1)
        else: # both none
            print("Creating new circuit")
            new_circuit = Circuit()
            new_circuit.add_box(box1)
            new_circuit.add_box(box2)
            circuits.append(new_circuit)
            print(f"Created new circuit {new_circuit}")
        print(f"Updated circuits {circuits}")

    print("Total number of circuits: ", len(circuits))
    circuits.sort(reverse=True)
    sizes = [len(x.boxes) for x in circuits]
    print(math.prod(sizes[:3]))
    # Sorting Connections by length
    # Iterate 1000 shortest
      # if one box already in circuit add other box to circus
    # Sort circuits by size
    # sum largest 3