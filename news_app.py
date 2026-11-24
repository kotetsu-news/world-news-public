import os
import urllib.request
import feedparser
import streamlit as st
from bs4 import BeautifulSoup
from google import genai

# ==========================================
# 1. ページ基本設定 & ブラウザ自動翻訳防止
# ==========================================
st.set_page_config(
    page_title="World News",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <meta name="google" content="notranslate" />
    <style>
        html, body, [class*="css"] {
            translate: no !important;
        }
        /* ボタンなどの見栄えを調整 */
        .stButton button {
            width: 100%;
            border-radius: 6px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. Gemini APIキーの安全な読み込み
# ==========================================
GEMINI_API_KEY = ""
try:
    if "GEMINI_API_KEY" in st.secrets:
        GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

if not GEMINI_API_KEY:
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# サイドバーでAPIキーが未設定の場合の入力欄
if not GEMINI_API_KEY:
    st.sidebar.warning("⚠️ Gemini APIキーが設定されていません。")
    GEMINI_API_KEY = st.sidebar.text_input("Gemini APIキーを入力してください", type="password")

# Client初期化（キーがある場合）
client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

# ==========================================
# 3. 全21メディアのRSSフィード定義
# ==========================================
# ホーム用のトランプ氏関連ニュース（Google News RSSを活用）
TRUMP_NEWS_RSS = "https://news.google.com/rss/search?q=Trump&hl=en-US&gl=US&ceid=US:en"

# 左右カラムに配置する全21メディア
LEFT_MEDIA_SOURCES = {
    "🇺🇸 CNN": "http://rss.cnn.com/rss/edition_world.rss",
    "🇺🇸 The New York Times": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "🇺🇸 Washington Post": "https://feeds.washingtonpost.com/rss/world",
    "🇷🇺 RT": "https://www.rt.com/rss/news/",
    "🇷🇺 Sputnik": "https://sputnikglobe.com/export/rss2/archive/index.xml",
    "🇬🇧 BBC News": "http://feeds.bbci.co.uk/news/world/rss.xml",
    "🇬🇧 The Guardian": "https://www.theguardian.com/world/rss",
    "🇬🇧 Reuters": "https://www.reutersagency.com/feed/?best-topics=world-news&post_type=best",
    "🇬🇧 The Independent": "https://www.independent.co.uk/news/world/rss",
    "🇫🇷 France 24": "https://www.france24.com/en/rss",
    "🇶🇦 Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml"
}

RIGHT_MEDIA_SOURCES = {
    "🇩🇪 Deutsche Welle (DW)": "https://rss.dw.com/rdf/rss-en-all",
    "🇨🇳 China Daily": "http://www.chinadaily.com.cn/rss/world_rss.xml",
    "🇭🇰 SCMP": "https://www.scmp.com/rss/91/feed",
    "🇨🇦 Globe and Mail": "https://www.theglobeandmail.com/arc/outboundfeeds/rss/category/world/",
    "🇦🇺 Sydney Morning Herald": "https://www.smh.com.au/rss/world.xml",
    "🇮🇳 Times of India": "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms",
    "🇪🇸 El País": "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/english/portada",
    "🇸🇬 Straits Times": "https://www.straitstimes.com/news/world/rss.xml",
    "🇯🇵 Japan Times": "https://www.japantimes.co.jp/feed/topstories",
    "🌐 USGS (地震・気象)": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_week.atom"
}

# ブロックされやすいメディア用の予備フィード（自動フォールバック）
BACKUP_RSS_SOURCES = {
    "🇷🇺 Sputnik": "https://news.google.com/rss/search?q=site:sputnikglobe.com&hl=en-US&gl=US&ceid=US:en",
    "🇷🇺 RT": "https://news.google.com/rss/search?q=site:rt.com&hl=en-US&gl=US&ceid=US:en",
    "🇬🇧 Reuters": "https://news.google.com/rss/search?q=site:reuters.com+world&hl=en-US&gl=US&ceid=US:en"
}

# ==========================================
# 4. キャッシュ & 補助関数（RSS取得・翻訳・要約・HTML除去）
# ==========================================
if "selected_media" not in st.session_state:
    st.session_state.selected_media = "HOME"  # 初期表示はトランプ氏ニュース

if "translated_cache" not in st.session_state:
    st.session_state.translated_cache = {}

if "ai_summary_cache" not in st.session_state:
    st.session_state.ai_summary_cache = {}

def fetch_rss_feed(url, media_key=""):
    """ブラウザのUser-Agentを付与してRSSを取得し、失敗時は予備フィードへ切り替える"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()
        feed = feedparser.parse(xml_data)
        if feed.entries:
            return feed
    except Exception:
        pass

    # 通常のfeedparserでも試す
    feed = feedparser.parse(url)
    if feed.entries:
        return feed

    # それでも0件なら予備フィード（Google News経由）で確実に取得する
    if media_key in BACKUP_RSS_SOURCES:
        try:
            backup_url = BACKUP_RSS_SOURCES[media_key]
            req = urllib.request.Request(backup_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                xml_data = response.read()
            return feedparser.parse(xml_data)
        except Exception:
            pass

    return feed

def clean_html(raw_html):
    if not raw_html:
        return "概要なし"
    soup = BeautifulSoup(raw_html, "html.parser")
    for s in soup(["script", "style", "img"]):
        s.decompose()
    text = soup.get_text(separator=" ").strip()
    return text[:300] + "..." if len(text) > 300 else (text if text else "概要なし")

def translate_title(title):
    if not client:
        return title
    if title in st.session_state.translated_cache:
        return st.session_state.translated_cache[title]
    try:
        prompt = f"以下の英語ニュースタイトルを自然な日本語に翻訳してください。結果のみ出力してください。\n\n{title}"
        response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
        jp_title = response.text.strip()
        st.session_state.translated_cache[title] = jp_title if jp_title else title
        return st.session_state.translated_cache[title]
    except Exception:
        return title

def get_ai_summary(title, summary, media_name):
    if not client:
        return "Gemini APIキーを設定するとAI要約が使用できます。"
    cache_key = title
    if cache_key in st.session_state.ai_summary_cache:
        return st.session_state.ai_summary_cache[cache_key]
    
    prompt = f"""
以下の海外ニュースについて日本語で分かりやすく解説してください。
1. 3行ポイント要約
2. ニュースの注目点・背景

配信メディア: {media_name}
タイトル: {title}
概要: {summary}
"""
    try:
        response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)
        result = response.text
        st.session_state.ai_summary_cache[cache_key] = result
        return result
    except Exception as e:
        return f"AI解説の生成に失敗しました: {e}"

# ==========================================
# 5. メインヘッダー
# ==========================================
st.title("🌐 World News")
st.caption("世界の主要21メディアの最新ニュース ＆ トランプ氏関連速報ポータル")
st.markdown("---")

# ==========================================
# 6. 3カラムレイアウト構築
# ==========================================
left_col, main_col, right_col = st.columns([1, 2.5, 1])

# --- 左カラム（11メディア） ---
with left_col:
    st.subheader("欧米・中東メディア")
    if st.button("🏠 ホーム（トランプ速報）", type="primary", key="home_btn_left"):
        st.session_state.selected_media = "HOME"
        st.rerun()
    
    st.markdown("---")
    for media_name, rss_url in LEFT_MEDIA_SOURCES.items():
        if st.button(media_name, key=f"btn_left_{media_name}"):
            st.session_state.selected_media = media_name
            st.rerun()

# --- 右カラム（10メディア） ---
with right_col:
    st.subheader("各国の主要メディア")
    for media_name, rss_url in RIGHT_MEDIA_SOURCES.items():
        if st.button(media_name, key=f"btn_right_{media_name}"):
            st.session_state.selected_media = media_name
            st.rerun()

# --- 中央メインカラム（ニュース一覧表示） ---
with main_col:
    current_target = st.session_state.selected_media
    
    # 取得対象URLとタイトルの決定
    if current_target == "HOME":
        display_title = "🇺🇸 トランプ氏 関連ニュース（最新速報）"
        target_url = TRUMP_NEWS_RSS
        media_label = "Google News (Trump)"
    else:
        display_title = f"📰 {current_target} の最新ニュース"
        # 左右の辞書からURLを検索
        target_url = LEFT_MEDIA_SOURCES.get(current_target) or RIGHT_MEDIA_SOURCES.get(current_target)
        media_label = current_target

    st.subheader(display_title)
    
    # 手動更新ボタン
    if st.button("🔄 最新情報に更新", key="refresh_news"):
        st.rerun()

    # RSS読み込みと表示（User-Agent付与＋予備フィード対応版）
    with st.spinner(f"「{current_target}」のニュースを取得・翻訳中..."):
        feed = fetch_rss_feed(target_url, media_key=current_target)
        entries = feed.entries[:7]  # 表示件数（上位7件）

    if not entries:
        st.warning("ニュースの取得に失敗したか、最新記事がありません。")
    else:
        for idx, entry in enumerate(entries):
            orig_title = getattr(entry, "title", "No Title")
            clean_sum = clean_html(getattr(entry, "summary", getattr(entry, "description", "")))
            link = getattr(entry, "link", "#")
            
            # Geminiで日本語翻訳
            jp_title = translate_title(orig_title)

            # アコーディオン（カード風）表示
            with st.expander(f"【#{idx+1}】 {jp_title}"):
                st.markdown(f"**🇬🇧 原文タイトル:** {orig_title}")
                st.link_button("🔗 元記事を新しいタブで開く", link)
                st.markdown("---")
                st.markdown(f"**📄 概要:**\n{clean_sum}")
                st.markdown("---")
                
                # AI要約ボタン
                if st.button("✨ この記事をAIで要約・解説する", key=f"ai_{current_target}_{idx}"):
                    with st.spinner("Geminiが分析中..."):
                        summary_result = get_ai_summary(orig_title, clean_sum, media_label)
                        st.info(summary_result)