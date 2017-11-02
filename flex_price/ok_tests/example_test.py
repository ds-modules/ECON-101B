test = {
  'name': 'Intro Test 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x == 10.5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> y == 7.2
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> import numpy as np
          >>> np.isclose(combo, 75.6)
          True
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