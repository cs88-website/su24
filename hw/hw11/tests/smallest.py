test = {
  'name': 'smallest',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest;
          Mateus Enter|33149
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw11.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
