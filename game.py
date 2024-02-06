import random
from itertools import cycle


def get_user_input(question: str, options: list) -> str:
    """
    Return user's picked element from the list options.

    :param question: a string
    :param options: non-empty list
    :precondition: list options is not empty and has at least 1 element
    :precondition: question is a non-empty string
    :postcondition: print out all elements from options with a number index
    :postcondition: convert user's input number into the corresponding element from options
    :postcondition: return user's chosen element from options
    :postcondition: the list argument passed to parameter options will not be changed
    :return: a string that is the user's chosen element from options
    """
    option_list = {str(index): option for index, option in enumerate(options, 1)}
    chose_option = ""
    while not chose_option:
        print("\n{}".format(question))
        for index, option in option_list.items():
            print("{} {}".format(index, option))
        user_input = input("Please enter the number of the option: ").strip()
        if user_input.isdigit() and user_input in option_list:
            chose_option = user_input
        else:
            print("That is not a valid option. Please only enter the number shown in the list.")
    return option_list[chose_option]


def story_opening() -> None:
    """
    Print a welcome message to user.
    """
    print("\nWelcome adventurer! You are a general in BCIT. There have been numerous reports of missing person lately. "
          "You found out it was a vampire named Dracula who has been kidnapping all those people. You decided to go to "
          "Dracula's castle and remove him once and for all. The castle is located at the upper right corner of your "
          "map. Be cautious! There are other dangers lurking around the area!")


def combine(pair: tuple) -> str:
    """
    Return a string that includes the 2 elements in parameter pair.

    :param pair: a non-empty tuple
    :precondition: pair is a tuple with only 2 string elements
    :postcondition: return a string that include the 2 string elements from pair, and a ": " between them
    :return: a string that include the 2 elements from pair

    >>> name = ("Name", "John")
    >>> combine(name)
    'Name: John'
    """
    return "{}: {}".format(pair[0], pair[1])


def make_character(rows: int) -> dict:
    """
    Create character in the form of a dictionary which contains character's information.

    :param rows: an integer
    :precondition: rows is a positive integer larger than 0
    :postcondition: return a dictionary with character's information
    :return: a dictionary with character's information
    """
    name = input("\nPlease enter your name: ")
    classes = {"Warrior": "Well-trained fighter with sword and shield. Warrior has the highest HP and accuracy, but his"
                          " attack is pretty bad.",
               "Thief": "A deadly class that uses daggers to eliminate his targets. Thief has high accuracy and attack,"
                        " but is low on HP.",
               "Mage": "Specialized in destructive magic, mage is the strongest in attack. He can eliminate foes "
                       "instantly if the attack actually lands. Mage has the lowest HP and accuracy in the game.",
               "Illusionist": "All rounded caster, with average stats. There is really nothing special about this guy."}
    class_options = list(map(combine, classes.items()))
    class_chosen = get_user_input("Before you start, please choose your class.", class_options)
    for character_class in classes.keys():
        if character_class in class_chosen:
            class_chosen = character_class
    character_info = {"Name": name, "Level": 1, "Class": class_chosen, "Exp": 0,
                      "Coordinate": [rows - 1, 0], "Ultimate": 2}
    return character_info


def update_class_stats(character: dict) -> None:
    """
    Update character dictionary with class-related information.

    :param character: a non-empty dictionary
    :precondition: character is a dictionary with one "Class" key
    :precondition: the value of "Class" in character must be "Warrior", "Thief", "Mage", or "Illusionist"
    :postcondition: update character with class-related information

    >>> character_info = {"Class": "Warrior"}
    >>> update_class_stats(character_info)
    >>> character_info == {"Class": "Warrior", "Jobs": ["Warrior", "Knight", "Berserker"], "Skills": ["Rising Slash",
    ...                    "Whirlwind", "Berserk mode"], "Exp Needed": [2, 10], "Max HP": 15, "Current HP": 15,
    ...                    "Attack": 1, "Accuracy": 0.9, "Invincible": 0}
    True

    >>> character_info = {"Class": "Thief"}
    >>> update_class_stats(character_info)
    >>> character_info == {"Class": "Thief", "Jobs": ["Thief", "Assassin", "Shadow"], "Skills": ["Assault Dive",
    ...                    "Divine Strike", "Shadow mode"], "Exp Needed": [4, 15], "Max HP": 10, "Current HP": 10,
    ...                    "Attack": 3, "Accuracy": 0.8, "Invincible": 0}
    True
    """
    if character["Class"] == "Warrior":
        class_info = {"Class": "Warrior", "Jobs": ["Warrior", "Knight", "Berserker"],
                      "Skills": ["Rising Slash", "Whirlwind", "Berserk mode"], "Exp Needed": [2, 10],
                      "Max HP": 15, "Current HP": 15, "Attack": 1, "Accuracy": 0.9, "Invincible": 0}
    elif character["Class"] == "Thief":
        class_info = {"Class": "Thief", "Jobs": ["Thief", "Assassin", "Shadow"],
                      "Skills": ["Assault Dive", "Divine Strike", "Shadow mode"], "Exp Needed": [4, 15],
                      "Max HP": 10, "Current HP": 10, "Attack": 3, "Accuracy": 0.8, "Invincible": 0}
    elif character["Class"] == "Mage":
        class_info = {"Class": "Mage", "Jobs": ["Mage", "Enchanter", "Wizard"],
                      "Skills": ["Fire ball", "Thunder Storm", "Ice shield"], "Exp Needed": [2, 10],
                      "Max HP": 8, "Current HP": 8, "Attack": 4, "Accuracy": 0.7, "Invincible": 0}
    else:
        class_info = {"Class": "Illusionist", "Jobs": ["Illusionist", "Mystic", "Mastermind"],
                      "Skills": ["Mind attack", "Terror Claw", "Hypnotize"], "Exp Needed": [3, 12],
                      "Max HP": 12, "Current HP": 12, "Attack": 2, "Accuracy": 0.8, "Invincible": 0}
    for attribute, stats in class_info.items():
        character[attribute] = stats


