import joblib

# Load model and vectorizer
model = joblib.load('models/email_classifier.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

def predict_single(text):
    text_vec = vectorizer.transform([text])
    pred = model.predict(text_vec)[0]
    prob = max(model.predict_proba(text_vec)[0])
    return {'category': pred, 'confidence': prob}

def predict_batch(df, text_col='text_clean'):
    texts_vec = vectorizer.transform(df[text_col])
    preds = model.predict(texts_vec)
    probs = model.predict_proba(texts_vec).max(axis=1)
    df['predicted_category'] = preds
    df['confidence'] = probs
    return df
