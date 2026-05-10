# 📊 Sentiment Insights AI: Amazon Review Predictor

![Python](https://shields.io/badge/Python-3.8%2B-blue) 
![Scikit-Learn](https://shields.io/badge/Scikit--Learn-0.24-green) 
![Streamlit](https://shields.io/badge/Streamlit-1.0.0-blue) 
![Accuracy](https://shields.io/badge/Accuracy-90%25-brightgreen)
![Status](https://shields.io/badge/Status-Production-brightgreen))

An end-to-end Machine Learning pipeline that classifies consumer product reviews into **Positive** or **Negative** sentiments using Natural Language Processing (NLP).

---

## 🔗 [Click here to try the Live Demo](https://sentiment-insights-ai.streamlit.app/)

> **Note to Recruiters:** This application is fully deployed. You can enter custom reviews to see real-time sentiment analysis and model confidence scores.

---

## 📌 Project Overview
This project demonstrates a professional AI/ML engineering lifecycle:
1. **Data Ingestion:** Processed 500k+ reviews from the [Kaggle Amazon Product Reviews Dataset](https://kaggle.com).
2. **Preprocessing:** Handled significant class imbalance through downsampling and cleaned raw text using Regex and NLTK.
3. **Feature Engineering:** Utilized **TF-IDF Vectorization** (5,000 features) to transform text into numerical input.
4. **Modeling:** Trained a **Logistic Regression** model optimized for high interpretability and inference speed.
5. **Deployment:** Built a production-ready interface using **Streamlit** for real-time model interaction.

## 📊 Performance Metrics
The model was evaluated on a balanced test set with the following results:


| Metric | Score |
| :--- | :--- |
| **Overall Accuracy** | **90%** |
| **Precision (Negative)** | **0.89** |
| **Recall (Negative)** | **0.90** |
| **F1-Score** | **0.90** |

## 🛠 Project Structure
```text
├── models/
│   ├── sentiment_model.pkl    # Trained Logistic Regression model
│   └── tfidf_vectorizer.pkl   # Fitted TF-IDF Vectorizer
├── notebooks/
│   └── Sentimental Analysis.ipynb  # Data exploration & training logic
├── app.py                     # Streamlit application script
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## ⚙️ Local Setup
1. **Clone the repo:**
   ```bash
   git clone https://github.com
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the App:**
   ```bash
   streamlit run app.py
   ```

---
**Developed by:** [Vicky Kamble]  
**Focus:** AI / ML Engineering & Production Deployment