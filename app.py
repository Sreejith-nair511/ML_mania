import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # important for Streamlit Cloud
import matplotlib.pyplot as plt

# ===============================
# DATASET
# ===============================
data = {
    "Year": [2025, 2025, 2025, 2025, 2025,
             2026, 2026, 2026, 2026, 2026],
    "Team": ["McLaren", "Red Bull", "Ferrari", "Mercedes", "Aston Martin",
             "McLaren", "Red Bull", "Ferrari", "Mercedes", "Aston Martin"],
    "Win_Probability": [0.40, 0.25, 0.15, 0.12, 0.08,   # 2025 predictions
                        0.30, 0.08, 0.25, 0.32, 0.05]   # 2026 predictions
}

df = pd.DataFrame(data)

# ===============================
# STREAMLIT APP
# ===============================
st.set_page_config(page_title="🏎️ F1 Winner Prediction", page_icon="🏁", layout="wide")

st.title("🏎️ Formula 1 Winner Predictions (2025-2026)")
st.write("This app shows **predicted winning probabilities** for Formula 1 constructors in 2025 & 2026.")

# Sidebar
year_choice = st.sidebar.selectbox("Select Year", [2025, 2026])

# Filter data
df_selected = df[df["Year"] == year_choice]

# Plot
fig, ax = plt.subplots(figsize=(8,6))
ax.bar(df_selected["Team"], df_selected["Win_Probability"], 
       color="orange" if year_choice == 2025 else "skyblue")
ax.set_title(f"F1 Predicted Winner Chances - {year_choice}")
ax.set_xlabel("Teams")
ax.set_ylabel("Winning Probability")

st.pyplot(fig)

# Show dataset
with st.expander("📊 Show Dataset"):
    st.dataframe(df_selected)

# Predicted Winner
winner = df_selected.loc[df_selected["Win_Probability"].idxmax()]["Team"]
st.success(f"🏆 Predicted Winner {year_choice}: **{winner}**")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Demo F1 Prediction")
