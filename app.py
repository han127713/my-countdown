import streamlit as st
from datetime import date

st.set_page_config(page_title="退伍倒數計時", page_icon="🪖")

# 設定退伍日期 (可以根據實際情況修改日期)
target_date = date(2026, 6, 16)
today = date.today()
days_left = (target_date - today).days

st.title("🪖 兵哥哥退伍倒數")
st.write("---")

if days_left > 0:
    st.metric(label="距離退伍還有", value=f"{days_left} 天")
    # 假設最後倒數 36 天的進度條
    progress = max(0.0, min(1.0, (36 - days_left) / 36))
    st.progress(progress)
    st.info("加油！再撐一下下就自由了 ❤️")
else:
    st.balloons()
    st.success("🎉 恭喜退伍！！")

st.write("---")
st.write("### 💌 給男友的小紙條")
st.info("這 36 天我會一直陪著你唷～")
