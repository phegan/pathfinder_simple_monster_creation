from pathfinder.models.arrays.array_factory import ArrayFactory
from pathfinder.models.monster.monster import Monster
from pathfinder.exceptions.array_exceptions import InvalidArrayTypeException
import json

def get_user_input(prompt, menu):
    with open("json/menus/" + menu + ".json", "r") as file:
        menu_options = json.load(file)

        menu = ""
        count = 1

        for option in menu_options:
            menu = menu + "\n" + str(count) + ". " + option
            count = count+1

        choice = int(raw_input(prompt + menu))

        if(isinstance(choice, ( int, long )) and len(menu_options)+1 > choice):
            return menu_options[choice-1]
        else:
            raise InvalidArrayTypeException()

def main():
    monster = Monster()

    cr = raw_input("Enter CR of monster:")
    print cr

    array_type = get_user_input("Select Array Type", "array_types")
    factory = ArrayFactory()
    array = factory.getArray(cr, array_type)

    monster.applyArray(array)

    high_ability_mod = get_user_input("Select high ability mod", "ability_scores")

    # ability_score_string = get_ability_score_string()
    #
    # high_mod = raw_input("Which Ability Modifier gets +" + str(array.getMasterAbilityMod()) + ability_score_string)
    #
    # great_mod = raw_input("Which Ability Modifier gets +" + str(array.getGreatAbilityMod()) + "\n 1. Strength\n 2. Dexterity \n 3. Constitution\n 4. Intelligence\n 5. Wisdom\n 6. Charisma")
    #
    # good_mod = raw_input("Which Ability Modifier gets +" + str(array.getGoodAbilityMod()) + "\n 1. Strength\n 2. Dexterity \n 3. Constitution\n 4. Intelligence\n 5. Wisdom\n 6. Charisma")
    #
    #
    # if(high_mod == 1):
    #     monster.setStrngth(array.getMasterAbilityMod())

if __name__ == "__main__":
    main()