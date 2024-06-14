test = {
  'name': 'long',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM long;
          You Oughta Know (Alternate)
          Stratus
          Wheels Of Confusion / The Straightener
          Book Of Thel
          The Alchemist
          Talkin' 'Bout Women Obviously
          Terra
          You Shook Me(2)
          How Many More Times
          Advance Romance
          Mercyful Fate
          Tuesday's Gone
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
