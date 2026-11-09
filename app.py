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
st.caption("世界の主要メディア・最新ニュース速報（日本語見出し・快適閲覧版）")

# RSS取得・表示関数（Google News方式で綺麗に日本語表示＆リンク分離）
def display_feed(url, limit=5):
    try:
        feed = feedparser.parse(url)
        if feed.entries:
            for entry in feed.entries[:limit]:
                title = entry.get('title', 'タイトルなし')
                link = entry.get('link', '#')
                
                # 日本語の見出しを表示し、下に元記事リンクを配置
                st.markdown(f"・**{title}**")
                st.markdown(f" ↳ [👉 記事の詳細・原文を読む]({link})")
                st.write("") # 余白
        else:
            st.info("ニュースを取得できませんでした。")
    except Exception as e:
        st.error(f"読み込みエラー: {e}")

# ---------------------------------------------------------
# 1. スマホ表示の一番上：トランプ速報（メイン）
# ---------------------------------------------------------
st.header("🔥 トランプ速報・最新注目ニュース")
trump_rss = "https://news.google.com/rss/search?q=Trump+when:24h&hl=ja&gl=US&ceid=US:en"
display_feed(trump_rss, limit=7)

st.divider()

# ---------------------------------------------------------
# 2. その下に続く 海外21主要メディア一覧
# ---------------------------------------------------------
st.header("📰 海外主要メディア一覧（21媒体・日本語見出し）")

# PCでは左右2カラム、スマホでは縦に綺麗に1列に並びます
col1, col2 = st.columns(2)

# --- 左側グループ（11メディア） ---
with col1:
    st.subheader("🇺🇸 欧米・国際主要紙（11媒体）")
    
    with st.expander("CNN News"):
        display_feed("https://news.google.com/rss/search?q=site:cnn.com+when:24h&hl=ja&gl=US&ceid=US:en")
    with st.expander("The New York Times"):
        display_feed("https://news.google.com/rss/search?q=site:nytimes.com+when:24h&hl=ja&gl=US&ceid=US:en")
    with st.expander("The Washington Post"):
        display_feed("https://news.google.com/rss/search?q=site:washingtonpost.com+when:24h&hl=ja&gl=US&ceid=US:en")
    with st.expander("RT (Russia Today)"):
        display_feed("https://news.google.com/rss/search?q=site:rt.com+when:24h&hl=ja&gl=US&ceid=US:en")
    with st.expander("Sputnik News"):
        display_feed("https://news.google.com/rss/search?q=site:sputnikglobe.com+when:24h&hl=ja&gl=US&ceid=US:en")
    with st.expander("BBC News"):
        display_feed("https://news.google.com/rss/search?q=site:bbc.com+when:24h&hl=ja&gl=US&ceid=US:en")
    with st.expander("The Guardian (UK)"):
        display_feed("https://news.google.com/rss/search?q=site:theguardian.com+when:24h&hl=ja&gl=US&ceid=US:en")
    with st.expander("Reuters"):
        display_feed("https://news.google.com/rss/search?q=site:reuters.com+when:24h&hl=ja&gl=US&ceid=US:en")
    with st.expander("The Independent"):
        display_feed("https://news.google.com/rss/search?q=site:independent.co.uk+when:24h&hl=ja&gl=US&ceid=US:en")
    with st.expander("Le Monde (France)"):
        display_feed("https://news.google.com/rss/search?q=site:lemonde.fr+when:24h&hl=ja&gl=FR&ceid=FR:fr")
    with st.expander("Al Jazeera"):
        display_feed("https://news.google.com/rss/search?q=site:aljazeera.com+when:24h&hl=ja&gl=QA&ceid=QA:en")

# --- 右側グループ（10メディア） ---
with col2:
    st.subheader("🌍 欧州・アジア・太平洋・防災（10媒体）")
    
    with st.expander("Deutsche Welle (Germany)"):
        display_feed("https://news.google.com/rss/search?q=site:dw.com+when:24h&hl=ja&gl=DE&ceid=DE:de")
    with st.expander("China Daily"):
        display_feed("https://news.google.com/rss/search?q=site:chinadaily.com.cn+when:24h&hl=ja&gl=CN&ceid=CN:zh")
    with st.expander("South China Morning Post (SCMP)"):
        display_feed("https://news.google.com/rss/search?q=site:scmp.com+when:24h&hl=ja&gl=HK&ceid=HK:en")
    with st.expander("The Globe and Mail (Canada)"):
        display_feed("https://news.google.com/rss/search?q=site:theglobeandmail.com+when:24h&hl=ja&gl=CA&ceid=CA:en")
    with st.expander("The Sydney Morning Herald"):
        display_feed("https://news.google.com/rss/search?q=site:smh.com.au+when:24h&hl=ja&gl=AU&ceid=AU:en")
    with st.expander("The Times of India"):
        display_feed("https://news.google.com/rss/search?q=site:timesofindia.indiatimes.com+when:24h&hl=ja&gl=IN&ceid=IN:en")
    with st.expander("El País (Spain)"):
        display_feed("https://news.google.com/rss/search?q=site:elpais.com+when:24h&hl=ja&gl=ES&ceid=ES:es")
    with st.expander("The Straits Times"):
        display_feed("https://news.google.com/rss/search?q=site:straitstimes.com+when:24h&hl=ja&gl=SG&ceid=SG:en")
    with st.expander("The Japan Times"):
        display_feed("https://news.google.com/rss/search?q=site:japantimes.co.jp+when:24h&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("USGS Earthquake Hazards"):
        display_feed("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom")