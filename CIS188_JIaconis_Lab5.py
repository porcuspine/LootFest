# Justin Iaconis CIS188 Lab 5
# This program uses a dictionary to store the inventory of a player character in a fantasy
# video game and provides methods to display and alter that inventory.
# The player can choose a monster to fight and recieves randomized rewards from it.


import random
import time


# Set this to True to recieve extra console output
DEBUG = False

# How long the console waits between printing blocks
WAIT_TIME = 2

# Loot tables - dicts of { string : (int, ...) } where
#   string = item name
#   int = chance of dropping 1 of the item; additional ints are chance to drop multiple
#       eg (95, 75) means there's a 95% chance to drop 1 and a 75% chance to drop 1
GOBLIN_LT = {
    'small bones' : (100,),
    'hide scrap' : (95, 65,),
    'gold coin' : (90, 80, 70, 60, 50, 40,),
    'earth rune' : (60, 40,),
    'iron dagger' : (30,),
    'bronze arrow' : (40, 30, 20,),
    'goblin chainmail' : (15,),
    'goblin trinket' : (5,),
    }

GIANT_LT = {
    'big bones' : (100,),
    'giant toe' : (95,),
    'steel arrow' : (60, 50, 40, 30,),
    'nature rune' : (60, 30, 10,),
    'water rune' : (75, 25,),
    'raw emerald' : (15,),
    'limpwurt root' : (5,),
    }

DARKWIZARD_LT = {
    'human bones' : (100,),
    'cloth scrap' : (90, 65, 35,),
    'fire rune' : (80, 70, 60, 50,),
    'chaos rune' : (75, 55, 25,),
    'death rune' : (60, 30,),
    'briolette ruby' : (15,),
    'mahogany wand' : (5,),
    }

DRAGON_LT = {
    'dragon bones' : (100, 40,),
    'dragon hide' : (95, 80, 65, 40, 25,),
    'fire essence' : (60,),
    'adamantium arrow' : (50, 40, 30, 20, 10),
    'dragon tooth' : (40,),
    'draconic essence' : (10,),
    'dragon egg' : (3,),
    }

# List of monsters to choose to fight - list of tuple (string, lootTable)
FIGHT_OPTIONS = [
    ('goblin', GOBLIN_LT),
    ('giant', GIANT_LT),
    ('dark wizard', DARKWIZARD_LT),
    ('dragon', DRAGON_LT)
    ]

TEST_DATA = [
    ('test monster', {
        'test item 1' : (100,),
        'test item 2' : (50,),
        }),
    ]


def main():
    #switch these around for a much easier time collecting everything
    monData = FIGHT_OPTIONS
    #monData = TEST_DATA
    
    inventory = {}
    uniqueItemsCount = countUniqueItemDrops(monData)
    maxInput = len(monData) + 1
    
    print("Welcome to Lootfest!")
    print("Try to get every item in the game!")
    print("Enter a command to play.")
    print("")

    displayCommands(monData)
    inp = getInt('>>> ', atLeast = -1, atMost = maxInput)
    while inp != -1:
        print("")

        if inp == 0:
            print("Try to collect all", uniqueItemsCount, "unique items!")
        elif inp == 1:
            print('Your inventory:')
            displayInventory(inventory, showTotal = True)
        else:
            monsterDrops = killMonster(monData[inp-2])
            addToInventory(inventory, monsterDrops)
            
        if len(inventory) == uniqueItemsCount:
            printWinBanner()
            
        print("")
        time.sleep(WAIT_TIME)
        displayCommands(monData)
        inp = getInt('>>> ', atLeast = -1, atMost = maxInput)
    #end while

    print('Thanks for playing!')
#end main

# Prints the passed  inventory
# inventory = dictionary of {string : int}
# showTotal = bool whether or not to count and display num of items
# returns None
def displayInventory(inventory, showTotal = False):
    if len(inventory) == 0:
        print("Nothing!")
        return

    totalItems = 0
    uniqueItems = 0
    for item in inventory:
        numOfItem = inventory[item]
        if numOfItem > 0:
            print(item.title(), 'x' + str(numOfItem))
            totalItems += numOfItem
            uniqueItems += 1

    if showTotal:
        print("")
        print("Total items:", totalItems)
        print("Unique items:", uniqueItems)
