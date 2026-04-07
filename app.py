import streamlit as st
from google import genai

# Contoh cara panggil API Key dari Secrets Streamlit
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
