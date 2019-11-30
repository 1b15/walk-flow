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

        mo,tu,we,th,fr,sa,su = get_predictions(
            query['countingPoint']
        )

        example_response = {
          "mo": round(mo),
          "tu": round(tu),
          "we": round(we),
          "th": round(th),
          "fr": round(fr),
          "sa": round(sa),
          "su": round(su),
          "weekday": round((mo+tu+we+th+fr)/5),
          "day": round((mo+tu+we+th+fr+sa+su)/7),
        }

        resp.body = json.dumps(example_response, ensure_ascii=False)
        resp.status = falcon.HTTP_200
