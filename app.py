import streamlit as st
from prediction_page import show_predictions_page,load_model_data

companies =  load_model_data()
show_predictions_page(companies)

