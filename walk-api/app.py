import falcon

from .predict import PredictResource
from .util import HandleCORS

api = application = falcon.API(middleware=[ HandleCORS() ])

predict = PredictResource()
api.add_route('/predict', predict)
