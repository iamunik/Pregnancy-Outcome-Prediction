import streamlit as st
from funcs import open_picture

st.set_page_config(
    page_title="Pregnancy Outcome Predictor",
    page_icon="🏥",
    layout="wide"
)

st.title("🩺 Intelligent Delivery Mode Prediction Platform 🏥👶")

st.markdown(f"""
<img style="border: 2px solid #b3a1c7" src="data:image/jpeg;base64,{open_picture('delivery.jpg')}" width="80%"><br>
""", unsafe_allow_html=True)

st.markdown("""
### Welcome  
Our platform leverages advanced machine learning to support healthcare professionals in predicting the most probable 
delivery method—vaginal or cesarean—tailored to each patient’s unique clinical profile. By entering key medical details, 
clinicians receive immediate, data-driven insights to guide prenatal care and delivery planning.

---

### 🌟 Key Goals  
- **Empower Clinical Judgement**: Deliver rapid, evidence-based predictions to enhance decision-making.
- **Highlight Critical Factors**: Surface patient-specific risks and indicators influencing delivery outcomes.
- **Ensure Seamless Experience**: Offer a user-friendly, responsive interface for efficient data entry and result 
review.

---

### 🧩 Technology Stack  
- **Gradient Boosting Classifier**: Delivers robust, high-accuracy predictions.
- **Streamlit**: Powers the interactive, web-based user interface.
- **Pandas & NumPy**: Manage data processing and validation.
- **Scikit-learn**: Supports model development and integration.

---

### 🔬 How It Works  
1. **Data Collection**: Enter clinical features such as age, BMI, gestational age, and obstetric history.
2. **Automated Preprocessing**: The system prepares and validates your input for the model.
3. **Prediction Engine**: The trained model analyzes the data and forecasts the likely delivery mode.
4. **Clear Results**: Outcomes and relevant insights are presented instantly for your review.

---

### ⚙️ System Highlights  
- **Comprehensive Feature Set**: Incorporates essential maternal and fetal indicators.
- **Clinically Validated Model**: Trained on real-world delivery data for reliable performance.
- **Optimized for Practice**: Designed for ease of use in busy clinical environments.

---

### 🤝 Our Commitment  
We are dedicated to integrating intelligent automation into maternal care, helping providers anticipate delivery needs 
and optimize patient outcomes. This tool is crafted to enhance both the quality and efficiency of prenatal care, 
fostering confidence and clarity in every decision.

""")