def make_board(rows: int, columns: int) -> dict:
    """
    Create a rows * columns sized game board in the form of a dictionary.

    :param rows: an integer
    :param columns: an integer
    :precondition: both rows and columns must be integers larger than or equal to 2
    :postcondition: create and return a dictionary with rows * columns key value pairs
    :postcondition: each key in the dictionary is a coordinate tuple
    :postcondition: each value in the dictionary is a single character string which represents the location type
    :return: a dictionary representing the game board
    """
    board = {}
    event_sequence = cycle(["C", "T", "M", "M"])
    for row in range(0, rows):
        for column in range(0, columns):
            random_number = random.randint(1, 100)
            if random_number <= 5:
                location = next(event_sequence)
            else:
                location = "."
            board[(row, column)] = location
    board[(rows - 1, 0)] = "."
    return board


def create_castle(board: dict, columns: int) -> None:
    """
    Create a castle in the upper right corner of board by replacing the values in dictionary board with new characters.

    "X" represents the wall of the castle, and "D" represents the entrance, and "." represents the surroundings.

    :param board: a non-empty dictionary
    :param columns: an integer
    :precondition: columns must be a positive integer that is larger than or equals to 6
    :precondition: board is a dictionary with tuple keys and single character string values
    :precondition: board must represent a game board, and the board must be at least 5 rows X 6 columns in size
    :precondition: the largest column coordinate in board must equal to parameter columns - 1
    :postcondition: update board with new values that represent a castle in the upper right corner

    >>> column_number = 6
    >>> game_board = {(0, 0): ".", (0, 1): ".", (0, 2): ".", (0, 3): ".", (0, 4): ".", (0, 5): ".",
    ...               (1, 0): ".", (1, 1): ".", (1, 2): ".", (1, 3): ".", (1, 4): ".", (1, 5): ".",
    ...               (2, 0): ".", (2, 1): ".", (2, 2): ".", (2, 3): ".", (2, 4): ".", (2, 5): ".",
    ...               (3, 0): ".", (3, 1): ".", (3, 2): ".", (3, 3): ".", (3, 4): ".", (3, 5): ".",
    ...               (4, 0): ".", (4, 1): ".", (4, 2): ".", (4, 3): ".", (4, 4): ".", (4, 5): "."}
    >>> create_castle(game_board, column_number)
    >>> game_board == {(0, 0): ".", (0, 1): "X", (0, 2): "X", (0, 3): "X", (0, 4): "X", (0, 5): "X",
    ...                (1, 0): ".", (1, 1): "X", (1, 2): "X", (1, 3): "X", (1, 4): "X", (1, 5): "X",
    ...                (2, 0): ".", (2, 1): "X", (2, 2): "X", (2, 3): "X", (2, 4): "X", (2, 5): "X",
    ...                (3, 0): ".", (3, 1): "X", (3, 2): "X", (3, 3): "D", (3, 4): "X", (3, 5): "X",
    ...                (4, 0): ".", (4, 1): ".", (4, 2): ".", (4, 3): ".", (4, 4): ".", (4, 5): "."}
    True
    """
    castle_width, castle_height = 5, 4
    castle_door_coordinate = (castle_height - 1, columns - int(castle_width / 2) - 1)
    for row in range(0, castle_height + 1):
        for column in range(columns - castle_width - 1, columns):
            if row == castle_height or column == columns - castle_width - 1:
                board[(row, column)] = "."
            elif (row, column) == castle_door_coordinate:
                board[(row, column)] = "D"
            else:
                board[(row, column)] = "X"


def print_map(rows: int, columns: int, board: dict, character: dict) -> None:
    """
    Print the game map with character position and map legend.

    :param rows: an integer
    :param columns: an integer
    :param board: a non-empty dictionary
    :param character: a non-empty dictionary
    :precondition: rows and columns must be integers that are larger than or equal to 2
    :precondition: board is a dictionary with coordinate tuple keys and single character string values
    :precondition: rows must equal to the largest row coordinate in board minus 1
    :precondition: columns must equal to the largest column coordinate in board minus 1
    :precondition: character is a dictionary with one "Coordinate" key, this key must have a coordinate list value
    :precondition: the coordinate list in character must equals to 1 and only 1 of the coordinate tuple keys in board
    :precondition: the values in the tuple keys in board must be greater than or equals to 0
    :postcondition: the dictionary arguments passed to this function will not be changed
    :postcondition: print a map with that shows all coordinates, the player position and map legend

    >>> row_number = 2
    >>> column_number = 3
    >>> character_info = {"Coordinate": [1, 0]}
    >>> game_board = {(0, 0): ".", (0, 1): ".", (0, 2): ".", (1, 0): ".", (1, 1): ".", (1, 2): "."}
    >>> print_map(row_number, column_number, game_board, character_info)
    <BLANKLINE>
    . . .
    \033[93m$\033[0m . .
    C:Church T:Treasure M:Elite Monster D:Castle Entrance
    >>> character_info == {"Coordinate": [1, 0]}
    True
    >>> game_board == {(0, 0): ".", (0, 1): ".", (0, 2): ".", (1, 0): ".", (1, 1): ".", (1, 2): "."}
    True
    """
    print()
    current_map = []
    character_row = character["Coordinate"][0]
    character_column = character["Coordinate"][1]
    for row in range(rows):
        map_row = [board[(row, column)] for column in range(columns)]
        current_map.append(map_row)
    current_map[character_row][character_column] = "\033[93m$\033[0m"
    for row in current_map:
        print(" ".join(row))
    print("C:Church T:Treasure M:Elite Monster D:Castle Entrance")


def get_command() -> str:
    """
    Return user's chosen command from the list of available commands.

    Available commands are "Up", "Down", "Left", "Right", "Check Map", "Check Status" and "Quit Game".

    :postcondition: print a list of command and get user's input
    :postcondition: return a string representing user's chosen command
    :return: a string representing user's chosen command
    """
    ask_for_command = "What do you want to do?"
    command_options = ["Up", "Down", "Left", "Right", "Check Map", "Check Status", "Quit Game"]
    entered_command = get_user_input(ask_for_command, command_options)
    return entered_command


