import os
import sys
import pandas as pd
from lightwood import Predictor
import lightwood

####################
config = {'input_features': [
                    {'name': 'number_of_bathrooms', 'type': 'numeric'}, {'name': 'sqft', 'type': 'numeric'},
                    {'name': 'location', 'type': 'categorical'}, {'name': 'days_on_market', 'type': 'numeric'},
                    {'name': 'neighborhood', 'type': 'categorical'}],
 'output_features': [{'name': 'number_of_rooms', 'type': 'categorical'},{'name': 'rental_price', 'type': 'numeric'}],
 'mixer':{'class': lightwood.BUILTIN_MIXERS.BayesianNnMixer}}
 #'mixer':{'class': lightwood.BUILTIN_MIXERS.NnMixer}}


df=pd.read_csv("https://mindsdb-example-data.s3.eu-west-2.amazonaws.com/home_rentals.csv")

predictor = Predictor(config)

def iter_function(epoch, error, test_error, test_error_gradient, test_accuracy):
    print(
        'epoch: {iter}, error: {error}, test_error: {test_error}, test_error_gradient: {test_error_gradient}, test_accuracy: {test_accuracy}'.format(
            iter=epoch, error=error, test_error=test_error, test_error_gradient=test_error_gradient,
            accuracy=predictor.train_accuracy, test_accuracy=test_accuracy))


predictor.learn(from_data=df, callback_on_iter=iter_function, eval_every_x_epochs=2, stop_training_after_seconds=20)
print(predictor.predict(when_data=df.iloc[0:20]))
#print(predictor.predict(when={'number_of_rooms':3, 'number_of_bathrooms':2, 'sqft':700, 'location':'great'}))
