test = {
  'name': 'Problem 3',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a9e49cff4ec1d6708c0b0b1ad10cc1aa',
          'choices': [
            r"""
            The ThrowerAnt finds the nearest place including and in front of its
            own place that has Bees and throws at a random Bee in that place
            """,
            r"""
            The ThrowerAnt finds the nearest place behind its own place
            that has Bees and throws at a random Bee in that place
            """,
            r"""
            The ThrowerAnt finds the nearest place in either direction that has
            Bees and throws at a random Bee in that place
            """,
            'The ThrowerAnt throws at a random Bee in its own Place'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What Bee should a ThrowerAnt throw at?'
        },
        {
          'answer': '541f2bab3e25cf2a2933c3a8a032b054',
          'choices': [
            "The place's entrance instance attribute",
            "The place's exit instance attribute",
            'Increment the place by 1',
            'Decrement the place by 1'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How do you get the Place object in front (on the right) of another Place object?'
        },
        {
          'answer': '735a4a66d469c96e84cc49330d20459f',
          'choices': [
            'The Hive',
            'None',
            'An empty Place'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the entrance of the first Place in a tunnel (i.e. where do the bees enter from)?'
        },
        {
          'answer': '078efebbf87ddce7bbae7026281f4aeb',
          'choices': [
            'by using the is_hive attribute of the place instance',
            'by checking the bees attribute of the place instance',
            'by checking the ant attribute of the place instance'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How can you determine if a given Place is the Hive?'
        },
        {
          'answer': '14930134252cc105652152c49c4dbbc1',
          'choices': [
            'None',
            'A random Bee in the Hive',
            'The closest Bee behind the ThrowerAnt'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What should nearest_bee return if there is no Bee in front of the ThrowerAnt in the tunnel?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing nearest_bee
          >>> near_bee = Bee(2) # A Bee with 2 health
          >>> far_bee = Bee(3)  # A Bee with 3 health
          >>> hive_bee = Bee(4) # A Bee with 4 health
          >>> hive_place = gamestate.beehive
          >>> hive_place.is_hive # Check if this place is the Hive
          154afc22815a37701b5fa71e532da526
          # locked
          >>> hive_place.add_insect(hive_bee)
          >>> thrower.nearest_bee() is hive_bee # Bees in the Hive can never be attacked
          e0390565eddec8c7f85375354a9d8b87
          # locked
          >>> near_place = gamestate.places['tunnel_0_3']
          >>> far_place = gamestate.places['tunnel_0_6']
          >>> near_place.is_hive # Check if this place is the Hive
          e0390565eddec8c7f85375354a9d8b87
          # locked
          >>> near_place.add_insect(near_bee)
          >>> far_place.add_insect(far_bee)
          >>> nearest_bee = thrower.nearest_bee()
          >>> nearest_bee is far_bee
          e0390565eddec8c7f85375354a9d8b87
          # locked
          >>> nearest_bee is near_bee
          154afc22815a37701b5fa71e532da526
          # locked
          >>> nearest_bee.health
          1218df75a941ebc08cec539b1f16208f
          # locked
          >>> thrower.action(gamestate)    # Attack! ThrowerAnts do 1 damage
          >>> near_bee.health
          10d7626438082950badf2b6216f9b0a8
          # locked
          >>> far_bee.health
          e22b4783782de9e5b17a082cf33c6f51
          # locked
          >>> thrower.place is ant_place    # Don't change self.place!
          154afc22815a37701b5fa71e532da526
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing Nearest bee not in the beehive
          >>> beehive = gamestate.beehive
          >>> bee = Bee(2)
          >>> beehive.add_insect(bee)      # Adding a bee to the beehive
          >>> thrower.nearest_bee() is bee
          False
          >>> thrower.action(gamestate)    # Attempt to attack
          >>> bee.health                 # Bee health should not change
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees on its own square
          >>> near_bee = Bee(2)
          >>> ant_place.add_insect(near_bee)
          >>> thrower.nearest_bee() is near_bee
          True
          >>> thrower.action(gamestate)   # Attack!
          >>> near_bee.health           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees at end of tunnel
          >>> near_bee = Bee(2)
          >>> gamestate.places["tunnel_0_8"].add_insect(near_bee)
          >>> thrower.nearest_bee() is near_bee
          True
          >>> thrower.action(gamestate)   # Attack!
          >>> near_bee.health           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Test that ThrowerAnt attacks bees 4 places away
          >>> near_bee = Bee(2)
          >>> gamestate.places["tunnel_0_4"].add_insect(near_bee)
          >>> thrower.nearest_bee() is near_bee
          True
          >>> thrower.action(gamestate)   # Attack!
          >>> near_bee.health           # should do 1 damage
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing ThrowerAnt chooses a random target
          >>> bee1 = Bee(1001)
          >>> bee2 = Bee(1001)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee1)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee2)
          >>> # Throw 1000 times. The first bee should take ~1000*1/2 = ~500 damage,
          >>> # and have ~501 remaining.
          >>> for _ in range(1000):
          ...     thrower.action(gamestate)
          >>> # Test if damage to bee1 is within 6 standard deviations (~95 damage)
          >>> # If bees are chosen uniformly, this is true 99.9999998% of the time.
          >>> def dmg_within_tolerance():
          ...     return abs(bee1.health-501) < 95
          >>> dmg_within_tolerance()
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> from ants import *
          >>> ThrowerAnt.is_implemented
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
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      >>> thrower = ThrowerAnt()
      >>> ant_place = gamestate.places["tunnel_0_0"]
      >>> ant_place.add_insect(thrower)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
