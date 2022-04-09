class ClassMain():
    def __init__(self, name, clasS, weapon, hp, atk_pwr):
        self.name = name
        self.clasS = clasS
        self.weapon = weapon
        self.hp = hp
        self.atk_pwr = atk_pwr

    def get_description(self):
        class_desc = f"\n {self.name} \n Class:{self.clasS} Weapon:{self.weapon} HP:{self.hp} ATK:{self.atk_pwr}"
        return class_desc.title()