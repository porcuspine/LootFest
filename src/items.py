"""
This module contains the Item class, which represents an item in the game, and constants to access
every item definition; items should likely not be directly constructed. This module also contains the ItemRarity enum.
"""

from dataclasses import dataclass
from enum import Enum

class ItemRarity(Enum):
    """Represents the rarity of an item. This property is categorical and does not itself affect drop chances."""
    MUNDANE = 0 #: Should ALWAYS and ONLY be a GUARANTEED drop
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    VERY_RARE = 4
    LEGENDARY = 5
    RELIC = 6

@dataclass(frozen=True)
class Item:
    """Represents an item in the game."""

    _name : str
    _rarity : ItemRarity = ItemRarity.COMMON

    def __init__(self, name:str, rarity:ItemRarity=ItemRarity.COMMON):
        """
        NOTICE: Items should most likely be accessed via corresponding constants in the items module and not be directly constructed.
        Args:
            name (str): The name of the item.
            rarity (ItemRarity = COMMON): The rarity of the item.
        """
        object.__setattr__(self, "_name", name)
        object.__setattr__(self, "_rarity", rarity)

    def __str__(self) -> str:
        return self._name
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def rarity(self) -> ItemRarity:
        return self._rarity
    
SMALL_BONES = Item("small bones", rarity=ItemRarity.MUNDANE)
HIDE_SCRAP = Item("hide scrap", rarity=ItemRarity.COMMON)
GOLD_COIN = Item("gold coin", rarity=ItemRarity.COMMON)
EARTH_RUNE = Item("earth rune", rarity=ItemRarity.UNCOMMON)
IRON_DAGGER = Item("iron dagger", rarity=ItemRarity.COMMON)
BRONZE_ARROW = Item("bronze arrow", rarity=ItemRarity.COMMON)
GOBLIN_CHAINMAIL = Item("goblin chainmail", rarity=ItemRarity.RARE)
GOBLIN_TRINKET = Item("goblin trinket", rarity=ItemRarity.VERY_RARE)
BIG_BONES = Item("big bones", rarity=ItemRarity.MUNDANE)
GIANT_TOE = Item("giant toe", rarity=ItemRarity.COMMON)
STEEL_ARROW = Item("steel arrow", rarity=ItemRarity.COMMON)
NATURE_RUNE = Item("nature rune", rarity=ItemRarity.UNCOMMON)
WATER_RUNE = Item("water rune", rarity=ItemRarity.UNCOMMON)
RAW_EMERALD = Item("raw emerald", rarity=ItemRarity.RARE)
LIMPWURT_ROOT = Item("limpwurt root", rarity=ItemRarity.VERY_RARE)
HUMAN_BONES = Item("human bones", rarity=ItemRarity.MUNDANE)
CLOTH_SCRAP = Item("cloth scrap", rarity=ItemRarity.COMMON)
FIRE_RUNE = Item("fire rune", rarity=ItemRarity.UNCOMMON)
CHAOS_RUNE = Item("chaos rune", rarity=ItemRarity.UNCOMMON)
DEATH_RUNE = Item("death rune", rarity=ItemRarity.UNCOMMON)
BRIOLETTE_RUBY = Item("briolette ruby", rarity=ItemRarity.RARE)
MAHOGANY_WAND = Item("mahogany wand", rarity=ItemRarity.VERY_RARE)
DRAGON_BONES = Item("dragon bones", rarity=ItemRarity.MUNDANE)
DRAGON_HIDE = Item("dragon hide", rarity=ItemRarity.COMMON)
FIRE_ESSENCE = Item("fire essence", rarity=ItemRarity.RARE)
ADAMANTIUM_ARROW = Item("adamantium arrow", rarity=ItemRarity.UNCOMMON)
DRAGON_TOOTH = Item("dragon tooth", rarity=ItemRarity.RARE)
DRACONIC_ESSENCE = Item("draconic essence", rarity=ItemRarity.VERY_RARE)
DRAGON_EGG = Item("dragon egg", rarity=ItemRarity.LEGENDARY)

#Megarares
IMPERIAL_COIN = Item("imperial coin", rarity=ItemRarity.RELIC)
CORRUPTED_DIAMOND = Item("corrupted diamond", rarity=ItemRarity.RELIC)
ANCIENT_RUNE = Item("ancient rune", rarity=ItemRarity.RELIC)
LOST_TALISMAN = Item("lost talisman", rarity=ItemRarity.RELIC)
CATALYTIC_HEART = Item("catalytic heart", rarity=ItemRarity.RELIC)
APOTHEOTIC_CORE = Item("apotheotic core", rarity=ItemRarity.RELIC)
