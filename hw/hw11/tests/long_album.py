test = {
  'name': 'long_album',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM long_album;
          Jagged Little Pill
          The Best Of Billy Cobham
          Black Sabbath Vol. 4 (Remaster)
          Chemical Wedding
          Chemical Wedding
          The Best Of Buddy Guy - The Millenium Collection
          Prenda Minha
          BBC Sessions [Disc 1] [Live]
          BBC Sessions [Disc 1] [Live]
          Bongo Fury
          Garage Inc. (Disc 1)
          Garage Inc. (Disc 1)
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
