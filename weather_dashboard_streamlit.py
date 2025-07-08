
# weather_dashboard_streamlit.py

import streamlit as st
import requests
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

# =============== USER SETTINGS ===============
API_KEY = "8c6ce0bddfc4a80eff7ee4faa52755a0"  # ✅ Your API Key
DEFAULT_CITY = "Bangalore"
UNITS = "metric"
# =============================================

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={UNITS}"
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def extract_data(data):
    dates, temps, hums = [], [], []
    for entry in data["list"]:
        dt_obj = dt.datetime.fromtimestamp(entry["dt"])
        dates.append(dt_obj)
        temps.append(entry["main"]["temp"])
        hums.append(entry["main"]["humidity"])
    return dates, temps, hums

def plot_chart(x, y, label, color):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(x, y, color=color, marker="o")
    ax.set_title(label)
    ax.set_xlabel("Date & Time")
    ax.set_ylabel(label)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ================= STREAMLIT UI ==================

st.set_page_config(page_title="Weather Dashboard", layout="centered")
st.title("🌦️ 5-Day Weather Forecast Dashboard")

city = st.text_input("Enter City Name", DEFAULT_CITY)

if st.button("Get Forecast"):
    with st.spinner("Fetching weather data..."):
        raw_data = fetch_weather(city)

    if raw_data and raw_data.get("cod") == "200":
        dates, temps, hums = extract_data(raw_data)
        
        st.subheader(f"📊 Temperature Forecast for {city}")
        plot_chart(dates, temps, "Temperature (°C)", "orange")

        st.subheader(f"💧 Humidity Forecast for {city}")
        plot_chart(dates, hums, "Humidity (%)", "blue")
    else:
        st.error("Failed to retrieve data. Check the city name or API key.")
