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
💖 **今日老婆的話：** ❤️ 既然你最近這麼愛健身，我就在下面開了一個巨巨專區，給我認真練，退伍我要驗收身材喔！
""")

st.divider()

# --- 2. 🎮 國軍生存運氣小遊戲 ---
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

# --- 4. 🏋️‍♂️ 區塊一：健身時間驗收 ---
st.subheader("🏋️‍♂️ 運動一：健身時間簽到")
workout_time = st.number_input("오늘 健身練了幾分鐘？", min_value=0, step=5, key="gym_time")

trash_gym = [
    "😒 練不到一小時也敢叫健身巨巨？給我去重練！",
    "👎 你這不是在健身，你是在健身房吹冷氣滑手機吧？",
    "💀 練這幾分鐘？摸魚進度 100% 喔，班長在看你。"
]

good_gym = [
    "🔥 太猛了吧！練了 {time} 分鐘，胸肌快爆出來了嗎？",
    "🚀 這麼拼！看來退伍後可以直接單手把我抱起來轉圈圈了！",
    "💪 完美！再接再厲，期待退伍看到你的魔鬼身材！"
]

if st.button("🏋️‍♂️ 送出健身時數驗收"):
    if workout_time >= 60:
        st.balloons()
        st.success(random.choice(good_gym).format(time=workout_time))
    elif workout_time > 0:
        st.error(random.choice(trash_gym))
    else:
        st.warning("你今天是不是根本沒去練時數？不要偷懶！")

st.divider()

# --- 5. 💪 區塊二：伏地挺身驗收 ---
st.subheader("💪 運動二：伏地挺身簽到")
pushups = st.number_input("오늘 伏地挺身做了幾下？", min_value=0, step=1, key="pushup_count")

trash_push = [
    "🤮 才做幾下？退伍後我看你連大賣場的米袋都扛不動。",
    "👎 你這不是伏地挺身，是在地板上蠕動吧？",
    "😒 只有這樣？等你有 50 下再跟我炫耀！"
]

good_push = [
    "🥰 哇塞，做了 {push} 下伏地挺身！不愧是我的大肌肌男友！",
    "🔥 這個下數可以喔！今晚給你加雞腿！",
    "👑 挺身巨巨是你！快讓我摸一下你的二頭肌！"
]

if st.button("💪 送出伏地挺身驗收"):
    if pushups >= 50:
        st.balloons()
        st.success(random.choice(good_push).format(push=pushups))
    elif pushups > 0:
        st.error(random.choice(trash_push))
    else:
        st.warning("按按鈕前先去做伏地挺身！立刻！")

st.divider()
st.caption(f"📅 台灣今日日期：{today_tw} | 我是全世界最漂亮的女友 ❤️")







 


    












 



     





  
    




