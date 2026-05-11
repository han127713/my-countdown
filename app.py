import streamlit as st
from datetime import date

# 頁面基本設定
st.set_page_config(page_title="陳新退伍倒數", page_icon="🪖")

st.title("🪖 陳新退伍倒數計時")

# --- 1. 妳每天要對他說的話 ---
# 妳每天只要來 GitHub 改下面這段引號裡的文字，他重新整理網頁就會看到新留言
st.chat_message("assistant").write("""
💖 **今日老婆的話：** 陳新加油！今天也要想我喔，剩下不到一個月了，等妳回來我們去吃大餐！
""")

st.divider()

# --- 2. 倒數邏輯 ---
target_date = date(2026, 6, 16) # 設定退伍日期
total_days = 36                # 總倒數天數
today = date.today()
days_left = (target_date - today).days

if days_left > 0:
    st.metric(label="距離自由還有", value=f"{days_left} 天")
    # 進度條計算
    progress = max(0.0, min(1.0, (total_days - days_left) / total_days))
    st.progress(progress)
    st.caption(f"目前的進度：{int(progress*100)}%")
elif days_left == 0:
    st.balloons()
    st.success("🎉 就是今天！陳新退伍快樂！")
else:
    st.header("🎉 已經退伍囉！")
    st.write(f"陳新已經自由 {-days_left} 天了！")

st.divider()

# --- 3. 體能簡單回應區 ---
st.subheader("🏋️‍♂️ 每日體能簽到")
num = st.number_input("今天伏地挺身做了幾下？", min_value=0, step=1)

if st.button("送出驗收"):
    if num >= 50:
        st.balloons()
        st.success(f"🔥 {num} 下！太棒了，不愧是我的男人！")
    elif num > 0:
        # 這裡是妳要求的邏輯
        st.error(f"😒 才 {num} 下？你很廢耶，給我去重做！")
    else:
        st.warning("趕快去運動，不要偷懶！")

st.divider()
st.caption("💡 溫馨提醒：這是一個簡單的倒數網頁，資料不會存檔，純粹用來互動喔！")




     





  
    




