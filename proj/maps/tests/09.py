test = {
  'name': 'Problem 9',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a00063476a45f76feace7d55b23152a2',
          'choices': [
            'restaurant names',
            'restaurants',
            'restaurant scores'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'rate_all returns a dictionary. What are the keys of this dictionary?'
        },
        {
          'answer': 'a2e23b1e6d342abe03197c673d0a74da',
          'choices': [
            'numbers - a mix of user scores and predicted scores',
            'numbers - user scores only',
            'numbers - predicted scores only',
            'numbers - mean restaurant scores',
            'lists - list of all restaurant scores'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What are the values of the returned dictionary?'
        },
        {
          'answer': 'a1b936b987dd1d8e04c4ca1970f64dea',
          'choices': [
            'a list of restaurants reviewed by the user',
            'a list of all possible restaurants',
            'a list of scores for restaurants reviewed by the user'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'In rate_all, what does the variable reviewed represent?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('Mr. Mean Score Minus One', [
          ...     make_review('A', 3),
          ...     make_review('B', 4),
          ...     make_review('C', 1),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [1, 2], [], 4, [
          ...         make_review('A', 4),
          ...         make_review('A', 4)
          ...     ]),
          ...     make_restaurant('B', [4, 2], [], 3, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 4], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3.5),
          ...     ]),
          ... ]
          >>> restaurants = {restaurant_name(r): r for r in cluster}
          >>> recommend.ALL_RESTAURANTS = cluster
          >>> to_rate = cluster[2:]
          >>> fns = [restaurant_price, restaurant_mean_score]
          >>> scores = rate_all(user, to_rate, fns)
          >>> type(scores)
          <class 'dict'>
          >>> len(scores) # Only the restaurants passed to rate_all
          2
          >>> scores['C'] # A restaurant scored by the user (should be an integer)
          1
          >>> round(scores['D'], 5) # A predicted score (should be a decimal)
          2.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('Mr. Mean Score Minus One', [
          ...     make_review('A', 3),
          ...     make_review('B', 4),
          ...     make_review('C', 1),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [1, 2], [], 4, [
          ...         make_review('A', 4),
          ...         make_review('A', 4)
          ...     ]),
          ...     make_restaurant('B', [4, 2], [], 3, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 2)
          ...     ]),
          ...     make_restaurant('D', [4, 4], [], 3.5, [
          ...         make_review('D', 2.5),
          ...         make_review('D', 3.5),
          ...     ]),
          ... ]
          >>> recommend.ALL_RESTAURANTS = cluster
          >>> to_rate = cluster[2:]
          >>> fns = [restaurant_price, restaurant_mean_score]
          >>> scores = rate_all(user, to_rate, fns)
          >>> type(scores)
          <class 'dict'>
          >>> len(scores) # Only the restaurants passed to rate_all
          2
          >>> scores['C'] # A restaurant scored by the user (should be an integer)
          1
          >>> round(scores['D'], 5) # A predicted score (should be a decimal)
          2.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> test.swap_implementations(recommend)
      >>> from recommend import *
      """,
      'teardown': r"""
      >>> test.restore_implementations(recommend)
      """,
      'type': 'doctest'
    }
  ]
}
