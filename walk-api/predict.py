import json
import falcon
import random
from .model_prediction import get_predictions

class PredictResource(object):

    def on_post(self, req, resp):
        # example_query = {
        #   "usage": "work",
        #   "measures": [
        #     {
        #       "date": "2019-11-20",
        #       "counted": "1",
        #       "temperature": "25",
        #       "rain": "11"
        #     }, ...
        #   ]
        # }
        # print(req.media)

        if req.media is None:
            resp.body = json.dumps({})
            resp.status = falcon.HTTP_400
            return

        query = req.media

        per_day, weekly = get_predictions(
            query['countingPoint'], query['dow']
        )

        example_response = {
          "day": round(per_day),
          "weekday": round(weekly)
        }

        resp.body = json.dumps(example_response, ensure_ascii=False)
        resp.status = falcon.HTTP_200
