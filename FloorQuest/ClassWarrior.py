from ClassMain import ClassMain


class Warrior(ClassMain):
    def __init__(self, name, clasS, weapon, hp, atk_pwr):
        super().__init__(name, clasS, weapon, hp, atk_pwr)

    def get_description_warrior(self):
        class_desc = f"\n {self.name} \n Class:{self.clasS} Weapon:{self.weapon} HP:{self.hp} ATK:{self.atk_pwr}"
        return class_desc.title()