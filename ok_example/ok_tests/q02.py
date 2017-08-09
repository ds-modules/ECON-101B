test = {
  'name': 'Test Example',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # can put comments here
          >>> 4 == 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # second case
          >>> 3 == 4
          True
          >>> # this will fail
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
