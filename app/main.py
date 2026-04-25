import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import glob

# ============================
# LOAD ALL 5 COUNTRIES SAFELY
# ============================
files = glob.glob("data/*_clean.csv")

df_list = []

for file in files:
    country = file.split("\\")[-1].replace("_clean.csv", "").capitalize()

    temp_df = pd.read_csv(file)

    # Normalize column names
    temp_df.columns = temp_df.columns.str.upper()

    # Add COUNTRY column
    temp_df["COUNTRY"] = country

    df_list.append(temp_df)

df = pd.concat(df_list, ignore_index=True)

# FINAL SAFETY CHECK
df.columns = df.columns.str.upper()

# ============================
# APP TITLE
# ============================
st.title("🌍 Climate Change Dashboard (5 Countries)")

# ============================
# DEBUG (IMPORTANT — REMOVE LATER IF YOU WANT)
# ============================
st.write("Columns:", df.columns)

# ============================
# SIDEBAR FILTERS
# ============================
st.sidebar.header("Filters")

# SAFE COUNTRY HANDLING
countries = list(df["COUNTRY"].dropna().unique())

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    countries,
    default=countries
)

# YEAR HANDLING (SAFE)
min_year = int(df["YEAR"].min())
max_year = int(df["YEAR"].max())

year_range = st.sidebar.slider(
    "Select Year Range",
    min_year,
    max_year,
    (min_year, max_year)
)

# ============================
# FILTER DATA
# ============================
filtered_df = df[
    (df["COUNTRY"].isin(selected_countries)) &
    (df["YEAR"] >= year_range[0]) &
    (df["YEAR"] <= year_range[1])
]

# ============================
# TEMPERATURE TREND
# ============================
st.subheader("🌡 Temperature Trend Comparison")

temp_by_country = filtered_df.groupby(["YEAR", "COUNTRY"])["T2M"].mean().reset_index()

fig1, ax1 = plt.subplots()

for c in filtered_df["COUNTRY"].unique():
    data = temp_by_country[temp_by_country["COUNTRY"] == c]
    ax1.plot(data["YEAR"], data["T2M"], label=c)

ax1.set_xlabel("Year")
ax1.set_ylabel("Temperature (T2M)")
ax1.legend()
st.pyplot(fig1)

# ============================
# PRECIPITATION BOXPLOT
# ============================
st.subheader("🌧 Precipitation Comparison")

fig2, ax2 = plt.subplots()

ax2.boxplot(
    [filtered_df[filtered_df["COUNTRY"] == c]["PRECTOTCORR"].dropna()
     for c in filtered_df["COUNTRY"].unique()],
    labels=filtered_df["COUNTRY"].unique()
)

ax2.set_ylabel("Precipitation")
st.pyplot(fig2)

# ============================
# SUMMARY TABLES
# ============================
st.subheader("📊 Summary Statistics")

st.write(
    "Temperature Stats",
    filtered_df.groupby("COUNTRY")["T2M"].agg(["mean", "median", "std"])
)

st.write(
    "Precipitation Stats",
    filtered_df.groupby("COUNTRY")["PRECTOTCORR"].agg(["mean", "median", "std"])
)

# ============================
# EXTREME HEAT
# ============================
st.subheader("🔥 Extreme Heat Days (>35°C)")

heat = filtered_df[filtered_df["T2M_MAX"] > 35]
heat_counts = heat.groupby("COUNTRY").size()

st.bar_chart(heat_counts)

# ============================
# DRY DAYS
# ============================
st.subheader("🌵 Dry Days (<1mm Rainfall)")

dry = filtered_df[filtered_df["PRECTOTCORR"] < 1]
dry_counts = dry.groupby("COUNTRY").size()

st.bar_chart(dry_counts)

# ============================
# KPIs
# ============================
st.subheader("📌 KPIs")

col1, col2 = st.columns(2)

col1.metric("Avg Temperature", round(filtered_df["T2M"].mean(), 2))
col2.metric("Avg Rainfall", round(filtered_df["PRECTOTCORR"].mean(), 2))
