import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration pour supprimer les marges de Streamlit
st.set_page_config(page_title="Agenda 4A", layout="wide")

# CSS pour cacher le menu Streamlit et coller le HTML aux bords
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px;}
    iframe {display: block; width: 100%; border: none;}
    </style>
    """, unsafe_allow_html=True)

# 2. Lecture de ton fichier HTML original
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # 3. Affichage en mode "Plein Écran"
    # On utilise height=2000 ou plus pour être sûr que tout s'affiche
    components.html(html_content, height=1200, scrolling=False)
except FileNotFoundError:
    st.error("Erreur : Le fichier index.html n'a pas été trouvé dans le dossier.")
