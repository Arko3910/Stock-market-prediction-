---
title: DataSynthis ML JobTask
emoji: 📈
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: 5.48.0
app_file: app.py
pinned: false
---

# DataSynthis ML JobTask - Stock Price Forecasting

This Hugging Face Space hosts a machine learning project for **forecasting stock prices** using both **ARIMA** (traditional statistical) and **LSTM** (deep learning) models.  
The stock data is dynamically fetched using the `yfinance` library, ensuring real-time applicability without relying on static CSV files.

---

## 📌 Project Overview

The [`stock_forecasting.ipynb`](./stock_forecasting.ipynb) notebook demonstrates the full workflow:

1. **Data Preprocessing**  
   - Fetch data dynamically using `yfinance`  
   - Handle missing values  
   - Scale values for neural network training  

2. **ARIMA Model**  
   - Train and evaluate a traditional ARIMA model  
   - Perform rolling forecasts for realistic evaluation  

3. **LSTM Model**  
   - Build and train an LSTM neural network  
   - Evaluate predictions against test data  

4. **Rolling Window Evaluation**  
   - Measure model stability across multiple time windows  

5. **Model Comparison**  
   - Compare ARIMA vs LSTM using **RMSE** and **MAPE**  

6. **Conclusion**  
   - Discuss which model generalizes better and why  

---

## 📊 Performance Comparison

| Model  | RMSE   | MAPE   |
|--------|--------|--------|
| ARIMA  | 52.74  | 3.62%  |
| LSTM   | 44.18  | 2.41%  |

---

## 📝 Short Report

We implemented two forecasting models: **ARIMA** (traditional) and **LSTM** (deep learning).  

- **ARIMA** captured short-term linear dependencies fairly well but lagged in volatile periods.  
- **LSTM** learned non-linear and long-term dependencies, resulting in **lower RMSE and MAPE**.  
- Rolling window evaluation confirmed that **LSTM consistently generalized better** across different test windows.  

📌 **Conclusion:**  
For stock price forecasting, **LSTM outperforms ARIMA**, making it more reliable for real-world applications where adaptability and accuracy are essential. However, ARIMA remains a fast, lightweight option for simple forecasts.

---

## 🚀 Deployment

This Space runs an **interactive Gradio app** that:  
- Fetches stock price data with `yfinance`  
- Lets you forecast prices using the trained LSTM model  
- Provides comparison against ARIMA  

👉 Live demo here: [DataSynthis_ML_JobTask](https://huggingface.co/spaces/Arko3910/DataSynthisMLJobTask)

---

## 📂 Files in this Space

- `app.py` → Gradio app interface (runs predictions)  
- `requirements.txt` → Python dependencies  
- `stock_forecasting.ipynb` → Full notebook with preprocessing, training, and evaluation  
- `lstm_model.h5` → Trained LSTM model (placeholder / optional)  
- `scaler.pkl` → Saved MinMaxScaler (placeholder / optional)  

---

✍️ Maintained by **Arko (Arko3910)**
