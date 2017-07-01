# Cityscape
WIP Esoteric 2D programming language

#Tutorial
You are a young gamin just trying to scrap a living. You will do whatever it takes to get some money. When given input, you will start moving on each line that starts with an `_` (ground) or a `:` (door). You will continue searching from each starting position until you have found all your money, or died trying.

You have two states: that of just walking around outside, and that of walking around inside a building. The most important thing you can do while walking outside is enter a building.

##2D Operators

| Name | Syntax | Usage
| - | - | -
| Air | ` ` | If the gamin attempts to walk into air, the gamin drops until he is not longer suspended.
| Ground/Floor | `_` | Allows the gamin to continue walking. If in the `0` index of a line, identifies that as a starting line.
| Door | `:` | The gamin switches from interior to exterior mode, or vice versa. If in the `0` index of a line, identifies that as a starting line.
| Wall | `|` | If the gamin walks into a wall, he turns around.
| Stairs | `/`, `\` | In addition to walking, the gamin also moves up a floor or down a floor, depending on orientation compared to the staircase
| Window | `@` | While walking inside a building, if the gamin encounters a window, he jumps out of it until he hits ground level.
| Trap Door | `-` | If encountered inside a building, the gamin drop a floor without walking. If moved up to by a ladder, stair, or elevator, the gamin moves up the trap door, exiting the building. If encountered outside (usually on top of) a building, the gamin drops a floor without walking, and enters the building.
| Ladder | `#` | When encountered inside a building, the gamin climbs the ladder until he reaches the top of it, then continues moving.
| Elevator Entrances | `^`, `v` | When encountered inside a building, the gamin moves in the appropriate direction until an elevator exit is found, then moves in that direction
| Elevator Exits | `>`, `<` | Identify the location and direction of an elevator exit
| End | `$` | When the gamin reaches the end, he has found the cash for this trip. He continues to the next starting location.
