test = {
  'name': 'Problem 7',
  'points': 7,
  'suites': [
    {
      'cases': [
        {
          'answer': '9f0d8b8a6df0430c5744a1850197d7b5',
          'choices': [
            r"""
            instance, each HungryAnt instance chews independently of other
            HungryAnt instances
            """,
            'instance, all HungryAnt instances in the game chew simultaneously',
            r"""
            class, each HungryAnt instance chews independently of other
            HungryAnt instances
            """,
            'class, all HungryAnt instances in the game chew simultaneously'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Should chew_countdown be an instance or class attribute? Why?'
        },
        {
          'answer': '62638a4740f4fa838124f56d235e9d16',
          'choices': [
            'When it is not chewing, i.e. when its chew_countdown attribute is 0',
            'When it is chewing, i.e. when its chew_countdown attribute is at least 1',
            'Each turn',
            'Whenever a Bee is in its place'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When is a HungryAnt able to eat a Bee?'
        },
        {
          'answer': 'b4ab7184847f6c944b437b024fa456ce',
          'choices': [
            'A random Bee in the same place as itself',
            'The closest Bee in front of it',
            'The closest Bee behind it',
            'The closest Bee in either direction'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When a HungryAnt is able to eat, which Bee does it eat?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing HungryAnt parameters
          >>> hungry = HungryAnt()
          >>> HungryAnt.food_cost
          5d2dcf69388c48f6f6885e4efff23a30
          # locked
          >>> hungry.health
          10d7626438082950badf2b6216f9b0a8
          # locked
          >>> hungry.chew_duration
          e22b4783782de9e5b17a082cf33c6f51
          # locked
          >>> hungry.chew_countdown
          40031e7755cbca1da159a160d30dbc21
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Abstraction tests
          >>> original = Ant.__init__
          >>> Ant.__init__ = lambda self, health: print("init")  # If this errors, you are not calling the parent constructor correctly.
          >>> hungry = HungryAnt()
          init
          >>> Ant.__init__ = original
          >>> hungry = HungryAnt()
          >>> # Class vs Instance attributes
          >>> hasattr(HungryAnt, 'chew_countdown')  # chew_countdown should be an instance attribute
          False
          >>> hungry.chew_countdown  # HungryAnt is ready to eat a bee
          0
          >>> HungryAnt.chew_duration
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt eats and chews
          >>> hungry = HungryAnt()
          >>> bee1 = Bee(1000)              # A Bee with 1000 health
          >>> place = gamestate.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> place.add_insect(bee1)         # Add the Bee to the same place as HungryAnt
          >>> hungry.action(gamestate)
          >>> bee1.health
          0
          >>> bee2 = Bee(1)                 # A Bee with 1 health
          >>> place.add_insect(bee2)
          >>> for _ in range(3):
          ...     hungry.action(gamestate)     # Digesting...not eating
          >>> bee2.health
          1
          >>> hungry.action(gamestate)
          >>> bee2.health
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt eats and chews
          >>> hungry = HungryAnt()
          >>> super_bee, wimpy_bee = Bee(1000), Bee(1)
          >>> place = gamestate.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> place.add_insect(super_bee)
          >>> hungry.action(gamestate)         # super_bee is no match for HungryAnt!
          >>> super_bee.health
          40031e7755cbca1da159a160d30dbc21
          # locked
          >>> place.add_insect(wimpy_bee)
          >>> for _ in range(3):
          ...     hungry.action(gamestate)     # chewing...not eating
          >>> wimpy_bee.health
          10d7626438082950badf2b6216f9b0a8
          # locked
          >>> hungry.action(gamestate)         # back to eating!
          >>> wimpy_bee.health
          40031e7755cbca1da159a160d30dbc21
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt only waits when chewing
          >>> hungry = HungryAnt()
          >>> place = gamestate.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> # Wait a few turns before adding Bee
          >>> for _ in range(5):
          ...     hungry.action(gamestate)  # shouldn't be chewing
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> hungry.action(gamestate)  # Eating time!
          >>> bee.health
          0
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> for _ in range(3):
          ...     hungry.action(gamestate)     # Should be chewing
          >>> bee.health
          3
          >>> hungry.action(gamestate)
          >>> bee.health
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt chew duration looked up on instance
          >>> very_hungry = HungryAnt()  # Add very hungry caterpi- um, ant
          >>> HungryAnt.chew_duration = 0
          >>> place = gamestate.places["tunnel_0_0"]
          >>> place.add_insect(very_hungry)
          >>> for _ in range(100):
          ...     place.add_insect(Bee(3))
          >>> for _ in range(100):
          ...     very_hungry.action(gamestate)   # Eat all the bees!
          >>> len(place.bees)
          0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt dies while eating
          >>> hungry = HungryAnt()
          >>> place = gamestate.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> place.add_insect(Bee(3))
          >>> hungry.action(gamestate)
          >>> len(place.bees)
          0
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> bee.action(gamestate) # Bee kills chewing ant
          >>> place.ant is None
          True
          >>> len(place.bees)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt can't eat a bee at another space
          >>> hungry = HungryAnt()
          >>> gamestate.places["tunnel_0_0"].add_insect(hungry)
          >>> gamestate.places["tunnel_0_1"].add_insect(Bee(3))
          >>> hungry.action(gamestate)
          >>> len(gamestate.places["tunnel_0_1"].bees)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # test proper call to death callback
          >>> original_death_callback = Insect.death_callback
          >>> Insect.death_callback = lambda x: print("insect died")
          >>> ant = HungryAnt()
          >>> bee = Bee(1000)              # A Bee with 1000 health
          >>> place = gamestate.places["tunnel_0_0"]
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> ant.action(gamestate) # if you fail this test you probably didn't correctly call Ant.reduce_health or Insect.reduce_health
          insect died
          >>> Insect.death_callback = original_death_callback
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing HungryAnt removes bee when eating.
          >>> hungry = HungryAnt()
          >>> place = gamestate.places["tunnel_0_0"]
          >>> place.add_insect(hungry)
          >>> place.add_insect(Bee(3))
          >>> place.add_insect(Bee(3))
          >>> hungry.action(gamestate)
          >>> len(place.bees)
          1
          >>> bee = Bee(3)
          >>> place.add_insect(bee)
          >>> bee.action(gamestate) # Bee kills chewing ant
          >>> place.ant is None
          True
          >>> len(place.bees)
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> from ants import *
          >>> HungryAnt.is_implemented
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
