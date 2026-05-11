
import streamlit as st
from datetime import date

# 頁面基本設定
st.set_page_config(page_title="陳新退伍倒數", page_icon="🪖")

# --- 1. 倒數邏輯 ---
# 2026/5/11 距離 2026/6/16 剛好是 36 天
target_date = date(2026, 6, 16)
today = date.today()
days_left = (target_date - today).days

st.title("🪖 陳新退伍倒數計時")
st.write("---")

if days_left > 0:
    # 顯示大大的天數
    st.metric(label="距離陳新自由還有", value=f"{days_left} 天")
    
    # 進度條 (以 36 天為最後衝刺期)
    progress = max(0.0, min(1.0, (36 - days_left) / 36))
    st.progress(progress)
    
    st.info(f"📅 預計退伍日：{target_date}")
    st.success("陳新加油！這就是最後一哩路了，我在外面等你 ❤️")
else:
    st.balloons()
    st.header("🎉 賀！陳新光榮退伍！")
    st.subheader("終於等到這一天，自由萬歲！")

st.write("---")

# --- 2. 留言板功能 ---
st.subheader("💌 我們的秘密留言板")

# 使用 session_state 來暫存留言
if 'notes' not in st.session_state:
    st.session_state.notes = ["歡迎來到我們的秘密基地！"]

with st.form("message_form", clear_on_submit=True):
    # 下拉選單選擇身分
    name = st.selectbox("你是誰？", ["女友 ❤️", "陳新 🪖"])
    text = st.text_area("想對對方說的話...")
    submitted = st.form_submit_button("送出留言")
    
    if submitted and text:
        # 將留言加進清單中
        st.session_state.notes.append(f"{name}: {text}")

# 顯示留言，最新的在最上面
for n in reversed(st.session_state.notes):
    st.write(n)
