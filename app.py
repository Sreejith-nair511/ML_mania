# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# F1 WINNER PREDICTION APP (2025-2026)
# ===============================

# Page Config
st.set_page_config(page_title="F1 Winner Prediction", page_icon="🏎️", layout="wide")

# Title
st.title("🏆 Formula 1 Constructor Winner Prediction (2025 - 2026)")
st.write("This app shows **simulated winning probabilities** for F1 constructors in 2025 & 2026.")

# Dataset
data = {
    "Year": [2025, 2025, 2025, 2025,
             2026, 2026, 2026, 2026],
    "Team": ["McLaren", "Ferrari", "Red Bull", "Mercedes",
             "McLaren", "Mercedes", "Ferrari", "Red Bull"],
    "Win_Probability": [0.40, 0.25, 0.20, 0.15,   # 2025 predictions
                        0.35, 0.30, 0.20, 0.15]   # 2026 predictions
}
df = pd.DataFrame(data)

# Sidebar Year Selection
st.sidebar.header("Select Year")
year_selected = st.sidebar.radio("Choose a season:", [2025, 2026])

# Filter Dataset
df_year = df[df["Year"] == year_selected]

# Show Dataset
st.subheader(f"📊 Prediction Dataset for {year_selected}")
st.dataframe(df_year)

# Plot Graph
fig, ax = plt.subplots(figsize=(8,6))
ax.bar(df_year["Team"], df_year["Win_Probability"],
       color="orange" if year_selected == 2025 else "skyblue")
ax.set_title(f"F1 Constructor Predicted Winner Chances - {year_selected}")
ax.set_xlabel("Teams")
ax.set_ylabel("Winning Probability")
st.pyplot(fig)

# Predicted Winner
winner = df_year.loc[df_year["Win_Probability"].idxmax()]["Team"]
st.success(f"🏆 Predicted Winner {year_selected}: **{winner}**")
