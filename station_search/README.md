# Python Exercise: Searching a Station

## Exercise

You are given a text file that represents a map of charging stations (indiciated by `#`) and the initial position and direction of your electric vehicle (indicated by `^`):

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

Unfortunately, all charging stations are either occupied or non-functional, but you keep trying.

Your electric vehicle drives by the following protocol:

* if there is a charging station in front of you, you turn 90 degrees clockwise
* otherwise, you take one step forward

In the given example, you drive straight until you reach the uppermost station (in this case, an Alpitronic Hypercharger).

```
----
....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
```

Sadly, your token is not authenticated, so you turn right and drive until you reach the next station (a Keba P30).
```
....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
```

Regrettably, the grid connection does not supply enough power for all connected vehicles to be charging with sufficient power. You turn right, and drive straight until you reach a ChargeHere TwinCharger.

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
```

Shockingly, someone cut and took the 11m long charging cable. This process takes you through most of Germany, until reach its south border:

```
....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
```

On your way (including your starting position), you have visited many interesting places:

```
....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
```

This example amounts to **41 distinct positions**

## Part 1
Given a different station map and initial position at `inputs/puzzle_map.txt`, predict the path of your vehicle.
**How many distinct positions will you visit before you leave the map?**

You should use pure Python (including the standard library) without additional dependencies.

## Running tests & main

You can use
```shell
python3 test.py
```
to run a test that covers the described example.

And use
```shell
python3 main.py inputs/puzzle_map.txt
```
to determine the number of positions of the larger puzzle.

Feel free to modify `main.py` and `test.py` as needed.

## Optional Part 2

You have the chance to install one additional defective charging station and cause an infinite loop.

In the previous example, there are 6 options:

Option one:

```
....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...
```

Option two:

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...
```

Option three:

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...
```

Option four:

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...
```

Option five:

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...
```
Option six:

```
....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..
```

Given a different station map and initial position at `inputs/puzzle_map.txt`, determine
**how many distinct locations in the map will cause infinite loops?**
