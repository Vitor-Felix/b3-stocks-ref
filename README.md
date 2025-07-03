# 📊 B3 Stock & FII Dashboard (MVP)

This project is a personal financial dashboard to analyze **Brazilian stocks and real estate investment funds (FIIs)** listed on **B3 (Brasil, Bolsa, Balcão)**.

The goal is to provide a **simple, visual, and interactive** way to:
- Search for a stock/FII by its ticker (e.g. PETR4, HGLG11)
- See valuation indicators and historical price data
- Visualize dividend distribution over time

---

## 🚀 Features (MVP Scope)

<details> <summary><strong>📌 Click to view planned features</strong> <em>(None implemented yet; target MVP scope)</em></summary>

- 🔍 Ticker search (stocks and FIIs)
- 📊 Key indicators (P/E, Dividend Yield, P/B, etc.)
- 📈 Price history chart (interactive time-series visualization)
- 💰 Dividend chart (track payouts over time)
- 📥 Export as PDF/PNG (optional stretch goal)

</details>

### 🏗️ In Progress -> Project Setup
- Initializing repository, environment, and dependency structure.

---

## 🛠️ Getting Started

### 1. Clone this repo
```bash
git clone https://github.com/YOUR-USERNAME/b3-stocks-ref.git
cd b3-stocks-ref
```

### 2. Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the dashboard
```bash
streamlit run main.py
```
It will start the dashboard at http://localhost:8501.

---

## 🧪 Project Structure
```pearl
b3-stocks-ref/
├── data/             # Local cache or saved data
├── main.py           # Streamlit app entry point
├── modules/          # Custom modules (scrapers, charts, indicators)
├── requirements.txt  # Project dependencies
└── README.md         # This file
```

---

## 💻 Technologies
- Python 3
- Streamlit (UI/dashboard framework)
- pandas, matplotlib (data processing/visualization)
- yfinance or B3 APIs (market data)
- Git & GitHub (version control)

---

## 📌 License
MIT – free to use, improve, and share!

---