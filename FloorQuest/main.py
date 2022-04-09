import random
from Floor_1 import FloorMapping1
import Floor_1
from ClassMain import ClassMain
from ClassRanger import Ranger
from ClassWarrior import Warrior

global inventory


def split(currentRoom):
    return [char for char in currentRoom]


# showstatus is the default status given to the user based on where they are located, this sets up the base
def showStatus(currentRoom):
    print('---------------------------')
    print('You are in ' + currentRoom)

    # this prints an item if present
    if "item" in Floor_1.roomsfloor1[currentRoom]:
        print('You see a ' + Floor_1.roomsfloor1[currentRoom]['item'])
    print("Type 'actions' to get list of actions")
    print("---------------------------")




def main():
    print("main")
    file_path_1 = 'Floor1.txt'

    # inventory
    inventory = []
    currentRoom = 'F1-14'
    currentRoomX = 1
    currentRoomY = 12
    newgamemap = []
    gamemap = Floor_1.get_list()

    x = 2
    print("Welcome traveler to RNGRPG.")
    while x > 1:
        classchoose = input("What class would you like to play? (Ranger, Warrior) ")
        # both these if blocks deal with the user choosing which class to play at the start
        if classchoose == "Ranger":
            rangername = input("What would you like to name your character? ")
            basic_ranger = Ranger(rangername, 'Ranger', 'bow', 90, 30, 'none')
            print(basic_ranger.get_description())
            inventory += ['Bow']
            x = 0

        if classchoose == "Warrior":
            warriorname = input("What would you like to name your character? ")
            basic_warrior = Warrior(warriorname, 'Warrior', 'mace', 130, 50)
            print(basic_warrior.get_description())
            inventory += ['Mace']
            x = 0

    # This is the map info
    map_1 = FloorMapping1('11 by 7', 'Goblin', 'Sword and Shield', 'Mondstadt')

    end_game = 1
    while end_game > 0:
        showStatus(currentRoom)

        move = ''
        while move == '':
            move = input('>')

        # taking the first word in a given response
        move = move.lower().split()

        # prints class info
        if move[0] == "class":
            if classchoose == "Ranger":
                print(basic_ranger.get_description_ranger())
            if classchoose == "Warrior":
                print(basic_warrior.get_description_warrior())

        # prints inventory if prompted
        if move[0] == "inventory":
            print('Inventory : ' + str(inventory))

        # prints info of map if prompted
        if move[0] == "info":
            print(map_1.get_map_info())

        # prints dictionary of actions
        if move[0] == "actions":
            moves_dictionary = {
                "Movement": "go north, go east, go south, go west",
                "Information": "map, inventory, class, info",
                "Actions": "get (item)"
            }
            print(moves_dictionary)

        # prints movement if possible
        if move[0] == 'go':
            if move[1] in Floor_1.roomsfloor1[currentRoom]:
            # this is my pride and joy, my love of code
            # using math to translate the Floor_1 floor map 2d list (array) to actual coordinates
            # made me feel accomplished for tying in other aspects of my education
            # I learned 2d arrays in Java, so also using that knowledge within my python code was cool
                currentRoom = Floor_1.roomsfloor1[currentRoom][move[1]]
                # if len(split(currentRoom)) == 5:
                mapx = split(currentRoom[3])
                map_x = mapx[0]
                mapy = split(currentRoom[4])
                map_y = mapy[0]

                currentRoomX = int(map_x)
                currentRoomY = int(map_y) * 3


            else:
                print('You can\'t go that way!')

            # prints map if prompted
        if move[0] == "map":
            gmap = Floor_1.get_list()
            gmap[currentRoomX][currentRoomY] = 1
            for x in range(0, len(gmap)):
                for y in range(0, len(gmap[x])):
                    print(gmap[x][y], end='')
                print("")

        if move[0] == 'get':
            # if the room contains an item, and the item is the one they want to get
            if "item" in Floor_1.roomsfloor1[currentRoom] and "Sword" in Floor_1.roomsfloor1[currentRoom]['item']:
                # add the item to inventory
                inventory += ["Sword"]
                print("Sword" + ' got!')
                # delete the item
                del Floor_1.roomsfloor1[currentRoom]['item']

            elif "item" in Floor_1.roomsfloor1[currentRoom] and "Shield" in Floor_1.roomsfloor1[currentRoom]['item']:
                # add the item to inventory
                inventory += ["Shield"]
                print("Shield" + ' got!')
                # delete the item
                del Floor_1.roomsfloor1[currentRoom]['item']

            elif "item" in Floor_1.roomsfloor1[currentRoom] and "Key" in Floor_1.roomsfloor1[currentRoom]['item']:
                # add the item to inventory
                inventory += ["Key"]
                print("Key" + ' got!')
                # delete the item
                del Floor_1.roomsfloor1[currentRoom]['item']

            elif "item" in Floor_1.roomsfloor1[currentRoom] and 'Treasure' in Floor_1.roomsfloor1[currentRoom]['item']:
                if "Key" in inventory:
                    # add the item to inventory
                    inventory += ["Treasure"]
                    print("Treasure" + ' got!')
                    inventory.remove("Key")
                    # delete the item
                    del Floor_1.roomsfloor1[currentRoom]['item']
                else:
                    print("You can't open the treasure chest.")

            elif "item" in Floor_1.roomsfloor1[currentRoom] and 'pet' in Floor_1.roomsfloor1[currentRoom]['item']:
                # if class is ranger, then can get pet
                if classchoose == "Ranger":
                    choose_pet = ['Dog', 'Cat', 'Wolf', 'Pig']
                    print(choose_pet)
                    choice = input("What pet do you want to take with you on your journey? ")
                    if choice == "Dog":
                        print("Woof. You companion barks enthusastically")
                        basic_ranger.pet = "Dog"
                        inventory += [choose_pet[0]]
                    if choice == "Cat":
                        print("Meow")
                        basic_ranger.pet = "Cat"
                        inventory += [choose_pet[1]]
                    if choice == "Wolf":
                        print("A fierce companion joins your party")
                        basic_ranger.pet = "Wolf"
                        inventory += [choose_pet[2]]
                    if choice == "Pig":
                        print("Oink. You stare at the future bacon")
                        basic_ranger.pet = "Pig"
                        inventory += [choose_pet[3]]
                    del Floor_1.roomsfloor1[currentRoom]['item']
                else:
                    print("You are not the ranger class, pet ran away")
                    del Floor_1.roomsfloor1[currentRoom]['item']

        # if item is monster in the room, this fight sequence pops up
        if "item" in Floor_1.roomsfloor1[currentRoom] and 'monster' in Floor_1.roomsfloor1[currentRoom]['item']:
            # here are all the variables
            monster_hp = 30
            remaining_monster_hp = "Monster has " + str(monster_hp) + " left"
            monster_dead = "You have killed the monster"
            random_int = random.randint(1, 20)
            del Floor_1.roomsfloor1[currentRoom]['item']

            print("You see a goblin with 30 hp. What do you want to do?")
            if classchoose == "Ranger":
                y1 = 1
                while y1 > 0:
                    print("")
                    fight_or_run = input("(Fight, Run) ")
                    print("")
                    print(fight_or_run)
                    if fight_or_run == "Fight":
                        if basic_ranger.hp > 0:
                            if "Dog" in inventory:
                                dog_random = random.randint(1, 50)
                                if dog_random > 30:
                                    print(
                                        "You draw your bow and land a hit to the monsters right shoulder. Your dog finishes it off with a clean bite. You have killed the monster!")
                                    print("")
                                    print("You did " + str(dog_random) + " damage")
                                    print(monster_dead)
                                    monster_hp = 0
                                    y1 = 0
                                else:
                                    print("You do " + str(dog_random) + " damage")

                            if "Cat" in inventory:
                                cat_random = random.randint(1, 45)
                                if cat_random > 30:
                                    print("")
                                    print("You did " + str(cat_random) + " damage")
                                    print(monster_dead)
                                    monster_hp = 0
                                    y1 = 0
                                else:
                                    print("You do " + str(cat_random) + " damage")

                            if "Wolf" in inventory:
                                wolf_random = random.randint(1, 60)
                                if wolf_random > 30:
                                    print("Your wolf eats the goblin whole. You did nothing")
                                    print("")
                                    print("You did " + str(wolf_random) + " damage")
                                    print(monster_dead)
                                    monster_hp = 0
                                    y1 = 0
                                else:
                                    print("You do " + str(wolf_random) + " damage")

                            if "Pig" in inventory:
                                pig_random = random.randint(1, 26)
                                if pig_random > 30:
                                    print("You draw your bow and land a hit to the monsters heart.")
                                    print("")
                                    print("You did " + str(pig_random) + " damage")
                                    print(monster_dead)
                                    y1 = 0
                                else:
                                    print("Your pig gets chopped up. The goblin runs away, leaving you with bacon")
                                    inventory.remove("Pig")
                                    basic_ranger.pet = "Bacon"
                                    inventory += ["Bacon"]
                                    monster_hp = 0
                                    y1 = 0
                            if random.randint(1, 30) > 25:
                                print("You pull your bow and sling an arrow at the monster. The monster has been killed!")
                                print(monster_dead)
                                monster_hp = 0
                                y1 = 0

                            if monster_hp > 0:
                                basic_ranger.hp = basic_ranger.hp - random.randint(1, 30)
                                monster_attack = 90 - basic_ranger.hp
                                print("The monster did " + str(monster_attack) + " total damage")
                                print("Your HP: " + str(basic_ranger.hp))

                        if basic_ranger.hp <= 0:
                            print(
                                "You died [SECRET ENDING: CONGRATUlATIONS, YOU MANAGED TO GET SO LUCKY TO NOT ROLL NUMBERS TO KILL THE GOBLIN WHILE ALSO DIMINISHING YOUR HEALTH]")
                            y1 = 0
                            end_game = 0

                    if fight_or_run == "Run":
                        if random_int > 15:
                            print("You roll an " + str(random_int) + ". You succesfully run away")
                            y1 = 0

            if classchoose == "Warrior":
                y2 = 2
                while y2 > 0:
                    print("")
                    fight_or_run = input("(Fight, Run) ")
                    print("")
                    print(fight_or_run)
                    if fight_or_run == "Fight":
                        if basic_warrior.hp > 0:
                            if random.randint(1, 50) > 25:
                                print("You draw your sword and slash the monster. The monster has been killed!")
                                print(monster_dead)
                                monster_hp = 0
                                y2 = 0

                        if basic_warrior.hp <= 0:
                            print(
                                "You died [SECRET ENDING: CONGRATUlATIONS, YOU MANAGED TO GET SO LUCKY TO NOT ROLL NUMBERS TO KILL THE GOBLIN WHILE ALSO DIMINISHING YOUR HEALTH]")
                            y1 = 0
                            end_game = 0

                        if monster_hp > 0:
                            basic_warrior.hp = basic_warrior.hp - random.randint(1, 30)
                            monster_attack = 130 - basic_warrior.hp
                            print("The monster did " + str(monster_attack) + " total damage")
                            print("Your HP: " + str(basic_warrior.hp))

                    if fight_or_run == "Run":
                        if random_int > 15:
                            print("You roll a" + str(random_int) + ". You succesfully run away")
                            y2 = 0
                        else:
                            print("Unsuccessful")

        if currentRoom == 'F1-113':
            print("Congratulations, you have beat the game!")
            end_game = 0


if __name__ == '__main__':
    main()