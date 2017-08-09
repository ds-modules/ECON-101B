test = {
  'name': 'q06',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all(match == True for match in total_unemployed == data[:,1])
          True
          >>> all(match == True for match in hpi == data[:,7])
          True
          >>> all(match == True for match in y_ == model.predict(x))
          True
          >>> prediction <= 147 and prediction >= 146
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
