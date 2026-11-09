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
st.caption("世界の主要メディア・最新ニュース速報（日本語表示版）")

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
# 2. その下に続く 海外21主要メディア一覧（日本語表示）
# ---------------------------------------------------------
st.header("📰 海外主要メディア一覧（21媒体・日本語表示）")

# PCでは左右2カラム、スマホでは縦に綺麗に1列に並びます
col1, col2 = st.columns(2)

# --- 左側グループ（11メディア） ---
with col1:
    st.subheader("🇺🇸 欧米・国際主要紙（11媒体）")
    
    with st.expander("CNN News"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:cnn.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The New York Times"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:nytimes.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Washington Post"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:washingtonpost.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("RT (Russia Today)"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:rt.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Sputnik News"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:sputnikglobe.com+OR+site:sputniknews.jp&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("BBC News"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:bbc.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Guardian (UK)"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:theguardian.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Reuters"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:reuters.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Independent"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:independent.co.uk&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Le Monde (France)"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:lemonde.fr&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Al Jazeera"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:aljazeera.com&hl=ja&gl=JP&ceid=JP:ja")

# --- 右側グループ（10メディア） ---
with col2:
    st.subheader("🌍 欧州・アジア・太平洋・防災（10媒体）")
    
    with st.expander("Deutsche Welle (Germany)"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:dw.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("China Daily"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:chinadaily.com.cn&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("South China Morning Post (SCMP)"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:scmp.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Globe and Mail (Canada)"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:theglobeandmail.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Sydney Morning Herald"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:smh.com.au&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Times of India"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:timesofindia.indiatimes.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("El País (Spain)"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:elpais.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Straits Times"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:straitstimes.com&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Japan Times"):
        display_feed("https://news.google.com/rss/search?q=when:24h+site:japantimes.co.jp&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("USGS Earthquake Hazards"):
        # 地震情報は英語原本が最も正確なためそのまま表示
        display_feed("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom")