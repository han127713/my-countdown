import streamlit as st
from datetime import datetime, timedelta, date
import pytz

# 頁面基本設定
st.set_page_config(page_title="陳新退伍倒數", page_icon="🪖")

st.title("🪖 陳新退伍倒數計時")

# --- 修正時區：強制使用台灣時間 ---
tw_tz = pytz.timezone('Asia/Taipei')
now_tw = datetime.now(tw_tz)
today_tw = now_tw.date()

# --- 1. 妳每天想對他說的話 ---
st.chat_message("assistant").write("""
💖 **今日老婆的話：** 陳新加油！今天是倒數第 35 天了，雖然在裡面很辛苦，但撐過去就是你的了！我在外面乖乖等你回來喔～ ❤️
""")

st.divider()

# --- 2. 自動倒數邏輯 ---
# 設定退伍日期：2026年6月16日
target_date = date(2026, 6, 16) 

# 使用台灣日期來相減
days_left = (target_date - today_tw).days

# 設定總長度（36天）
total_duration = 36

if days_left > 0:
    # 這樣 5/12 點開，days_left 就會準確顯示 35 天
    st.metric(label="距離自由還有", value=f"{days_left} 天")
    
    # 計算進度條
    progress = max(0.0, min(1.0, (total_duration - days_left) / total_duration))
    st.progress(progress)
    st.caption(f"加油！已經撐過 {total_duration - days_left} 天了！")
    
elif days_left == 0:
    st.balloons()
    st.success("🎉 就是今天！陳新退伍快樂！")
else:
    st.header("🎉 已經退伍囉！")
    st.write(f"陳新已經回歸社會 {-days_left} 天了！")

st.divider()

# --- 3. 體能簡單回應區 ---
st.subheader("🏋️‍♂️ 每日體能簽到")
num = st.number_input("今天伏地挺身做了幾下？", min_value=0, step=1)

if st.button("送出驗收"):
    if num >= 50:
        st.balloons()
        st.success(f"🔥 {num} 下！太棒了，不愧是我的男人！")
    elif num > 0:
        st.error(f"😒 才 {num} 下？你很廢耶，給我去重做！")
    else:
        st.warning("趕快去運動，不要偷懶！")

st.divider()
# 這裡會顯示台灣的日期，讓妳確認
st.caption(f"📅 台灣今日日期：{today_tw} (已修正時區差)")









 



     





  
    




