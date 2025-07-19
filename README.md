Weather Dashboard

This is a simple project built with Streamlit. It displays a 5‑day weather forecast for any city, with temperature and humidity visualized on charts. Data is fetched from the OpenWeatherMap API.

How to Run

Install the required libraries:


> pip install streamlit requests matplotlib seaborn

Open the Python file and set your OpenWeatherMap API key in the API_KEY variable.

Start the app from your terminal:

> streamlit run weather_dashboard_streamlit.py

or, if that does not work:

> python -m streamlit run weather_dashboard_streamlit.py

The app will open in your browser at http://localhost:8501.

Features :

   . Enter any city name.

   . View temperature and humidity trends for the next 5 days.

   . Clear and simple charts generated using Matplotlib and Seaborn.
