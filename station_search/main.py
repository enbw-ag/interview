from pathlib import Path
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("map_file", type=Path, help="text file with map input")
    args = parser.parse_args()
    station_map = args.map_file.read_text()

    n = num_distinct_visited_positions(station_map)
    print(f"You will visit {n} distinct positions")


def num_distinct_visited_positions(station_map: str) -> int:
    return 0


if __name__ == "__main__":
    main()
