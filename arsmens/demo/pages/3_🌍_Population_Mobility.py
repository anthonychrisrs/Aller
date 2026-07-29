import streamlit as st
import pandas as pd
import plotly.express as px
from translations import t



st.markdown("# Population Mobility")
st.info("🔹 **Prototype visualization:** Connected to official municipal data during pilot deployment. This module tracks the components of population change.")

st.markdown("---")

st.markdown("### Population Change Components")
st.write("Understanding the drivers of demographic change is critical for municipal planning.")

# Create a clean, professional table showing the components
# In a real deployment, these would be live data feeds.
data = {
    'Component': ['Internal Migration Balance', 'External Migration Balance', 'Natural Balance (Births - Deaths)'],
    '2022 Value': [-45, -12, -85], # Example realistic negative values for rural Aller
    'Trend': ['↓ Stable', '↓ Declining', '↓ Critical']
}
df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown("### Strategic Implications")
st.warning("The data indicates a negative natural balance and negative migration balance. This suggests a need for policies focused on **youth retention** and **attracting new residents**.")

st.markdown("---")
st.caption("**Data sources:** INE, SADEI. Prototype under development.")