def get_vector(move_command: str) -> tuple:
    """
    Convert a move command into equivalent vector.

    Command "Up", "Down", "Left",and "Right" corresponds to vector (0, -1), (0, 1), (-1, 0) and (1, 0) respectively.

    :param move_command: a string
    :precondition: move_command must only be "Up", "Down", "Left",or "Right"
    :postcondition: return a tuple representing the vector of move_command
    :return: a tuple representing the vector of move_command

    >>> move_direction = "Up"
    >>> get_vector(move_direction)
    (-1, 0)

    >>> move_direction = "Right"
    >>> get_vector(move_direction)
    (0, 1)
    """
    if move_command == "Up":
        vector = (-1, 0)
    elif move_command == "Down":
        vector = (1, 0)
    elif move_command == "Left":
        vector = (0, -1)
    else:
        vector = (0, 1)
    return vector


def validate_move(board: dict, character: dict, direction: tuple) -> bool:
    """
    Check if user's move is valid. Return True if move is valid, False if move is invalid.

    A move is only valid if new coordinate is within board and not a castle wall.

    :param board: a dictionary
    :param character: a dictionary
    :param direction: a tuple
    :precondition: board is a dictionary with coordinate tuple keys and single character string values
    :precondition: character is a dictionary with one "Coordinate" key, this key must have a coordinate list value
    :precondition: the coordinate list in character must equals to 1 and only 1 of the coordinate tuple keys in board
    :precondition: the values in the tuple keys in board must be greater than or equals to 0
    :precondition: direction can only be (0, -1), (0, 1), (-1, 0) or (1, 0)
    :postcondition: return a boolean that determines if user's move is valid
    :postcondition: board and character will not be changed
    :return: a boolean that determines if user's move is valid

    >>> game_board = {(0, 0): ".", (0, 1): ".", (0, 2): ".", (1, 0): ".", (1, 1): ".", (1, 2): "."}
    >>> character_info = {"Coordinate": [0, 0]}
    >>> vector = (1, 0)
    >>> validate_move(game_board, character_info, vector)
    True
    >>> game_board == {(0, 0): ".", (0, 1): ".", (0, 2): ".", (1, 0): ".", (1, 1): ".", (1, 2): "."}
    True
    >>> character_info == {"Coordinate": [0, 0]}
    True

    >>> game_board = {(0, 0): ".", (0, 1): ".", (0, 2): ".", (1, 0): ".", (1, 1): ".", (1, 2): "."}
    >>> character_info = {"Coordinate": [0, 2]}
    >>> vector = (0, 1)
    >>> validate_move(game_board, character_info, vector)
    False
    >>> game_board == {(0, 0): ".", (0, 1): ".", (0, 2): ".", (1, 0): ".", (1, 1): ".", (1, 2): "."}
    True
    >>> character_info == {"Coordinate": [0, 2]}
    True
    """
    new_coordinate = character["Coordinate"][0] + direction[0], character["Coordinate"][1] + direction[1]
    is_move_valid = new_coordinate in board and board[new_coordinate] != "X"
    return is_move_valid


def move_character(character: dict, direction: tuple) -> None:
    """
    Update character's coordinate after movement.

    :param character: a dictionary
    :param direction: a tuple
    :precondition: character should be a dictionary with one "Coordinate" key
    :precondition: the value of "Coordinate" in character must be a list with 2 integer elements that are >= 0
    :precondition: direction can only be (0, -1), (0, 1), (-1, 0) or (1, 0)
    :postcondition: update the value of "Coordinate" in character to new coordinate after movement

    >>> character_info = {"Coordinate": [0, 0]}
    >>> chose_direction = (0, 1)
    >>> move_character(character_info, chose_direction)
    >>> character_info ==  {"Coordinate": [0, 1]}
    True
    """
    character["Coordinate"][0] += direction[0]
    character["Coordinate"][1] += direction[1]


def check_current_location(board: dict, character: dict) -> str:
    """
    Return the single character that represents current location.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board is a dictionary with coordinate tuple keys and single character string values
    :precondition: character is a dictionary with one "Coordinate" key, this key must have a coordinate list value
    :precondition: the coordinate list in character must equals to 1 and only 1 of the coordinate tuple keys in board
    :precondition: the values in the tuple keys in board must be greater than or equals to 0
    :postcondition: return the single character string that represents current location
    :postcondition: board and character will not be changed
    :return: a string with a single character that represents current location

    >>> game_board = {(0, 0): "D", (0, 1): ".", (1, 0): ".", (1, 1): "."}
    >>> character_info = {"Coordinate": [0, 0]}
    >>> check_current_location(game_board, character_info)
    'D'
    >>> game_board == {(0, 0): "D", (0, 1): ".", (1, 0): ".", (1, 1): "."}
    True
    >>> character_info == {"Coordinate": [0, 0]}
    True
    """
    location = board[character["Coordinate"][0], character["Coordinate"][1]]
    return location


def check_for_foe() -> bool:
    """
    Check if user has encountered a foe. Return True if user has encountered a foe, otherwise return False.

    :postcondition: generate a random number and use it to determine if user has encountered a foe
    :postcondition: return True if random number is less than or equals to 25, False if it is not
    :return: a boolean that determines if user has encountered a foe
    """
    foe_encounter = random.randint(1, 100) <= 25
    return foe_encounter


