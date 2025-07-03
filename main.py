import streamlit as st
import yfinance as yf
import altair as alt

st.set_page_config(page_title="B3 Dashboard", layout="wide")
st.title("📊 B3 Stock & FII Dashboard")

ticker_input = st.text_input("Enter a ticker (e.g. PETR4.SA, HGLG11.SA):").upper()

if ticker_input:
    try:
        # --- INFO GATHERING SECTION ---
        stock = yf.Ticker(ticker_input)
        info = stock.info

        st.subheader(f"📌 {info.get('shortName', 'Unknown')}")
        st.metric(label="💵 Current Price", value=f"R${info['currentPrice']:.2f}")
        st.metric(label="📈 Daily Change (%)", value=f"{info['regularMarketChangePercent']:.2f}%")
        st.metric(label="🏢 Market Cap", value=f"R${info['marketCap']:,}")

        # --- PRICE HISTORY SECTION ---
        st.divider()
        st.subheader("📈 Price History (Last 6 Months)")

        # Let the user choose the period
        period_option = st.selectbox(
            "Select period to display:",
            options=["6 months", "1 year"]
        )

        # Map selection to yfinance's accepted values
        period_map = {
            "6 months": "6mo",
            "1 year": "1y"
        }
        selected_period = period_map[period_option]

        # Fetch price history
        history = stock.history(period=selected_period)

        if not history.empty:
            history.reset_index(inplace=True)
            chart = alt.Chart(history).mark_line().encode(
                x="Date:T",
                y=alt.Y("Close:Q", title="Price (R$)"),
                tooltip=["Date:T", "Close:Q"]
            ).properties(width=800, height=400)

            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("No price history found for this asset.")

    except Exception as e:
        st.error("Error fetching data. Make sure the ticker is valid and ends in `.SA`.")
        st.exception(e)
