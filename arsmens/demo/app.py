
import streamlit as st
from translations import t # Import the translation function

# 1. Initialize language in session state (Default to Spanish for evaluators)
if "lang" not in st.session_state:
    st.session_state.lang = "es"

# 2. Page config
st.set_page_config(
    page_title=t("platform_title", st.session_state.lang),
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 3. Language Toggle in Sidebar
st.sidebar.title("ArsMens Platform")
st.sidebar.markdown("---")

# Radio buttons or selectbox for language
lang_option = st.sidebar.radio(
    "Language / Idioma",
    options=["es", "en"],
    format_func=lambda x: "🇪🇸 Español" if x == "es" else "🇬🇧 English",
    index=0 if st.session_state.lang == "es" else 1
)

# Update session state if changed
if lang_option != st.session_state.lang:
    st.session_state.lang = lang_option
    st.rerun() # Refresh the app to apply the new language

st.sidebar.success("Versión Piloto: Aller" if st.session_state.lang == "es" else "Pilot Version: Aller")

# The rest of your app.py (Streamlit will automatically load pages/1_Home.py, etc.)



st.set_page_config(
    page_title="Territorial Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
st.sidebar.title("ArsMens Platform")
st.sidebar.markdown("---")

# Footer Component
def render_footer():
    st.markdown("---")
    st.caption(
        "**Data sources:** INE, SADEI, Catastro, OpenStreetMap, Gobierno del Principado de Asturias. "
        "Prototype under development. © 2025 ArsMens."
    )

# Main App Logic
st.sidebar.success("Pilot Version: Aller")

# We use Streamlit's multipage feature. 
# The pages in the 'pages' folder will automatically appear in the sidebar.
# This file just sets the global state.

# You can add a home button or logo here if needed.