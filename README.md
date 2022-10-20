# Apartment-Rent-Prediction---Sao-Carlos

[EM PORTUGUÊS]

Esse repositório mostra meu modelo de machine learning para estimar o valor do aluguel de apartamentos na cidade de São Carlos, São Paulo, Brasil.

Os cadernos do jupyter mostram como eu coletei os dados e os motivos do porque eu escolhi usar o algoritmo "decision tree regressor" para meu modelo de machine learning.

Por fim, o guiapp é um programa simples que carrega o modelo e a pipeline que vai processar os dados. A interface gráfica vai te pedir os dados para conseguir prever o aluguel desse apartamento.

Para conseguir rodar o programa, você vai precisar:
- Clonar esse repositório;
- Ter instalado Python3, Pandas, Joblib, Tkinter, Scikit-Learn e Pickle;
- Entrar no repositório clonado e rodar o guiapp.py.

Caso você não saiba seguir esses passos, abra seu terminal e o rode os seguintes comandos:
1. git clone https://github.com/fuzao-jbl/Apartment-Rent-Prediction---Sao-Carlos;

Caso você use ubuntu ou mint (ou qualquer outra distro linux baseada em debian): 
3. sudo apt install python3 python3-pip;
4. pip install pandas sklearn;
5. cd Apartment-Rent-Prediction---Sao-Carlos;
6. python3 guiapp.py;

Espere um pouco que, provavelmente, vai aparecer a tela do programa para você :)

[IN ENGLISH]

This repository shows a machine learning model that can estimate the value of appartment rents in the city of São Carlos,  state of Sao Paolo, in Brazil.

The Jupyter notebooks shows how I have fetched the data and reasons why I have choosen the decision tree regression as my machine learning model.
I have saved the pipeline to work with raw data and the model using pickle.

At last, the guiapp is actually just a simple program that loads the pipeline, the model and asks for data, then it predicts the rent price.

To run the GUI application, you must have installed the requirements:
  - Pandas,
  - Scikit Learn;
  - Joblib;
  - Tkinter;
  - Pickle;
  
You can install them running: pip install pandas, sklearn, joblib, tkinter, pickle

Warning: my dataset is really small, so the prediction won't be perfect but just a good approximation and the data won't be collected again,
so if you are using the program too long after the data was collected (13/09/2022), there might be differences because of the age of the dataset.