#endfunc

# Adds passed items to the passed inventory
# inventory = dictionary of { string : int }
# items = dictionary of { string : int }
# returns None
def addToInventory(inventory, itemDict):
    for item in itemDict:
        inventory.setdefault(item, 0)
        inventory[item] += itemDict[item]
    #end for
#endfunc

# Displays all possible commands the user can enter
# fightOptions = list of tuples of monster data [(string, lootTable), ...]
#   where lootTable is { string : (int, int...) }
# returns None
def displayCommands(fightOptions):
    print("-1 : QUIT GAME")
    print("0 : REVIEW GOAL")
    print("1 : SHOW INVENTORY")
    for index in range(len(fightOptions)):
        print(index + 2, ": FIGHT", fightOptions[index][0].title())
#endfunc

# Generates an inventory of dropped items from a loot table
# lootTable = loot table to generate from { string : (int, int...) }
# returns dict { string : int } of item and how many
def getLoot(lootTable):
    drops = {}
    
    if DEBUG:
        print("# Rolling for loot...")
        
    for item in lootTable: #for every item in the loot table...
        for chance in lootTable[item]: #for every chance to roll that item...
            roll = random.randint(1, 100) #roll to see if that item drops at that chance
            didDrop = roll <= chance
            if didDrop: #if that item did drop, ...
                addToInventory(drops, { item : 1 }) #...add 1 of it to the drops dict
                
            if DEBUG:
                print('# Rolled', str(roll), 'for', str(item), 'vs', str(chance), ' -- Dropped:', didDrop)
            
        #end for
    #end for
    return drops
#endfunc

# Slays a monster and generates a loot drop from it
# monData = (string, lootTable) where string = monster name
# returns inventory of dropped items { string : int } 
def killMonster(monData):
    print("You slayed " + monData[0].title() + "!")
    drops = getLoot(monData[1])
    print(monData[0].title(), "dropped...")
    displayInventory(drops)
    return drops
#endfunc

# Counts how many unique items there are in a set of monster data
# monData = (string, lootTable) where string = monster name
# returns int num of unique items
def countUniqueItemDrops(monData):
    if DEBUG:
        print("# Counting unique items...")
        
    total = 0
    for monster in monData:
        uniqueMonsterItems = len(monster[1])
        total += uniqueMonsterItems
        
        if DEBUG:
            print("#",monster[0].title(), "has",uniqueMonsterItems,"unique items.")
    #end for

    if DEBUG:
        print("# Counted",total,"total unique items.")
        print("")
    
    return total
#endfunc

# Prints a win banner
# returns None
def printWinBanner():
    print("")
    print("---------------------------------------------")
    print("            CONGRATULATIONS!!!!")
    print("You've collected every item in the game!")
    print("---------------------------------------------")
#endfunc

# Prompts the user and gets an integer input
# message = string to be printed as prompt for input, no linebreak
# atLeast = if not set to None, will consider integers SMALLER than this number invalid
# atMost = if not set to None, will consider integers LARGER than this number invalid
# Returns validated integer input as int
def getInt(message, atLeast = None, atMost = None):
    valid = False
    while not valid:
        inp = input(message)
        
        #Verify if input is an integer
        try :
            inp = int(inp)
        except:
            print("InputError: could not cast input to integer!")
            continue
            
        #Restrict input to given bounds
        if atLeast != None:
            if inp < atLeast:
                print("InputError: input must be at least " + str(atLeast) + "!")
                continue
        if atMost != None:
            if inp > atMost:
                print("InputError: input must be at most " + str(atMost) + "!")
                continue

        #If passed all tests, valid
        valid = True
    #end while
    return inp
#endfunc


if __name__ == "__main__":
    main()
