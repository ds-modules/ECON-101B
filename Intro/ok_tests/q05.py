test = {
  'name': 'q05',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> data = np.array(unemployment_data[:len(unemployment_data)])
          >>> all(total_unemployed == data[:,1])
          True
          >>> all(unemp_15_weeks == data[:,2])
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
