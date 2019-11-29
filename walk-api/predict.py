import json
import falcon
import random

class PredictResource(object):

    def on_get(self, req, resp):
        example_query = {
          "usage": "work",
          "measures": [
            {
              "date": "2019-11-20",
              "counted": "1",
              "temperature": "25",
              "rain": "11"
            },
            {
              "date": "2019-11-14",
              "counted": "12",
              "temperature": "2",
              "rain": "22"
            }
          ]
        }

        query = example_query
        # query = json.parse(req)

        perfect_calculation_per_day = random.randint(1, 1000)
        perfect_calculation_per_weekday = int(perfect_calculation_per_day * random.randint(70, 130) / 100)

        example_response = {
          "day": perfect_calculation_per_day,
          "weekday": perfect_calculation_per_weekday
        }

        resp.body = json.dumps(example_response, ensure_ascii=False)
        resp.status = falcon.HTTP_200
