import streamlit as st
import feedparser
from deep_translator import MyMemoryTranslator, GoogleTranslator
import time

st.set_page_config(
    page_title="World News",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 World News")
st.caption("世界の主要メディア・最新ニュース速報（本場現地版・日本語見出し表示）")

# 翻訳関数（MyMemory優先＋キャッシュ）
@st.cache_data(ttl=3600)
def translate_to_japanese(text: str) -> str:
    try:
        if not text or text == "タイトルなし":
            return text
        # まずMyMemoryを試す（制限が比較的緩い）
        return MyMemoryTranslator(source='auto', target='ja').translate(text)
    except:
        try:
            time.sleep(0.4)  # 少し待ってからGoogleを試す
            return GoogleTranslator(source='auto', target='ja').translate(text)
        except:
            return text  # 失敗したら原文を返す

def display_feed(url, limit=5, always_translate=False):
    try:
        feed = feedparser.parse(url)
        if not feed.entries:
            st.info("ニュースを取得できませんでした。")
            return

        # 常に翻訳するかどうかの判定
        if always_translate:
            do_translate = True
        else:
            do_translate = st.checkbox("この見出しを日本語に翻訳する", key=f"trans_{url}")

        for entry in feed.entries[:limit]:
            original_title = entry.get('title', 'タイトルなし')
            link = entry.get('link', '#')

            if do_translate:
                title = translate_to_japanese(original_title)
            else:
                title = original_title

            st.markdown(f"・**{title}**")
            st.markdown(f" ↳ [👉 原文を読む]({link})")
            st.write("")
    except Exception as e:
        st.error(f"読み込みエラー: {e}")

# ---------------------------------------------------------
# 1. トランプ速報（常に日本語）
# ---------------------------------------------------------
st.header("🔥 トランプ速報・最新注目ニュース")
trump_rss = "https://news.google.com/rss/search?q=Trump+when:24h&hl=ja&gl=US&ceid=US:en"
display_feed(trump_rss, limit=7, always_translate=True)  # ← ここだけTrue

st.divider()

# ---------------------------------------------------------
# 2. 海外主要メディア一覧（デフォルト英語・必要時だけ翻訳）
# ---------------------------------------------------------
st.header("📰 海外主要メディア一覧（本場現地版・21媒体）")

col1, col2 = st.columns(2)

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