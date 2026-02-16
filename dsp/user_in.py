"""This module contains input-related utility functions."""

from typing import Callable

def get_int(prompt:str, condition:Callable[[int], bool]|None = None) -> int:
    """
    Gets an integer from user input. The integer must satisfy the given condition if provided.
    
    Args:
        prompt (str): The prompt to display to the user.
        condition (Callable[[int], bool], optional = None): A function that takes an integer and returns a bool. Defaults to None
    """
    
    while True:
        print(prompt)
        given = input(">>> ")
        try:
            given = int(given)
            if condition is None:
                return given
            else:
                if condition(given):
                    return given
                else:
                    print("INVALID INPUT, PLEASE TRY AGAIN")
        except ValueError:
            print("INVALID INPUT, PLEASE TRY AGAIN")
