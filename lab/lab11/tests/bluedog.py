test = {
  'name': 'bluedog',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM blue_dog;
          blue|dog
          blue|dog
          blue|dog
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab11.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
