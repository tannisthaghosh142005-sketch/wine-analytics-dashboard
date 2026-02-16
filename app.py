import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv("sample_data.csv")

df = load_data()


# ===== FUTURISTIC BACKGROUND =====
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #0f2027, #203a43, #2c5364);
    color: white;
}

h1, h2, h3 {
    color: #00FFD1;
}

[data-testid="stMetricValue"] {
    font-size: 40px;
    color: #00FFD1;
}
</style>
""", unsafe_allow_html=True)


st.title("🚀 3D Wine Intelligence Dashboard")

# ===== KPI METRICS =====
col1, col2, col3 = st.columns(3)

col1.metric("Total Wines", len(df))
col2.metric("Avg Price", round(df["price"].mean(), 2))
col3.metric("Avg Rating", round(df["points"].mean(), 2))


# ===== 3D SCATTER =====
st.subheader("🌌 3D Wine Market Landscape")

fig3d = px.scatter_3d(
    df.sample(5000),
    x="price",
    y="points",
    z="country",
    color="points",
    size="price",
    opacity=0.7,
)

fig3d.update_layout(
    scene=dict(
        bgcolor="#0f2027",
        xaxis=dict(backgroundcolor="#203a43"),
        yaxis=dict(backgroundcolor="#203a43"),
        zaxis=dict(backgroundcolor="#203a43"),
    ),
    paper_bgcolor="#0f2027",
    font_color="white"
)

st.plotly_chart(fig3d, width="stretch")



# ===== INTERACTIVE HEATMAP =====
st.subheader("🔥 Price vs Rating Density")

heatmap = px.density_heatmap(
    df,
    x="price",
    y="points",
    nbinsx=40,
    nbinsy=40,
    color_continuous_scale="Turbo"
)

heatmap.update_layout(
    paper_bgcolor="#0f2027",
    font_color="white"
)

st.plotly_chart(heatmap, width="stretch")


# ===== GLOW BAR CHART =====
st.subheader("🌍 Global Wine Leaders")

country_counts = df['country'].value_counts().head(10)

bar = px.bar(
    x=country_counts.values,
    y=country_counts.index,
    orientation="h",
    color=country_counts.values,
    color_continuous_scale="Plasma"
)

bar.update_layout(
    paper_bgcolor="#0f2027",
    font_color="white"
)

st.plotly_chart(bar, width="stretch")

