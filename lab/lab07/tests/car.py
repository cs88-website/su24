test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab07 import *
          >>> srinaths_car = Car('Tesla', 'Model S')
          >>> srinaths_car.model
          d44fbfeedd5748e8ed04de29de968251
          # locked
          >>> srinaths_car.gas = 10
          >>> srinaths_car.drive()
          08adfbe4efff8d65757aa6e3130e95d6
          # locked
          >>> srinaths_car.drive()
          ed7e31d39fdaefb22a23971c5b0eb43d
          # locked
          >>> srinaths_car.fill_gas()
          73199fd3939cadd5e1e581b76e26a9e9
          # locked
          >>> srinaths_car.gas
          e1b5abca0ce46c01fbc9ffe5da884d06
          # locked
          >>> Car.gas
          cf3b881608904e51c384abfbd72a7cc8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from lab07 import *
          >>> srinaths_car = Car('Tesla', 'Model S')
          >>> srinaths_car.wheels = 2
          >>> srinaths_car.wheels
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> Car.num_wheels
          f2991d685f624ad59b79213e20800653
          # locked
          >>> srinaths_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          ed7e31d39fdaefb22a23971c5b0eb43d
          # locked
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          >>> Car.drive(srinaths_car) # Type Error if an error occurs and Nothing if nothing is displayed
          ed7e31d39fdaefb22a23971c5b0eb43d
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
