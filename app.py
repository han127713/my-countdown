import streamlit as st
from datetime import date

# 頁面基本設定
st.set_page_config(page_title="陳新退伍倒數", page_icon="🪖")

# --- 1. 倒數與日期設定 ---
st.title("🪖 陳新退伍倒數計時")

with st.expander("⚙️ 設定退伍日期與進度條"):
    user_target_date = st.date_input("請選擇陳新的退伍日期：", date(2026, 6, 16))
    total_days_input = st.number_input("總倒數天數設定：", value=36)

today = date.today()
days_left = (user_target_date - today).days

st.write("---")

if days_left > 0:
    st.metric(label="距離 陳新 自由還有", value=f"{days_left} 天")
    
    # 進度條計算
    progress_val = max(0.0, min(1.0, (total_days_input - days_left) / total_days_input))
    st.progress(progress_val)
    
    st.write(f"📅 目前設定退伍日：{user_target_date}")
    st.success("陳新加油！我在外面等你 ❤️")
elif days_left == 0:
    st.balloons()
    st.header("🎉 就在今天！！")
    st.subheader("陳新終於退伍啦！快去接他！")
else:
    st.header("🎉 已經退伍囉！")
    st.write(f"陳新已經自由 {-days_left} 天了！")

st.divider()

# --- 2. 體能驗收區 ---
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

# --- 3. 簡易留言板 ---
st.subheader("💌 我們的專屬留言板")
st.caption("(註：此留言板為暫時性，網頁重新整理後會清空)")

# 初始化 session_state 來存放留言
if 'notes' not in st.session_state:
    st.session_state.notes = []

with st.form("message_form", clear_on_submit=True):
    name = st.selectbox("你是誰？", ["女友 ❤️", "陳新 🪖"])
    text = st.text_area("想對對方說的話...")
    submitted = st.form_submit_button("送出留言")
    
    if submitted and text:
        st.session_state.notes.append(f"{name}: {text}")

# 顯示留言
if st.session_state.notes:
    for n in reversed(st.session_state.notes):
        st.info(n)
else:
    st.write("目前還沒有留言唷～")
