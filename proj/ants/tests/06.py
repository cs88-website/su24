test = {
  'name': 'Problem 6',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': '846ee8e35ba6b7a71285553d2b6eb865',
          'choices': [
            'Ant',
            'ThrowerAnt',
            'HungryAnt',
            'The WallAnt class does not inherit from any class'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What class does WallAnt inherit from?'
        },
        {
          'answer': '3560f5c897e42f3744228f370b181d78',
          'choices': [
            'A WallAnt takes no action each turn',
            'A WallAnt increases its own health by 1 each turn',
            'A WallAnt reduces its own health by 1 each turn',
            'A WallAnt attacks all the Bees in its place each turn'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': "What is a WallAnt's action?"
        },
        {
          'answer': 'efe758bb607265f51ff5c0c8fffafca4',
          'choices': [
            'Ant subclasses inherit the action method from the Insect class',
            'Ant subclasses inherit the action method from the Ant class',
            'Ant subclasses do not inherit the action method from any class'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Where do Ant subclasses inherit the action method from?'
        },
        {
          'answer': '40d207151baf8f4364ce09eb3b7d86da',
          'choices': [
            'Nothing',
            'Throw a leaf at the nearest Bee',
            'Move to the next place',
            'Reduce the health of all Bees in its place'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If a subclass of Ant does not override the action method, what is the
          default action?
          """
        },
        {
          'answer': '0af2bbf5dac788ad67a49cb25e9288f2',
          'choices': [
            'class, all Ants of the same subclass have the same health',
            'class, all Ants have the same health no matter what type of Ant it is',
            'instance, all Ants keep track of their own health',
            'instance, all Ants have different default starting healths'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What type of attribute is health?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing WallAnt parameters
          >>> wall = WallAnt()
          >>> wall.name
          'Wall'
          >>> wall.health
          4
          >>> # `health` should not be a class attribute
          >>> not hasattr(WallAnt, 'health') # hasattr checks if the WallAnt class has a class attribute called 'health'
          True
          >>> WallAnt.food_cost
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Abstraction tests
          >>> original = Ant.__init__
          >>> Ant.__init__ = lambda self, health: print("init") #If this errors, you are not calling the parent constructor correctly.
          >>> wall = WallAnt()
          init
          >>> Ant.__init__ = original
          >>> wall = WallAnt()
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing WallAnt holds strong
          >>> beehive, layout = Hive(AssaultPlan()), dry_layout
          >>> gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))
          >>> place = gamestate.places['tunnel_0_4']
          >>> wall = WallAnt()
          >>> bee = Bee(1000)
          >>> place.add_insect(wall)
          >>> place.add_insect(bee)
          >>> for i in range(3):
          ...     bee.action(gamestate)
          ...     wall.action(gamestate)   # WallAnt does nothing
          >>> wall.health
          1
          >>> bee.health
          1000
          >>> wall.place is place
          True
          >>> bee.place is place
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> from ants import *
          >>> WallAnt.is_implemented
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
