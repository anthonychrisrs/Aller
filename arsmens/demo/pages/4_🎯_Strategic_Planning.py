import streamlit as st
from translations import t

st.markdown("# Strategic Planning")
st.info("🔹 **Decision Support:** This module translates demographic data into evidence-informed planning considerations for municipal technicians.")

st.markdown("---")

st.markdown("### Current Demographic Profile: Aller")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Aging Index", "436%", delta="Critical")
with col2:
    st.metric("Median Age", "52.8 years")
with col3:
    st.metric("Population Trend", "Declining")

st.markdown("---")

st.markdown("### Evidence-Informed Planning Considerations")
st.write("Based on the current demographic profile, the following areas are prioritized for strategic intervention:")

considerations = [
    {
        "Priority": "High",
        "Area": "Health & Accessibility",
        "Action": "Improve accessibility to health services for an aging population. Consider mobile health units or telemedicine hubs."
    },
    {
        "Priority": "High",
        "Area": "Housing & Urbanism",
        "Action": "Promote rehabilitation of vacant housing to attract new residents and improve energy efficiency."
    },
    {
        "Priority": "Medium",
        "Area": "Economic Development",
        "Action": "Encourage business succession programs to prevent closure of local enterprises due to retirement."
    },
    {
        "Priority": "Medium",
        "Area": "Connectivity",
        "Action": "Strengthen public transport connections to larger urban centers (Oviedo/Gijón) for younger residents."
    }
]

for c in considerations:
    st.markdown(f"**{c['Area']}** ({c['Priority']} Priority)")
    st.write(f"- {c['Action']}")
    st.markdown("---")

st.markdown("---")
st.caption("**Data sources:** INE, SADEI. Prototype under development.")