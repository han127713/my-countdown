import streamlit as st
from datetime import date
import pandas as pd

# 頁面基本設定
st.set_page_config(page_title="陳新退伍倒數計時", page_icon="💪")

st.title("🪖 陳新退伍倒數計時")

# --- 1. 倒數與日期設定 ---
with st.expander("⚙️ 設定退伍日期"):
    user_target_date = st.date_input("選擇退伍日：", date(2026, 6, 16))
    total_days = st.number_input("總倒數天數：", value=36)

days_left = (user_target_date - date.today()).days

if days_left > 0:
    st.metric(label="距離 陳新 自由還有", value=f"{days_left} 天")
    st.progress(max(0.0, min(1.0, (total_days - days_left) / total_days)))
    st.success("陳新加油！我在外面等你 ❤️")
else:
    st.balloons()
    st.header("🎉 退伍快樂！！")

st.divider()

# --- 2. 體能現場評價 ---
st.subheader("🏋️‍♂️ 現場體能驗收")
num = st.number_input("今天伏地挺身做了幾下？", min_value=0)
if st.button("查看評價"):
    if num >= 50:
        st.balloons()
        st.success(f"🔥 {num} 下！太強了，不愧是陳新！")
    elif num > 0:
        st.error(f"😒 才 {num} 下？太廢了，重做！")

st.divider()

# --- 3. 留言板功能 ---
st.subheader("💌 秘密留言板")

# 妳的表單網址
form_url = "https://forms.gle/uWuUBACmMAVG4vT8A"
st.link_button("👉 點我寫留言 / 紀錄體能", form_url)

st.write("---")
st.write("💬 **最近的紀錄與留言：**")

# 【教妳一招】直接顯示 Google 試算表的內容
# 只要妳去表單的「回覆」分頁，點「連結至試算表」，並把該試算表「發布到網路」
# 妳就能在下面這行貼上試算表的 CSV 連結，這裡就會顯示出大家的留言喔！
st.info("陳新填完表單後，妳可以去 Google 表單後台看回覆紀錄唷！")

# 這裡先幫妳放一個簡單的模擬顯示，讓畫面漂亮一點
st.caption("這 36 天的所有紀錄都會存在妳的 Google 表單裡，不怕弄丟！")

  
    




