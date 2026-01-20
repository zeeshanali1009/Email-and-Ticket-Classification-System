import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
from src.predict import predict_single, predict_batch
from src.preprocess import clean_text

st.set_page_config(page_title="Email / Ticket Classifier", layout="wide")
st.title("AI-Powered Email / Ticket Classification System")

# Single ticket prediction
st.header("Single Email / Ticket")
text_input = st.text_area("Enter Ticket Subject + Description:")
if st.button("Predict Single"):
    if text_input.strip() != "":
        text_clean = clean_text(text_input)
        result = predict_single(text_clean)
        st.success(f"Category: {result['category']} | Confidence: {result['confidence']:.2f}")
    else:
        st.warning("Please enter some text.")

# Batch prediction
st.header("Batch Prediction")
uploaded_file = st.file_uploader("Upload CSV with Ticket Subject + Ticket Description", type=['csv'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # Combine columns if needed
    if 'Ticket Subject' in df.columns and 'Ticket Description' in df.columns:
        df['text'] = df['Ticket Subject'].fillna('') + ' ' + df['Ticket Description'].fillna('')
        df['text_clean'] = df['text'].apply(clean_text)
        df_result = predict_batch(df)
        st.dataframe(df_result[['text', 'predicted_category', 'confidence']])
        st.download_button(
            "Download Predictions CSV",
            df_result.to_csv(index=False),
            file_name="predictions.csv",
            mime="text/csv"
        )
    else:
        st.error("CSV must contain 'Ticket Subject' and 'Ticket Description'")
