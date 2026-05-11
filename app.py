import streamlit as st
from datetime import date

# 頁面基本設定
st.set_page_config(page_title="陳新退伍倒數", page_icon="🪖")

st.title("🪖 陳新退伍倒數計時")

# --- 1. 妳每天想對他說的話 ---
# 提示：妳隨時可以回來 GitHub 修改這段文字，按 Commit 後，他重新整理網頁就會更新
st.chat_message("assistant").write("""
💖 **今日老婆的話：** 陳新加油！今天也要想我喔，剩下不到一個月了，等妳回來我們去吃大餐！
""")

st.divider()

# --- 2. 自動倒數邏輯 ---
# 這裡設定退伍日期，程式會自動拿「今天」來減，所以天數每天都會變少
target_date = date(2026, 6, 16) 
today = date.today()
days_left = (target_date - today).days

# 設定總天數（固定 36 天不變，用來算進度條跑了多少 %）
total_duration = 36

if days_left > 0:
    # 這行會自動顯示最新的天數
    st.metric(label="距離陳新自由還有", value=f"{days_left} 天")
    
    # 計算進度條比例
    progress = max(0.0, min(1.0, (total_duration - days_left) / total_duration))
    st.progress(progress)
    st.caption(f"已經撐過 {total_duration - days_left} 天，進度：{int(progress*100)}%")
    
elif days_left == 0:
    st.balloons()
    st.success("🎉 就是今天！陳新退伍快樂！趕快去門口接他！")
else:
    st.header("🎉 已經退伍囉！")
    st.write(f"陳新已經回歸社會 {-days_left} 天了，恭喜！")

st.divider()

# --- 3. 體能簽到區 ---
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
st.caption(f"📅 今天的日期是：{today} (系統會自動根據這天倒數)")



 



     





  
    




