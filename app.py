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
trump_rss = "https://news.google.com/rss/search?q=Trump&hl=ja&gl=JP&ceid=JP:ja"
display_feed(trump_rss, limit=7)

st.divider()

# ---------------------------------------------------------
# 2. その下に続く 海外21主要メディア一覧
# ---------------------------------------------------------
st.header("📰 海外主要メディア一覧（21媒体）")

# PCでは左右2カラム、スマホでは縦に綺麗に1列に並びます
col1, col2 = st.columns(2)

# --- 左側グループ（11メディア） ---
with col1:
    st.subheader("🇺🇸 アメリカ・国際主要紙（左グループ）")
    
    with st.expander("CNN News"):
        display_feed("http://rss.cnn.com/rss/edition.rss")
    with st.expander("BBC News"):
        display_feed("http://feeds.bbci.co.uk/news/rss.xml")
    with st.expander("Reuters"):
        display_feed("https://www.statweest.com/rss/reuters.xml")
    with st.expander("The New York Times"):
        display_feed("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    with st.expander("The Washington Post"):
        display_feed("https://feeds.washingtonpost.com/rss/national")
    with st.expander("The Wall Street Journal"):
        display_feed("https://feeds.a.dj.com/rss/RSSWorldNews.xml")
    with st.expander("Bloomberg"):
        display_feed("https://feeds.bloomberg.com/news.rss")
    with st.expander("Associated Press (AP)"):
        display_feed("https://news.google.com/rss/search?q=when:24h+allinurl:apnews.com&hl=en-US&gl=US&ceid=US:en")
    with st.expander("USA Today"):
        display_feed("http://rssfeeds.usatoday.com/usatoday-NewsTopStories")
    with st.expander("TIME"):
        display_feed("https://time.com/feed/")
    with st.expander("Politico"):
        display_feed("https://www.politico.com/rss/politicopicks.xml")

# --- 右側グループ（10メディア） ---
with col2:
    st.subheader("🌍 欧州・アジア・主要メディア（右グループ）")
    
    with st.expander("The Guardian (UK)"):
        display_feed("https://www.theguardian.com/world/rss")
    with st.expander("Financial Times"):
        display_feed("https://www.ft.com/?format=rss")
    with st.expander("The Economist"):
        display_feed("https://www.economist.com/sections/full-print-edition/rss.xml")
    with st.expander("Le Monde (France)"):
        display_feed("https://www.lemonde.fr/rss/une.xml")
    with st.expander("Deutsche Welle (Germany)"):
        display_feed("https://rss.dw.com/rdf/rss-en-all")
    with st.expander("Al Jazeera"):
        display_feed("https://www.aljazeera.com/xml/rss/all.xml")
    with st.expander("South China Morning Post"):
        display_feed("https://www.scmp.com/rss/91/feed")
    with st.expander("The Straits Times"):
        display_feed("https://www.straitstimes.com/news/world/rss.xml")
    with st.expander("Japan Times"):
        display_feed("https://www.japantimes.co.jp/feed/")
    with st.expander("ABC News"):
        display_feed("https://abcnews.go.com/abcnews/topstories")