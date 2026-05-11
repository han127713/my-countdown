import streamlit as st
from datetime import date
import random

# 頁面設定
st.set_page_config(page_title="陳新退伍倒數計時", page_icon="💪")

# --- 1. 倒數與日期設定 ---
st.title("🪖 陳新退伍倒數計時")

with st.expander("⚙️ 設定退伍日期"):
    target_date = st.date_input("選擇退伍日：", date(2026, 6, 16))
    total_countdown = st.number_input("設定倒數總天數：", value=36)

today = date.today()
days_left = (target_date - today).days

if days_left > 0:
    st.metric(label="距離 陳新 自由還有", value=f"{days_left} 天")
    st.progress(max(0.0, min(1.0, (total_countdown - days_left) / total_countdown)))
else:
    st.balloons()
    st.header("🎉 恭喜陳新退伍！")

st.divider()

# --- 2. 體能驗收區 (妳要求的邏輯) ---
st.subheader("🏋️‍♂️ 陳新體能驗收")
st.write("沒超過 50 下就看著辦吧！")

num_pushups = st.number_input("今天伏地挺身做了幾下？", min_value=0, step=1)

if st.button("查看評價"):
    if num_pushups >= 50:
        st.balloons()
        st.success(f"🔥 做得好！{num_pushups} 下很棒，不愧是陳新！")
    elif num_pushups > 0:
        st.error(f"😒 才 {num_pushups} 下？太廢了吧，給我回去重做！")
    else:
        st.warning("還不快去動起來！")

st.divider()

# --- 3. 永久留言 (由妳手動在 GitHub 更新) ---
st.subheader("💌 給陳新的話")
# 妳只要在下面這行引號內改字，儲存後他那邊就會更新，永遠不會消失
st.info("這 36 天我會一直陪著你，在外面等你回來 ❤️")

# --- 4. 隨機加油小語 ---
if st.button("點我領取今日份的鼓勵"):
    cheers = ["你是最帥的！", "再撐一下就放假了", "加油，你是我的英雄", "回家人家幫你按摩"]
    st.write(f"💖 **{random.choice(cheers)}**")
