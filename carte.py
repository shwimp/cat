import os

class Carte(object):
    """
    """

    def __init__(self, map):
        """_summary_

        Args:
            map (_type_): _description_
        """
        self.compass = ['N', 'E', 'S', 'O']
        self.map = map
        self.x_size = 0
        self.y_size = 0
        self.map_array = []
        self.draw_map()
        self.adventurers = {}
        self.get_adv_info()

    def get_adv_info(self):
        """_summary_
        """
        for elem in self.map:
            if elem[0] == "A":
                name = elem[1]
                x = int(elem[2])
                y = int(elem[3])
                self.check_position(x, y, name)
                direction = elem[4]
                move = elem[5]
                self.adventurers[name] = {"x": x, "y": y, "direction": direction, "move": move, "treasures": 0}

    def check_position(self, x, y, name):
        """_summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_
            name (_type_): _description_

        Raises:
            Exception: _description_
        """
        if self.map_array[y][x] == "M":
            raise Exception(f"the adventurer {name} is on a mountain. choose an other start position.")

    def draw_map(self):
        """_summary_
        """
        self.create_map()
        self.add_mountain()
        self.add_treasure()
    
    def create_map(self):
        """_summary_
        """
        for elem in self.map:
            if elem[0] == "C":
                self.x_size = int(elem[1])
                self.y_size = int(elem[2])
                for i in range(self.y_size):
                    self.map_array.append(["."] * self.x_size)

    
    def add_mountain(self):
        """_summary_
        """
        for elem in self.map:
            if elem[0] == "M":
                x = int(elem[1])
                y = int(elem[2])
                self.map_array[y][x] = "M"

    
    def add_treasure(self):
        """_summary_
        """
        for elem in self.map:
            if elem[0] == "T":
                x = int(elem[1])
                y = int(elem[2])
                nb_t = int(elem[3])
                self.map_array[y][x] = nb_t
    
    def execute_orders(self):
        """_summary_

        Raises:
            Exception: _description_
        """
        for charac in self.adventurers:
            perso = self.adventurers[charac]
            for order in perso["move"]:
                if order == "A":
                    self.move_on(perso)
                elif order == "D":
                    self.turn_right(perso)
                elif order == "G":
                    self.turn_left(perso)
                else:
                    raise Exception(f"the order {order} does not exist")

    def check_treasure(self, perso):
        """_summary_

        Args:
            perso (_type_): _description_
        """
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
        """_summary_

        Args:
            perso (_type_): _description_
        """
        index = self.compass.index(perso["direction"])
        perso["direction"] = self.compass[index + 1] if index < len(self.compass) - 1 else self.compass[0]

    def turn_left(self, perso):
        """_summary_

        Args:
            perso (_type_): _description_
        """
        index = self.compass.index(perso["direction"])
        perso["direction"] = self.compass[index - 1]
    
    def create_answer(self):
        """_summary_
        """
        answer = ""
        ln_map = len(self.map)
        for idx, elem in enumerate(self.map):
            if elem[0] == "T":
                elem[3] = str(self.map_array[int(elem[2])][int(elem[1])])
            elif elem[0] == "A":
                charac = self.adventurers[elem[1]]
                elem[2] = str(charac["x"])
                elem[3] = str(charac["y"])
                elem[4] = charac["direction"]
                elem[5] = str(charac["treasures"])
            if elem[0] != "#":
                answer += " - ".join(elem)
                if idx < ln_map - 1:
                    answer += "\n"
        file = "answer.txt"
        if os.path.exists(file):
            os.remove(file)
        with open(file, "w") as f:
            f.write(answer)
