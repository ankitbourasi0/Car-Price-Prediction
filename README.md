# Car-Price-Prediction
Project link: https://ankitbourasi0-car-price-prediction-prediction-page-0c5z5j.streamlit.app/
# Aim
This project aims to predict the Price of an used Car by taking it's Company name, it's Model name, Year of Purchase, and other parameters.
# How to use? 
    1.Clone the repository
    2.Install the required packages in "requirements.txt" file.  
Some packages are:

    1. numpy
    2. pandas
    3. scikit-learn
Run the "prediction_page.py" file And you are good to go.
# Description
# What this project does? 

This project takes the parameters of an used car like: Company name, Model name, Year of Purchase, Fuel Type and Number of Kilometers it has been driven.
It then predicts the possible price of the car. For example, the image below shows the predicted price of our Hyundai Grand i10.


# How this project does?
First of all the data was scraped from Quikr.com (https://quikr.com) Link for data: https://github.com/ankitbourasi0/Car-Price-Prediction/blob/main/quikr_car.csv

The data was cleaned (it was super unclean :( ) and analysed.

Then a Linear Regression model was built on top of it which had 0.92 R2_score.

Link for notebook: https://github.com/ankitbourasi0/Car-Price-Prediction/blob/main/CarPricePrediction.ipynb

This project was given the form of an website built on Streamlit where we used the Linear Regression,Decesion Tree, Random Forest Regressor models to perform predictions.
