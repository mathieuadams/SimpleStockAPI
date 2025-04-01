# 📈 Stock Stats API

A simple Flask-based API that provides key technical indicators for any stock symbol using Yahoo Finance data.

---

## 🚀 Features

- ✅ Current Price  
- 📈 Moving Averages (10, 20, 50-day)  
- 🔄 Correlation to SPY  
- 📉 RSI (Relative Strength Index)  
- 🧮 MACD (Moving Average Convergence Divergence)  

---

## 🛠 Tech Stack

- Python 3  
- Flask  
- yfinance  
- pandas  
- ta (Technical Analysis library)  

---

## 🛁 API Endpoint

### `GET /api/v1/stats?symbol=XYZ`

**Query Parameters:**

- `symbol`: Stock ticker (e.g., `AAPL`, `TSLA`, `GOOGL`)

**Example:**
```http
GET /api/v1/stats?symbol=AAPL
```

---

## 📦 Example Response

```json
{
  "symbol": "AAPL",
  "price": 172.45,
  "ma_10": 170.92,
  "ma_20": 169.84,
  "ma_50": 165.33,
  "correlation_to_SPY": 0.91,
  "rsi": 58.23,
  "macd": {
    "macd": 1.45,
    "signal": 1.21,
    "histogram": 0.24
  }
}
```

---

## 🌐 Web Interface

Visit the homepage at `/` for simple API documentation and an example response:

```
http://127.0.0.1:5000/
```

---

## 📦 Setup Instructions

### Clone the repository

```bash
git clone https://github.com/your-username/stockstats-api.git
cd stockstats-api
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the app

```bash
python app.py
```

---

## 📁 Project Structure

```bash
stockstats-flask-api/
├── app.py          # Main Flask app
├── utils.py        # Data processing & indicators
├── templates/
│   └── index.html  # Frontend documentation page
└── requirements.txt
```

---

## 📄 License

MIT License

---

## ✨ Acknowledgments

- [Yahoo Finance via yfinance](https://github.com/ranaroussi/yfinance)  
- [Technical Analysis Library in Python](https://technical-analysis-library-in-python.readthedocs.io/)
