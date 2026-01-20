import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os, sys

# Ensure imports work even if running directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)  # remove punctuation/numbers
    words = [lemmatizer.lemmatize(w) for w in text.split() if w not in stop_words]
    return ' '.join(words)

def load_and_preprocess(csv_path):
    df = pd.read_csv(csv_path)
    
    # Combine Ticket Subject + Ticket Description
    df['text'] = df['Ticket Subject'].fillna('') + ' ' + df['Ticket Description'].fillna('')
    df['text_clean'] = df['text'].apply(clean_text)
    
    # Check Ticket Type column exists
    if 'Ticket Type' not in df.columns:
        raise Exception("No Ticket Type column found in dataset")
    
    return df[['text_clean', 'Ticket Type']]