def make_foe(character: dict, current_location: str) -> dict:
    """
    Create foe in the form of a dictionary which contains foe's information.

    :param character: a dictionary
    :param current_location: a string
    :precondition: character is a dictionary with a "Level" key, this key has an integer value that is larger than 0
    :precondition: current_location is a single character string
    :postcondtion: print a message introducing the foe character encoutered
    :postcondition: return a dictionary which contains foe's information
    :postcondition: dictionary character will not be changed
    :return: a dictionary which contains foe's information

    >>> character_info = {"Level": 2}
    >>> location = "M"
    >>> make_foe(character_info, location)
    <BLANKLINE>
    You have awakened a level 3 Cyclops!
    {'Name': 'Cyclops', 'Current HP': 20, 'Attack': 4, 'Skill': 'Ground Slam', 'Level': 3, 'Accuracy': 0.6}
    >>> character_info == {"Level": 2}
    True
    """
    if current_location == ".":
        foe_level = random.randint(1, character["Level"])
        if random.randint(1, 10) <= 5:
            print("\nYou encountered a level {} Barbarian!".format(foe_level))
            foe = {"Name": "Barbarian", "Current HP": 4 * foe_level + (5 * (foe_level - 1)), "Attack": 1 * foe_level,
                   "Skill": "Cleave", "Level": foe_level, "Accuracy": 0.8}
        else:
            print("\nSuddenly a level {} Assassin came out of nowhere!".format(foe_level))
            foe = {"Name": "Assassin", "Current HP": 3 * foe_level + (3 * (foe_level - 1)), "Attack": 2 * foe_level,
                   "Skill": "Swift Edge", "Level": foe_level, "Accuracy": 0.7}
    elif current_location == "D":
        foe = {"Name": "Dracula", "Current HP": 40, "Attack": 6, "Skill": "Blood Edge", "Level": 3, "Accuracy": 0.9}
    else:
        print("\nYou have awakened a level 3 Cyclops!")
        foe = {"Name": "Cyclops", "Current HP": 20, "Attack": 4, "Skill": "Ground Slam", "Level": 3, "Accuracy": 0.6}
    return foe


def create_action_list(character: dict, foe: str) -> list:
    """
    Create a list of actions based on the character dictionary.

    :param character: a dictionary
    :param foe: a string
    :precondition: foe is a non-empty string
    :precondition: character is a dictionary with a "Skills" key, a "Level" key, and an "Ultimate" key
    :precondition: "Level" key in character has an integer value that is larger than 0
    :precondition: "Level" key in character has an integer value that is larger than or equals to 0
    :precondition: "Skills" key in character has a non-empty list as value, this list contains only string elements
    :precondition: the list value of "Skills" has a length larger than or equal to "Level" key's integer value
    :postcondtition: return a list with string elements which represent character's available actions
    :postcondtition: character dictionary will not be changed
    :return: a list with string elements which represent character's available actions

    >>> foe_name = "Assassin"
    >>> character_info = {"Skills": ["Skill 1", "Skill 2", "Skill 3", "Skill 4"], "Level": 3, "Ultimate": 1}
    >>> create_action_list(character_info, foe_name)
    ['Skill 1', 'Skill 2', 'Skill 3 (1 time left)', 'Flee']
    >>> character_info == {"Skills": ["Skill 1", "Skill 2", "Skill 3", "Skill 4"], "Level": 3, "Ultimate": 1}
    True
    """
    action_list = [character["Skills"][level] for level in range(character["Level"])]
    if len(action_list) == 3:
        if character["Ultimate"] == 0:
            del action_list[2]
        else:
            action_list[2] += " ({} time left)".format(character["Ultimate"])
    if foe != "Dracula":
        action_list.append("Flee")
    return action_list


def print_hp_message(foe: dict, character: dict) -> None:
    """
    Print character's and foe's HP information.

    :param foe: a dictionary
    :param character: a dictionary
    :precondition: foe is a dictionary with a "Level" key, a "Name" key and a "Current HP" key
    :precondition: character is a dictionary with a "Current HP" key
    :postconditioin: print character's and foe's HP information
    :postconditioin: foe and character will not be changed

    >>> foe_info = {"Level": 3, "Name": "Dracula", "Current HP": 40}
    >>> character_info = {"Current HP": 30}
    >>> print_hp_message(foe_info, character_info)
    <BLANKLINE>
    Level 3 Dracula has 40 HP left.
    You have 30 HP left.
    """
    print("\nLevel {} {} has {} HP left.".format(foe["Level"], foe["Name"], foe["Current HP"]))
    print("You have {} HP left.".format(character["Current HP"]))


def foe_attack(foe: dict, character: dict) -> None:
    """
    Update character stats based on foe's attack.

    :param foe: a dictionary
    :param character: a dictionary
    :precondition: foe has one "Accuracy" key and one "Attack" key, both keys have a positive integer as value
    :precondition: foe has one "Name" key and one "Skill" key, both keys have a non-empty string value
    :precondition: character has one "Invincible" key which has an integer value that is larger than or equals to 0
    :precondition: character has one "Current HP" key which has an integer value that is larger than 0
    :precondition: character has one "Class" key which has a non-empty string value
    :postcondition: foe dictionary will not be changed
    :postcondition: update character dictionary based on foe's attack
    :postcondition: print a message that describe foe's attack, and it's effect on character

    >>> foe_info = {"Accuracy": 0.7, "Attack": 7, "Name": "Assassin", "Skill": "Poke"}
    >>> character_info = {"Current HP": 10, "Invincible": 1, "Class": "Shadow"}
    >>> foe_attack(foe_info, character_info)
    <BLANKLINE>
    Assassin uses Poke, but you are quick as the shadow and dodge the attack.
    >>> character_info == {"Current HP": 10, "Invincible": 0, "Class": "Shadow"}
    True
    >>> foe_info == {"Accuracy": 0.7, "Attack": 7, "Name": "Assassin", "Skill": "Poke"}
    True
    """
    if character["Invincible"] > 0:
        character["Invincible"] -= 1
        attack_blocked_message(character["Class"], foe)
    else:
        if random.randint(1, 100) <= foe["Accuracy"] * 100:
            character["Current HP"] -= foe["Attack"]
            print("\n{} uses {} and deal {} damage to you.".format(foe["Name"], foe["Skill"], foe["Attack"]))
        else:
            print("\n{} uses {}, but he missed.".format(foe["Name"], foe["Skill"], foe["Attack"]))


