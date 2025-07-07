import streamlit as st
import joblib
import re

# Load model and vectorizer
model = joblib.load("svm_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(page_title="News Category Classifier", layout="centered")

# Minimal Styling for Smooth UI
st.markdown("""
<style>
body {
    background-color: #fafafa;
}
.main-title {
    font-size: 2.2rem;
    font-weight: 700;
    text-align: center;
    color: #2d3436;
    margin-top: 20px;
}
.subtext {
    font-size: 1rem;
    color: #636e72;
    text-align: center;
    margin-bottom: 25px;
}
.stButton>button {
    background-color: #0984e3;
    color: white;
    font-weight: 600;
    border-radius: 8px;
    padding: 10px 20px;
    margin-top: 15px;
    font-size: 1rem;
}
.stButton>button:hover {
    background-color: #74b9ff;
    color: black;
}
.prediction-box {
    background: #ffffff;
    border-radius: 8px;
    padding: 18px;
    text-align: center;
    font-size: 1.2rem;
    border: 1px solid #dfe6e9;
    margin-top: 25px;
    box-shadow: 0 1px 5px rgba(0,0,0,0.05);
}
.footer {
    text-align: center;
    font-size: 0.9rem;
    color: #b2bec3;
    margin-top: 4rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>📰 News Category Classifier</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Know your news type in one click!</div>", unsafe_allow_html=True)

# Updated real-time examples
examples = [
    "India defeats South Africa to win T20 World Cup 2024",
    "Apple announces iPhone 16 with AI features",
    "Stock markets surge as RBI holds interest rates steady",
    "WHO warns about new COVID-19 subvariant",
    "NASA's Artemis mission delayed due to technical issues"
]
example = st.selectbox("📌 Try an example headline:", ["Choose an example..."] + examples)

user_input = st.text_area("✍️ Enter headline or article:",
    value=example if example != "Choose an example..." else "",
    height=120, placeholder="e.g. Supreme Court Passes New Law on Climate Change")

if st.button("🚀 Classify"):
    if user_input.strip():
        cleaned = re.sub(r'[^a-z\s]', '', user_input.lower())
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()
        user_vec = vectorizer.transform([cleaned])
        prediction = model.predict(user_vec)[0]

        st.markdown(f"<div class='prediction-box'><strong>Predicted Category:</strong><br><span style='color:#0984e3'>{prediction}</span></div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a headline first.")

st.markdown("<div class='footer'>Made with ❤️ using Streamlit • Developed by <strong>Nadeem</strong></div>", unsafe_allow_html=True)
