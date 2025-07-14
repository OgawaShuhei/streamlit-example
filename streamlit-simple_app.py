"""
[実行方法] anaconda promptで対象の環境を起動して以下を実行

streamlit run simple_app.py
"""

import streamlit as st
from datetime import datetime, date

# タイトル表示
st.title("簡単なStreamlitアプリ")

# ユーザーからテキスト入力を受ける
name = st.text_input("あなたの名前を教えてください")

# ユーザーからカレンダー入力を受ける（様々な年齢に対応）
# 120年前から今日まで選択可能、初期値は30年前に設定
today = date.today()
min_date = date(today.year - 120, 1, 1)  # 120年前
max_date = today  # 今日
default_date = date(today.year - 30, today.month, today.day)  # 30年前（30歳想定）

birthday = st.date_input(
    "あなたの誕生日を教えてください",
    value=default_date,
    min_value=min_date,
    max_value=max_date,
    help="生まれた年月日を選択してください（1904年〜現在まで対応）"
)

# 誕生日から年齢を自動計算
calculated_age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

# ユーザーからスライダー入力を受ける (最小値, 最大値, デフォルト値)
# 計算された年齢をデフォルト値として使用
age = st.number_input("あなたの年齢を教えてください", 0, 100, calculated_age)

# 計算された年齢を表示
st.info(f"誕生日から計算された年齢: {calculated_age}歳")

# ユーザーからチェックボックス入力を受ける
is_student = st.checkbox("学生ですか？")

# ユーザーからセレクトボックス入力を受ける
favorite_color = st.selectbox("あなたの好きな色は？", ["赤", "青", "緑", "黄色", "紫"])


# 結果表示
if name:    # もしname変数が空(null)ではなかったら
    st.write(f"こんにちは、{name}さん！あなたは{age}歳なのですね。")
    st.write(f"{age-5}歳に見えます！")
    if is_student:
        st.write("あなたは学生ですね！")
        st.write(f"あなたの好きな色は{favorite_color}ですね！")
else:
    st.write("あなたのことを教えてください。")