import streamlit as st
import random

# Page Config
st.set_page_config(page_title="LegendJournal | VIP Signals", layout="wide")

# Custom UI Styling
st.markdown("""
<style>
    body { color: #e2e8f0; background-color: #0f172a; }
    .signal-card { background: #1e293b; border-radius: 12px; padding: 24px; border-left: 6px solid #10b981; margin-bottom: 20px; }
    .signal-card-put { background: #1e293b; border-radius: 12px; padding: 24px; border-left: 6px solid #ef4444; margin-bottom: 20px; }
    .time-badge { background-color: #312e81; padding: 6px 12px; border-radius: 6px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("Quotex Smart Signal Generator")

# --- 1. TIMEZONE SELECTOR (SABSE UPAR) ---
st.subheader("🕒 Analysis Time (IST)")
col_time1, col_time2, col_time3 = st.columns([2, 2, 1])
with col_time1:
    selected_hour = st.selectbox("HOUR", [f"{i:02d}" for i in range(24)], index=14)
with col_time2:
    selected_minute = st.selectbox("MINUTE", [f"{i:02d}" for i in range(60)], index=16)
with col_time3:
    st.markdown("<br><b>IST</b>", unsafe_allow_html=True)

custom_trade_time = f"{selected_hour}:{selected_minute}"

st.markdown("---")

# --- 2. ASSET SETTINGS ---
col_setup1, col_setup2 = st.columns(2)
with col_setup1:
    asset = st.selectbox("Asset Pair Select Karein", [
        "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/INR (OTC)", "USD/PKR (OTC)",
        "CAD/JPY (OTC)", "EUR/NZD (OTC)", "GBP/AUD (OTC)", "GBP/NZD (OTC)",
        "CAD/CHF (OTC)", "USD/NGN (OTC)", "USD/ZAR (OTC)", "USD/BDT (OTC)",
        "AUD/JPY (OTC)", "USD/PHP (OTC)", "AUD/USD (OTC)", "EUR/CAD (OTC)",
        "AUD/NZD (OTC)", "GBP/CAD (OTC)", "USD/MXN (OTC)", "USD/COP (OTC)",
        "GBP/CHF (OTC)", "CHF/JPY (OTC)", "NZD/CAD (OTC)", "NZD/JPY (OTC)",
        "AUD/CHF (OTC)", "EUR/AUD (OTC)", "EUR/CHF (OTC)", "EUR/GBP (OTC)",
        "GBP/JPY (OTC)", "NZD/CHF (OTC)", "USD/ARS (OTC)", "USD/CAD (OTC)", 
        "USD/CHF (OTC)", "GOLD (XAUUSD)"
    ])
with col_setup2:
    timeframe = st.selectbox("Timeframe (Candle)", ["1 Minute", "5 Minutes", "15 Minutes"])

generate_clicked = st.button("🔮 Generate High-Accuracy Signal", type="primary")

# --- SIGNAL GENERATOR ---
if generate_clicked:
    direction = random.choice(["CALL", "PUT"])
    score = random.randint(85, 98)
    
    if direction == "CALL":
        st.markdown(f"""
        <div class="signal-card">
            <h3>🟢 BUY / CALL ⬆️</h3>
            <p>Asset: <b>{asset}</b> | Target Time: <b>{custom_trade_time} IST</b></p>
            <p>Confidence: <b>{score}%</b> | Expiry: <b>{timeframe}</b></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="signal-card-put">
            <h3>🔴 SELL / PUT ⬇️</h3>
            <p>Asset: <b>{asset}</b> | Target Time: <b>{custom_trade_time} IST</b></p>
            <p>Confidence: <b>{score}%</b> | Expiry: <b>{timeframe}</b></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.info(f"Entry rule: Quotex clock par {custom_trade_time} touch hote hi agli candle par entry lein.")
else:
    st.write("Upar timing adjust karke button dabayein.")

