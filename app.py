import streamlit as st
from datetime import date, datetime
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# 頁面基本設定
st.set_page_config(page_title="陳新退伍倒數計時", page_icon="💪")

# 建立 Google Sheets 連線 (會自動去讀 Secrets 裡的網址)
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🪖 陳新退伍倒數計時")

# --- 1. 倒數邏輯 ---
with st.expander("⚙️ 設定退伍日期"):
    target_date = st.date_input("選擇退伍日：", date(2026, 6, 16))
    total_days = st.number_input("總倒數天數：", value=36)

today = date.today()
days_left = (target_date - today).days

if days_left > 0:
    st.metric(label="距離 陳新 自由還有", value=f"{days_left} 天")
    st.progress(max(0.0, min(1.0, (total_days - days_left) / total_days)))
else:
    st.balloons()
    st.success("🎉 退伍快樂！！")

st.divider()

# --- 2. 留言與紀錄功能 ---
st.subheader("💌 秘密留言板與體能紀錄")

# 讀取現有留言 (ttl=0 表示不緩存，每次都讀新的)
try:
    df = conn.read(ttl="0")
    df = df.dropna(how="all")
except:
    df = pd.DataFrame(columns=['name', 'content', 'date'])

with st.form("msg_form", clear_on_submit=True):
    user = st.selectbox("你是誰？", ["女友 ❤️", "陳新 🪖"])
    num = st.number_input("今天伏地挺身幾下？", min_value=0, step=1)
    msg = st.text_area("想對對方說的話...")
    submit = st.form_submit_button("送出紀錄與留言")
    
    if submit and (msg or num > 0):
        # 體能評價邏輯
        evaluation = ""
        if num >= 50:
            evaluation = f"(做了{num}下，超棒！🔥)"
        elif num > 0:
            evaluation = f"(才做{num}下，太廢了😒)"
            
        new_row = pd.DataFrame([{
            "name": user,
            "content": f"{msg} {evaluation}",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }])
        
        updated_df = pd.concat([df, new_row], ignore_index=True)
        conn.update(data=updated_df)
        st.success("紀錄成功！重新整理網頁即可看到新內容。")
        st.cache_data.clear()

st.write("---")
st.write("💬 **最近的 5 則紀錄：**")

# 顯示最後 5 筆留言
if not df.empty:
    recent = df.tail(5).iloc[::-1] # 最新的在上面
    for i, row in recent.iterrows():
        st.info(f"**{row['name']}** ({row['date']})\n\n{row['content']}")
else:
    st.write("目前還沒有紀錄，快來留言吧！")



  
    




