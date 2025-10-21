import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib
import os

# Ensure model and scaler exist
if not os.path.exists("lstm_model.h5") or not os.path.exists("scaler.pkl"):
    print("No trained model found. Creating dummy LSTM model and scaler...")

    # Dummy model
    dummy_model = Sequential()
    dummy_model.add(LSTM(50, return_sequences=True, input_shape=(100, 1)))
    dummy_model.add(LSTM(50, return_sequences=True))
    dummy_model.add(LSTM(50))
    dummy_model.add(Dense(1))
    dummy_model.compile(loss="mean_squared_error", optimizer="adam")
    dummy_model.save("lstm_model.h5")

    # Dummy scaler
    dummy_scaler = MinMaxScaler()
    dummy_scaler.fit(np.array([100, 200, 300, 400, 500]).reshape(-1, 1))
    joblib.dump(dummy_scaler, "scaler.pkl")

# Now load model + scaler
model = load_model("lstm_model.h5")
scaler = joblib.load("scaler.pkl")

# Download stock data
ticker = "005930.KS"  # Samsung Electronics
df_yf = yf.download(ticker, start="2010-01-01", end="2025-01-01", interval="1d")
df_yf = df_yf.reset_index()[["Date", "Close"]]

def preprocess_data(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    df.ffill(inplace=True)
    df["Close_scaled"] = scaler.transform(df["Close"].values.reshape(-1, 1))
    return df

def create_dataset(dataset, time_step=1):
    dataX = []
    for i in range(len(dataset) - time_step - 1):
        a = dataset[i:(i + time_step), 0]
        dataX.append(a)
    return np.array(dataX)

def predict_stock_price(df_input, time_step=100):
    processed_df = preprocess_data(df_input.copy())
    last_time_step_data = processed_df["Close_scaled"].values[-time_step:].reshape(1, time_step, 1)
    predicted_scaled_price = model.predict(last_time_step_data)
    predicted_price = scaler.inverse_transform(predicted_scaled_price)
    return predicted_price[0][0]

# Hugging Face (Gradio UI)
import gradio as gr

def predict_ui(ticker="AAPL"):
    df = yf.download(ticker, start="2020-01-01", end="2025-01-01", interval="1d")
    df = df.reset_index()[["Date", "Close"]]
    pred_price = predict_stock_price(df)
    return f"Predicted next day closing price for {ticker}: {pred_price:.2f}"

iface = gr.Interface(fn=predict_ui, inputs="text", outputs="text", title="Stock Price Prediction (LSTM)")
iface.launch()
