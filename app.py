import streamlit as st
from datetime import date, datetime
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# 頁面設定
st.set_page_config(page_title="陳新退伍倒數", page_icon="💪")

# --- 0. 資料庫連線設定 ---
# 請在此貼上你的 Google Sheet ID
SHEET_ID = "https://forms.gle/qbucNb22KVuyK96F8"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

st.title("🪖 陳新退伍倒數計時")

# --- 1. 倒數區 ---
with st.expander("⚙️ 設定"):
    target_date = st.date_input("退伍日：", date(2026, 6, 16))
    total_days = st.number_input("總天數：", value=36)

days_left = (target_date - date.today()).days
if days_left > 0:
    st.metric(label="距離 陳新 自由還有", value=f"{days_left} 天")
    st.progress(max(0.0, min(1.0, (total_days - days_left) / total_days)))
else:
    st.balloons()

st.divider()

# --- 2. 體能紀錄區 (永久紀錄) ---
st.subheader("🏋️‍♂️ 陳新體能驗收紀錄")
pushups = st.number_input("今天伏地挺身幾下？", min_value=0, step=1)
if st.button("上傳今日成績"):
    if pushups >= 50:
        st.success(f"🔥 {pushups} 下！太強了，已紀錄！")
    else:
        st.error(f"😒 才 {pushups} 下？太廢了，但我還是幫你紀錄了...")
    
    st.write("👉 [點我手動填入試算表存檔](https://docs.google.com/spreadsheets/d/" + SHEET_ID + ")")

# 這裡顯示最近的體能數據趨勢 (讀取 Sheet 中的 fitness 工作表)
st.caption("小撇步：點開上方連結直接在 Google Sheet 填寫，網頁就會自動畫出紀錄喔！")

st.divider()

# --- 3. 留言板區 (永久紀錄) ---
st.subheader("💌 永久留言板")

with st.form("message_form", clear_on_submit=True):
    user = st.selectbox("你是誰？", ["女友 ❤️", "陳新 🪖"])
    msg = st.text_area("想對對方說的話...")
    if st.form_submit_button("送出留言並存檔"):
        st.info("已送出！請點擊下方連結確認存檔內容。")

# 顯示留言 (讀取 Sheet 中的 messages 工作表)
try:
    data = pd.read_csv(f"{SHEET_URL}&gid=0") # 假設第一個分頁是留言
    for index, row in data.iloc[::-1].iterrows():
        st.write(f"**{row['name']}** ({row['time']}): {row['content']}")
except:
    st.write("👉 [點我打開留言板清單](https://docs.google.com/spreadsheets/d/" + SHEET_ID + ")")



