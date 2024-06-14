test = {
  'name': 'Problem 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> soda_reviews = [make_review('Soda', 4.5),
          ...                 make_review('Soda', 4)]
          >>> soda = make_restaurant('Soda', [127.0, 0.1],
          ...                        ['Restaurants', 'Breakfast & Brunch'],
          ...                        1, soda_reviews)
          >>> restaurant_scores(soda)
          c52ba51cad5e79ee30b921114196f3a7
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from abstractions import *
      >>> import abstractions
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> test.swap_implementations(abstractions, rest=False)
          >>> make_review = abstractions.make_review
          >>> soda_reviews = [make_review('Soda', 4.5),
          ...                 make_review('Soda', 4)]
          >>> soda = make_restaurant('Soda', [127.0, 0.1],
          ...                        ['Restaurants', 'Breakfast & Brunch'],
          ...                        1, soda_reviews)
          >>> restaurant_scores(soda)
          [4.5, 4]
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from abstractions import *
      >>> import abstractions
      >>> import tests.test_functions as test
      """,
      'teardown': r"""
      >>> test.restore_implementations(abstractions)
      """,
      'type': 'doctest'
    }
  ]
}
