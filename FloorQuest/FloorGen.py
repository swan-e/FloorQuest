class FM:
    def __init__(self, size, monsters, items):
        self.size = size
        self.monsters = monsters
        self.items = items

    def get_map_info(self):
        map_name = f"This map is {self.size} size, with {self.monsters}, you will need {self.items}"
        return map_name.title()