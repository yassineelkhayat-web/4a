import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(page_title="Agenda 4A", layout="wide")

# Lecture de ton fichier HTML original
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Affichage du code HTML original dans Streamlit
components.html(html_content, height=1000, scrolling=True)
