import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ページ設定
st.set_page_config(page_title="ライバー配信分析", layout="wide")

st.title("🎤 ライバー配信分析ダッシュボード")

# --- データ読み込み ---
uploaded_file = st.file_uploader("日次CSVデータをアップロード", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/sample_data.csv")
    st.info("サンプルデータを使用しています。")

# --- データ表示 ---
st.subheader("📊 データプレビュー")
st.dataframe(df)

# --- 指標選択 ---
st.sidebar.header("分析設定")
x_axis = st.sidebar.selectbox("横軸を選択", df.columns, index=0)
y_axis = st.sidebar.selectbox("縦軸を選択", df.columns, index=1)

# --- グラフ描画 ---
fig, ax = plt.subplots()
ax.scatter(df[x_axis], df[y_axis])
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.set_title(f"{x_axis} と {y_axis} の関係")
st.pyplot(fig)

# --- 集計 ---
st.subheader("📈 指標サマリー")
st.write(df.describe())

st.caption("Powered by Streamlit / Created by ちゃり")
