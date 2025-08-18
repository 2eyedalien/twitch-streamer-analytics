import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Twitch Stream Analysis", layout="wide")

st.title("📊 Twitch Stream Analysis Dashboard")
st.markdown("""
This dashboard analyzes the **Top Twitch Channels (July 17 – Aug 16, 2025)** dataset.  
Explore airtime, average viewers, and engagement metrics.
""")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("../data/top_twitch_channels.csv")

df = load_data()

# Feature Engineering
df['Viewers_per_Hour'] = df['Hours Watched'] / df['Airtime Hours']
df['Audience_Stability'] = df['Average Viewers'] / df['Peak Viewers']

# Sidebar filters
channels = st.sidebar.multiselect("Select Channels", options=df['Channel'], default=df['Channel'].head(5))

filtered_df = df[df['Channel'].isin(channels)] if channels else df

st.subheader("Dataset Preview")
st.dataframe(filtered_df.head())

# Visualization 1: Airtime vs Average Viewers
st.subheader("Airtime vs Average Viewers")
fig, ax = plt.subplots(figsize=(10,6))
sns.scatterplot(data=df, x='Airtime Hours', y='Average Viewers', size='Peak Viewers', legend=False, alpha=0.7, ax=ax)
ax.set_title("Airtime vs Average Viewers (bubble size = Peak Viewers)")
st.pyplot(fig)

# Visualization 2: Leaderboard
st.subheader("Top 10 by Viewers per Hour")
top_eff = df.sort_values('Viewers_per_Hour', ascending=False).head(10)
st.table(top_eff[['Channel', 'Viewers_per_Hour', 'Audience_Stability']])
