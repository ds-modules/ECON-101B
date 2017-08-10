test = {
  'name': 'Intro Test 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # first case
          >>> len(my_list) == 10
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # second case
          >>> len(my_list_sliced) == 5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # third case
          >>> last_of_sliced == my_list_sliced[4]
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