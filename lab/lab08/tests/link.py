test = {
  'name': 'Link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab08 import *
          >>> link = Link(1, Link(2, Link(3)))
          >>> link.first
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> link.rest.first
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> link.rest.rest.rest is Link.empty
          0528ddea472f19174e0c4eb75b4de3de
          # locked
          >>> link.first = 9001
          >>> link.first
          2f870cb7220a96bf2531180ebc182058
          # locked
          >>> link.rest = link.rest.rest
          >>> link.rest.first
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          >>> link = Link(1)
          >>> link.rest = link
          >>> link.rest.rest.rest.rest.first
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> link = Link(2, Link(3, Link(4)))
          >>> link2 = Link(1, link)
          >>> link2.first
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> link2.rest.first
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> print_link(link2) # Look at print_link in lab08.py
          be012533c7c6d6a34c47734aefc52c5d
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
