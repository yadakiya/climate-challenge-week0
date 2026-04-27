# import Streamlit library for building the web dashboard UI
import streamlit as st  

# import pandas for data manipulation (tables, filtering, grouping)
import pandas as pd  

# import matplotlib for plotting graphs
import matplotlib.pyplot as plt  

# import glob to read multiple files using a pattern (like all CSV files)
import glob  


# get all CSV files in the "data" folder that end with "_clean.csv"
files = glob.glob("data/*_clean.csv")  

# create an empty list to store each country's dataframe
df_list = []  


# loop through each file found in the folder
for file in files:
    
    # extract country name from file path
    # example: "data/ethiopia_clean.csv" → "Ethiopia"
    country = file.split("\\")[-1].replace("_clean.csv", "").capitalize()  

    # read the CSV file into a pandas DataFrame
    temp_df = pd.read_csv(file)  

    # convert all column names to uppercase to avoid inconsistency errors
    temp_df.columns = temp_df.columns.str.upper()  

    # create a new column called COUNTRY and assign the country name
    temp_df["COUNTRY"] = country  

    # add this dataframe to the list
    df_list.append(temp_df)  


# combine all individual country dataframes into one big dataframe
df = pd.concat(df_list, ignore_index=True)  

# ensure all column names are uppercase (extra safety step)
df.columns = df.columns.str.upper()  


# set the title of the Streamlit app
st.title("🌍 Climate Change Dashboard (5 Countries)")  


# display column names (used for debugging to check data structure)
st.write("Columns:", df.columns)  


# add a sidebar section for filters
st.sidebar.header("Filters")  


# get unique country names (drop missing values just in case)
countries = list(df["COUNTRY"].dropna().unique())  


# create a multi-select widget so user can choose countries
selected_countries = st.sidebar.multiselect(
    "Select Countries",      # label shown to user
    countries,               # available options
    default=countries        # all selected by default
)  


# find minimum year in dataset
min_year = int(df["YEAR"].min())  

# find maximum year in dataset
max_year = int(df["YEAR"].max())  


# create a slider to filter data by year range
year_range = st.sidebar.slider(
    "Select Year Range",     # label
    min_year,                # minimum value
    max_year,                # maximum value
    (min_year, max_year)     # default range
)  


# filter dataset based on selected countries and year range
filtered_df = df[
    (df["COUNTRY"].isin(selected_countries)) &   # keep selected countries
    (df["YEAR"] >= year_range[0]) &              # apply start year
    (df["YEAR"] <= year_range[1])                # apply end year
]  


# show section title in app
st.subheader("🌡 Temperature Trend Comparison")  


# group data by YEAR and COUNTRY and calculate average temperature (T2M)
temp_by_country = filtered_df.groupby(["YEAR", "COUNTRY"])["T2M"].mean().reset_index()  


# create a matplotlib figure and axis
fig1, ax1 = plt.subplots()  


# loop through each country to plot its temperature trend
for c in filtered_df["COUNTRY"].unique():
    
    # get data only for this country
    data = temp_by_country[temp_by_country["COUNTRY"] == c]  
    
    # plot year vs temperature
    ax1.plot(data["YEAR"], data["T2M"], label=c)  


# label x-axis
ax1.set_xlabel("Year")  

# label y-axis
ax1.set_ylabel("Temperature (T2M)")  

# show legend (country names)
ax1.legend()  


# display the plot inside Streamlit app
st.pyplot(fig1)  


# section title for precipitation comparison
st.subheader("🌧 Precipitation Comparison")  


# create new figure for boxplot
fig2, ax2 = plt.subplots()  


# create boxplot showing rainfall distribution per country
ax2.boxplot(
    [
        # for each country, get precipitation values and remove missing values
        filtered_df[filtered_df["COUNTRY"] == c]["PRECTOTCORR"].dropna()
        for c in filtered_df["COUNTRY"].unique()
    ],
    labels=filtered_df["COUNTRY"].unique()  # label each box with country name
)  


# label y-axis
ax2.set_ylabel("Precipitation")  

# display the plot
st.pyplot(fig2)  


# section title for summary statistics
st.subheader("📊 Summary Statistics")  


# show temperature statistics: mean, median, and standard deviation
st.write(
    "Temperature Stats",
    filtered_df.groupby("COUNTRY")["T2M"].agg(["mean", "median", "std"])
)  


# show rainfall statistics
st.write(
    "Precipitation Stats",
    filtered_df.groupby("COUNTRY")["PRECTOTCORR"].agg(["mean", "median", "std"])
)  


# section title for extreme heat analysis
st.subheader("🔥 Extreme Heat Days (>35°C)")  


# filter rows where max temperature exceeds 35°C
heat = filtered_df[filtered_df["T2M_MAX"] > 35]  


# count number of extreme heat days per country
heat_counts = heat.groupby("COUNTRY").size()  


# display as bar chart
st.bar_chart(heat_counts)  


# section title for dry days (drought indicator)
st.subheader("🌵 Dry Days (<1mm Rainfall)")  


# filter rows where rainfall is less than 1 mm
dry = filtered_df[filtered_df["PRECTOTCORR"] < 1]  


# count dry days per country
dry_counts = dry.groupby("COUNTRY").size()  


# display as bar chart
st.bar_chart(dry_counts)  


# section title for key performance indicators
st.subheader("📌 KPIs")  


# create two columns for displaying metrics side by side
col1, col2 = st.columns(2)  


# show average temperature KPI
col1.metric("Avg Temperature", round(filtered_df["T2M"].mean(), 2))  


# show average rainfall KPI
col2.metric("Avg Rainfall", round(filtered_df["PRECTOTCORR"].mean(), 2))  