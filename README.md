\# 📊 SentimentFlow: Amazon Review AI Predictor



!\[Python](https://shields.io)

!\[Framework](https://shields.io)

!\[ML](https://shields.io)



An end-to-end Machine Learning pipeline that classifies consumer product reviews into \*\*Positive\*\* or \*\*Negative\*\* sentiments with \*\*90% accuracy\*\*.



\## 🚀 Live Demo

> \*\*Note to Recruiters:\*\* I have deployed this model using Streamlit. You can test it by entering custom reviews to see real-time sentiment analysis and confidence scores.



\## 📌 Project Overview

This project demonstrates a full ML lifecycle:

1\. \*\*Data Ingestion:\*\* Processed 500k+ reviews from the \[Kaggle Amazon Product Reviews Dataset](https://kaggle.com).

2\. \*\*Preprocessing:\*\* Handled class imbalance through downsampling and cleaned raw text using Regex and NLTK.

3\. \*\*Feature Engineering:\*\* Utilized TF-IDF Vectorization (5,000 features) to convert text to numerical data.

4\. \*\*Modeling:\*\* Trained a Logistic Regression model to achieve high interpretability and speed.

5\. \*\*Deployment:\*\* Built an interactive UI using Streamlit to serve the model for real-time inference.



\## 📊 Performance Metrics

The model was evaluated on a balanced test set:





| Metric | Score |

| :--- | :--- |

| \*\*Accuracy\*\* | \*\*0.90\*\* |

| \*\*Precision (Negative)\*\* | \*\*0.89\*\* |

| \*\*Recall (Negative)\*\* | \*\*0.90\*\* |

| \*\*F1-Score\*\* | \*\*0.90\*\* |



\## 🛠 Project Structure

```text

├── models/

│   ├── sentiment\_model.pkl    # Trained Logistic Regression model

│   └── tfidf\_vectorizer.pkl   # Fitted TF-IDF Vectorizer

├── notebooks/

│   └── Sentimental Analysis.ipynb  # Data exploration \& training logic

├── app.py                     # Streamlit application script

├── requirement.txt            # Project dependencies

└── README.md                  # Project documentation

```



\## ⚙️ Local Setup

1\. \*\*Clone the repo:\*\*

&#x20;  ```bash

&#x20;  git clone https://github.com

&#x20;  ```

2\. \*\*Install Dependencies:\*\*

&#x20;  ```bash

&#x20;  pip install -r requirement.txt

&#x20;  ```

3\. \*\*Run the App:\*\*

&#x20;  ```bash

&#x20;  streamlit run app.py

&#x20;  ```



\---

\*\*Author:\*\* \[Vicky kamble](https://www.linkedin.com/in/vicky-kamble-270488155/)  

\*\*Field:\*\* AI / ML Engineering  



