import streamlit as st
import pandas as pd
import numpy as np
import random
import time

# Page Configuration - Standard Light Mode
st.set_page_config(page_title="LegendJournal | Signals", layout="wide")

# Light Mode Styling
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    .signal-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #e2e8f0;
        border-left: 6px solid #10b981;
        margin-bottom: 25px;
    }
    .signal-card-put {
        background: #ffffff;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #e2e8f0;
        border-left: 6px solid #ef4444;
        margin-bottom: 25px;
    }
    .trigger-box {
        background-color: #eff6ff;
        border: 1px solid #bfdbfe;
        border-radius: 8px;
        padding: 20px;
        color: #1e3a8a;
    }
</style>
""", unsafe_allow_html=True)

# Main UI
st.title("LegendJournal Signal Generator")

# Controls
col1, col2 = st.columns(2)
with col1:
    asset = st.selectbox("Asset", ["USD/COP (OTC)", "EUR/USD (OTC)", "GOLD (XAUUSD)"])
with col2:
    target_time = st.text_input("Enter Target Time (e.g., 09:53)")

if st.button("🔮 Generate Signal"):
    direction = random.choice(["CALL", "PUT"])
    score = random.randint(85, 98)
    
    # Entry Logic Instruction
    card_class = "signal-card" if direction == "CALL" else "signal-card-put"
    arrow = "🟢 BUY / CALL ⬆️" if direction == "CALL" else "🔴 SELL / PUT ⬇️"
    
    st.markdown(f"""
    <div class="{card_class}">
        <h3>{arrow}</h3>
        <p>Asset: {asset} | Target: {target_time} IST</p>
        <p>Confidence: <b>{score}%</b> | Expiry: 1 Minute</p>
    </div>
    
    <div class="trigger-box">
        <b>⚡ ENTRY RULE (CRITICAL):</b><br>
        1. Quotex chart par wait karein jab tak clock <b>{target_time}:00</b> na ho jaye.<br>
        2. Jaise hi <b>{target_time}:00</b> touch ho (current candle khatam hote hi), <b>TURANT</b> agli candle ke liye trade lein.<br>
        3. Delay mat karein, exact second par click karein.
    </div>
    """, unsafe_allow_html=True)
    
