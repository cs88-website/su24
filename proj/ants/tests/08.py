test = {
  'name': 'Problem 8',
  'points': 7,
  'suites': [
    {
      'cases': [
        {
          'answer': 'aa071c4b2e09ae38b3a6c2b46e35631b',
          'choices': [
            'The Ant instance that is in the same place as itself',
            'The Ant instance in the place closest to its own place',
            'A random Ant instance in the gamestate',
            'All the Ant instances in the gamestate'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which Ant does a BodyguardAnt guard?'
        },
        {
          'answer': '1e7b699e037562ebb2a4d021a1d46a64',
          'choices': [
            'By protecting the ant from Bees and allowing it to perform its original action',
            'By attacking Bees that try to attack it',
            "By increasing the ant's health",
            'By allowing Bees to pass without attacking'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How does a BodyguardAnt guard its ant?'
        },
        {
          'answer': 'a098286a9b3b3346f4903a9af0c61c61',
          'choices': [
            "In the BodyguardAnt's ant_contained instance attribute",
            "In the BodyguardAnt's ant_contained class attribute",
            "In its place's ant instance attribute",
            "Nowhere, a BodyguardAnt has no knowledge of the ant that it's protecting"
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Where is the ant contained by a BodyguardAnt stored?'
        },
        {
          'answer': '431c118bcc729d4300de549e48da117f',
          'choices': [
            r"""
            When exactly one of the Ant instances is a container and the
            container ant does not already contain another ant
            """,
            'When exactly one of the Ant instances is a container',
            'When both Ant instances are containers',
            'There can never be two Ant instances in the same place'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When can a second Ant be added to a place that already contains an Ant?'
        },
        {
          'answer': 'eba41010f7a59f4d3fb7587b44e4c595',
          'choices': [
            'The Container Ant',
            'The Ant being contained',
            'A list containing both Ants',
            'Whichever Ant was placed there first'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If two Ants occupy the same Place, what is stored in that place's ant
          instance attribute?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing BodyguardAnt parameters
          >>> bodyguard = BodyguardAnt()
          >>> BodyguardAnt.food_cost
          5d2dcf69388c48f6f6885e4efff23a30
          # locked
          >>> bodyguard.health
          1218df75a941ebc08cec539b1f16208f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Abstraction tests
          >>> original = ContainerAnt.__init__
          >>> ContainerAnt.__init__ = lambda self, health: print("init") #If this errors, you are not calling the parent constructor correctly.
          >>> bodyguard = BodyguardAnt()
          init
          >>> ContainerAnt.__init__ = original
          >>> bodyguard = BodyguardAnt()
          >>> hasattr(bodyguard, 'ant_contained')
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
          >>> bodyguard = BodyguardAnt()
          >>> bodyguard.action(gamestate) # Action without contained ant should not error
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Bodyguard ant added before another ant
          >>> bodyguard = BodyguardAnt()
          >>> other_ant = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(bodyguard)  # Bodyguard in place first
          >>> place.add_insect(other_ant)
          >>> place.ant is bodyguard
          154afc22815a37701b5fa71e532da526
          # locked
          >>> bodyguard.ant_contained is other_ant
          154afc22815a37701b5fa71e532da526
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Bodyguard ant can be added after another ant
          >>> bodyguard = BodyguardAnt()
          >>> other_ant = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(other_ant)  # Other ant in place first
          >>> place.ant is other_ant
          154afc22815a37701b5fa71e532da526
          # locked
          >>> place.add_insect(bodyguard)
          >>> place.ant is bodyguard
          154afc22815a37701b5fa71e532da526
          # locked
          >>> bodyguard.ant_contained is other_ant
          154afc22815a37701b5fa71e532da526
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing bodyguard performs thrower's action
          >>> bodyguard = BodyguardAnt()
          >>> thrower = ThrowerAnt()
          >>> bee = Bee(2)
          >>> # Place bodyguard before thrower
          >>> gamestate.places["tunnel_0_0"].add_insect(bodyguard)
          >>> gamestate.places["tunnel_0_0"].add_insect(thrower)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee)
          >>> bodyguard.action(gamestate)
          >>> bee.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing bodyguard performs thrower's action
          >>> bodyguard = BodyguardAnt()
          >>> thrower = ThrowerAnt()
          >>> bee = Bee(2)
          >>> # Place thrower before bodyguard
          >>> gamestate.places["tunnel_0_0"].add_insect(thrower)
          >>> gamestate.places["tunnel_0_0"].add_insect(bodyguard)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee)
          >>> bodyguard.action(gamestate)
          >>> bee.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing removing a bodyguard doesn't remove contained ant
          >>> place = gamestate.places['tunnel_0_0']
          >>> bodyguard = BodyguardAnt()
          >>> test_ant = Ant(1)
          >>> # add bodyguard first
          >>> place.add_insect(bodyguard)
          >>> place.add_insect(test_ant)
          >>> gamestate.remove_ant('tunnel_0_0')
          >>> place.ant is test_ant
          True
          >>> bodyguard.place is None
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing removing a bodyguard doesn't remove contained ant
          >>> place = gamestate.places['tunnel_0_0']
          >>> bodyguard = BodyguardAnt()
          >>> test_ant = Ant(1)
          >>> # add ant first
          >>> place.add_insect(test_ant)
          >>> place.add_insect(bodyguard)
          >>> gamestate.remove_ant('tunnel_0_0')
          >>> place.ant is test_ant
          True
          >>> bodyguard.place is None
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing bodyguarded ant keeps instance attributes
          >>> test_ant = Ant()
          >>> def new_action(gamestate):
          ...     test_ant.health += 9000
          >>> test_ant.action = new_action
          >>> place = gamestate.places['tunnel_0_0']
          >>> bodyguard = BodyguardAnt()
          >>> place.add_insect(test_ant)
          >>> place.add_insect(bodyguard)
          >>> place.ant.action(gamestate)
          >>> place.ant.ant_contained.health
          9001
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing single BodyguardAnt cannot hold two other ants
          >>> bodyguard = BodyguardAnt()
          >>> first_ant = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(bodyguard)
          >>> place.add_insect(first_ant)
          >>> second_ant = ThrowerAnt()
          >>> place.add_insect(second_ant)
          Traceback (most recent call last):
          ...
          AssertionError: Two ants in tunnel_0_0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing BodyguardAnt cannot hold another BodyguardAnt
          >>> bodyguard1 = BodyguardAnt()
          >>> bodyguard2 = BodyguardAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(bodyguard1)
          >>> place.add_insect(bodyguard2)
          Traceback (most recent call last):
          ...
          AssertionError: Two ants in tunnel_0_0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing BodyguardAnt takes all the damage
          >>> thrower = ThrowerAnt()
          >>> bodyguard = BodyguardAnt()
          >>> bee = Bee(1)
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(thrower)
          >>> place.add_insect(bodyguard)
          >>> place.add_insect(bee)
          >>> bodyguard.health
          2
          >>> bee.action(gamestate)
          >>> (bodyguard.health, thrower.health)
          (1, 1)
          >>> bee.action(gamestate)
          >>> (bodyguard.health, thrower.health)
          (0, 1)
          >>> bodyguard.place is None
          True
          >>> place.ant is thrower
          True
          >>> bee.action(gamestate)
          >>> thrower.health
          0
          >>> place.ant is None
          True
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
          >>> place = gamestate.places["tunnel_0_0"]
          >>> bee = Bee(3)
          >>> bodyguard = BodyguardAnt()
          >>> ant = ThrowerAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> place.add_insect(bodyguard)
          >>> bee.action(gamestate)
          >>> bee.action(gamestate)
          insect died
          >>> bee.action(gamestate) # if you fail this test you probably didn't correctly call Ant.reduce_health or Insect.reduce_health
          insect died
          >>> Insect.death_callback = original_death_callback
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
      >>> gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))
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
          >>> BodyguardAnt.is_implemented
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
