
import streamlit as st
import numpy as np
import joblib
import os

# Load model and scaler
model = joblib.load("models/logreg_heart_attack_model.pkl")
scaler = joblib.load("models/standard_scaler.pkl")

# Set page config
st.set_page_config(page_title="Heart Attack Risk Assessment", layout="centered")

# Base directory path
BASE_DIR = os.path.dirname(__file__)
infographic_path = os.path.join(BASE_DIR, "assets", "image_01.png")
logo_path = os.path.join(BASE_DIR, "assets", "BEDA_logo2WHITE.png")

# Display logo at the top (small size)
if os.path.exists(logo_path):
    st.image(logo_path, width=120)

# App Title and Introduction
st.title("🫀 Heart Attack Risk Assessment")

st.markdown("""
This application was developed using a logistic regression model trained on real clinical patient data. Features such as age, gender, blood pressure, heart rate, and cardiac biomarkers like CK-MB and Troponin were used to estimate the likelihood of a heart attack event. The model was trained and validated using standard machine learning best practices, including data scaling, cross-validation, and feature engineering.
""")

# Display the educational infographic image using updated parameter
if os.path.exists(infographic_path):
    st.image(infographic_path, use_container_width=True)

# Sidebar form for input
with st.sidebar.form("patient_form"):
    st.header("Patient Input")
    age = st.slider("Age", 18, 100, 50)
    gender = st.selectbox("Gender", options=["Male", "Female"])
    heart_rate = st.slider("Heart Rate (BPM)", 40, 180, 72)
    systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", 90, 200, 120)
    blood_sugar = st.slider("Blood Sugar (mg/dL)", 60, 400, 110)
    ckmb = st.number_input("CK-MB Level (ng/mL)", min_value=0.0, max_value=10.0, value=2.5, step=0.1)
    troponin = st.number_input("Troponin Level (ng/mL)", min_value=0.0, max_value=10.0, value=0.05, step=0.01)
    submitted = st.form_submit_button("Predict")

# Handle prediction
if submitted:
    gender_num = 1 if gender == "Male" else 0
    input_data = np.array([[age, gender_num, heart_rate, systolic_bp, blood_sugar, ckmb, troponin]])
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.subheader("📋 Prediction Result")
    if prediction == 1:
        st.error(f"⚠️ High Risk of Heart Attack ({probability*100:.2f}%)")
        st.markdown("Please consult a medical professional immediately.")
    else:
        st.success(f"✅ Low to Moderate Risk ({probability*100:.2f}%)")
        st.markdown("Maintain a healthy lifestyle and monitor regularly.")

    st.markdown("---")

# Disclaimer section
st.markdown("#### ⚠️ Disclaimer")
st.markdown("*This application is intended for educational purposes only. It does not offer medical advice, diagnosis or treatment.*")

# Contact section
st.markdown("---")
st.markdown("### 📬 Contact Us")
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    contact_submit = st.form_submit_button("Send Message")
    if contact_submit:
        st.success("Thank you! Your message has been received.")

st.markdown("---")
st.markdown("© 2025 William C. Phiri – Powered by BEDA | Email: wphiri@beda.ie")
