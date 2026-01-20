# Email-and-Ticket-Classification-System

[![CI/CD Pipeline](https://github.com/zeeshanali1009/Email-and-Ticket-Classification-System/actions/workflows/ci.yml/badge.svg)](https://github.com/zeeshanali1009/Email-and-Ticket-Classification-System/actions/workflows/ci.yml)

## 📝 Project Overview

The **Email and Ticket Classification System** is an AI-powered solution designed to automatically categorize incoming emails and support tickets into predefined categories (e.g., Support, Complaint, Inquiry, Spam). This enables teams to efficiently handle large volumes of messages, prioritize critical issues, and improve customer service response times.

**Live Demo:** [Streamlit App](https://email-and-ticket-classification-system-dirosfhvxedkpuhdj6hbjs.streamlit.app/)

---

## 1️⃣ Client Problem Statement

> “We receive hundreds of emails/tickets daily. We want an AI system that automatically classifies them into categories so the team can handle them efficiently.”

**Client Requirements:**

* Accept batch email input (CSV or JSON)
* Classify emails into predefined categories
* Display confidence scores
* Provide a simple web UI for demonstration
* Include a REST API for future integration
* Optional: Highlight keywords influencing classification

---

## 2️⃣ Project Goals

* Build an **end-to-end NLP pipeline** for text classification
* Deploy a **Streamlit UI** with optional **FastAPI backend**
* Provide client-ready folder structure and documentation
* Include **explainability** for model predictions (keywords or SHAP)

---

## 3️⃣ Technology Stack

**Programming Language & Libraries:**

* Python 3.10+
* Pandas, NumPy — data handling
* Scikit-learn — ML models (Logistic Regression, Random Forest)
* NLTK / SpaCy — text preprocessing
* TfidfVectorizer — feature extraction

**Web & Deployment:**

* FastAPI — API endpoint
* Streamlit — user interface
* Optional: SHAP / LIME — explainable AI

---

## 4️⃣ Execution Workflow

### Step 1 — Data Collection & Preparation

* Use sample email/ticket datasets (or generate dummy data)
* Preprocessing:

  * Convert text to lowercase
  * Remove punctuation and stopwords
  * Lemmatization or stemming
* Split dataset: Train / Test / Validation (70/15/15)

### Step 2 — Feature Extraction

* Convert text → numeric vectors using TF-IDF
* Optional: add keyword frequency features

### Step 3 — Model Training & Selection

* Baseline: Logistic Regression
* Advanced: Random Forest / XGBoost
* Evaluate with:

  * Accuracy, Precision, Recall, F1-score
  * Confusion Matrix
* Save best-performing model using **joblib**

### Step 4 — Explainability

* Extract top contributing words for each classification
* Optional: Use **SHAP values** to explain model predictions

### Step 5 — FastAPI Backend

* Endpoint: `/predict`
* Accept: single or batch email JSON
* Return: category, confidence score, top keywords

### Step 6 — Streamlit UI

* Upload CSV or paste ticket text
* Display predicted category + confidence
* Optional: display top contributing keywords
* Add **downloadable predictions** button

---

## 5️⃣ Deliverables

* **Streamlit Web App** for real-time classification
* **FastAPI Endpoint** for future integrations
* Trained ML model files (`joblib`)
* Documentation for usage and retraining
* Sample predictions for demo purposes

---

## 6️⃣ Freelance Value Proposition

* **Marketable Product Name:** “AI-Powered Email / Ticket Automation System”
* **Use Cases:**

  * Support ticket routing
  * Spam detection
  * Complaint categorization
* **Freelance Rate:** $150–400 depending on number of categories & UI polish

---