def attack_blocked_message(character_class: str, foe: dict) -> None:
    """
    Print attack blocked message based on character's class.

    :param character_class: a non-empty string
    :param foe: a dictionary
    :precondition: character_class is a non-empty string
    :precondition: foe is a dictionary with one "Name" key and one "Skill" key, both keys have a non-empty string value
    :postcondition: print an attack blocked message based on character's class
    :postcondition: foe dictionary will not be changed

    >>> job = "Wizard"
    >>> foe_info = {'Name': 'Dracula', 'Skill': 'Slap'}
    >>> attack_blocked_message(job, foe_info)
    <BLANKLINE>
    Your Ice shield blocks Dracula's Slap.
    >>> foe_info == {'Name': 'Dracula', 'Skill': 'Slap'}
    True
    """
    if character_class == "Berserker":
        print("\n{} uses {} on you, but you are not feeling anything.".format(foe["Name"], foe["Skill"]))
    elif character_class == "Shadow":
        print("\n{} uses {}, but you are quick as the shadow and dodge the attack.".format(foe["Name"], foe["Skill"]))
    elif character_class == "Wizard":
        print("\nYour Ice shield blocks {}'s {}.".format(foe["Name"], foe["Skill"]))
    else:
        print("\n{} is hypnotized, he does not know what he is doing.".format(foe["Name"]))


def character_skill_effect(action: str, foe: dict, character: dict) -> None:
    """
    Update foe dictionary and character dictionary based on the character's chosen skill.

    :param action: a string
    :param foe: a dictionary
    :param character: a dictionary
    :precondition: action is a non-empty string that must equal to one of the elements in character's "Skills" list
    :precondition: foe is a dictionary with one "Name" key and one "Current HP" key, "Name" has a non-empty string value
                   and "Current HP" has a positive non-zero integer value
    :precondition: character is a dictionary with one "Skills" key with a non-empty string list as value
    :precondition: character has one "Accuracy" key with a float value that is between 1 and 0 inclusive
    :precondition: character has one "Attack" key with an integer value that is greater than 0
    :precondition: character has one "Invincible" key with an integer value that is greater than or equals to 0
    :precondition: character has one "Class" key with a non-empty string value
    :precondition: character has one "Ultimate" key with an integer value that is greater than or equals to 0
    :postcondition: print a message describing the character's chosen skill effect
    :postcondition: update foe dictionary and character dictionary based on the character's chosen skill

    >>> skill_picked = "Block"
    >>> foe_info = {"Name": "Dracula", "Current HP": "50"}
    >>> character_info = {"Skills": ["1", "2", "Block"], "Accuracy": 1, "Attack": 5, "Invincible": 0,
    ...                   "Ultimate": 2 ,"Class": "Shadow"}
    >>> character_skill_effect(skill_picked, foe_info, character_info)
    <BLANKLINE>
    You are in Shadow mode now. Your speed dramatically increases for 2 rounds.
    >>> character_info == {"Skills": ["1", "2", "Block"], "Accuracy": 1, "Attack": 5, "Invincible": 2,
    ...                    "Ultimate": 1 ,"Class": "Shadow"}
    True
    """
    skill_index = 0
    for index, skill in enumerate(character["Skills"]):
        if skill in action:
            skill_index = index
    if skill_index < 2:
        if random.randint(1, 100) <= character["Accuracy"] * 100 - skill_index * 10:
            damage = character["Attack"] * (1 + skill_index)
            foe["Current HP"] -= damage
            print("\nYour {} deal {} damage to {}.".format(action, damage, foe["Name"]))
        else:
            print("\nYou tried to use {} on {}, but you missed.".format(action, foe["Name"]))
    elif skill_index == 2:
        character["Invincible"] = 2
        character["Ultimate"] -= 1
        skill_3_message(character["Class"], foe["Name"])


def skill_3_message(character_class: str, foe_name: str) -> None:
    """
    Print message describing character's ultimate skill.

    :param character_class: a non-empty string
    :param foe_name: a non-empty string
    :precondition: character_class and foe_name are both non-empty string
    :postcondition: print message describing character's ultimate skill based on character's class

    >>> character = "MasterMind"
    >>> foe = "Barbarian"
    >>> skill_3_message(character, foe)
    <BLANKLINE>
    You have Hypnotized the Barbarian. He will not attack you for 2 rounds.
    """
    if character_class == "Berserker":
        print("\nYou are in Berserk mode now. You will not take any damage for 2 rounds.")
    elif character_class == "Shadow":
        print("\nYou are in Shadow mode now. Your speed dramatically increases for 2 rounds.")
    elif character_class == "Wizard":
        print("\nYou have casted an Ice shield. This shield will protect you for 2 rounds.")
    else:
        print("\nYou have Hypnotized the {}. He will not attack you for 2 rounds.".format(foe_name))


def hit_when_flee(character: dict, foe: dict) -> None:
    """
    Update character HP if character was hit by foe when fleeing.

    :param character: a dictionary
    :param foe: a dictionary
    :precondition: character is a dictionary with one "Current HP" key, the key has a non-zero positive integer as value
    :precondition: foe is a dictionary with one "Name" key, the key has a non-empty string value
    :precondition: foe has one "Attack" key, the key has a non-zero positive integer as value
    :postcondition: determine if character was hit using random number
    :postcondition: update character dictionary's "Current HP" value if character was hit
    :postcondition: print a message about the attack if character was hit
    """
    if random.randint(1, 100) <= 20:
        character["Current HP"] -= foe["Attack"]
        print("\nYou got hit when you turned your back to {}.".format(foe["Name"]))


def combat_result(foe: dict, character: dict, result: str) -> None:
    """
    Update character stats after combat.

    :param foe: a dictionary
    :param character: a dictionary
    :param result: a string
    :precondition: result is a non-empty string
    :precondition: foe is a dictionary with one "Name" key and one "Level" key, "Name" has a non-empty string value, and
                   "Level" has a non-zero positive integer value
    :precondition: character is a dictionary with an "Invincible" key, an "Exp" key, and an "Ultimate" key, they all
                   have an integer value that is larger than or equals to 0
    :postcondition: print a message describing the combat result and the effect on character
    :postcondition: set character "Invincible" value to 0 and increase character exp if character won the combat
    :postcondition: foe dictionary will not be changed

    >>> the_result = "win"
    >>> foe_info = {"Name": "Cyclops", "Level": 5}
    >>> character_info = {"Invincible": 2,"Exp": 0, "Ultimate": 1}
    >>> combat_result(foe_info, character_info, the_result)
    <BLANKLINE>
    You defeated Cyclops!
    You gained 5 experience.
    >>> character_info == {"Invincible": 0,"Exp": 5, "Ultimate": 2}
    True
    >>> foe_info == {"Name": "Cyclops", "Level": 5}
    True
    """
    character["Invincible"] = 0
    character["Ultimate"] = 2
    if result == "character flee":
        print("\nYou fled the fight.")
    elif result == "foe flee":
        print("\n{} fled the fight.".format(foe["Name"]))
    elif result == "win":
        print("\nYou defeated {}!\nYou gained {} experience.".format(foe["Name"], foe["Level"]))
        character["Exp"] += foe["Level"]
    else:
        print("\nYou died in the hand of {}.".format(foe["Name"]))


