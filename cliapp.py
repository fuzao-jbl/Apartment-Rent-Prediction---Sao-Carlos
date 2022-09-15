import pickle
from joblib import load
import pandas as pd

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeRegressor

class RentCalc():
    """ This class is responsible for calculating your rent """

    def __init__(self, area, rooms, bathrooms, neighbourhood):
        # It must have the variables to predict rent, let's prepare this data
        data_dict = {
                'area': [area],
                'rooms': [rooms],
                'bathrooms': [bathrooms],
                'neighbourhood': [neighbourhood]
            }
        data_series = pd.DataFrame(data_dict)

        # Now we need to prepare this data, using the pipeline
        pipeline = load('pipe.pkl')
        self.data = pipeline.transform(data_series)
        # Load the model
        self.model = load('tree_reg.pkl')

    def calc_rent(self):
        """ Loads the training model and calculates the data """

        predict = self.model.predict(self.data)
        return predict[0]

if __name__ == '__main__':
    rooms = int(input('rooms: '))
    bathrooms = int(input('bathrooms: '))
    area = int(input('area: '))
    neighbourhood = input('neighbourhood: ')
    rent = RentCalc(area, rooms, bathrooms, neighbourhood)
    print('Rent prediction:', rent.calc_rent())
