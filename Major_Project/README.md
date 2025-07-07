# 📰 News Category Classifier

This is a machine learning web application that classifies news headlines or article snippets into predefined categories using a trained Support Vector Machine (SVM) model. The app is built using Streamlit for the frontend and Python for the backend.

## 🚀 Features

- Input any news headline or article text.
- Classifies the input into one of the trained news categories.
- Simple and interactive web interface built with Streamlit.
- Uses a pre-trained SVM model and TF-IDF vectorizer.

## 📁 Project Structure

├── app.py # Streamlit app
├── news_category_classification.ipynb
 #Notebook for training and evaluation
├── NewsCategorizer.csv # Dataset used for training
├── svm_model.pkl # Trained SVM model (saved with joblib)
├── vectorizer.pkl # TF-IDF vectorizer used in model


## 🧠 Model Info

- **Model**: Support Vector Machine (SVM)
- **Text Vectorization**: TF-IDF
- **Dataset**: News headlines/articles with associated categories

## ▶️ How to Run

### Prerequisites

- Python 3.7+
- Required packages: `streamlit`, `scikit-learn`, `joblib`, `pandas`

### Installation

```bash
pip install -r requirements.txt