def level_up(character: dict) -> None:
    """
    Update character stats if character levels up.

    :param character: a dictionary
    :precondition: character is a dictionary with a "Exp", a "Level", a "Max HP", a "Current HP", an "Attack", a
                   "Class", a "Jobs", a "Skills", and a "Exp Needed" key
    :precondition: in character, "Exp" has an integer value that is greater than or equals to 0
    :precondition: in character, "Level" and "Attack" both have an integer value that is greater than 0 or equals to 0
    :precondition: in character, "Max HP" and "Current HP" both have an integer value that is greater than 0
    :precondition: in character, "Class" has an non-empty string value
    :precondition: in character, "Jobs" and "Skills" both have a string list as value, these two lists must have at
                   least 3 elements
    :precondition: in character, "Exp Needed" has a list value, inside it there are 2 greater than 0 integer elements in
                   ascending order
    :postcondition: update character dictionary with new value if the character levels up
    :postcondition: print messages describing stats change if the character levels up
    :postcondition: dictionary character will not be changed if character does not meet level up requirement

    >>> character_info = {"Exp": 3, "Level": 1, "Max HP": 5, "Current HP": 3, "Attack": 1, "Class": "Mage",
    ...                   "Jobs": ["Mage", "Enchanter", "Wizard"], "Skills": ["Fire ball", "Thunderstorm", "Ice Wall"],
    ...                   "Exp Needed": [3, 15]}
    >>> level_up(character_info)
    <BLANKLINE>
    Congratulations! You level up to level 2.
    You have been promoted to Enchanter.
    Max HP, Attack increases.
    Current HP has been fully restored.
    You have learnt Thunderstorm.
    >>> character_info == {"Exp": 3, "Level": 2, "Max HP": 15, "Current HP": 15, "Attack": 2, "Class": "Enchanter",
    ...                    "Jobs": ["Mage", "Enchanter", "Wizard"], "Skills": ["Fire ball", "Thunderstorm", "Ice Wall"],
    ...                    "Exp Needed": [3, 15]}
    True
    """
    for level, exp_needed in enumerate(character["Exp Needed"], 2):
        if character["Exp"] >= exp_needed and character["Level"] < level:
            character["Level"] += 1
            character["Max HP"] += 10
            character["Current HP"] = character["Max HP"]
            character["Attack"] += 1
            character["Class"] = character["Jobs"][level - 1]
            print("\nCongratulations! You level up to level {}.".format(level))
            print("You have been promoted to {}.".format(character["Class"]))
            print("Max HP, Attack increases.\nCurrent HP has been fully restored.")
            print("You have learnt {}.".format(character["Skills"][level - 1]))


def life_regenerate(character: dict) -> None:
    """
    Regenerate character HP by increasing the "Current HP" value in character dictionary.

    :param character: a dictionary
    :precondition: character is a dictionary that has a "Current HP" and a "Max HP" key, both keys have a non-zero
                   positive integer as value
    :postcondition: increase the integer value of "Current HP" in character by 1 if it is less than the integer value of
                    "Max HP"
    :postcondition: print a message about the regeneration if regeneration actually happens
    :postcondition: character dictionary will not be changed if regeneration does not happen

    >>> character_info = {"Current HP": 5, "Max HP": 10}
    >>> life_regenerate(character_info)
    <BLANKLINE>
    Regenerate 1 HP.
    >>> character_info == {"Current HP": 6, "Max HP": 10}
    True

    >>> character_info = {"Current HP": 10, "Max HP": 10}
    >>> life_regenerate(character_info)
    >>> character_info == {"Current HP": 10, "Max HP": 10}
    True
    """
    if character["Current HP"] < character["Max HP"]:
        character["Current HP"] += 1
        print("\nRegenerate 1 HP.")


def show_status(character: dict) -> None:
    """
    Print character status.

    :param character: a dictionary
    :precondition: character is a dictionary with a "Skills" key, a "Level" key, an "Exp" key, and an "Exp Needed" key
    :precondition: in character, "Skills" has a string list value, the list length must be at least 3
    :precondition: in character, "Level" has an integer value that is between 1 and 3 inclusive
    :precondition: in character, "Exp" has an integer value that is greater than or equals to 0
    :precondition: in character, "Exp Needed" has a list value, inside it there are 2 greater than 0 integer elements in
                   ascending order
    :postcondition: dictionary character will not be changed
    :postcondition: print all information in dictionary character, except "Coordinate", "Invincible", "Jobs", and "Exp"

    >>> character_info = {"Coordinate": [1, 1], "HP": 5, "Class": "Shadow", "Skills": ["A", "B", "C"], "Level": 2,
    ...                   "Exp": 5 ,"Exp Needed": [3, 13]}
    >>> show_status(character_info)
    <BLANKLINE>
    HP : 5
    Class : Shadow
    Level : 2
    Exp to Next Level : 8
    Skill :
    A: Basic class attack. Low attack but high accuracy.
    B: Advanced class skill with high attack but low accuracy.
    >>> character_info == {"Coordinate": [1, 1], "HP": 5, "Class": "Shadow", "Skills": ["A", "B", "C"], "Level": 2,
    ...                   "Exp": 5 ,"Exp Needed": [3, 13]}
    True
    """
    print()
    for key in character.keys():
        if key not in ["Coordinate", "Invincible", "Jobs", "Skills", "Exp", "Exp Needed", "Ultimate"]:
            print("{} : {}".format(key, character[key]))
    available_skill = [character["Skills"][level] for level in range(character["Level"])]
    if character["Level"] < 3:
        print("Exp to Next Level : {}".format(character["Exp Needed"][character["Level"] - 1] - character["Exp"]))
    print("Skill :")
    for index, skill in enumerate(available_skill, 1):
        if index == 1:
            print("{}: Basic class attack. Low attack but high accuracy.".format(skill))
        elif index == 2:
            print("{}: Advanced class skill with high attack but low accuracy.".format(skill))
        else:
            print("{}: Ultimate class skill that protects you from any attack for 2 rounds. This can only be used 2 "
                  "times per fight.".format(skill))


