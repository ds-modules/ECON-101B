test = {
  'name': 'q05',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all(match == True for match in total_unemployed == data[:,1])
          True
          >>> all(match == True for match in unemp_15_weeks == data[:,2])
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
