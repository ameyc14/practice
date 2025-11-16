def per(status):
    diff=status["journeyTime"]-status["cancellationTime"]
    for rule in status['cancellationPolicy']['rule']:
        if rule['fromCancellationTime']>diff>rule['ToCancellationTime']:
            return rule['cancellationPercentage']
    return 0

status1=[
  {
    "journeyTime": 1732280400000,
    "cancellationTime": 1732259460436,
    "createdByUserId": "62d955f0015c0bf194ed55d3",
    "cancelledByUserId": "62d955f0015c0bf194ed55d3",
    "status": "CANCELLED",
    "cancellationPolicy": {
      "conditions": {
        "maxCancellationAllowed": -1,
        "thresholdTime": -1
      },
      "rule": [
        {
          "fromCancellationTime": 2592000000,
          "toCancellationTime": 604800000,
          "cancellationPercentage": 10
        },
        {
          "fromCancellationTime": 604800000,
          "toCancellationTime": 259200000,
          "cancellationPercentage": 10
        },
        {
          "fromCancellationTime": 259200000,
          "toCancellationTime": 86400000,
          "cancellationPercentage": 10
        },
        {
          "fromCancellationTime": 86400000,
          "toCancellationTime": 43200000,
          "cancellationPercentage": 25
        },
        {
          "fromCancellationTime": 43200000,
          "toCancellationTime": 21600000,
          "cancellationPercentage": 50
        },
        {
          "fromCancellationTime": 21600000,
          "toCancellationTime": 0,
          "cancellationPercentage": 100
        }
      ]
    }
  }
]
print(per(status1))
