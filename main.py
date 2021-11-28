from dices import *

# Prompts the user to select the number of each dice
def select():
    dice_list = ['d4','d6','d8','d10','d12','d20']
    dices_input = input("Input the number of each die you would like to throw\n"+
    "using the format of:\n"+
    "num_d4,num_d6,num_d8,num_d10,num_d12,num_d20\n")
    dices_input = dices_input.split(",")
    dices_input = list(map(int, dices_input))
    dice_bag = {"d4":[],"d6":[],"d8":[],"d10":[],"d12":[],"d20":[]}

    for x in range(len(dices_input)):
        for y in range(dices_input[x]):
            dice_bag[dice_list[x]].append(eval(dice_list[x]+"()"))
    return dice_bag

# Calculates sum of current dice_bag
def sum(bag):
    sum = 0
    for dice_type in bag:
        for dice_object in bag[dice_type]:
            sum+=dice_object.value
    return sum

# Rerandomizes current bag of dice by simulating a roll
def reroll(bag):
    for dice_type in bag:
        for dice_object in bag[dice_type]:
            dice_object.roll()

# Drops n number of minimum values from bag by omitting them from sum
def drop_n_min(bag):
    n = input("Input an integer number for how many of the lowest values you would like to drop\n")
    sum_of_mins = 0
    for i in range(n):
        sum_of_mins += min(min(bag.values()))
    return sum(bag)-sum_of_mins

# Drops n number of maximum values from bag by omitting them from sum
def drop_n_min(bag):
    n = int(input("Input an integer number for how many of the highest values you would like to drop\n"))
    sum_of_maxs = 0
    for i in range(n):
        sum_of_mins += max(max(bag.values()))
    return sum(bag)-sum_of_maxs

# Keeps n maximum values from bag and omits the rest from sum
def keep_n_max(bag):
    n = int(input("Input an integer number for how many of the highest values you would like to keep\n"))
    sum_of_maxs = 0
    for i in range(n):
        sum_of_mins += max(max(bag.values()))
    return sum_of_maxs

# Keeps values that meet specified requirements by comparison of <,>, or =
def keep_success(bag):
    target_value = int(input("Input an integer target value for which to compare dice rolls to:\n"))
    comparison = input("Input which comparison operator you would like to use: >, <, or =\n")
    if comparison == '>':
        successes = 0
        for dice_type in dice_bag:
            for dice_object in dice_bag[dice_type]:
                if dice_object.value > target_value:
                    successes += dice_object.value
        return successes
    elif comparison == '<':
        for dice_type in dice_bag:
            for dice_object in dice_bag[dice_type]:
                if dice_object.value < target_value:
                    successes += dice_object.value
        return successes
    elif comparison == '=':
        for dice_type in dice_bag:
            for dice_object in dice_bag[dice_type]:
                if dice_object.value == target_value:
                    successes += dice_object.value
        return successes


def main():
    dice_bag = select()

    print("Here is what your bag rolled: \n")
    for dice_type in dice_bag:
        for dice_object in dice_bag[dice_type]:
            dice_object.display()

    print("Sum of bag is: "+str(sum(dice_bag)))
    choices = [ "print(\"Now exiting...\")", "reroll(dice_bag)", "select()", "drop_n_min(dice_bag)", "drop_n_max(dice_bag)",
    "keep_n_max(dice_bag)", "keep_success(dice_bag)"]
    choice = 10
    while choice > 0:
        choice = int(input("Please select from the following options:\n"+
        "1 - Reroll: Re-roll  all dice in current bag\n"+
        "2 - Reselect: Select new set of dice for the bag.\n"+
        "3 - Drop lowest n: Report the current bag's value after dropping the lowest n dice\n"+
        "4 - Drop highest n: Report the current bag's value after dropping the highest n dice\n"+
        "5 - Keep highest n: Report the current bag's value after keeping the highest n dice\n"+
        "6 - Keep success: Report the current bag's value after keeping the success by comparison operators\n"+
        "0 - Exit: Exit out of this program.\n"))
        eval(choices[choice])


if __name__ == '__main__':
    main()
