import streamlit as st
from datetime import date, datetime
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# 頁面設定
st.set_page_config(page_title="陳新退伍倒數計時", page_icon="💪")

# 建立連線
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🪖 陳新退伍倒數計時")

# 1. 倒數邏輯
with st.expander("⚙️ 設定退伍日期"):
    target_date = st.date_input("選擇退伍日：", date(2026, 6, 16))
    total_days = st.number_input("總倒數天數：", value=36)

days_left = (target_date - date.today()).days
if days_left > 0:
    st.metric(label="距離 陳新 自由還有", value=f"{days_left} 天")
    st.progress(max(0.0, min(1.0, (total_days - days_left) / total_days)))
else:
    st.balloons()

st.divider()

# 2. 留言與紀錄
st.subheader("💌 秘密留言板與體能紀錄")

# 讀取資料
try:
    # 這裡明確指定工作表名稱，如果妳的是「工作表1」請改名
    df = conn.read(worksheet="Sheet1", ttl="0") 
    df = df.dropna(how="all")
except:
    df = pd.DataFrame(columns=['name', 'content', 'date'])

with st.form("msg_form", clear_on_submit=True):
    user = st.selectbox("你是誰？", ["女友 ❤️", "陳新 🪖"])
    num = st.number_input("今天伏地挺身幾下？", min_value=0, step=1)
    msg = st.text_area("想對對方說的話...")
    submit = st.form_submit_button("送出紀錄與留言")
    
    if submit:
        # 整理評價
        eval_text = ""
        if num >= 50: eval_text = f" (做了{num}下，超強🔥)"
        elif num > 0: eval_text = f" (才{num}下，太廢了😒)"
        
        new_row = pd.DataFrame([{
            "name": user,
            "content": f"{msg}{eval_text}",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }])
        
        # 重新合併並寫入
        updated_df = pd.concat([df, new_row], ignore_index=True)
        # 這裡也明確指定 worksheet
        conn.update(worksheet="Sheet1", data=updated_df)
        st.success("紀錄成功！請重新整理網頁。")
        st.cache_data.clear()

st.write("---")
st.write("💬 **最近的 5 則紀錄：**")

if not df.empty:
    recent = df.tail(5).iloc[::-1]
    for i, row in recent.iterrows():
        st.info(f"**{row['name']}** ({row['date']})\n\n{row['content']}")





  
    




