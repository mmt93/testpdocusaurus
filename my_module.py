# my_module.py

"""
This is a sample module for demonstrating pdoc.
"""

def square(num):
    """
    Returns the square of a number.

    Args:
        num (int): The number to be squared.

    Returns:
        int: The square of the number.
    """
    return num * num

class MyClass:
    """
    A simple class for demonstrating pdoc.
    """

    def __init__(self, name):
        """
        Initializes an instance of MyClass. Test

        Args:
            name (str): The name of the instance.
        """
        self.name = name

    def greet(self):
        """
        Prints a greeting message.

        Returns:
            str: The greeting message.
        """
        message = f"Hello, my name is {self.name}."
        print(message)
        return message