import streamlit as st
from datetime import date, datetime
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# 頁面基本設定
st.set_page_config(page_title="陳新退伍倒數計時", page_icon="💪")

# 建立 Google Sheets 連線
# 妳的試算表網址：https://docs.google.com/spreadsheets/d/1ZCBWa3co1y3C5PU8_yvlHQcE5qtsCNGeiQ2Uho1Eouc/edit
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🪖 陳新退伍倒數計時")

# --- 1. 倒數邏輯 ---
with st.expander("⚙️ 設定退伍日期"):
    user_target_date = st.date_input("選擇退伍日：", date(2026, 6, 16))
    total_days = st.number_input("總倒數天數：", value=36)

days_left = (user_target_date - date.today()).days
if days_left > 0:
    st.metric(label="距離 陳新 自由還有", value=f"{days_left} 天")
    st.progress(max(0.0, min(1.0, (total_days - days_left) / total_days)))
else:
    st.balloons()

st.divider()

# --- 2. 體能驗收區 ---
st.subheader("🏋️‍♂️ 現場體能驗收")
num = st.number_input("今天伏地挺身做了幾下？", min_value=0, step=1)
if st.button("查看評價"):
    if num >= 50:
        st.balloons(); st.success(f"🔥 {num} 下！太強了，不愧是陳新！")
    elif num > 0:
        st.error(f"😒 才 {num} 下？太廢了，重做！")

st.divider()

# --- 3. 留言板功能 (直接顯示與寫入) ---
st.subheader("💌 秘密留言板")

# 讀取現有留言
try:
    # 這裡的 spreadsheet 網址要換成妳的
    df = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1ZCBWa3co1y3C5PU8_yvlHQcE5qtsCNGeiQ2Uho1Eouc/edit", ttl="0")
    df = df.dropna(how="all") # 去除空行
except Exception as e:
    df = pd.DataFrame(columns=['name', 'content', 'date'])

# 填寫留言介面
with st.form("msg_form", clear_on_submit=True):
    name = st.selectbox("你是誰？", ["女友 ❤️", "陳新 🪖"])
    content = st.text_area("想說的話 / 紀錄體能...")
    submit = st.form_submit_button("送出留言")
    
    if submit and content:
        # 建立新資料
        new_data = pd.DataFrame([{
            "name": name,
            "content": content,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }])
        # 合併並寫回試算表
        updated_df = pd.concat([df, new_data], ignore_index=True)
        conn.update(spreadsheet="https://docs.google.com/spreadsheets/d/1ZCBWa3co1y3C5PU8_yvlHQcE5qtsCNGeiQ2Uho1Eouc/edit", data=updated_df)
        st.success("留言成功！重新整理網頁即可看到新留言。")
        st.cache_data.clear() # 強制清除緩存

st.write("---")
st.write("💬 **最近的 5 則留言：**")

# 顯示最後 5 筆留言
if not df.empty:
    recent_msgs = df.tail(5).iloc[::-1] # 取最後 5 筆並反轉（最新的在上面）
    for index, row in recent_msgs.iterrows():
        st.info(f"**{row['name']}** ({row['date']}): \n\n {row['content']}")
else:
    st.write("目前還沒有留言，快來當第一個！")

  
    




