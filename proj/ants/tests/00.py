test = {
  'name': 'Problem 0',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '70e772ab89da6efa9faf6e7d3dfb0985',
          'choices': [
            r"""
            It represents health protecting the insect, so the insect can only
            be damaged when its health reaches 0
            """,
            r"""
            It represents the strength of an insect against attacks, which
            doesn't change throughout the game
            """,
            r"""
            It represents the amount of health the insect has left, so the
            insect is eliminated when it reaches 0
            """
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          What is the significance of an Insect's health attribute? Does this
          value change? If so, how?
          """
        },
        {
          'answer': '48b3cdb37b6261681ab292496acfb6c8',
          'choices': [
            'damage',
            'health',
            'place',
            'bees'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which of the following is a class attribute of the Insect class?'
        },
        {
          'answer': '54f0b3ed978cb77f4abb66cac31e881a',
          'choices': [
            'instance, each Ant instance needs its own health value',
            'instance, each Ant starts out with a different amount of health',
            'class, Ants of the same subclass all have the same amount of starting health',
            'class, when one Ant gets damaged, all ants receive the same amount of damage'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Is the health attribute of the Ant class an instance attribute or class attribute? Why?'
        },
        {
          'answer': 'f5295b4767c62ef6bcc2678487f1e86d',
          'choices': [
            'instance, each Ant does damage to bees at different rates',
            'instance, the damage an Ant depends on where the Ant is',
            'class, all Ants of the same subclass deal the same damage',
            'class, all Ants deal the same damage'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          Is the damage attribute of an Ant subclass (such as ThrowerAnt) an
          instance or class attribute? Why?
          """
        },
        {
          'answer': 'df93334c805113354eb6d6a74bcdd61f',
          'choices': [
            'Insect',
            'Place',
            'Bee',
            'Ant'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Which class do both Ant and Bee inherit from?'
        },
        {
          'answer': '8a182bb3fa50317ed8e09365c9eb84af',
          'choices': [
            r"""
            Ants and Bees both have the attributes health, damage, and place
            and the methods reduce_health and action
            """,
            r"""
            Ants and Bees both have the attribute damage and the methods
            reduce_health and action
            """,
            'Ants and Bees both take the same action each turn',
            'Ants and Bees have nothing in common'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What do instances of Ant and instances of Bee have in common? Please choose the most correct answer.'
        },
        {
          'answer': 'bc5cd86150b70eb5c32ed1f082b22ecb',
          'choices': [
            'There can be one Ant and many Bees in a single Place',
            'There can be one Bee and many Ants in a single Place',
            'There is no limit on the number of insects of any type in a single Place',
            'Only one insect can be in a single Place at a time'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          How many insects can be in a single Place at any given time in the
          game (before Problem 8)?
          """
        },
        {
          'answer': 'cd289725acf45c0670b47073426d0212',
          'choices': [
            'The bee moves to the next place, then stings the ant in that place',
            'The bee flies to the nearest Ant and attacks it',
            'The bee stings the ant in its place or moves to the next place if there is no ant in its place',
            'The bee stings the ant in its place and then moves to the next place'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What does a Bee do during one of its turns?'
        },
        {
          'answer': '9d857eafc53500120957b6455a94f898',
          'choices': [
            'When the bees enter the colony',
            'When the colony runs out of food',
            'When any bee reaches the end of the tunnel or when the Queen Ant is killed',
            'When any bee reaches the end of the tunnel and the Queen Ant is killed',
            'When no ants are left on the map'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'When is the game lost?'
        }
      ],
      'scored': True,
      'type': 'concept'
    }
  ]
}
