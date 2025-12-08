# 🎓 Student Performance Predictor


## 🔗 Project Demo & Resources

| Platform | Type | Link |
| :--- | :--- | :--- |
| **Streamlit** | Live App | [🚀 Launch App](https://ml-student-performanceidxgit-lqbo7xargytrfhdri2qs4b.streamlit.app/) |
| **Kaggle** | Notebook | [📓 View Analysis & EDA](https://www.kaggle.com/code/ahmedabbas757/student-performance-prediction-eda-ml) |

A machine learning web application built with **Streamlit** that predicts a student's **Performance Index** based on their study habits and extracurricular activities. This tool provides instant predictions and personalized recommendations to help students improve their academic outcomes.

## 📄 Project Description

The Student Performance Dataset is designed to examine the factors influencing academic student performance. This application uses a **Multiple Linear Regression** model trained on 10,000 student records to analyze the relationship between predictor variables and the performance index.

The app provides an interactive interface where users can input specific data points to receive a predicted score ranging from 10 to 100.

## 📊 Dataset & Features

The model predicts the target variable **Performance Index** based on the following input features:

| Feature | Description |
| :--- | :--- |
| **Hours Studied** | The total number of hours spent studying per day. |
| **Previous Scores** | The scores obtained by students in previous tests (0-100). |
| **Extracurricular Activities** | Participation in sports, arts, clubs, etc. (Yes/No). |
| **Sleep Hours** | The average number of hours of sleep per day. |
| **Sample Papers Practiced** | The number of sample question papers the student practiced. |

**Target Variable:**
* **Performance Index:** A rounded integer (10-100) indicating the student's overall academic performance.

## 🛠️ Tech Stack

* **Python:** Core programming language.
* **Streamlit:** For creating the web interface.
* **Scikit-Learn:** For the Linear Regression model.
* **Pandas & NumPy:** For data manipulation.
* **Plotly:** For interactive gauge charts and visualizations.
* **Joblib:** For loading the trained model.

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/student-performance-predictor.git](https://github.com/your-username/student-performance-predictor.git)
    cd student-performance-predictor
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure

```text
├── app.py                       # The main Streamlit application code
├── linear_regression_model.pkl  # The trained ML model (Required)
├── requirements.txt             # List of python dependencies
└── README.md                    # Project documentation
