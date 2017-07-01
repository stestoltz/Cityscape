import re

source = open("source.sky").read().split("\n")

print(source)

length = max(len(line) for line in source)

print(length)

ground = []

GROUND = ["_"]
FLOOR = ["_"]
WALLS = ["|"]
DOORS = [":"]
STAIRS = ["/", "\\"]
WINDOWS = ["#"]
TRAP_DOORS = ["-"]
AIR = [" "]

END = ["$"]


def is_ground(line):
    if len(line) <= 1:
        return False

    wall = False

    for char in line:
        if char in WALLS:
            wall = not wall
        elif not wall and char not in GROUND:
            return False
    return True


i = 0
for line in source:
    line = line.ljust(length)
    if is_ground(line):
        ground.append(i)
    i += 1


class Cityscape:
    def __init__(self):
        self.in_building = False
        self.x_move = 1
        self.x = 0
        self.y = 0
        self.HEALTH = 99
        self.health = self.HEALTH

    def walk(self):
        print(ground)

        for start in ground:
            self.y = start
            self.x = 0

            print("-" * (length + 1))
            while self.move(start):
                print("-" * (length + 1))
            print("-" * (length + 1))

        print("Health: " + str(self.health) + "/" + str(self.HEALTH))

    def move(self, start):
        def drop():
            nonlocal do_x_move
            if self.y < start:
                do_x_move = False
                while source[self.y][self.x] in AIR and self.y < start:
                    self.y += 1
                    self.health -= 1

        cur = source[self.y][self.x]

        do_x_move = True

        # FIXME: with actual code
        for j in range(len(source)):
            l = ""
            s = source[j]
            for k in range(len(s)):
                if j == self.y and k == self.x:
                    l += "*"
                else:
                    l += s[k]
            print(l)

        if cur in END:
            return False

        if self.in_building:
            if cur in STAIRS:

                # can be optimized with index in STAIRS
                if cur == "/":
                    if self.x_move > 0:
                        self.y -= 1
                    elif self.x_move < 0:
                        self.y += 1
                elif cur == "\\":
                    if self.x_move > 0:
                        self.y += 1
                    elif self.x_move < 0:
                        self.y -= 1

            elif cur in WALLS:
                self.x_move = -self.x_move

            elif cur in WINDOWS:
                self.health -= start - self.y
                self.y = start
                self.in_building = False
                do_x_move = False

            elif cur in DOORS:
                self.in_building = False

            elif cur in TRAP_DOORS:
                self.in_building = False
            elif cur in FLOOR:
                pass

            elif cur in AIR:
                drop()

            else:
                # raise NameError("Unknown : " + str(cur))
                pass
        else:
            if cur in DOORS:
                self.in_building = True
            elif cur in AIR:
                drop()
            else:
                pass

        if do_x_move:
            self.x += self.x_move

        return True

cityscape = Cityscape()
cityscape.walk()
