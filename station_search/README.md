# Python Exercise: Searching a Station

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

* if there is a charging station **in front of you, you turn 90 degrees clockwise**
* otherwise, you **take one step forward**

In the given example, you drive straight upwards until you reach the uppermost station (in this case, an Alpitronic Hypercharger).

```
....#.....
....^....#
....X.....
..#.X.....
....X..#..
....X.....
.#..X.....
........#.
#.........
......#...
```

An `X` marks already visited positions.
Sadly, your token is not authenticated, so you turn right and drive until you reach the next station (a Keba P30).
```
....#.....
....XXXX>#
....X.....
..#.X.....
....X..#..
....X.....
.#..X.....
........#.
#.........
......#...
```

Regrettably, the grid connection does not supply enough power for all connected vehicles to be charging with sufficient power. You turn right, and drive straight downwards until you reach a ChargeHere TwinCharger.

```
....#.....
....XXXXX#
....X...X.
..#.X...X.
....X..#X.
....X...X.
.#..X...v.
........#.
#.........
......#...
```

Shockingly, someone cut and took the 11m long charging cable. This process takes you through most of Germany, until reach its south border:

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

This example amounts to **41 distinct positions** (`X`s).

Given a different station map and initial position at `inputs/puzzle_map.txt`, predict the path of your vehicle.
**How many distinct positions will you visit before you leave the map?**

You should use **pure Python (including the standard library) without additional dependencies**.
Please, **do not use Copilot, ChatGPT** or equivalent products.

You can use
```shell
python3 test_example.py
```
to run a test that covers the described example. Feel free to extend the tests.

Your program should be callable from the command line and receive the puzzle input as the first argument:
```shell
python3 main.py inputs/puzzle_map.txt
```
It should determine the number of positions of the larger puzzle and print it to stdout.

