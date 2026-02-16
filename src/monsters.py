"""This module contains the Monster class to represent a monster in the game and constants
to access each monster definition."""

from src import items
from src.loot_tables import Drop, LootTable
from src.loot_tables import MEGARARE_LOOT_TABLE

class Monster:
    """Represents a monster in the game."""

    def __init__(self, name:str, loot_table:LootTable):
        """
        Args:
            name (str): The name of the monster.
            loot_table (LootTable): The loot table for this monster.
        """
        self._name = name
        self._loot_table = loot_table
    
    def __str__(self) -> str:
        return self.name
    
    @property
    def name(self) -> str:
        return self._name
    
    def roll_loot(self) -> dict[items.Item, int]:
        """Roll the loot table and returns the resulting drops as a dictionary of items to quantities."""

        return self._loot_table.roll()

GOBLIN = Monster(
    "goblin", 
    LootTable(
        Drop(items.SMALL_BONES, 1000),
        Drop(items.HIDE_SCRAP, 950),
        Drop(items.HIDE_SCRAP, 650),
        Drop(items.GOLD_COIN, 900),
        Drop(items.GOLD_COIN, 800),
        Drop(items.GOLD_COIN, 700),
        Drop(items.GOLD_COIN, 600),
        Drop(items.GOLD_COIN, 500),
        Drop(items.GOLD_COIN, 400),
        Drop(items.EARTH_RUNE, 600),
        Drop(items.EARTH_RUNE, 400),
        Drop(items.IRON_DAGGER, 300),
        Drop(items.BRONZE_ARROW, 400),
        Drop(items.BRONZE_ARROW, 400),
        Drop(items.BRONZE_ARROW, 300),
        Drop(items.BRONZE_ARROW, 300),
        Drop(items.GOBLIN_CHAINMAIL, 150),
        Drop(items.GOBLIN_TRINKET, 50),
        MEGARARE_LOOT_TABLE(0.1)
    ))

HILL_GIANT = Monster(
    "hill giant",
    LootTable(
        Drop(items.BIG_BONES, 1000),
        Drop(items.GIANT_TOE, 950),
        Drop(items.STEEL_ARROW, 600),
        Drop(items.STEEL_ARROW, 500),
        Drop(items.STEEL_ARROW, 400),
        Drop(items.STEEL_ARROW, 300),
        Drop(items.NATURE_RUNE, 600),
        Drop(items.NATURE_RUNE, 300),
        Drop(items.NATURE_RUNE, 100),
        Drop(items.WATER_RUNE, 750),
        Drop(items.WATER_RUNE, 250),
        Drop(items.RAW_EMERALD, 150),
        Drop(items.LIMPWURT_ROOT, 50),
        MEGARARE_LOOT_TABLE(0.2)
    ))

DARK_WIZARD = Monster(
    "dark wizard",
    LootTable(
        Drop(items.HUMAN_BONES, 1000),
        Drop(items.CLOTH_SCRAP, 900),
        Drop(items.CLOTH_SCRAP, 650),
        Drop(items.CLOTH_SCRAP, 350),
        Drop(items.FIRE_RUNE, 800),
        Drop(items.FIRE_RUNE, 700),
        Drop(items.FIRE_RUNE, 600),
        Drop(items.FIRE_RUNE, 500),
        Drop(items.CHAOS_RUNE, 750),
        Drop(items.CHAOS_RUNE, 550),
        Drop(items.CHAOS_RUNE, 250),
        Drop(items.DEATH_RUNE, 600),
        Drop(items.DEATH_RUNE, 300),
        Drop(items.BRIOLETTE_RUBY, 150),
        Drop(items.MAHOGANY_WAND, 50),
        MEGARARE_LOOT_TABLE(1.0)
    ))

RED_DRAGON = Monster(
    "red dragon",
    LootTable(
        Drop(items.DRAGON_BONES, 1000),
        Drop(items.DRAGON_HIDE, 900),
        Drop(items.DRAGON_HIDE, 800),
        Drop(items.DRAGON_HIDE, 650),
        Drop(items.DRAGON_HIDE, 400),
        Drop(items.DRAGON_HIDE, 250),
        Drop(items.FIRE_ESSENCE, 600),
        Drop(items.ADAMANTIUM_ARROW, 500),
        Drop(items.ADAMANTIUM_ARROW, 400),
        Drop(items.ADAMANTIUM_ARROW, 300),
        Drop(items.ADAMANTIUM_ARROW, 200),
        Drop(items.ADAMANTIUM_ARROW, 100),
        Drop(items.DRAGON_TOOTH, 400),
        Drop(items.DRACONIC_ESSENCE, 100),
        Drop(items.DRAGON_EGG, 20),
        MEGARARE_LOOT_TABLE(2.25)
    ))
