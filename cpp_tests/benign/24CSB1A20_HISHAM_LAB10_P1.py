import mysql.connector
import requests
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

# connect to mysql and create schema and tables
def makebase():
    con = mysql.connector.connect(host="localhost", user="root", password="NITW@123")
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS `24CSB1A20`")
    cur.execute("USE `24CSB1A20`")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS weather(
            date DATE,
            tempmax FLOAT,
            tempmin FLOAT,
            precip FLOAT,
            windmax FLOAT,
            windmean FLOAT,
            humid FLOAT,
            press FLOAT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS forex_data(
            date DATE,
            openin FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT
        )
    """)
    con.commit()
    cur.close()
    con.close()

# get weather data
def getweather(lat=17.98, lon=79.53, yr=2025):
    url = "https://archive-api.open-meteo.com/v1/archive"
    pars = {
        "latitude": lat,
        "longitude": lon,
        "start_date": f"{yr}-09-01",
        "end_date": f"{yr}-09-30",
        "timezone": "auto",
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "wind_speed_10m_max",
            "wind_speed_10m_mean",
            "relative_humidity_2m_mean",
            "pressure_msl_mean"
        ]
    }
    res = requests.get(url, params=pars)
    res.raise_for_status()
    dat = res.json()
    day = dat["daily"]
    df = pd.DataFrame(day)
    return df

# insert weather data
def putweather(df):
    con = mysql.connector.connect(host="localhost", user="root", password="NITW@123", database="24CSB1A20")
    cur = con.cursor()
    for _, r in df.iterrows():
        cur.execute("""
            INSERT INTO weather VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
        """, (r["time"], r["temperature_2m_max"], r["temperature_2m_min"], r["precipitation_sum"],
              r["wind_speed_10m_max"], r["wind_speed_10m_mean"], r["relative_humidity_2m_mean"], r["pressure_msl_mean"]))
    con.commit()
    cur.close()
    con.close()

# get forex data
def getforex():
    t = "USDINR=X"
    dat = yf.download(t, start="2025-09-01", end="2025-09-30", interval="1d")
    if dat.empty:
        return None
    df = dat.reset_index()[["Date", "Open", "High", "Low", "Close"]]
    df.columns = ["date", "openin", "high", "low", "close"]
    return df

# insert forex data
def putforex(df):
    con = mysql.connector.connect(host="localhost", user="root", password="NITW@123", database="24CSB1A20")
    cur = con.cursor()
    for _, r in df.iterrows():
        cur.execute("""
            INSERT INTO forex_data VALUES(%s,%s,%s,%s,%s)
        """, (r["date"], r["openin"], r["high"], r["low"], r["close"]))
    con.commit()
    cur.close()
    con.close()

# plot weather
def plotweather():
    con = mysql.connector.connect(host="localhost", user="root", password="NITW@123", database="24CSB1A20")
    df = pd.read_sql("SELECT * FROM weather", con)
    con.close()
    plt.figure()
    plt.plot(df["tempmax"], label="tempmax")
    plt.plot(df["tempmin"], label="tempmin")
    plt.legend()
    plt.title("Temperature line plot")
    plt.figure()
    plt.plot(df["windmax"], label="windmax")
    plt.plot(df["windmean"], label="windmean")
    plt.legend()
    plt.title("Wind line plot")
    plt.figure()
    plt.plot(df["humid"], label="humidity")
    plt.title("Humidity line plot")
    plt.figure()
    plt.plot(df["press"], label="pressure")
    plt.title("Pressure line plot")
    plt.figure()
    plt.plot(df["precip"], label="precipitation")
    plt.title("Precipitation line plot")
    plt.show()

# plot forex candlestick
def plotforex():
    con = mysql.connector.connect(host="localhost", user="root", password="NITW@123", database="24CSB1A20")
    df = pd.read_sql("SELECT * FROM forex_data", con)
    con.close()
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    mpf.plot(df, type="candle", style="charles", title="USD INR Candlestick")

# main part
if __name__ == "__main__":
    makebase()
    
    print("getting forex data")
    sdata = getforex()
    if sdata is not None:
        print("sending to mysql")
        putforex(sdata)
        print("done inserting")

    print("getting weather data")
    wdata = getweather()
    putweather(wdata)

    print("plotting weather data")
    plotweather()

    print("plotting forex candlestick")
    plotforex()

    print("done all")
