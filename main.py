"""This module contains the Lootfest game, run through the default print stream."""

from dsp import user_in
from src import items, monsters

class LootfestGame:
    """An instance of the game Lootfest, containing all state and logic."""

    MONSTERS = [
        monsters.GOBLIN,
        monsters.HILL_GIANT,
        monsters.DARK_WIZARD,
        monsters.RED_DRAGON
    ]

    def __init__(self):
        self.inventory:dict[items.Item, int] = {}

    @staticmethod
    def get_user_input() -> int:
        prompt = "Enter a command...\n" \
        "0: Quit\n" \
        "1: Display inventory\n"
        for i, monster in enumerate(LootfestGame.MONSTERS):
            prompt += f"{i+2}: Fight {monster.name}\n"
        return user_in.get_int(prompt, lambda x: 0 <= x <= len(LootfestGame.MONSTERS) + 1)

    def mainloop(self):
        """Start the game. Call only once to start. Function persists until the user quits."""

        print()
        print("Welcome to Lootfest!")
        user_commad = LootfestGame.get_user_input()

        while True:
            if user_commad == 0:
                print("Thanks for playing!")
                return
            elif user_commad == 1:
                self.display_inventory()
            else:
                self.slay_monster(LootfestGame.MONSTERS[user_commad-2])
                #TODO check for victory
        
            user_commad = LootfestGame.get_user_input()

    def display_inventory(self): #TODO
        sorted_inventory = list(self.inventory.items())
        sorted_inventory.sort(key=lambda x: x[0].rarity.value)
        for item, quantity in sorted_inventory:
            print(f"{quantity}x {item.name} ({item.rarity.name.lower()})")
        print("NotImplementedException")
        input("Submit anything to continue...\n")

    def slay_monster(self, monster:monsters.Monster):
        print(f"You slayed {monster.name}!")
        loot = monster.roll_loot()
        loot = list(loot.items())
        loot.sort(key=lambda x: x[0].rarity.value)
        legendary_loot:list[tuple[items.Item, int]] = []
        divine_loot:list[tuple[items.Item, int]] = []
        print("You receive:")
        for item, quantity in loot:
            drop_message = f"{quantity}x {item.name}"
            if item.rarity.value < items.ItemRarity.UNCOMMON.value:
                drop_message += "."
            elif item.rarity.value <= items.ItemRarity.VERY_RARE.value:
                drop_message += "!" * (item.rarity.value - 1)
            elif item.rarity.value == items.ItemRarity.LEGENDARY.value:
                legendary_loot.append((item, quantity))
                continue
            elif item.rarity.value == items.ItemRarity.RELIC.value:
                divine_loot.append((item, quantity))
                continue
            print(drop_message)
        for item, quantity in legendary_loot:
            print(f"You also recieve {quantity}x {item.name}! Amazing!!")
        for item, quantity in divine_loot:
            print(f"You find an incredible relic: {quantity}x {item.name}!!!")
        for item, quantity in loot:
            self.inventory[item] = self.inventory.get(item, 0) + quantity
        
        input("Submit anything to continue...\n")

if __name__ == "__main__":
    LootfestGame().mainloop()
