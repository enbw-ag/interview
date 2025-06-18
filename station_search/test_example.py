import unittest

from main import num_distinct_visited_positions

EXAMPLE = """
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
""".strip()


class TestStationSearch(unittest.TestCase):
    def test_example(self):
        self.assertEqual(num_distinct_visited_positions(EXAMPLE), 41)


if __name__ == "__main__":
    unittest.main()
