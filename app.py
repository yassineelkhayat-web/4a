import streamlit as st
import streamlit.components.v1 as components

# Configuration pour enlever les marges
st.set_page_config(page_title="Agenda 4A", layout="wide")

# CSS pour supprimer tous les espaces blancs et menus de Streamlit
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0px; margin: 0px;}
    iframe {border: none;}
    /* Supprime le défilement sur Streamlit */
    .main {overflow: hidden;} 
    </style>
    """, unsafe_allow_html=True)

# Lecture de ton fichier HTML original
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # Le script ci-dessous calcule la hauteur de l'écran (100vh) 
    # pour que l'index.html s'affiche en entier sans dépasser.
    components.html(
        f"""
        <style>
            body, html {{ margin: 0; padding: 0; height: 100vh; overflow: hidden; }}
        </style>
        {html_content}
        """,
        height=800, # Hauteur par défaut, le CSS s'occupe du reste
        scrolling=False
    )
except FileNotFoundError:
    st.error("Fichier index.html introuvable.")
