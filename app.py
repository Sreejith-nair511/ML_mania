import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# ======================
# LOAD MODEL
# ======================
@st.cache_resource
def load_model():
    try:
        model = joblib.load("model.pkl")  # Make sure model.pkl is in repo root
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

model = load_model()

# ======================
# APP CONFIG
# ======================
st.set_page_config(
    page_title="🏎️ F1 Race Predictor",
    page_icon="🏁",
    layout="wide"
)

st.title("🏎️ Formula 1 Race Prediction")
st.markdown("This app predicts **Formula 1 race results** based on input data. 🚦")

# ======================
# INPUT FORM
# ======================
with st.form("prediction_form"):
    st.subheader("Enter Race Details")

    driver = st.selectbox("Select Driver", [
        "Max Verstappen", "Lewis Hamilton", "Charles Leclerc", "Lando Norris", "Fernando Alonso"
    ])

    team = st.selectbox("Select Team", [
        "Red Bull", "Mercedes", "Ferrari", "McLaren", "Aston Martin"
    ])

    quali_pos = st.number_input("Qualifying Position", min_value=1, max_value=20, value=5)

    weather = st.selectbox("Weather", ["Sunny", "Rainy", "Cloudy", "Mixed"])

    track_type = st.selectbox("Track Type", ["Street Circuit", "Race Track", "High Speed", "Technical"])

    submit = st.form_submit_button("Predict")

# ======================
# PREDICTION
# ======================
if submit:
    if model is None:
        st.error("⚠️ Model not loaded. Please check `model.pkl` in your repo.")
    else:
        # Dummy encoding (replace with actual preprocessing used during training)
        input_data = pd.DataFrame([{
            "driver": driver,
            "team": team,
            "quali_pos": quali_pos,
            "weather": weather,
            "track_type": track_type
        }])

        # NOTE: Preprocessing must match training! Replace with your pipeline
        try:
            prediction = model.predict(input_data)[0]
            st.success(f"🏁 Predicted Race Result: **{prediction}**")
        except Exception as e:
            st.error(f"❌ Prediction failed: {e}")

# ======================
# FOOTER
# ======================
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | F1 Prediction Demo")
