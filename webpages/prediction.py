import streamlit as st
import joblib
import pandas as pd
from funcs import yes_no_to_binary
import os

# Navigate directories
parent_dir = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(parent_dir, "best_model.pkl")
scaler_path = os.path.join(parent_dir, "scaler.pkl")

# Load the trained model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Title of the app
st.title("🤰🏾 Mode of Delivery Prediction App")
st.write("This app predicts whether a delivery will be **Vaginal** or **Cesarean** based on input features.")

# Input fields for user to enter feature values
# st.sidebar.header("Input Features")

st.header("Input Features")

col1, col2 = st.columns(2)
# Input fields for the selected features
with col1:
    miomectomy = yes_no_to_binary("Miomectomy", "selectbox")
    uterine_malformation = yes_no_to_binary("Uterine Malformation", "selectbox")
    cardiotocography_continuous = yes_no_to_binary("Cardiotocography", "selectbox")
    non_id_gestational_diabetes = yes_no_to_binary("Non-ID Gestational Diabetes", "selectbox")
    complications = yes_no_to_binary("Complications", "selectbox")
    cardiotocography_None = yes_no_to_binary("Cardiotocography None", "selectbox")
    fetal_malformation = yes_no_to_binary("Fetal Malformation", "selectbox")
    amniotic_liquid_clear = yes_no_to_binary("Amniotic Liquid Clear", "selectbox")
    induction = yes_no_to_binary("Induction", "selectbox")
    previous_cesarean = yes_no_to_binary("Previous Cesarean", "selectbox")
    amniotic_liquid_stained = yes_no_to_binary("Amniotic Liquid Stained", "selectbox")
    gestational_hypertension = yes_no_to_binary("Gestational Hypertension", "selectbox")
    initial_prolonged_pregnancy = yes_no_to_binary("Initial Prolonged Pregnancy", "selectbox")
    prom = yes_no_to_binary("PROM", 'selectbox')

with col2:
    previous_term_pregnancies = st.number_input("Previous Term Pregnancies", min_value=0, max_value=10, value=0)
    robson_group = st.number_input("Robson Group", min_value=1, max_value=10, value=1)
    gestagional_age = st.number_input("Gestational Age (weeks)", min_value=20, max_value=45, value=38)
    alive_new_borns = st.number_input("Alive Newborns", min_value=0, max_value=10, value=1)
    bmi = st.number_input("BMI", min_value=15.0, max_value=50.0, value=22.0)
    fetal_intrapartum_ph = st.number_input("Fetal Intrapartum pH", min_value=6.5, max_value=7.5, value=7.0)
    c_weight = st.number_input("C-Weight (kg)", min_value=30.0, max_value=150.0, value=70.0)
    age = st.number_input("Age", min_value=15, max_value=50, value=25)
    height = st.number_input("Height (m)", min_value=1.0, max_value=2.5, value=1.6)
    miscarriages = st.number_input("Miscarriages", min_value=0, max_value=10, value=0)
    preinduction = yes_no_to_binary("Preinduction", "selectbox")
    malignant_tumor = yes_no_to_binary("Malignant Tumor", "selectbox")
    cardiotocography_discontinuous = yes_no_to_binary("Cardiotocography Discontinuous", "selectbox")
    maternal_disease = yes_no_to_binary("Maternal Disease", "selectbox")


# Create a dictionary of input features
input_data = {
    'age': age,
    'alive_new_borns': alive_new_borns,
    'amniotic_liquid_clear': amniotic_liquid_clear,
    'amniotic_liquid_stained': amniotic_liquid_stained,
    'bmi': bmi,
    'c_weight': c_weight,
    'cardiotocography_None': cardiotocography_None,
    'cardiotocography_continuous': cardiotocography_continuous,
    'cardiotocography_discontinuous': cardiotocography_discontinuous,
    'complications': complications,
    'fetal_intrapartum_ph': fetal_intrapartum_ph,
    'fetal_malformation': fetal_malformation,
    'gestagional_age': gestagional_age,
    'gestational_hypertension': gestational_hypertension,
    'height': height,
    'induction': induction,
    'initial_prolonged_pregnancy': initial_prolonged_pregnancy,
    'malignant_tumor': malignant_tumor,
    'maternal_disease': maternal_disease,
    'miomectomy': miomectomy,
    'miscarriages': miscarriages,
    'non_id_gestational_diabetes': non_id_gestational_diabetes,
    'preinduction': preinduction,
    'previous_cesarean': previous_cesarean,
    'previous_term_pregnancies': previous_term_pregnancies,
    'prom': prom,
    'robson_group': robson_group,
    'uterine_malformation': uterine_malformation,

}

# Convert input data to a DataFrame
input_df = pd.DataFrame([input_data])
input_df_scaled = scaler.transform(input_df)

# Display the input data
st.subheader("Input Data")
st.dataframe(input_df)
input_df_scaled = pd.DataFrame(input_df_scaled, columns=input_df.columns)

# Make predictions
if st.button("Predict"):
    prediction = model.predict(input_df_scaled)
    prediction_proba = model.predict_proba(input_df_scaled)

    # Display the prediction
    st.subheader("Prediction")
    if prediction[0] == 0:
        st.write("The predicted mode of delivery is **Cesarean**.")
    else:
        st.write("The predicted mode of delivery is **Vaginal**.")

    # Display prediction probabilities
    st.subheader("Prediction Probabilities")
    if prediction_proba[0][0] > prediction_proba[0][1]:
        st.success(f"Probability of Cesarean Delivery: {prediction_proba[0][0] * 100:.2f}%")
    else:
        st.success(f"Probability of Vaginal Delivery: {prediction_proba[0][1] * 100:.2f}%")
