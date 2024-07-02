test = {
  'name': 'Problem Lambda the Free',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '1201c1ae92c2aa2d2ca6d5ddb4a8da7c',
          'choices': [
            'A lambda expression does not automatically bind the function object that it returns to any name.',
            'A lambda expression cannot have more than two parameters.',
            'A lambda expression cannot return another function.',
            'A def statement can only have one line in its body.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          Which of the following statements describes a difference between a def statement
          and a lambda expression?
          """
        },
        {
          'answer': '57a41c7b63c6e105258d48ade39aac7c',
          'choices': [
            'one',
            'two',
            'three',
            'Not enough information'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          How many parameters does the following lambda expression have?
          lambda a, b: c + d
          """
        },
        {
          'answer': '75a9cd36d8beafc3fae0e269c7be7051',
          'choices': [
            'When the function returned by the lambda expression is called.',
            'When you assign the lambda expression to a name.',
            'When the lambda expression is evaluated.',
            'When you pass the lambda expression into another function.'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When is the return expression of a lambda expression executed?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> lambda x: x  # A lambda expression with one parameter x
          659ff188e141211878c9838e1df2c80e
          # locked
          >>> a = lambda x: x  # Assigning a lambda function to the name a
          >>> a(5)
          05ddbbaaec055d602188518c1a14dc43
          # locked
          >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
          62cb7be5b3f27b8761401e9f99897a30
          # locked
          >>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
          >>> c = b(88)
          >>> c
          659ff188e141211878c9838e1df2c80e
          # locked
          >>> c()
          584ab9b274fbed36e374e534a2e6d109
          # locked
          >>> d = lambda f: f(4)  # They can have functions as arguments as well
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          71802dc4b7796a636f98e42a1d36f0c3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> x = None # remember to review the rules of WWPD given above!
          >>> x
          >>> lambda x: x
          659ff188e141211878c9838e1df2c80e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> # Pay attention to the scope of variables
          >>> z = 3
          >>> e = lambda x: lambda y: lambda: x + y + z
          >>> e(0)(1)()
          e6efc1fcfbebed28c5068a807b6cce64
          # locked
          >>> f = lambda z: x + z
          >>> f(3)
          8dfecce35cfbb620490b1aa9637bdafd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> g = lambda x: x * x
          >>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
          8dfecce35cfbb620490b1aa9637bdafd
          # locked
          >>> higher_order_lambda(g)(2)
          e6efc1fcfbebed28c5068a807b6cce64
          # locked
          >>> call_thrice = lambda f: lambda x: f(f(f(x)))
          >>> call_thrice(lambda y: y + 1)(0)
          62cb7be5b3f27b8761401e9f99897a30
          # locked
          >>> print_lambda = lambda z: print(z)
          >>> print_lambda
          659ff188e141211878c9838e1df2c80e
          # locked
          >>> one_thousand = print_lambda(1000)
          15252ac63a27e53e5ab22fd53fe77893
          # locked
          >>> one_thousand
          5c5b429063049b010ee9d6da4aff0f09
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
