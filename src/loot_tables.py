"""
This module contains the Drop class to define the potential for one item to be dropped,
and the LootTable class to represent a collection of Drops that can be rolled for.
It also defines the MEGARARE_LOOT_TABLE.
"""

from typing import Iterable, Iterator
from src import items
from src.items import Item

class Drop:
    """Represents a potential drop of an item, with a certain chance to drop."""

    MAX_DROP_CHANCE = 1000

    def __init__(self, item:Item, drop_chance:int, quantity:int=1):
        """
        Args:
            item (Item): The item that can be dropped.
            quantity (int): The quantity of the item that can be dropped.
            drop_chance (int): The weight of this item dropping, clamped from 1 to Drop.MAX_DROP_CHANCE.
        """
        drop_chance = max(1, min(drop_chance, Drop.MAX_DROP_CHANCE))
        self._item = item
        self._quantity = quantity
        self._drop_chance = drop_chance
    
    @property
    def item(self) -> Item:
        return self._item
    
    @property
    def quantity(self) -> int:
        return self._quantity
    
    @property
    def drop_chance(self) -> int:
        return self._drop_chance

class LootTable(Iterable[Drop]):
    """Represents a loot table, which is a collection of items and their drop chances."""

    def __init__(self, *drops:Drop|Iterable[Drop]):
        """
        Args:
            drops (Drop | Iterable[Drop]): The drops to be added to the loot table.
        """

        self._table: list[Drop] = []
        for entry in drops:
            if isinstance(entry, Drop):
                self._table.append(entry)
            elif isinstance(entry, Iterable): #type:ignore
                for subentry in entry:
                    if isinstance(subentry, Drop): #type:ignore
                        self._table.append(subentry)
                    else:
                        raise ValueError("Invalid drop: " + str(subentry))
            else:
                raise ValueError("Invalid drop: " + str(entry))
    
    def __iter__(self) -> Iterator[Drop]:
        return iter(self._table)
    
    @property
    def table(self) -> list[Drop]:
        return self._table

    def roll(self) -> dict[Item, int]:
        """
        Roll for each item in the loot table and returns a dictionary of the items that were dropped and their quantities.
        """

        from random import randint
        dropped_items: dict[Item, int] = {}
        for drop in self._table:
            roll = randint(1, Drop.MAX_DROP_CHANCE)
            if roll <= drop.drop_chance:
                if drop.item not in dropped_items:
                    dropped_items[drop.item] = drop.quantity
                else:
                    dropped_items[drop.item] += drop.quantity
        return dropped_items

def MEGARARE_LOOT_TABLE(chance_factor:float = 1.0) -> LootTable:
    """
    Loot table with incredibly rare items. Should not be tied to any specific monster.
    Drop chances are scaled by the given chance factor.

    Args:
        chance_factor (float) = 1.0: Factor to scale the drop chances of the items in the table by. Drops may be scaled to 0%.
    """

    if chance_factor < 0:
        raise ValueError("Chance factor must be non-negative.")

    return LootTable(
        Drop(items.IMPERIAL_COIN, int(10 * chance_factor)),
        Drop(items.CORRUPTED_DIAMOND, int(7 * chance_factor)),
        Drop(items.ANCIENT_RUNE, int(5 * chance_factor)),
        Drop(items.LOST_TALISMAN, int(3 * chance_factor)),
        Drop(items.CATALYTIC_HEART, int(2 * chance_factor)),
        Drop(items.APOTHEOTIC_CORE, int(1 * chance_factor))
    )
