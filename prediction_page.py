import streamlit as st
import pickle
import pandas as pd
cars = pd.read_csv('cleaned_car_price_prediction_dataset.csv')

model =  pickle.load(open("LinearRegressionModel.pkl","rb"))
def load_model_data():
   st.title("Car Price Prediction 🚗")
   st.write("""### We need some information to predict the price""")

   companies =  sorted(cars['company'].unique())

   return companies


def show_predictions_page(companies):
   
   selected_Company = st.selectbox("Company",companies)
   car_model_list =  cars[cars['company'] == selected_Company]
   car_name =  sorted(car_model_list["name"].unique())
   car_years = sorted(car_model_list["year"].unique())
   car_fuel = sorted(car_model_list["fuel_type"].unique())
   kms_driven = sorted(car_model_list["kms_driven"].unique())

   selected_Car_name = st.selectbox("Car model",car_name)
   selected_year = st.selectbox("Year of purchase",car_years)
   selected_fuel_type  = st.selectbox("Fuel type",car_fuel)
   selected_kms_driven = st.selectbox("How many kilometers driven",kms_driven)
   res = st.button("Calculate Price")
   if res:
      predictions = model.predict(pd.DataFrame([[selected_Car_name,selected_Company,selected_year,selected_kms_driven,selected_fuel_type]],columns=['name','company','year','kms_driven','fuel_type']))
      st.header(f"The estimated car price is ₹{predictions[0]:.2f}")



def main():
   companies =  load_model_data()
   show_predictions_page(companies)

if __name__ == "__main__":
    main()