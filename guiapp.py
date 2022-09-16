from joblib import load
import tkinter as tk
from tkinter import ttk

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeRegressor

class RentCalc():
    """ This class is responsible for calculating your rent """

    def __init__(self, rooms, bathrooms, area, neighbourhood):
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

class CalcView(tk.Frame):
    """ This class represents the widgets the user views to calculate
    the rent """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Defining variables
        self.rooms = tk.IntVar()
        self.bathrooms = tk.IntVar()
        self.area = tk.IntVar()
        self.neighbourhood = tk.StringVar()
        self.rent = tk.StringVar()
        self.rent.set('')
        
        # Defining the labels
        name_label = ttk.Label(self, text='''Sao Carlos Appartment 
            Rent Predictor''', font=('TKDefaultFont', 32), wraplength=800)
        author_label = ttk.Label(self, text='Author: Pedro Fuziwara Filho',
                font=('TKDefaultFont', 16))
        rooms_label = ttk.Label(self, text='Rooms:')
        bathrooms_label = ttk.Label(self, text='Bathrooms:')
        area_label = ttk.Label(self, text='Area:')
        neighbourhoods_label = ttk.Label(self, text='Neighbourhood:')
        rent_label = ttk.Label(self, textvariable=self.rent)

        # Creating the input
        rooms_spinbox = tk.Spinbox(self, from_=1, to=4, increment=1,
                textvariable=self.rooms)
        bathrooms_spinbox = tk.Spinbox(self, from_=1, to=4, increment=1,
                textvariable=self.bathrooms)
        area_spinbox = tk.Spinbox(self, from_=5, to=160, increment=1,
                textvariable=self.area)
        neighbourhoods = ['Centro', 'Jardim Paraíso', 'Jardim Gibertoni',
                'Jardim Bethania', 'Jardim Sao Carlos', 'Jardim Centenário',
                'Parque Arnold Schimidt', 'Jardim Alvorada', 'Jardim Brasil',
                'Gleba I', 'Jardim Lutfalla', 'Parque Fehr', 'Cidade Jardim',
                'Jardim Bandeirantes', 'Vila Irene', 'Jardim Ipanema ',
                'Parque Santa Felícia Jardim'] 
        neighbourhoods_combobox = ttk.Combobox(self,
                textvariable=self.neighbourhood, values=neighbourhoods)
        calc_button = ttk.Button(self, text='Calculate',
                command=self.calculate)

        # Putting the pieces together
        name_label.grid(row=0, column=0, columnspan=4, sticky=(tk.W + tk.E))
        author_label.grid(row=1, column=2, rowspan=2, columnspan=2, sticky=(tk.W + tk.E))
        rooms_label.grid(row=1, column=0, sticky=tk.W)
        rooms_spinbox.grid(row=1, column=1, sticky=(tk.W + tk.E))
        bathrooms_label.grid(row=2, column=0, sticky=tk.W)
        bathrooms_spinbox.grid(row=2, column=1, sticky=(tk.W + tk.E))
        area_label.grid(row=3, column=0, sticky=tk.W)
        area_spinbox.grid(row=3, column=1, sticky=(tk.W + tk.E))
        neighbourhoods_label.grid(row=4, column=0, sticky=tk.W)
        neighbourhoods_combobox.grid(row=4, column=1, sticky=(tk.W + tk.E))
        calc_button.grid(row=5, column=0, sticky=tk.W)
        rent_label.grid(row=5, column=1, sticky=(tk.W + tk.E))

    def calculate(self):
        """ This method calculates the rent """
            
        appartment = RentCalc(self.rooms.get(), self.bathrooms.get(),
                self.area.get(), self.neighbourhood.get())
        self.rent.set('Rent: R$' + str(appartment.calc_rent()))


class MyApplication(tk.Tk):
    """ Appartment Rent Prediction Main Application """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Appartment Rent Prediction')
        self.geometry('800x600')
        self.resizable(width=False, height=False)
        CalcView(self).grid(sticky=(tk.W + tk.E + tk.N + tk.S))

def main():
    """ Main function """

    app = MyApplication()
    app.mainloop()

if __name__ == '__main__':
    main()
