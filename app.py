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
st.caption("世界の主要メディア・最新ニュース速報（本場現地版）")

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
# 1. スマホ表示の一番上：トランプ速報（本場・英語圏の最新動向）
# ---------------------------------------------------------
st.header("🔥 トランプ速報・最新注目ニュース")
trump_rss = "https://news.google.com/rss/search?q=Trump&hl=en-US&gl=US&ceid=US:en"
display_feed(trump_rss, limit=7)

st.divider()

# ---------------------------------------------------------
# 2. その下に続く 海外21主要メディア一覧（本場の直接RSS）
# ---------------------------------------------------------
st.header("📰 海外主要メディア一覧（本場現地版・21媒体）")
st.caption("※スマホやブラウザの「翻訳機能」を使うと、本場のニュースをそのまま日本語で快適に読めます。")

# PCでは左右2カラム、スマホでは縦に綺麗に1列に並びます
col1, col2 = st.columns(2)

# --- 左側グループ（11メディア） ---
with col1:
    st.subheader("🇺🇸 欧米・国際主要紙（11媒体）")
    
    with st.expander("CNN News"):
        display_feed("http://rss.cnn.com/rss/edition.rss")
    with st.expander("The New York Times"):
        display_feed("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
    with st.expander("The Washington Post"):
        display_feed("https://feeds.washingtonpost.com/rss/national")
    with st.expander("RT (Russia Today)"):
        display_feed("https://www.rt.com/rss/news/")
    with st.expander("Sputnik News"):
        display_feed("https://sputnikglobe.com/export/rss2/archive/index.xml")
    with st.expander("BBC News"):
        display_feed("http://feeds.bbci.co.uk/news/rss.xml")
    with st.expander("The Guardian (UK)"):
        display_feed("https://www.theguardian.com/world/rss")
    with st.expander("Reuters"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:reuters.com&hl=en-US&gl=US&ceid=US:en")
    with st.expander("The Independent"):
        display_feed("https://www.independent.co.uk/news/world/rss")
    with st.expander("Le Monde (France)"):
        display_feed("https://www.lemonde.fr/rss/une.xml")
    with st.expander("Al Jazeera"):
        display_feed("https://www.aljazeera.com/xml/rss/all.xml")

# --- 右側グループ（10メディア） ---
with col2:
    st.subheader("🌍 欧州・アジア・太平洋・防災（10媒体）")
    
    with st.expander("Deutsche Welle (Germany)"):
        display_feed("https://rss.dw.com/rdf/rss-en-all")
    with st.expander("China Daily"):
        display_feed("http://www.chinadaily.com.cn/rss/world_rss.xml")
    with st.expander("South China Morning Post (SCMP)"):
        display_feed("https://www.scmp.com/rss/91/feed")
    with st.expander("The Globe and Mail (Canada)"):
        display_feed("https://www.theglobeandmail.com/arc/outboundfeeds/rss/category/world/")
    with st.expander("The Sydney Morning Herald"):
        display_feed("https://www.smh.com.au/rss/world.xml")
    with st.expander("The Times of India"):
        display_feed("https://timesofindia.indiatimes.com/rssfeeds/296589292.cms")
    with st.expander("El País (Spain)"):
        display_feed("https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada")
    with st.expander("The Straits Times"):
        display_feed("https://www.straitstimes.com/news/world/rss.xml")
    with st.expander("The Japan Times"):
        display_feed("https://www.japantimes.co.jp/feed/")
    with st.expander("USGS Earthquake Hazards"):
        display_feed("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom")