"""Optional questions for Homework 7"""

class Keyboard:
    """A Keyboard takes in a list of buttons, and has a
    dictionary of positions as keys, and Buttons as values.

    >>> b1 = Button("button1", "H")
    >>> b2 = Button("button2", "I")
    >>> k = Keyboard([b1, b2])
    >>> "button1" in k.buttons.keys() # Make sure to add the button to dictionary
    True
    >>> k.buttons["button1"].letter
    'H'
    >>> k.buttons["button1"].name
    'button1'
    >>> k.press("button1")
    'H'
    >>> k.press("button100")
    ''
    >>> b1.pressed
    1
    >>> b2.pressed
    0
    >>> k.typing(["button1", "button2"])
    'HI'
    >>> k.typing(["button2", "button1"])
    'IH'
    >>> b1.pressed # make sure typing calls press!
    3
    >>> b2.pressed
    2
    """

    def __init__(self, buttons):
        self.buttons = {}
        "*** YOUR CODE HERE ***"

    def press(self, name):
        """Takes in a name of the button pressed, and
        returns that button's letter. Return an empty string 
        if the button does not exist. You can access the keys 
        of a dictionary d with d.keys(). """
        "*** YOUR CODE HERE ***"

    def typing(self, typing_input):
        """Takes in a list of names of buttons to be pressed, and
        returns the total output. Make sure to call self.press"""
        "*** YOUR CODE HERE ***"

class Button:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter
        self.pressed = 0

