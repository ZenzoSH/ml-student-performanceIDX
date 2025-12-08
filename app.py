import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# -----------------------
# Simple Student Performance Predictor
# -----------------------
# Features explained, neutral UI, informative text

st.set_page_config(page_title="Student Performance Predictor",
                   page_icon="🎓",
                   layout="centered")

# Minimal neutral styling
st.markdown("""
<style>
body {background-color: #f7f7f8;}
.main .block-container {padding-top: 1rem;}
h1 {color: #2f4f4f;}
.description {color: #4b5563;}
</style>
""", unsafe_allow_html=True)

# Load model (keeps caching simple)
@st.cache_resource
def load_model(path='linear_regression_model.pkl'):
    try:
        return joblib.load(path)
    except Exception:
        return None

model = load_model()

# Header
st.title("Student Performance Predictor 🎓")
st.markdown("""
<div class='description'>
This lightweight app predicts a student's **Performance Index** (10 - 100) using a Multiple Linear Regression model trained on 10,000 records. 
Use the controls below to enter features — each control includes a short explanation.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Informational expander about dataset & features
with st.expander("About the dataset and features", expanded=False):
    st.markdown("""
**Dataset summary**
- 10,000 student records
- Target: *Performance Index* (10 - 100)

**Feature meanings**
- **Hours Studied**: Total hours studied per day (higher generally helps).
- **Previous Scores**: Average of past test scores (0-100).
- **Extracurricular Activities**: Whether the student participates (Yes/No). Can indicate time allocation and holistic development.
- **Sleep Hours**: Average daily sleep. Adequate sleep improves retention and focus.
- **Sample Papers Practiced**: Number of practice question papers completed. Helps exam readiness.
""")

st.markdown("---")

# Inputs (clear, with help text)
st.header("Enter student information")
cols = st.columns(2)

with cols[0]:
    hours_studied = st.slider("Hours Studied per Day", 0.0, 12.0, 5.0, 0.5,
                              help="Total hours student studies each day.")
    previous_scores = st.slider("Previous Test Scores", 0, 100, 75, 1,
                                help="Recent average test scores (0-100).")
    sample_papers = st.slider("Sample Papers Practiced", 0, 20, 5, 1,
                              help="Number of full sample papers completed.")

with cols[1]:
    sleep_hours = st.slider("Sleep Hours per Day", 0.0, 12.0, 7.0, 0.5,
                            help="Average daily sleep hours.")
    extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"],
                                  help="Participation in sports, arts, clubs, etc.")
    extracurricular_value = 1 if extracurricular == "Yes" else 0

st.markdown("---")

# Predict
predict = st.button("Predict Performance")

if predict:
    if model is None:
        st.error("Model not found. Make sure 'linear_regression_model.pkl' exists in the app directory.")
    else:
        X = np.array([[hours_studied, previous_scores, extracurricular_value, sleep_hours, sample_papers]])
        pred = model.predict(X)[0]
        pred = int(np.clip(round(pred), 10, 100))

        # Result area
        st.subheader("Prediction")
        st.metric(label="Predicted Performance Index", value=f"{pred} / 100")

        # Simple gauge using plotly
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pred,
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={'axis': {'range': [10, 100]}, 'bar': {'color': "#2f4f4f"}}
        ))
        fig.update_layout(height=260, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)

        # Interpretation
        if pred >= 80:
            st.success("Excellent — strong prospects based on the inputs.")
        elif pred >= 60:
            st.info("Good — steady performance; slight improvements could help.")
        else:
            st.warning("Needs improvement — consider more study time and practice papers.")

        # Show input summary
        summary = pd.DataFrame({
            "Feature": ["Hours Studied", "Previous Scores", "Extracurricular", "Sleep Hours", "Sample Papers"],
            "Value": [f"{hours_studied} hrs", f"{previous_scores}/100", extracurricular, f"{sleep_hours} hrs", sample_papers]
        })
        st.table(summary)

        # Simple personalized tips
        tips = []
        if hours_studied < 4:
            tips.append("Increase study hours to 4-6 per day for better coverage.")
        if sleep_hours < 6:
            tips.append("Aim for 7-8 hours of sleep to improve focus and memory.")
        if sample_papers < 3:
            tips.append("Practice more full-length sample papers to build exam stamina.")
        if previous_scores < 60:
            tips.append("Review foundational topics and revise regularly.")

        if tips:
            st.subheader("Recommendations")
            for t in tips:
                st.write("- ", t)
        else:
            st.success("Balanced inputs — keep up the good habits!")

# Footer
st.markdown("---")
st.caption("Student Performance Dataset: 10,000 records. Model: Multiple Linear Regression. Target: Performance Index (10-100).")
