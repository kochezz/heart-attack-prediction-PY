
# Heart Attack Risk Prediction using Logistic Regression

[![Python](https://img.shields.io/badge/Built%20With-Python-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()
[![Data](https://img.shields.io/badge/Data-Cleaned-lightgrey)]()

This project builds a logistic regression model to identify patients at risk of experiencing a heart attack based on clinical and demographic features. The model is trained on a clean medical dataset and deployed via a Streamlit dashboard for real-time prediction.

---

## 📌 Project Description

This machine learning project uses medical data to classify whether a patient is likely to experience a heart attack. It employs a logistic regression model and emphasizes model explainability, clinical relevance, and reproducibility.

---

## 📁 Project Structure

```
Heart_Attack_Risk_Assessment_PY/
├── data/                 # Raw and processed data
├── models/               # Saved model and scaler (joblib)
├── notebooks/            # Jupyter notebooks for EDA and model dev
├── reports/              # Final model report (.docx)
├── src/                  # Source code (pipeline, utils)
├── dashboards/           # Streamlit app
├── main.py               # Entrypoint (for CLI or app use)
└── README.md             # Project overview
```

---

## 📊 Features

- Logistic regression for binary classification
- Feature scaling with StandardScaler
- Multicollinearity check using VIF
- Model evaluation: accuracy, precision, recall, ROC-AUC
- Cross-validation (5-fold)
- Model deployment using Streamlit
- Clean modular project layout (production-ready)

---

## 🚀 Getting Started

### 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/kochezz/heart-attack-risk-assessment.git
cd heart-attack-risk-assessment

# Create environment and install dependencies
conda create -n heart-env python=3.10
conda activate heart-env
pip install -r environment/requirements.txt
```

---

### ▶️ Run Streamlit App

```bash
streamlit run dashboards/streamlit_app.py
```

> ⚠️ You’ll need to run this after building the Streamlit interface.

---

## 🧠 Model Summary

- Trained on 7 features: Age, Gender, Heart rate, Systolic BP, Blood Sugar, CK-MB, Troponin
- Accuracy: 80.7%
- AUC Score: 0.89
- Cross-validation accuracy: 99.9%
- Final model and scaler saved with `joblib` for deployment

---

## 🛠️ Tech Stack

- Python 3.10
- pandas, scikit-learn, statsmodels, matplotlib, seaborn
- Streamlit (for app interface)
- Jupyter Notebooks (EDA)
- joblib (for model persistence)

---

## 🧾 Author

**William C. Phiri**  
[GitHub: @kochezz](https://github.com/kochezz)  
[LinkedIn](https://www.linkedin.com/in/william-phiri-866b8443/)  
Email: wphiri@beda.ie

---

## 📷 App Screenshot

_To be added once Streamlit UI is finalized._

---

## 📄 License

This project is licensed under the MIT License.

