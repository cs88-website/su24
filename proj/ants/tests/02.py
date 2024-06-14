test = {
  'name': 'Problem 2',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'answer': 'fb0be894e1636bc283d3e4e9f586faa3',
          'choices': [
            r"""
            A single tile that an Ant can be placed on and that connects to
            other Places
            """,
            'The entire space where the game takes place',
            'The tunnel that bees travel through',
            'Where the bees start out in the game'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does a Place represent in the game?'
        },
        {
          'answer': '8a060fb5f87941cc197bf03eab6db796',
          'choices': [
            'When p is constructed',
            'When q is constructed',
            'Never, it is always set to None'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'p is a Place whose entrance is q and exit is r (q and r are not None). When is p.entrance first set to a non-None value?'
        },
        {
          'answer': 'b8392d3d93b632375cfbca7bd5396aac',
          'choices': [
            'When p is constructed',
            'When q is constructed',
            'Never, it is always set to None'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'p is a Place whose entrance is q and exit is r (q and r are not None). When is p.exit first set to a non-None value?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Simple test for Place
          >>> place0 = Place('place_0')
          >>> print(place0.exit)
          14930134252cc105652152c49c4dbbc1
          # locked
          >>> print(place0.entrance)
          14930134252cc105652152c49c4dbbc1
          # locked
          >>> place1 = Place('place_1', place0)
          >>> place1.exit is place0
          154afc22815a37701b5fa71e532da526
          # locked
          >>> place0.entrance is place1
          154afc22815a37701b5fa71e532da526
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing if entrances are properly initialized
          >>> tunnel_len = 9
          >>> len(gamestate.bee_entrances)
          1
          >>> tile_1 = gamestate.bee_entrances[0]
          >>> tile_2 = tile_1.exit
          >>> tile_3 = tile_2.exit
          >>> tile_1.entrance is gamestate.beehive
          True
          >>> tile_1.exit is tile_2
          True
          >>> tile_2.entrance is tile_1
          True
          >>> tile_2.exit is tile_3
          True
          >>> tile_3.entrance is tile_2
          True
          >>> tile_3.exit is gamestate.base
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
      >>> from ants_plans import *
      >>> #
      >>> # Create a test layout where the gamestate is a single row with 3 tiles
      >>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
      >>> dimensions = (1, 3)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
