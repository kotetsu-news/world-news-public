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
# 2. その下に続く 海外21主要メディア一覧（日本語表示修正版）
# ---------------------------------------------------------
st.header("📰 海外主要メディア一覧（21媒体・日本語表示）")

# PCでは左右2カラム、スマホでは縦に綺麗に1列に並びます
col1, col2 = st.columns(2)

# --- 左側グループ（11メディア） ---
with col1:
    st.subheader("🇺🇸 欧米・国際主要紙（11媒体）")
    
    with st.expander("CNN News"):
        display_feed("https://news.google.com/rss/search?q=CNN&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The New York Times"):
        display_feed("https://news.google.com/rss/search?q=%22New+York+Times%22+OR+%22%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%A9%E3%83%BC%E3%82%AF%E3%83%88%E3%83%BC%E3%83%A0%E3%82%BA%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Washington Post"):
        display_feed("https://news.google.com/rss/search?q=%22Washington+Post%22+OR+%22%E3%83%AF%E3%82%B7%E3%83%B3%E3%83%88%E3%83%B3%E3%83%9D%E3%82%B9%E3%83%88%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("RT (Russia Today)"):
        display_feed("https://news.google.com/rss/search?q=RT+OR+%22%E3%83%AD%E3%82%B7%E3%82%A2%E3%83%88%E3%82%A5%E3%83%87%E3%82%A4%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Sputnik News"):
        display_feed("https://news.web.sputniknews.jp/rss/sputnik.xml")
    with st.expander("BBC News"):
        display_feed("https://news.google.com/rss/search?q=BBC&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Guardian (UK)"):
        display_feed("https://news.google.com/rss/search?q=Guardian+OR+%22%E3%82%AC%E3%83%BC%E3%83%87%E3%82%A3%E3%82%A2%E3%83%B3%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Reuters"):
        display_feed("https://news.google.com/rss/search?q=%E3%83%AD%E3%82%A4%E3%82%BF%E3%83%BC&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Independent"):
        display_feed("https://news.google.com/rss/search?q=Independent+OR+%22%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%9A%E3%83%B3%E3%83%87%E3%83%B3%E3%83%88%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Le Monde (France)"):
        display_feed("https://news.google.com/rss/search?q=%22Le+Monde%22+OR+%22%E3%83%AB%E3%83%BB%E3%83%A2%E3%83%B3%E3%83%89%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Al Jazeera"):
        display_feed("https://news.google.com/rss/search?q=%22Al+Jazeera%22+OR+%22%E3%82%A2%E3%83%AB%E3%82%B8%E3%83%A3%E3%82%B6%E3%83%BC%E3%83%A9%22&hl=ja&gl=JP&ceid=JP:ja")

# --- 右側グループ（10メディア） ---
with col2:
    st.subheader("🌍 欧州・アジア・太平洋・防災（10媒体）")
    
    with st.expander("Deutsche Welle (Germany)"):
        display_feed("https://news.google.com/rss/search?q=%22Deutsche+Welle%22+OR+%22%E3%83%89%E3%82%A4%E3%83%84%E5%85%AC%E5%85%B1%EBroadcast%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("China Daily"):
        display_feed("https://news.google.com/rss/search?q=%22China+Daily%22+OR+%22%E3%83%81%E3%83%A3%E3%82%A4%E3%83%8A%E3%83%87%E3%82%A4%E3%83%AA%E3%83%BC%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("South China Morning Post (SCMP)"):
        display_feed("https://news.google.com/rss/search?q=SCMP+OR+%22%E5%8D%97%E8%8F%AF%E6%97%A9%E5%A0%B1%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Globe and Mail (Canada)"):
        display_feed("https://news.google.com/rss/search?q=%22Globe+and+Mail%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Sydney Morning Herald"):
        display_feed("https://news.google.com/rss/search?q=%22Sydney+Morning+Herald%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Times of India"):
        display_feed("https://news.google.com/rss/search?q=%22Times+of+India%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("El País (Spain)"):
        display_feed("https://news.google.com/rss/search?q=%22El+Pais%22+OR+%22%E3%82%A8%E3%83%AB%E3%83%BB%E3%83%91%E3%82%A4%E3%82%B9%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Straits Times"):
        display_feed("https://news.google.com/rss/search?q=%22Straits+Times%22+OR+%22%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%83%84%E3%83%BB%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%BA%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Japan Times"):
        display_feed("https://news.google.com/rss/search?q=%22Japan+Times%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("USGS Earthquake Hazards"):
        display_feed("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.atom")