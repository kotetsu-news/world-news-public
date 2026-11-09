import streamlit as st
import feedparser

# ページ基本設定（スマホ・PC両対応）
st.set_page_config(
    page_title="World News",
    page_icon="🌐",
    layout="wide"
)

# タイトル
st.title("🌐 World News")
st.caption("世界の主要メディア・最新ニュース速報")

# RSS取得・表示関数
def display_feed(url, limit=5):
    try:
        feed = feedparser.parse(url)
        if feed.entries:
            for entry in feed.entries[:limit]:
                title = entry.get('title', 'タイトルなし')
                link = entry.get('link', '#')
                st.markdown(f"- [{title}]({link})")
        else:
            st.info("ニュースを取得できませんでした。")
    except Exception as e:
        st.error(f"読み込みエラー: {e}")

# ---------------------------------------------------------
# 1. スマホ表示の一番上：トランプ速報（メイン）
# ---------------------------------------------------------
st.header("🔥 トランプ速報・最新注目ニュース")

# RSS URLはご自身で設定されているものに差し替えてください
trump_rss = "https://news.google.com/rss/search?q=Trump&hl=ja&gl=JP&ceid=JP:ja"
display_feed(trump_rss, limit=7)

st.divider()

# ---------------------------------------------------------
# 2. その下に続く各ニュースメディア
# ---------------------------------------------------------
st.header("📰 主要ニュースメディア一覧")

# PCでは2カラム、スマホでは自動で縦に綺麗に並びます
col1, col2 = st.columns(2)

with col1:
    st.subheader("🇺🇸 アメリカ・国際主要紙")
    with st.expander("CNN News"):
        display_feed("http://rss.cnn.com/rss/edition.rss")
    with st.expander("BBC News"):
        display_feed("http://feeds.bbci.co.uk/news/rss.xml")
    with st.expander("Reuters"):
        display_feed("https://www.news-feed-url-example.com/rss") # お持ちのURL

with col2:
    st.subheader("🇯🇵 日本・その他メディア")
    with st.expander("NHKニュース"):
        display_feed("https://www.nhk.or.jp/rss/news/cat0.xml")
    with st.expander("Yahoo!ニュース"):
        display_feed("https://news.yahoo.co.jp/rss/topics/top-picks.xml")