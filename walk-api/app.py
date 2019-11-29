import falcon

from .predict import PredictResource

api = application = falcon.API()

predict = PredictResource()
api.add_route('/predict', predict)
