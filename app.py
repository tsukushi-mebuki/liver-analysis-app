import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# ---- 日本語フォント設定部 ----
def setup_font():
    """日本語フォント設定を自動適用"""
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        base_dir = os.getcwd()  # __file__が使えない場合に備える

    if os.name == "nt":  # Windows
        plt.rcParams["font.family"] = "Meiryo"
        plt.rcParams["axes.unicode_minus"] = False
        return "Meiryo"

    # Linux (Streamlit Cloudなど)
    font_dir = os.path.join(base_dir, "fonts")
    font_path = os.path.join(font_dir, "ipaexg.ttf")

    if os.path.exists(font_path):
        font_prop = fm.FontProperties(fname=font_path)
        plt.rcParams['font.family'] = font_prop.get_name()
        font_name = font_prop.get_name()
    else:
        st.warning("⚠ フォントが見つかりません。fonts/ipaexg.ttf を配置してください。")
        plt.rcParams["font.family"] = "DejaVu Sans"
        font_name = "DejaVu Sans"

    plt.rcParams["axes.unicode_minus"] = False
    return font_name


font_used = setup_font()

# ---- ページ設定 ----
st.set_page_config(page_title="ライバー配信分析", layout="wide")
st.title("🎤 ライバー配信分析ダッシュボード")

st.caption(f"使用フォント: {font_used}")

# ---- データアップロード ----
uploaded_file = st.file_uploader("日次CSVデータをアップロード", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    sample_path = "data/sample_data.csv"
    if os.path.exists(sample_path):
        df = pd.read_csv(sample_path)
        st.info("📄 サンプルデータを使用しています。")
    else:
        st.error("❌ CSVファイルが見つかりません。アップロードしてください。")
        st.stop()

# ---- データプレビュー ----
st.subheader("📊 データプレビュー")
st.dataframe(df)

# ---- グラフ設定 ----
st.sidebar.header("分析設定")
x_axis = st.sidebar.selectbox("横軸を選択", df.columns, index=0)
y_axis = st.sidebar.selectbox("縦軸を選択", df.columns, index=1)

# ---- グラフ描画 ----
#fig, ax = plt.subplots()
fig, ax = plt.subplots(figsize=(10, 5))  # 幅10インチ、高さ6インチ
ax.scatter(df[x_axis], df[y_axis])
ax.set_xlabel(x_axis, fontproperties=fm.FontProperties(fname=os.path.join("fonts", "ipaexg.ttf")))
ax.set_ylabel(y_axis, fontproperties=fm.FontProperties(fname=os.path.join("fonts", "ipaexg.ttf")))
ax.set_title(f"{x_axis} と {y_axis} の関係", fontproperties=fm.FontProperties(fname=os.path.join("fonts", "ipaexg.ttf")))
#fig, ax = plt.subplots(figsize=(3, 2), constrained_layout=True)
st.pyplot(fig)

# ---- 集計 ----
st.subheader("📈 指標サマリー")
st.write(df.describe())

st.caption("Powered by Streamlit / Created by つくし")








