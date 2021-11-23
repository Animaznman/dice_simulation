from dices import *

def main():
    run = True
    dice_list = ['d4','d6','d8','d10','d12','d20']
    dices_input = input("Please enter in the number of each dice you would like.\n"+
    "[d4,d6,d8,d10,d12,d20]\n"+
    "For example, if you want to roll 3 d4s, and 2 d20s, you would input\n"+
    "3,0,0,0,0,2\n"+
    "Make sure to have , in between each number.\n")
    dices_input = dices_input.split(",")
    dices_input = list(map(int, dices_input))
    dice_bag = {"d4":[],"d6":[],"d8":[],"d10":[],"d12":[],"d20":[]}
    while(run):
        for x in range(len(dices_input)):
            for y in range(dices_input[x]):
                dice_bag[dice_list[x]].append(eval(dice_list[x]+"()"))
        run=False

    print("Here is what your bag rolled: \n")
    for dice_type in dice_bag:
        for dice_object in dice_bag[dice_type]:
            dice_object.display()
    sum = 0
    for dice_type in dice_bag:
        for dice_object in dice_bag[dice_type]:
            sum+=dice_object.value
    print("Sum of bag is: "+str(sum))

if __name__ == '__main__':
    main()