def church_event(character: dict) -> None:
    """
    Restore character's current HP to max HP.

    :param character: a dictionary
    :precondition: character is a dictionary with a "Current HP" key and a "Max HP" key
    :precondition: in character, "Current HP" has a non-zero positive integer value
    :precondition: in character, "Max HP" has a non-zero positive integer value which is larger than or equals to
                   "Current HP" value
    :postcondition: set the value of "Current HP" in character to the value of "Max HP"
    :postcondition: print a message informing user the character's HP was fully restored

    >>> character_info = {"Current HP": 7, "Max HP": 10}
    >>> church_event(character_info)
    <BLANKLINE>
    The priest inside the church healed your wounds.
    Your HP was fully restored.
    >>> character_info == {"Current HP": 10, "Max HP": 10}
    True
    """
    print("\nThe priest inside the church healed your wounds.")
    print("Your HP was fully restored.")
    character["Current HP"] = character["Max HP"]


def treasure_event(board: dict, character: dict) -> None:
    """
    Update character stats and board location after treasure event.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board is a dictionary with tuple coordinate keys and single character string values
    :precondition: character is a dictionary with a "Max HP" key, an "Attack" key, and a "Coordinate" key
    :precondition: in character, "Coordinate" has a coordinate list as value, this coordinate must equal to one of the
                   tuple coordinate keys in board
    :precondition: in character, "Attack" and "Max HP" both have an integer value that is larger than 0
    :postcondition: determine the treasure found with random number
    :postcondition: update character stats based on the treasure found
    :postcondition: update board and remove treasure event by changing current coordinate's value to "."
    """
    random_number = random.randint(1, 100)
    if random_number <= 80:
        print("\nAt the center of the ruin, you found an old tree.\n"
              "There was a mysterious glowing fruit on the tree. Out of curiosity, you ate the fruit.\n"
              "Suddenly, You felt a surge of energy within your body.\n"
              "Your Max HP increased by 5.")
        character["Max HP"] += 5
    else:
        print("\nYou noticed a glowing object in the corner of the ruin.\n"
              "It was an enchanted ring! You did not know what the ring does, but you put it on anyway.\n"
              "You could feel the power stored within the ring flowing to your body.\n"
              "Your attack power increased.")
        character["Attack"] += 1
    board[(character["Coordinate"][0], character["Coordinate"][1])] = "."


def check_goal_attained(current_location: str, result: str) -> bool:
    """
    Return a boolean that determines if the player has defeated final boss.

    :param current_location: a string
    :param result: a string
    :precondition: current_location and result are non-empty strings
    :postcondition: return a boolean that determines if the player has defeated final boss
    :return: a boolean that determines if the player has defeated final boss

    >>> location = "."
    >>> battle_result = "win"
    >>> check_goal_attained(location, battle_result)
    False

    >>> location = "D"
    >>> battle_result = "win"
    >>> check_goal_attained(location, battle_result)
    True
    """
    return result == "win" and current_location == "D"


def describe_location(current_location: str) -> None:
    """
    Print a message describing player's current location.

    :param current_location: a string
    :precondition: current_location is a single character non-empty string
    :postcondition: print a message describing player's current location

    >>> location = "C"
    >>> describe_location(location)
    <BLANKLINE>
    You came across a church that was decorated with colorful stained-glass.
    """
    if current_location == "D":
        print("\nYou have finally reached the castle. Dracula is sitting in the hall and looking at you. It is as if "
              "he has been expecting you. He sneers and says \"Let's start, shall we?\"")
    elif current_location == "C":
        print("\nYou came across a church that was decorated with colorful stained-glass.")
    elif current_location == "T":
        print("\nYou found an ancient ruin. You felt lucky at the moment, so you started searching the area.")
    elif current_location == "M":
        print("\nYou found a monster lair. There was a sleeping Cyclops. Out of curiosity, you poked the Cyclops.")
    else:
        if random.randint(1, 100) <= 10:
            print("\nYou found a lake. It is so calm and clear. You stopped and took a little rest.")
        elif random.randint(1, 100) <= 40:
            print("\nYou walked into the woods. You feel like you are being watched.")
        else:
            print("\nYou are in the forest.")


def combat(foe: dict, character: dict) -> str:
    """
    Drive the combat loop of the game.
    """
    character_flee = False
    foe_flee = False
    while not character_flee and not foe_flee and foe["Current HP"] > 0 and character["Current HP"] > 0:
        action_list = create_action_list(character, foe["Name"])
        print_hp_message(foe, character)
        chosen_action = get_user_input("What do you want to do?", action_list)
        if chosen_action == "Flee":
            hit_when_flee(character, foe)
            character_flee = True
        else:
            character_skill_effect(chosen_action, foe, character)
        if not character_flee and foe["Current HP"] > 0:
            foe_attack(foe, character)
            if random.randint(1, 100) <= 20 and foe["Name"] != "Dracula":
                foe_flee = True
    if character_flee:
        return "character flee"
    elif foe_flee:
        return "foe flee"
    elif foe["Current HP"] <= 0:
        return "win"
    else:
        return "die"


def win_message() -> None:
    """
    Print win message.
    """
    print("\nCongratulations! You have restored peace to the people. Your achievement has been recognized and you are "
          "now the leader of BCIT.")
    print("Thanks for playing.")


def game_over_message() -> None:
    """
    Print game over message.
    """
    print("Game Over. BCIT is still under Dracula's threat. Please try again.")


def wrong_direction_message() -> None:
    """
    Print wrong direction message.
    """
    print("\nYou cannot go that way!")


