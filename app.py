import streamlit as st
import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rcParams

# ✅ 日本語フォント設定（Windows・Mac・Linux対応）
# 利用可能なフォントの中から自動で日本語フォントを選ぶ
font_candidates = [
    "MS Gothic",        # Windows
    "Yu Gothic",        # Windows10+
    "Noto Sans CJK JP", # Google / Linux
    "IPAPGothic",       # IPAフォント
    "TakaoGothic"       # Ubuntu日本語環境
]
available_fonts = [f for f in font_candidates if f in [font.name for font in font_manager.fontManager.ttflist]]

if available_fonts:
    rcParams['font.family'] = available_fonts[0]
else:
    st.warning("日本語フォントが見つかりません。文字化けする可能性があります。")

# ---- ページ設定 ----
st.set_page_config(page_title="ライバー配信分析", layout="wide")
st.title("🎤 ライバー配信分析ダッシュボード")

# ---- データアップロード ----
uploaded_file = st.file_uploader("日次CSVデータをアップロード", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/sample_data.csv")
    st.info("サンプルデータを使用しています。")

# ---- データプレビュー ----
st.subheader("📊 データプレビュー")
st.dataframe(df)

# ---- グラフ設定 ----
st.sidebar.header("分析設定")
x_axis = st.sidebar.selectbox("横軸を選択", df.columns, index=0)
y_axis = st.sidebar.selectbox("縦軸を選択", df.columns, index=1)

# ---- グラフ描画 ----
fig, ax = plt.subplots()
ax.scatter(df[x_axis], df[y_axis])
ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.set_title(f"{x_axis} と {y_axis} の関係")
st.pyplot(fig)

# ---- 集計 ----
st.subheader("📈 指標サマリー")
st.write(df.describe())

st.caption("Powered by Streamlit / Created by ちゃり")
