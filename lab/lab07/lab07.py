"""
C88C Summer 2024:

Please credit any folks in C88C that you collaborated with,
and any online sources you searched for.
Remember, it's OK to ask for help, and to search for topics, but
you may not search for specific solutions or copy any code directly.

List Collaborators:

Credit Any Online Sources (google searches, etc):


"""


# Car

class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)



# Quidditch

class QuidditchPlayer:
    def __init__(self, name, energy):
        """
        QuidditchPlayers have a name and begin with some amount of energy.
        """
        self.name = name
        self.energy = energy


class Beater(QuidditchPlayer):

    def play(self, time):
        """
        >>> fred = Beater("Fred Weasley", 640)
        >>> fred.play(0)
        "You can't divide by zero!"
        >>> fred.play(40)
        'Fred Weasley played for 40 minutes'
        >>> fred.energy  # Fred lost 640 / 40 energy points
        624.0
        >>> fred.play(10)
        'Fred Weasley played for 10 minutes'
        >>> fred.energy  # Fred lost 624 / 10 energy points
        561.6
        """
        "*** YOUR CODE HERE ***"
        


class Chaser(QuidditchPlayer):
    energy_expended = 20
    
    def __init__(self, name, energy, goals):
        """
        Chasers have a name, starting energy, and number of goals scored.
        """
        "*** YOUR CODE HERE ***"
        

    def play(self, time):
        """
        >>> katie = Chaser("Katie Bell", 230, 2)
        >>> katie.play(20)
        'Katie Bell played for 20 minutes'
        >>> katie.energy
        190
        >>> katie.play(10)
        'Katie Bell played for 10 minutes'
        >>> katie.energy
        150
        >>> ginny = Chaser("Ginny Weasley", 400, 3)
        >>> ginny.play(45)
        'Ginny Weasley played for 45 minutes'
        >>> ginny.energy
        338.0
        """
        "*** YOUR CODE HERE ***"
        


class Seeker(QuidditchPlayer):
    energy_expended = 5

    def play(self, time):
        """
        >>> harry = Seeker("Harry Potter", 700)
        >>> harry.play(30)
        'Harry Potter played for 30 minutes'
        >>> harry.energy
        550
        >>> harry.play(10)
        'Harry Potter played for 10 minutes'
        >>> harry.energy
        500
        """
        "*** YOUR CODE HERE ***"
        


class Keeper(QuidditchPlayer):
    energy_expended = 50

    def play(self, time):
        """
        >>> oliver = Keeper("Oliver Wood", 380)
        >>> oliver.play(45)
        'Oliver Wood played for 45 minutes'
        >>> oliver.energy
        260.0
        >>> oliver.play(10)
        'Oliver Wood played for 10 minutes'
        >>> oliver.energy
        260.0
        """
        "*** YOUR CODE HERE ***"
        

