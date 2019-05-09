import game
from characters import MainCharacter


def enable_continue():
    pass


try:
    f = open("character.txt", "x")
    f.close()
except FileExistsError:
    enable_continue()


def create_character():
    # insert a name
    name = "OLEG"
    main_character = MainCharacter(name)
    character_info = open("character.txt", "w")
    for attr_name in main_character.__dict__:
        character_info.write(
            attr_name + " " + str(main_character.__dict__[attr_name]) + "\n")
    character_info.close()


def new_game():
    create_character()
    game.main()


new_game()


def event_loop():
    # check for events
    pass

# start new game
# continue
# settings
# quit
