test = {
  'name': 'Problem 4',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'answer': '6421c341bf2d6fba08f83f7036110a4b',
          'choices': [
            'ThrowerAnt',
            'ShortThrower',
            'LongThrower',
            'Bee'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What class do ShortThrower and LongThrower inherit from?'
        },
        {
          'answer': '518cf1abbe2dae8aa23750b848467c41',
          'choices': [
            'A regular ThrowerAnt can only attack Bees at least 3 places away',
            'A regular ThrowerAnt can only attack Bees at most 3 places away',
            'A regular ThrowerAnt can only attack Bees at most 5 places away',
            'There is no restriction on how far a regular ThrowerAnt can throw'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What constraint does a regular ThrowerAnt have on its throwing distance?'
        },
        {
          'answer': '25ee49b03ca2512edbe84614f50731c6',
          'choices': [
            'A LongThrower can only attack Bees at least 5 places away',
            'A LongThrower can only attack Bees at least 3 places away',
            'A LongThrower can only attack Bees at most 5 places away',
            'There is no restriction on how far a LongThrower can throw'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What constraint does a LongThrower have on its throwing distance?'
        },
        {
          'answer': 'dca6b74bba9df322000a79d3f521517a',
          'choices': [
            'A ShortThrower can only attack Bees at least 3 places away',
            'A ShortThrower can only attack Bees at most 3 places away',
            'A ShortThrower can only attack Bees at most 5 places away',
            'There is no restriction on how far a ShortThrower can throw'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What constraint does a ShortThrower have on its throwing distance?'
        },
        {
          'answer': 'cad237b037db9bc56ead0ba408e535b0',
          'choices': [
            'The closest Bee in front of it within range',
            'The closest Bee behind it within range',
            'Any Bee in its current Place',
            'Any Bee within range'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          With the addition of these new ThrowerAnt subclasses, we must modify
          our definition of nearest_bee. Now what Bee should ThrowerAnts throw
          at?
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
          >>> # Testing Long/ShortThrower parameters
          >>> ShortThrower.food_cost
          1218df75a941ebc08cec539b1f16208f
          # locked
          >>> LongThrower.food_cost
          1218df75a941ebc08cec539b1f16208f
          # locked
          >>> short_t = ShortThrower()
          >>> long_t = LongThrower()
          >>> short_t.health
          10d7626438082950badf2b6216f9b0a8
          # locked
          >>> long_t.health
          10d7626438082950badf2b6216f9b0a8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from ants import *
          >>> LongThrower.is_implemented
          True
          >>> ShortThrower.is_implemented
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Test ShortThrower hit
          >>> ant = ShortThrower()
          >>> in_range = Bee(2)
          >>> gamestate.places['tunnel_0_0'].add_insect(ant)
          >>> gamestate.places["tunnel_0_3"].add_insect(in_range)
          >>> ant.action(gamestate)
          >>> in_range.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing ShortThrower miss
          >>> ant = ShortThrower()
          >>> out_of_range = Bee(2)
          >>> gamestate.places["tunnel_0_0"].add_insect(ant)
          >>> gamestate.places["tunnel_0_4"].add_insect(out_of_range)
          >>> ant.action(gamestate)
          >>> out_of_range.health
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Test LongThrower Hit
          >>> ant = LongThrower()
          >>> in_range = Bee(2)
          >>> gamestate.places['tunnel_0_0'].add_insect(ant)
          >>> gamestate.places["tunnel_0_5"].add_insect(in_range)
          >>> ant.action(gamestate)
          >>> in_range.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing LongThrower miss
          >>> ant = LongThrower()
          >>> out_of_range = Bee(2)
          >>> gamestate.places["tunnel_0_0"].add_insect(ant)
          >>> gamestate.places["tunnel_0_4"].add_insect(out_of_range)
          >>> ant.action(gamestate)
          >>> out_of_range.health
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing LongThrower miss next to the hive
          >>> ant = LongThrower()
          >>> gamestate.places["tunnel_0_4"].add_insect(ant)
          >>> ant.action(gamestate) # should not error
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing LongThrower targets farther one
          >>> ant = LongThrower()
          >>> out_of_range = Bee(2)
          >>> in_range = Bee(2)
          >>> gamestate.places["tunnel_0_0"].add_insect(ant)
          >>> gamestate.places["tunnel_0_4"].add_insect(out_of_range)
          >>> gamestate.places["tunnel_0_5"].add_insect(in_range)
          >>> ant.action(gamestate)
          >>> out_of_range.health
          2
          >>> in_range.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing LongThrower ignores bees outside range
          >>> thrower = LongThrower()
          >>> gamestate.places["tunnel_0_0"].add_insect(thrower)
          >>> bee1 = Bee(1001)
          >>> bee2 = Bee(1001)
          >>> gamestate.places["tunnel_0_4"].add_insect(bee1)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee2)
          >>> thrower.action(gamestate)
          >>> bee1.health
          1001
          >>> bee2.health
          1000
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing LongThrower attacks nearest bee in range
          >>> thrower = LongThrower()
          >>> gamestate.places["tunnel_0_0"].add_insect(thrower)
          >>> bee1 = Bee(1001)
          >>> bee2 = Bee(1001)
          >>> gamestate.places["tunnel_0_5"].add_insect(bee1)
          >>> gamestate.places["tunnel_0_6"].add_insect(bee2)
          >>> thrower.action(gamestate)
          >>> bee1.health
          1000
          >>> bee2.health
          1001
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing case when min_range of LongThrower is outside of the tunnel
          >>> bee = Bee(2)
          >>> ant = LongThrower()
          >>> gamestate.places["tunnel_0_6"].add_insect(ant)
          >>> gamestate.places["tunnel_0_7"].add_insect(bee)
          >>> ant.action(gamestate)
          >>> bee.health
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing if max_range is looked up in the instance
          >>> # and check that the code isnt dependent on the ants name
          >>> ant = ShortThrower()
          >>> ant.name = 'short2'
          >>> ant.max_range = 10   # Buff the ant's range
          >>> gamestate.places["tunnel_0_0"].add_insect(ant)
          >>> bee = Bee(2)
          >>> gamestate.places["tunnel_0_6"].add_insect(bee)
          >>> ant.action(gamestate)
          >>> bee.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing there is no new nearest_bee function in ShortThrower / LongThrower
          >>> assert ShortThrower.nearest_bee is ThrowerAnt.nearest_bee
          >>> assert LongThrower.nearest_bee is ThrowerAnt.nearest_bee
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
          >>> # Testing if min_range is set appropriately in ThrowerAnt
          >>> ant = ThrowerAnt()
          >>> gamestate.places["tunnel_0_0"].add_insect(ant)
          >>> bee = Bee(2)
          >>> gamestate.places["tunnel_0_0"].add_insect(bee)
          >>> ant.action(gamestate)
          >>> bee.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing if max_range is set appropriately in ThrowerAnt
          >>> ant = ThrowerAnt()
          >>> gamestate.places["tunnel_0_0"].add_insect(ant)
          >>> bee = Bee(2)
          >>> gamestate.places["tunnel_0_99"].add_insect(bee)
          >>> ant.action(gamestate)
          >>> bee.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Special thrower class that just hits things 6 away
          >>> class JustSixThrower(ThrowerAnt):
          ...   min_range = max_range = 6
          >>> ant = JustSixThrower()
          >>> gamestate.places["tunnel_0_0"].add_insect(ant)
          >>> exact_bee = Bee(2)
          >>> gamestate.places["tunnel_0_6"].add_insect(exact_bee)
          >>> ant.action(gamestate)
          >>> exact_bee.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Special thrower class that just hits things 6 away
          >>> class JustSixThrower(ThrowerAnt):
          ...   min_range = max_range = 6
          >>> ant = JustSixThrower()
          >>> gamestate.places["tunnel_0_0"].add_insect(ant)
          >>> close_bee = Bee(2)
          >>> gamestate.places["tunnel_0_5"].add_insect(close_bee)
          >>> ant.action(gamestate)
          >>> close_bee.health
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
      >>> dimensions = (1, 100)
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
          >>> # Special thrower class that just hits things 6 away
          >>> class JustSixThrower(ThrowerAnt):
          ...   min_range = max_range = 6
          >>> ant = JustSixThrower()
          >>> gamestate.places["tunnel_0_0"].add_insect(ant)
          >>> far_bee = Bee(2)
          >>> gamestate.places["tunnel_0_7"].add_insect(far_bee)
          >>> ant.action(gamestate)
          >>> far_bee.health
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing LongThrower Inheritance from ThrowerAnt
          >>> def new_action(self, gamestate):
          ...     raise NotImplementedError()
          >>> def new_throw_at(self, target):
          ...     raise NotImplementedError()
          >>> ThrowerAnt.action = new_action
          >>> test_long = LongThrower()
          >>> passed = 0
          >>> try:
          ...     test_long.action(gamestate)
          ... except NotImplementedError:
          ...     passed += 1
          >>> ThrowerAnt.action = old_thrower_action
          >>> ThrowerAnt.throw_at = new_throw_at
          >>> test_long = LongThrower()
          >>> try:
          ...     test_long.throw_at(Bee(1))
          ... except NotImplementedError:
          ...     passed += 1
          >>> ThrowerAnt.throw_at = old_throw_at
          >>> passed
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing ShortThrower Inheritance from ThrowerAnt
          >>> def new_action(self, gamestate):
          ...     raise NotImplementedError()
          >>> def new_throw_at(self, target):
          ...     raise NotImplementedError()
          >>> ThrowerAnt.action = new_action
          >>> test_short = ShortThrower()
          >>> passed = 0
          >>> try:
          ...     test_short.action(gamestate)
          ... except NotImplementedError:
          ...     passed += 1
          
          >>> ThrowerAnt.action = old_thrower_action
          >>> ThrowerAnt.throw_at = new_throw_at
          >>> test_short = ShortThrower()
          >>> try:
          ...     test_short.throw_at(Bee(1))
          ... except NotImplementedError:
          ...     passed += 1
          
          >>> ThrowerAnt.throw_at = old_throw_at
          >>> passed
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
      >>> old_thrower_action = ThrowerAnt.action
      >>> old_throw_at = ThrowerAnt.throw_at
      >>> #
      """,
      'teardown': r"""
      >>> ThrowerAnt.action = old_thrower_action
      >>> ThrowerAnt.throw_at = old_throw_at
      """,
      'type': 'doctest'
    }
  ]
}