def opening_ascii_art() -> None:
    """
    Print opening ASCII art.
    """
    print()
    print("▄████████    ▄████████    ▄████████     ███      ▄█          ▄████████              ▄████████ ███▄▄▄▄   ████"
          "████▄            ████████▄     ▄████████    ▄████████  ▄████████ ███    █▄   ▄█          ▄████████\n███    █"
          "██   ███    ███   ███    ███ ▀█████████▄ ███         ███    ███             ███    ███ ███▀▀▀██▄ ███   ▀███ "
          "          ███   ▀███   ███    ███   ███    ███ ███    ███ ███    ███ ███         ███    ███\n███    █▀    ██"
          "█    ███   ███    █▀     ▀███▀▀██ ███         ███    █▀              ███    ███ ███   ███ ███    ███        "
          "   ███    ███   ███    ███   ███    ███ ███    █▀  ███    ███ ███         ███    ███\n███          ███    ██"
          "█   ███            ███   ▀ ███        ▄███▄▄▄                 ███    ███ ███   ███ ███    ███           ███ "
          "   ███  ▄███▄▄▄▄██▀   ███    ███ ███        ███    ███ ███         ███    ███\n███        ▀███████████ ▀████"
          "███████     ███     ███       ▀▀███▀▀▀               ▀███████████ ███   ███ ███    ███           ███    ███ "
          "▀▀███▀▀▀▀▀   ▀███████████ ███        ███    ███ ███       ▀███████████\n███    █▄    ███    ███          ███"
          "     ███     ███         ███    █▄              ███    ███ ███   ███ ███    ███           ███    ███ ▀██████"
          "█████   ███    ███ ███    █▄  ███    ███ ███         ███    ███\n███    ███   ███    ███    ▄█    ███     ██"
          "█     ███▌    ▄   ███    ███             ███    ███ ███   ███ ███   ▄███           ███   ▄███   ███    ███  "
          " ███    ███ ███    ███ ███    ███ ███▌    ▄   ███    ███\n████████▀    ███    █▀   ▄████████▀     ▄████▀   █"
          "████▄▄██   ██████████             ███    █▀   ▀█   █▀  ████████▀            ████████▀    ███    ███   ███   "
          " █▀  ████████▀  ████████▀  █████▄▄██   ███    █▀\n")


def win_ascii_art() -> None:
    """
    Print winning ASCII art.
    """
    print()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/&@%/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,((@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  .  %@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.  (  @@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%  @@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/&  ,#@@@@@@@@@( ( (@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&.*%@@*   (@@@@@@@%   &@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(&,(.&%@ & @@@&(@*  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#, **/ %& @* & /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   ##@ , @  .  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# .*    ,/@# /@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         #@@ @, .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@#*   . @@@*%(#*  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  .      ,@&((, %@ .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.       .& #.&@,  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& @     #.  /  #   *.&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(.#./ * &@ *      (.   &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.& .    ,/, %##   .    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  &@@#  /.@ @/(,#@ .   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  ,#&@&&&  . @@&     @ . @ /   *            ,/((%@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/% @@@    (  * &&@/  @@@.@@&(&&@@&(,,,*/#@@&%##%&@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(&@@@@@%#@@&# &@@@..@@,    @@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/(  .%@@@@@ ,@@ &@@@@@@@@     &@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      @@@@@*    @@@@@@@@/     @@@@@@@@@@@@@@@@@@ &@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%     / @&@@@ .,  @@@@@@@@@ &  *@@@@@@@@@@@@@@@# (%@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@&@@@@@@@@@@@@@@      . *%  & @/ /*  %@@@@@@@@,   @@@@@@@@@@@@@@@@. @@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@.@@@@@   @ *      @@#* .*@@@@@@@@@@@@  *@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@*#(.//@@@@@@. ( ,(@(   &% &@&       /  (@@@@    @@@@&@@@@@@@.@*@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@(,* ,/  ** %  @@@@@@ ,    @  (   @@#% ///  @@@@@@@@@@     *&@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@#                                .,.@@&   ,    @@@@@@@.     @@@&@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/,                  @@@@#/,(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@%@@#*.   *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"
          "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


def game_over_ascii() -> None:
    """
    Print game over ASCII art.
    """
    print()
    print("     ▄████  ▄▄▄       ███▄ ▄███▓▓█████        ▒█████   ██▒   █▓▓█████  ██▀███\n     ██▒ ▀█▒▒████▄    ▓██▒▀█"
          "▀ ██▒▓█   ▀       ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒\n     ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███         ▒██░  "
          "██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒\n     ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄       ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀"
          "█▄\n     ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒      ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒\n     ░▒   ▒  ▒▒   ▓▒"
          "█░░ ▒░   ░  ░░░ ▒░ ░      ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░\n     ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░      "
          "  ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░\n     ░ ░   ░   ░   ▒   ░      ░      ░         ░ ░ ░ ▒       ░░     ░  "
          "   ░░   ░\n     ░       ░  ░       ░      ░  ░          ░ ░        ░     ░  ░   ░\n")


def game() -> None:
    """
    Drive the main game loop.
    """
    rows = 25
    columns = 25
    opening_ascii_art()
    story_opening()
    character = make_character(rows)
    update_class_stats(character)
    board = make_board(rows, columns)
    create_castle(board, columns)
    print_map(rows, columns, board, character)
    achieved_goal = False
    while not achieved_goal and character["Current HP"] > 0:
        command = get_command()
        if command == "Check Map":
            print_map(rows, columns, board, character)
            continue
        if command == "Check Status":
            show_status(character)
            continue
        if command == "Quit Game":
            break
        direction = get_vector(command)
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            print_map(rows, columns, board, character)
            life_regenerate(character)
            current_location = check_current_location(board, character)
            describe_location(current_location)
            if current_location == "C":
                church_event(character)
            elif current_location == "T":
                treasure_event(board, character)
            elif (current_location == "." and check_for_foe()) or current_location == "M" or current_location == "D":
                foe = make_foe(character, current_location)
                result = combat(foe, character)
                combat_result(foe, character, result)
                level_up(character)
                achieved_goal = check_goal_attained(current_location, result)
        else:
            wrong_direction_message()
            print_map(rows, columns, board, character)
    if achieved_goal:
        win_ascii_art()
        win_message()
    else:
        game_over_ascii()
        game_over_message()


def main() -> None:
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
