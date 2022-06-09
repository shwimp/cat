import os
import sys

from carte import Carte

def get_map(file_path) -> list:
    with open(file_path, "r") as file:
        raw_map = file.read()
    map = raw_map.split("\n")
    clean_map = []
    for elem in map:
        if elem[0] is not "#":
            clean_map.append(elem.split(" - "))
    return clean_map


def main(file_path) -> None:
    map = get_map(file_path)
    carte = Carte(map)
    carte.execute_orders()


if __name__ == "__main__":
    path = sys.argv[1:]
    if len(path) != 1:
        raise Exception("specify the file path")
    if not os.path.exists(path[0]):
        raise Exception("the file does not exist")
    if not os.path.isfile(path[0]):
        raise Exception("this is not a file")
    main(path[0])