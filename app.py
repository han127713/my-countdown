import streamlit as st
from datetime import date

# 頁面基本設定
st.set_page_config(page_title="陳新退伍倒數計時", page_icon="💪")

# --- 1. 倒數與日期設定區 ---
st.title("🪖 陳新退伍倒數計時")

# 這裡可以點開來手動微調
with st.expander("⚙️ 設定退伍日期與進度條"):
    user_target_date = st.date_input("請選擇陳新的退伍日期：", date(2026, 6, 16))
    total_days_input = st.number_input("總倒數天數設定（用於計算進度）：", value=36)

today = date.today()
days_left = (user_target_date - today).days

st.write("---")

if days_left > 0:
    # 顯示天數大圖標
    st.metric(label="距離 陳新 自由還有", value=f"{days_left} 天")
    
    # 自動計算進度條
    progress_val = max(0.0, min(1.0, (total_days_input - days_left) / total_days_input))
    st.progress(progress_val)
    
    st.write(f"📅 目前設定退伍日：{user_target_date}")
    st.success("陳新加油！這就是最後一哩路了，我在外面等你 ❤️")
elif days_left == 0:
    st.balloons()
    st.header("🎉 就在今天！！")
    st.subheader("陳新終於退伍啦！快去接他！")
else:
    st.header("🎉 已經退伍囉！")
    st.write(f"陳新已經自由 {-days_left} 天了！")

st.divider()

# --- 2. 永久紀錄區 (連動 Google 表單) ---
st.subheader("📝 每日紀錄與永久留言")
st.write("為了讓我們的對話與體能紀錄永遠保存，請點擊下方按鈕填寫：")

# 這是妳提供的表單網址
form_url = "https://forms.gle/uWuUBACmMAVG4vT8A"

st.link_button("👉 點我紀錄今日伏地挺身與留言", form_url)

st.caption("💡 溫馨提醒：在這裡填寫的內容會永久保存在 Google 表單後台，不會因為網頁重整而消失唷！")

st.divider()

# --- 3. 現場評價區 (現場玩玩看) ---
st.subheader("🏋️‍♂️ 陳新體能現場驗收")
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

    




