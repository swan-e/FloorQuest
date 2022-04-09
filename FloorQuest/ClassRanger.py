from ClassMain import ClassMain


class Pet:
    def __init__(self, pet):
        self.pet = pet


class Ranger(ClassMain):
    def __init__(self, name, clasS, weapon, hp, atk_pwr, pet):
        super().__init__(name, clasS, weapon, hp, atk_pwr)
        self.pet = Pet(pet)

    def get_description_ranger(self):
        class_desc = f"\n {self.name} \n Class:{self.clasS} Weapon:{self.weapon} HP:{self.hp} ATK:{self.atk_pwr} PET:{self.pet}"
        return class_desc.title()