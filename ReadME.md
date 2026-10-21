# Healthcare Insurance Premium Prediction

A machine learning regression project that predicts annual health insurance premiums from an individual's profile, served through an interactive **Streamlit** web app.

🔗 **Live demo:** [rupesh-ml-premium-prediction.streamlit.app](https://rupesh-ml-premium-prediction.streamlit.app/)

---

## Overview

Premiums vary widely from person to person depending on age, lifestyle, and medical history. This project trains regression models on historical insurance data and exposes them through a simple UI so a user can enter their details and instantly get an estimated premium.

A key design choice: **two separate models** are used, because the relationship between features and premium differs between younger and older customers.

| Model | Applies to | Training notebook |
|-------|-----------|-------------------|
| Young model | Age 25 and under | `healthcare_premium_young_with_gr.ipynb` |
| Rest model | Adults and older people (above 25) | `healthcare_premium_rest_with_gr.ipynb` |

The app routes each input to the right model automatically based on age.

---

## Features

- Interactive Streamlit form for entering applicant details
- Automatic model selection based on age group
- Shared preprocessing pipeline (`prediction_helper.py`) so training and inference stay consistent
- Notebooks covering EDA, feature engineering, model training, and hyperparameter tuning

---

## Project Structure

```
healthcare-premium-prediction-regression-/
├── main.py                      # Streamlit app (entry point)
├── prediction_helper.py         # Preprocessing + prediction logic
├── healthcare_premium_young_with_gr.ipynb   # EDA, training, tuning (age <= 25)
├── healthcare_premium_rest_with_gr.ipynb    # EDA, training, tuning (age > 25)
├── artifacts/                   # Saved models / scalers (adjust to your folder name)
├── requirements.txt
└── README.md
```

> Update the tree above if your folder names differ.

---

## Tech Stack

- **Language:** Python 3.13
- **Data:** pandas, NumPy
- **Modeling:** scikit-learn, XGBoost
- **Model persistence:** joblib
- **App & deployment:** Streamlit, Streamlit Community Cloud

---

## Input Features

_Fill in the exact features your app collects. Typical examples:_

| Feature | Description |
|---------|-------------|
| Age | Applicant's age |
| Gender | Male / Female |
| BMI category | Underweight / Normal / Overweight / Obesity |
| Smoking status | Smoking frequency |
| Number of dependants | Count of dependants |
| Region | Geographic region |
| Marital status | Single / Married |
| Employment status | Salaried / Self-employed / Freelancer |
| Income level / lakhs | Annual income |
| Medical history | Existing conditions |
| Insurance plan | Bronze / Silver / Gold |
| Genetical risk | Risk score (if used in your models) |

---

## Methodology

1. **Exploratory Data Analysis** – distributions, correlations, outlier checks, and age-group comparison.
2. **Feature Engineering** – encoding categorical variables, scaling numeric features, and creating derived features.
3. **Model Training** – regression models trained separately for each age group.
4. **Hyperparameter Tuning** – search over model parameters to improve error metrics.
5. **Evaluation** – models compared using R², RMSE, and MAE.
6. **Deployment** – best models saved with joblib and served via Streamlit.

### Results

_Add your final metrics here:_

| Model | R² | RMSE | MAE |
|-------|----|------|-----|
| Young (≤ 25) | – | – | – |
| Rest (> 25) | – | – | – |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rupeshkumarp/healthcare-premium-prediction-regression-.git
cd healthcare-premium-prediction-regression-
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`.

---

## Deployment

The app is deployed on **Streamlit Community Cloud**:

1. Push the repo to GitHub with `main.py` at the repository root.
2. On [share.streamlit.io](https://share.streamlit.io), create a new app and select this repo.
3. Set the **main file path** to `main.py`.
4. Make sure `requirements.txt` lists all dependencies (pinned versions help avoid build issues).

---

## Requirements

Versions used during development:

```
pandas==2.3.3
numpy==2.4.4
scikit-learn==1.8.0
xgboost==3.4.1
joblib==1.5.3
streamlit
```

> Keep scikit-learn and xgboost versions identical between training and deployment — models saved with one version may not load correctly in another.

---

## Future Improvements

- Add model explainability (e.g., SHAP) to show what drives each prediction
- Add input validation and clearer error messages in the UI
- Add automated tests for the preprocessing pipeline
- Retrain periodically as new data becomes available

---

## Author

**Rupesh Kumar P**
MSDA student · [GitHub](https://github.com/rupeshkumarp)
