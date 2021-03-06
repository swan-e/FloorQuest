from FloorGen import FM


class FloorMapping1(FM):
    def __init__(self, size, monsters, items, name_1):
        self.size = size
        self.monsters = monsters
        self.items = items
        self.name_1 = name_1

def get_list():
    gamemap = [

        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '  Rows'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '0', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|   ', '1'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '0', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '   2 '],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '0', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '   3 '],
        ['|', ' ', '|', '0', '|', '|', '0', '|', '|', '3', '|', '|', '0', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '   4 '],
        ['|', ' ', '|', '0', '|', ' ', ' ', ' ', '|', '0', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '   5 '],
        ['|', ' ', '|', '0', '|', ' ', ' ', ' ', '|', '0', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '   6 '],
        ['|', ' ', '|', '3', '|', '|', '0', '|', '|', '0', '|', '|', '0', '|', '|', '0', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', '   7 '],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', 'M', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '   8 '],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '0', '|', '|', '0', '|', '|', '0', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', '   9'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '0', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '  10'],
        ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', 'E', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '  11'],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
    ]

    return gamemap



# this code is for printing the dictionary with the items
roomsfloor1 = {
    'F1-14': {
        'south': 'F1-24',
    },

    'F1-24': {
        'north': 'F1-14',
        'south': 'F1-34'
    },

    'F1-34': {
        'north': 'F1-24',
        'south': 'F1-44'
    },

    'F1-44': {
        'north': 'F1-34',
        'west': 'F1-43'
    },

    'F1-43': {
        'west': 'F1-42',
        'south': 'F1-53',
        'item': 'Sword'
    },

    'F1-42': {
        'west': 'F1-41',
        'east': 'F1-43'
    },

    'F1-41': {
        'south': 'F1-51',
        'east': 'F1-42',
        'item': 'Key'

    },

    'F1-53': {
        'north': 'F1-43',
        'south': 'F1-63'
    },

    'F1-51': {
        'north': 'F1-41',
        'south': 'F1-61'
    },

    'F1-63': {
        'north': 'F1-53',
        'south': 'F1-73',
        'item': 'pet'
    },

    'F1-61': {
        'north': 'F1-51',
        'south': 'F1-71'
    },

    'F1-75': {
        'west': 'F1-74',
    },

    'F1-74': {
        'west': 'F1-73',
        'east': 'F1-75',
        'south': 'F1-84'
    },

    'F1-73': {
        'west': 'F1-72',
        'east': 'F1-74',
        'north': 'F1-63'
    },

    'F1-72': {
        'west': 'F1-71',
        'east': 'F1-73'
    },

    'F1-71': {
        'east': 'F1-72',
        'north': 'F1-61',
        'item': 'Shield'
    },

    'F1-84': {
        'north': 'F1-74',
        'south': 'F1-94',
        'item': 'monster'
    },

    'F1-95': {
        'west': 'F1-94',
        'item': 'Treasure'
    },

    'F1-94': {
        'west': 'F1-93',
        'east': 'F1-95',
        'north': 'F1-84'
    },

    'F1-93': {
        'east': 'F1-94',
        'south': 'F1-103'
    },

    'F1-103': {
        'north': 'F1-93',
        'south': 'F1-113'
    },
}


