import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="Climate Intelligence Dashboard",
    layout="wide"
)

# Load Data
climate_df = pd.read_csv("climate_data.csv")
forecast_df = pd.read_csv("temperature_forecast.csv")

# Convert Date Columns
climate_df["Date"] = pd.to_datetime(climate_df["Date"])
forecast_df["ds"] = pd.to_datetime(forecast_df["ds"])


# Title
st.title(" Climate Intelligence & Forecasting Dashboard")

# Sidebar Filter
st.sidebar.header("Filters")

selected_date = st.sidebar.date_input(
    "Select Date"
)


# KPI CARDS
st.subheader(" Climate Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Max Temp",
    f"{climate_df['Temp_Max'].mean():.2f} °C"
)

col2.metric(
    "Total Rainfall",
    f"{climate_df['Rainfall'].sum():.2f} mm"
)

col3.metric(
    "Average Wind Speed",
    f"{climate_df['WindSpeed'].mean():.2f}"
)

st.subheader(" Climate Overview")

col1, col2, col3 = st.columns(3)

# Existing Metrics
heatwave_days = len(
    climate_df[climate_df["Temp_Max"] > 40]
)

st.metric(
    " Heatwave Days",
    heatwave_days
)


# TEMPERATURE TREND
st.subheader(" Maximum Temperature Trend")

fig1 = px.line(
    climate_df,
    x="Date",
    y="Temp_Max"
)

st.plotly_chart(fig1, use_container_width=True)


# RAINFALL TREND
st.subheader(" Rainfall Trend")

fig2 = px.bar(
    climate_df,
    x="Date",
    y="Rainfall"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader(" Temperature Forecast")

future_temp = forecast_df["yhat"].iloc[-1]

st.metric(
    " Predicted Temperature",
    round(future_temp, 2)
)
# FORECAST GRAPH
st.subheader(" Temperature Forecast")

fig3 = px.line(
    forecast_df,
    x="ds",
    y="yhat"
)

st.plotly_chart(fig3, use_container_width=True)

st.subheader(" Actual vs Forecast Comparison")

fig = px.line()

fig.add_scatter(
    x=climate_df["Date"],
    y=climate_df["Temp_Max"],
    name="Actual"
)

fig.add_scatter(
    x=forecast_df["ds"],
    y=forecast_df["yhat"],
    name="Forecast"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# CONFIDENCE INTERVAL
st.subheader(" Forecast Confidence Range")

fig4 = px.line(
    forecast_df,
    x="ds",
    y=["yhat_lower", "yhat_upper"]
)

st.plotly_chart(fig4, use_container_width=True)


# CLIMATE RISK ALERTS
st.subheader(" Climate Risk Intelligence")

latest_temp = climate_df["Temp_Max"].iloc[-1]
latest_rain = climate_df["Rainfall"].iloc[-1]

if latest_temp > 40:
    st.error(" Heatwave Risk Detected")

elif latest_rain > 50:
    st.warning(" Heavy Rainfall Risk Detected")

else:
    st.success("Climate Conditions Normal")


# DATA PREVIEW
st.subheader(" Climate Dataset")

st.dataframe(climate_df.tail())


# PROJECT SUMMARY
st.subheader(" Project Summary")

st.write("""
This Climate Intelligence and Forecasting System integrates live weather data collection,
climate analysis, forecasting, and risk detection. Historical climate patterns were analyzed
using temperature, rainfall, and wind speed data. Prophet was used to generate future climate
forecasts, while risk intelligence was implemented to identify potential heatwave and rainfall risks.
""")


# PROJECT CONCLUSION
st.subheader(" Project Conclusion")

st.write("""
The project successfully transformed historical climate data into predictive environmental intelligence.
By combining API-based data collection, forecasting, risk detection, and interactive visualization,
the system provides valuable insights for climate monitoring and future environmental decision-making.
""")
st.success(
    " Climate Intelligence System Successfully Developed with API Integration, Forecasting, Risk Detection, and Interactive Dashboard Visualization."
)
