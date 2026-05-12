import streamlit as st
from datetime import datetime, date
import pytz
import random

# 頁面基本設定
st.set_page_config(page_title="陳新退伍倒數", page_icon="🪖")

# --- 修正時區：確保是台灣時間 ---
tw_tz = pytz.timezone('Asia/Taipei')
now_tw = datetime.now(tw_tz)
today_tw = now_tw.date()

st.title("🪖 陳新退伍倒數計時")

# --- 1. 妳每天想對他說的話 ---
st.chat_message("assistant").write("""
💖 **今日老婆的話：** 今天的測驗要加油喔，繼續努力！ ❤️
""")

st.divider()

# --- 2. 🎮 新增：國軍生存運氣小遊戲 ---
st.subheader("🎲 今日國軍生存運氣")
st.write("點擊按鈕看看你今天的軍旅運氣如何：")

if st.button("🎲 抽取今日運勢"):
    fortunes = [
        {"status": "大吉", "msg": "今天長官心情好，全體提早放假！", "icon": "✨"},
        {"status": "小吉", "msg": "公差很輕鬆，還有冷氣吹。", "icon": "🍃"},
        {"status": "平", "msg": "無事忙，安全下莊就是勝利。", "icon": "😐"},
        {"status": "凶", "msg": "班長路過看了你一眼，皮繃緊一點。", "icon": "⚡"},
        {"status": "大凶", "msg": "這桌的菜...你自己保重吧。", "icon": "🤮"},
        {"status": "老婆保佑", "msg": "雖然在裡面很累，但老婆愛你，戰鬥力 +999！", "icon": "❤️"}
    ]
    pick = random.choice(fortunes)
    st.info(f"結果：{pick['icon']} **{pick['status']}** \n\n {pick['msg']}")

st.divider()

# --- 3. 自動倒數邏輯 ---
target_date = date(2026, 6, 16) 
days_left = (target_date - today_tw).days
total_duration = 36

if days_left > 0:
    st.metric(label="距離自由還有", value=f"{days_left} 天")
    progress = max(0.0, min(1.0, (total_duration - days_left) / total_duration))
    st.progress(progress)
    st.caption(f"目前戰鬥進度：{int(progress*100)}% (再撐一下！)")
elif days_left == 0:
    st.balloons()
    st.success("🎉 就是今天！陳新退伍快樂！")
else:
    st.write("🎉 已經自由囉！")

st.divider()

# --- 4. 體能簽到回應 ---
st.subheader("🏋️‍♂️ 體能生存驗收")
num = st.number_input("今天伏地挺身做了幾下？", min_value=0, step=1)

trash_talk = ["😒 才做幾下？你是進去度假的嗎？", "🤮 這種體能，退伍後拿不動我的包包吧？", "👎 你這是在地板上蠕動吧？"]
good_talk = ["🔥 帥喔！這肌肉我可以！", "🥰 猛男陳新回來了！", "💪 完美！期待看到你的八塊肌！"]

if st.button("點我領取老婆評價"):
    if num >= 100:
        st.balloons()
        st.success(random.choice(good_talk) + f" (紀錄：{num} 下)")
    elif num > 0:
        st.error(random.choice(trash_talk) + f" (笑死，才 {num} 下)")
    else:
        st.warning("趕快去運動，不要偷懶！")

st.divider()
st.caption(f"📅 台灣今日日期：{today_tw} | 妳是全世界最幽默的女友 ❤️")

    












 



     





  
    




