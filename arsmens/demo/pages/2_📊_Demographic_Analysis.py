import streamlit as st
import pandas as pd
import plotly.express as px
import os
from translations import t

st.set_page_config(page_title="Demographic Insights", layout="wide")
st.markdown("# Demographic Analysis")

@st.cache_data
def load_data():
    demo_df = pd.read_parquet("data/03_processed/municipal_demographics.parquet")
    paro_path = "data/03_processed/unemployment_aller.csv"
    paro_df = None
    if os.path.exists(paro_path):
        paro_df = pd.read_csv(paro_path)
    return demo_df, paro_df

df, paro_df = load_data()

st.sidebar.header("Filters")
municipalities = df['Municipality'].unique()
selected_mun = st.sidebar.selectbox("Select Municipality", municipalities)

# Slider covers the full range 1996-2025
selected_year = st.sidebar.slider("Select Year", min_value=1996, max_value=2025, value=2022)

filtered_df = df[(df['Municipality'] == selected_mun) & (df['Year'] == selected_year)]

col1, col2 = st.columns(2)

# --- POPULATION PYRAMID ---
with col1:
    st.markdown(f"### Population Structure ({selected_year})")
    
    if filtered_df.empty:
        st.warning(f"No detailed population data available for {selected_mun} in {selected_year}. (Real data for Aller: 2001-2022)")
    else:
        pyramid_df = filtered_df[filtered_df['Sex'] != 'Total'].copy()
        pyramid_df.loc[pyramid_df['Sex'] == 'Male', 'Population'] = -pyramid_df['Population']
        
        age_order = ["100+", "95-99", "90-94", "85-89", "80-84", "75-79", "70-74", "65-69", "60-64", 
                     "55-59", "50-54", "45-49", "40-44", "35-39", "30-34", "25-29", "20-24", 
                     "15-19", "10-14", "5-9", "0-4"]
        
        fig_pyr = px.bar(pyramid_df, y='Age_Group', x='Population', color='Sex', orientation='h',
                         barmode='relative', 
                         color_discrete_map={'Male': '#1f77b4', 'Female': '#ff7f0e'},
                         category_orders={"Age_Group": age_order})
        st.plotly_chart(fig_pyr, use_container_width=True)

# --- HISTORICAL TRENDS (FIXED) ---
with col2:
    st.markdown(f"### Historical Evolution ({selected_mun})")
    mun_data = df[df['Municipality'] == selected_mun]
    
    # FIX: Aggregate by Year and Sex to get Total Population per year (sums all age groups)
    plot_data = mun_data.groupby(['Year', 'Sex'])['Population'].sum().reset_index()
    
    fig_trend = px.line(plot_data, x='Year', y='Population', color='Sex', 
                        color_discrete_map={'Total': '#FFFFFF', 'Male': '#1f77b4', 'Female': '#ff7f0e'},
                        title="Population Evolution by Sex")
    
    st.plotly_chart(fig_trend, use_container_width=True)

# --- LABOR METRICS ---
st.markdown("### Labor Market Indicators")
if selected_mun == 'Aller' and paro_df is not None:
    st.write("Real registered unemployment data (Annual averages):")
    fig_paro = px.line(paro_df, x='Year', y=['Total_Unemployment', 'Male_Unemployment', 'Female_Unemployment'], 
                       title="Registered Unemployment by Sex",
                       labels={'value': 'Unemployed People', 'variable': 'Category'})
    st.plotly_chart(fig_paro, use_container_width=True)
else:
    st.info("Real labor data available for Aller.")