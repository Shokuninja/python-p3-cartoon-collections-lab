def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf.title()}")  

def summon_captain_planet(planeteer_calls):
    return [planeteer.title() + "!" for planeteer in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    for item in planeteer_calls:
        if len(item) > 4:
            return True
    return False

def find_the_cheese(food_list):
    cheese_list = ["cheddar", "gouda", "camembert"]
    for food in food_list:
        if food in cheese_list:
            return food


