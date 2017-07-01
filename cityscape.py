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
WINDOWS = ["@"]
TRAP_DOORS = ["-"]
LADDERS = ["#"]
AIR = [" "]

ELEVATOR_ENTRANCES = ["^", "v"]
ELEVATOR_EXITS = ["<", ">"]

END = ["$"]


def is_ground(line):
    # if len(line) <= 1:
    #     return False

    # wall = False

    # for char in line:
    #     if char in WALLS:
    #         wall = not wall
    #   elif not wall and char not in GROUND:
    #         return False
    # return True

    return line[0] in GROUND or line[0] in DOORS

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
        self.trap_fall = True
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
                    if self.in_building:
                        l += "&"
                    else:
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

                do_x_move = False
                self.x += self.x_move

                if source[self.y][self.x] in TRAP_DOORS:
                    self.in_building = False
                    self.trap_fall = False

            if cur in LADDERS:
                do_x_move = False

                self.y -= 1
                while source[self.y][self.x] in LADDERS:
                    self.y -= 1

                if source[self.y][self.x] in TRAP_DOORS:
                    self.in_building = False
                    self.trap_fall = False
                    # self.y -= 1

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
                if self.trap_fall:
                    self.y += 1
                    do_x_move = False
                else:
                    self.trap_fall = True

            elif cur in ELEVATOR_ENTRANCES:
                do_x_move = False

                if cur == "^":
                    y_inc = -1
                elif cur == "v":
                    y_inc = 1

                self.y += y_inc
                while source[self.y][self.x] not in ELEVATOR_EXITS:
                    self.y += y_inc

                # can be optimized
                if source[self.y][self.x] == ">":
                    self.x_move = 1
                elif source[self.y][self.x] == "<":
                    self.x_move = -1

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

            elif cur in TRAP_DOORS:
                if self.trap_fall:
                    self.in_building = True
                    self.y += 1
                    do_x_move = False
                else:
                    self.trap_fall = True

            elif cur in AIR:
                drop()
            else:
                pass

        if self.health <= 0:
            return False

        if do_x_move:
            self.x += self.x_move

        return True

cityscape = Cityscape()
cityscape.walk()
