
from unicodedata import name


class Carte(object):

    def __init__(self, map):
        self.compass = ['N', 'E', 'S', 'O']
        self.map = map
        self.x_size = 0
        self.y_size = 0
        self.map_array = []
        self.draw_map()
        self.adventurers = {}
        self.get_adv_info()

    def get_adv_info(self):
        for elem in self.map:
            if elem[0] == "A":
                name = elem[1]
                x = int(elem[2])
                y = int(elem[3])
                self.check_position()
                direction = elem[4]
                move = elem[5]
                self.adventurers[name] = {"x": x, "y": y, "direction": direction, "move": move, "treasures": 0}

    def check_position(self):
        pass

    def draw_map(self):
        self.create_map()
        self.add_mountain()
        self.add_treasure()
    
    def create_map(self):
        for elem in self.map:
            if elem[0] == "C":
                self.x_size = int(elem[1])
                self.y_size = int(elem[2])
                for i in range(self.y_size):
                    self.map_array.append(["."] * self.x_size)

    
    def add_mountain(self):
        for elem in self.map:
            if elem[0] == "M":
                x = int(elem[1])
                y = int(elem[2])
                self.map_array[y][x] = "M"

    
    def add_treasure(self):
        for elem in self.map:
            if elem[0] == "T":
                x = int(elem[1])
                y = int(elem[2])
                nb_t = int(elem[3])
                self.map_array[y][x] = nb_t
    
    def execute_orders(self):
        for charac in self.adventurers:
            perso = self.adventurers[charac]
            for order in perso["move"]:
                print(order)
                if order == "A":
                    self.move_on(perso)
                elif order == "D":
                    self.turn_right(perso)
                elif order == "G":
                    self.turn_left(perso)
                else:
                    raise Exception(f"the order {order} does not exist")
                print(perso)
                print(self.adventurers)

    def check_treasure(self, perso):
        place = self.map_array[perso["y"]][perso["x"]]
        if type(place) is int and place != 0:
            self.map_array[perso["y"]][perso["x"]] -= 1
            perso["treasures"] += 1

    def move_on(self, perso):
        direction = perso["direction"]
        if direction not in self.compass:
            raise Exception(f"the direction {direction} does not exist")
        if direction == "N":
            if perso["y"] != 0:
                if self.map_array[perso["y"] - 1][perso["x"]] != "M":
                    perso["y"] -= 1
                    self.check_treasure(perso)
        elif direction == "E":
            if perso["x"] < self.x_size - 1:
                if self.map_array[perso["y"]][perso["x"] + 1] != "M":
                    perso["x"] += 1
                    self.check_treasure(perso)
        elif direction == "S":
            if perso["y"] < self.y_size - 1:
                if self.map_array[perso["y"] + 1][perso["x"]] != "M":
                    perso["y"] += 1
                    self.check_treasure(perso)
        elif direction == "O":
            if perso["x"] != 0:
                if self.map_array[perso["y"]][perso["x"] - 1] != "M":
                    perso["x"] -= 1
                    self.check_treasure(perso)

    def turn_right(self, perso):
        index = self.compass.index(perso["direction"])
        perso["direction"] = self.compass[index + 1] if index < len(self.compass) - 1 else self.compass[0]

    def turn_left(self, perso):
        index = self.compass.index(perso["direction"])
        perso["direction"] = self.compass[index - 1]