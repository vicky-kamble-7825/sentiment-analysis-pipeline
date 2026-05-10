import streamlit as st
import joblib
import re

# Page Config (Makes it feel like a real app)
st.set_page_config(page_title="Sentiment Insights AI", page_icon="📊", layout="centered")

# Load Assets
model = joblib.load('models/sentiment_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'<br />', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

# --- SIDEBAR ---
with st.sidebar:
    st.title("Project Info")
    st.info("This AI model uses Logistic Regression and TF-IDF to analyze Amazon reviews with **90% accuracy**.")
    st.markdown("### Tech Stack")
    st.code("Python\nScikit-Learn\nStreamlit\nNLTK")

# --- MAIN UI ---
st.title("📊 Sentiment Insights AI")
st.markdown("---")

user_input = st.text_area("Drop your product review here:", placeholder="The battery life was amazing...", height=150)

if st.button("Analyze Sentiment", use_container_width=True):
    if user_input:
        cleaned_input = clean_text(user_input)
        vectorized_input = vectorizer.transform([cleaned_input])
        
        # Get Prediction & Probabilities
        prediction = model.predict(vectorized_input)[0]
        probs = model.predict_proba(vectorized_input)[0] # This shows the confidence!
        
        # Display Results in a nice container
        with st.container():
            st.markdown("### Analysis Results")
            if prediction == 1:
                confidence = probs[1] * 100
                st.success(f"**POSITIVE** ({confidence:.1f}% Confidence)")
                st.balloons() # Fun effect for positive results
            else:
                confidence = probs[0] * 100
                st.error(f"**NEGATIVE** ({confidence:.1f}% Confidence)")
            
            # Progress bar for visual probability
            st.progress(probs[1]) 
    else:
        st.warning("Please enter a review first!")
