# Appartment-Rent-Prediction---Sao-Carlos
This repository shows a machine learning model that can estimate the value of appartment rents in the city of São Carlos,  state of Sao Paolo, in Brazil.

The Jupyter notebooks shows how I have fetched the data and reasons why I have choosen the decision tree regression as my machine learning model.
I have saved the pipeline to work with raw data and the model using pickle.

At last, the guiapp is actually just a simple program that loads the pipeline, the model and asks for data, then it predicts the rent price.

Warning: my dataset is really small, so the prediction won't be perfect but just a good approximation and the data won't be collected again,
so if you are using the program too long after the data was collected (13/09/2022), there might be differences because of the age of the dataset.
