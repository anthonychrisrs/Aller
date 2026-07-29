import streamlit as st
import pandas as pd
import pydeck as pdk
from translations import t # Import the translation function

st.set_page_config(page_title="Territorial Intelligence Platform", layout="wide")

# Get current language (fallback to 'es' if not set yet)
lang = st.session_state.get('lang', 'es')

# --- STRATEGIC REBRANDING (Translated) ---
st.markdown(f"# {t('platform_title', lang)}")
st.markdown(f"### {t('platform_subtitle', lang)}")
st.markdown("---")

@st.cache_data
def load_data():
    try:
        # Using the path from your working code
        demo_df = pd.read_parquet("data/03_processed/municipal_demographics.parquet")
        return demo_df
    except FileNotFoundError:
        st.error("Data not found. Please run the data generation script first.")
        return None

demo_df = load_data()

if demo_df is not None:
    # --- MUNICIPAL OVERVIEW ---
    st.markdown(f"### {t('municipal_overview', lang)}")
    st.write(t('municipal_overview_desc', lang))
    
    # Filter for the latest available year
    latest_year = int(demo_df['Year'].max())
    current_data = demo_df[demo_df['Year'] == latest_year]
    
    # --- OBJECTIVE KPI CALCULATIONS (From your working code) ---
    if 'Total' in current_data['Sex'].values:
        total_pop = current_data[current_data['Sex'] == 'Total']['Population'].sum()
    else:
        total_pop = current_data['Population'].sum()
        
    def get_pop(age_groups):
        mask = current_data['Age_Group'].isin(age_groups)
        if 'Total' in current_data['Sex'].values:
            mask = mask & (current_data['Sex'] == 'Total')
        return current_data[mask]['Population'].sum()

    pop_0_14 = get_pop(['0-4', '5-9', '10-14'])
    pop_15_64 = get_pop(['15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64'])
    pop_65_plus = get_pop(['65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95-99', '100+'])

    aging_index = (pop_65_plus / pop_0_14 * 100) if pop_0_14 > 0 else 0
    dependency_ratio = ((pop_0_14 + pop_65_plus) / pop_15_64 * 100) if pop_15_64 > 0 else 0

    age_midpoints = {
        '0-4': 2, '5-9': 7, '10-14': 12, '15-19': 17, '20-24': 22, '25-29': 27, 
        '30-34': 32, '35-39': 37, '40-44': 42, '45-49': 47, '50-54': 52, '55-59': 57, 
        '60-64': 62, '65-69': 67, '70-74': 72, '75-79': 77, '80-84': 82, '85-89': 87, 
        '90-94': 92, '95-99': 97, '100+': 100
    }
    
    total_weighted_age = 0
    total_count = 0
    for idx, row in current_data.iterrows():
        if row['Sex'] == 'Total' or 'Total' not in current_data['Sex'].values:
            midpoint = age_midpoints.get(row['Age_Group'], 50)
            total_weighted_age += midpoint * row['Population']
            total_count += row['Population']
    
    median_age_approx = total_weighted_age / total_count if total_count > 0 else 0

    # --- DISPLAY KPIs (Translated) ---
    st.markdown(f"### {t('global_kpis', lang)} ({latest_year})")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label=t('total_pop', lang), value=f"{total_pop:,.0f}")
    with col2:
        # Dynamic unit translation
        unit = "años" if lang == "es" else "years"
        st.metric(label=t('median_age', lang), value=f"{median_age_approx:.1f} {unit}")
    with col3:
        st.metric(label=t('aging_index', lang), value=f"{aging_index:.0f}%")
    with col4:
        st.metric(label=t('dependency_ratio', lang), value=f"{dependency_ratio:.0f}%")

    # --- DEMOGRAPHIC RISK MAP (Translated) ---
    st.markdown(f"### {t('risk_map', lang)}")
    st.write(t('risk_map_desc', lang))
    
    if 'Total' in current_data['Sex'].values:
        map_data = current_data[current_data['Sex'] == 'Total'].groupby(['Municipality', 'Lat', 'Lon'])['Population'].sum().reset_index()
    else:
        map_data = current_data.groupby(['Municipality', 'Lat', 'Lon'])['Population'].sum().reset_index()
    
    max_pop = map_data['Population'].max()
    map_data['weight'] = 1 - (map_data['Population'] / max_pop) 
    
    layer = pdk.Layer(
        "HeatmapLayer",
        map_data,
        opacity=0.8,
        get_position=["Lon", "Lat"],
        get_weight="weight",
        threshold=0.3,
        radius=30000
    )
    
    view_state = pdk.ViewState(
        latitude=43.15,
        longitude=-5.65,
        zoom=9,
        pitch=45
    )
    
    # Translate tooltip text
    inhabitants_label = "habitantes" if lang == "es" else "inhabitants"
    
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": f"{{Municipality}}: {{Population}} {inhabitants_label}"}
    )
    st.pydeck_chart(r)