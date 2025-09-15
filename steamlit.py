import streamlit as st
import pickle
from datetime import datetime
import logging
import joblib
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()  # También en consola
    ]
)

logger = logging.getLogger()

logger.info("App started")


def load_model():
    try:
        model = joblib.load('Random_forest_regression.pkl')
        logging.info("Model loaded successfully")
        return model
    except Exception as e:
        logging.error(f"Error loading model: {str(e)}")
        raise e

model =None

try:
    model=load_model()
    st.success("Model load successfuly")
except Exception as e:
    st.error("Failed to load the model. Please ensure the model file is present.")
    st.stop()

st.title("Evaluador de Autos Usados")

st.sidebar.header("Caracteristicas del auto", divider='rainbow')


import streamlit as st

# Valores aproximados (ajústalos si quieres)

model_year = st.sidebar.number_input(
    "Año del modelo", min_value=1990, max_value=2025, value=2016, step=1
)

milage = st.sidebar.number_input(
    "Millaje (mi)", min_value=0, max_value=300000, value=60000, step=1000
)

horsepower = st.sidebar.number_input(
    "Potencia (HP)", min_value=50.0, max_value=800.0, value=250.0, step=5.0
)

displacement = st.sidebar.number_input(
    "Cilindrada", min_value=0.8, max_value=8.0, value=2.5, step=0.1, format="%.1f"
)

vehicle_age = st.sidebar.number_input(
    "Antigüedad (años)", min_value=0, max_value=35, value=9, step=1
)

milage_per_year = st.sidebar.number_input(
    "Millaje por año (mi/año)", min_value=0.0, max_value=60000.0, value=10000.0, step=500.0
)

power_to_weight_ratio = st.sidebar.number_input(
    "HP por litro (HP/L)", min_value=0.0, max_value=300.0, value=100.0, step=1.0
)

if st.button("Calcular precio aproximado"):
    if model:
        input_data=[[model_year, milage, horsepower, displacement, vehicle_age, milage_per_year, power_to_weight_ratio]]
        prediction=model.predict(input_data)
        st.subheader(f"Predición del precio del auto: {prediction[0]:.2f}")
    else:
        st.error("El modelo no esta disponible")