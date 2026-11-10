import streamlit as st
import feedparser

# ---------------------------------------------------------
# ページ基本設定
# ---------------------------------------------------------
st.set_page_config(
    page_title="World News",
    page_icon="🌐",
    layout="wide"
)

# RSS取得・表示関数
def display_feed(url, limit=5):
    try:
        feed = feedparser.parse(url)
        if feed.entries:
            for entry in feed.entries[:limit]:
                title = entry.get('title', 'タイトルなし')
                link = entry.get('link', '#')
                
                st.markdown(f"・**{title}**")
                st.markdown(f" ↳ [👉 記事の詳細・原文を読む]({link})")
                st.write("")
        else:
            st.info("ニュースを取得できませんでした。")
    except Exception as e:
        st.error(f"読み込みエラー: {e}")

# ---------------------------------------------------------
# サイドバーによる画面切り替え
# ---------------------------------------------------------
st.sidebar.title("📌 Navigation")
app_mode = st.sidebar.radio(
    "表示するページを選択",
    ["🌐 World News (メイン速報)", "🏛️ トランプ大統領令・インパクトTop5"]
)

# =========================================================
# ページ 1: メインニュース速報
# =========================================================
if app_mode == "🌐 World News (メイン速報)":
    st.title("🌐 World News")
    st.caption("世界の主要メディア・最新ニュース速報（日本語見出し・快適閲覧版）")

    st.header("🔥 トランプ速報・最新注目ニュース")
    trump_rss = "https://news.google.com/rss/search?q=Trump+when:24h&hl=ja&gl=US&ceid=US:en"
    display_feed(trump_rss, limit=7)

    st.divider()

    st.header("📰 海外主要メディア一覧（21媒体・日本語見出し）")
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

# =========================================================
# ページ 2: 特設・トランプ大統領令アーカイブ
# =========================================================
elif app_mode == "🏛️ トランプ大統領令・インパクトTop5":
    st.title("🏛️ 世界を揺るがしたトランプ大統領令 Top 5")
    st.caption("第1次・第2次政権において、世界情勢や経済・社会に絶大なインパクトを与えた重要署名の要約アーカイブ")

    tab1, tab2 = st.tabs(["⚡ 第2次政権（2025年〜）", "📜 第1次政権（2017年〜2021年）"])

    with tab1:
        st.header("⚡ 第2次政権：就任直後からの電撃署名 Top 5")
        st.markdown("""
        **1. 国境非常事態宣言と強制送還の全面加速**
        * **日付・番号:** 2025年1月
        * **要約:** 南部国境における国家非常事態を宣言し、連邦軍・国営警備隊の投入を可能に。不法滞在者の拘留・送還プロセスを劇的に加速させた。
        * **ポイント:** 前政権からの移民政策を即座に大転換し、中南米諸国や国際社会に大きな衝撃を与えた。

        ---

        **2. 「エネルギー緊急事態宣言」と国内掘削の全面解禁 (Drill, Baby, Drill)**
        * **日付・番号:** 2025年1月
        * **要約:** 石油・天然ガスの新規掘削制限やバイデン政権時代のEV推進・環境規制を大量撤廃。エネルギー自給率向上とコスト削減を最優先に指定。
        * **ポイント:** 世界の原油市場やグリーンエネルギー産業、脱炭素政策の枠組みに甚大な影響。

        ---

        **3. 政府効率化（DOGE）と連邦行政機構の大改革**
        * **日付・番号:** 2025年1月
        * **要約:** 連邦政府の無駄な支出削減、規制の一括見直し、在宅勤務の原則廃止などを指示。政府組織のスリム化を強制推進。
        * **ポイント:** 行政国家（Administrative State）の解体を掲げ、連邦職員の大量削減や組織再編の引き金に。

        ---

        **4. 出生地主義（Birthright Citizenship）の見直し指示**
        * **日付・番号:** 2025年1月
        * **要約:** 米国内で生まれた不法滞在者の子供に対する自動的な米国国籍付与（憲法修正第14条の解釈）を再検討・制限するよう命じた。
        * **ポイント:** 法的・憲法上の大きな議論を呼び、最高裁まで巻き込む大法的闘争の引き金となった。

        ---

        **5. フェンタニル等・国際薬物組織の「指定強化」**
        * **日付・番号:** 2025年
        * **要約:** 米国内で深刻な猛威を振るう医療用麻薬フェンタニルおよび密輸カルテルに対し、国家安全保障上の重大な脅威として厳罰・制裁措置を連発。
        * **ポイント:** 外交問題（中国やメキシコとの通商交渉・制裁）とも直結する重要安全保障案件に指定。
        """)

    with tab2:
        st.header("📜 第1次政権：歴史を決定づけた主要署名 Top 5")
        st.markdown("""
        **1. 入国一時停止・トラベル・バン（EO 13769 / EO 13780）**
        * **日付:** 2017年1月
        * **要約:** イスラム圏を中心とする特定諸国の国民に対し、米国への入国を一時的に全面禁止した大統領令。
        * **ポイント:** 世界中の空港で即座に大混乱が発生し、大規模な抗議デモや法廷闘争へと発展した第1次政権を象徴する命令。

        ---

        **2. オバマケア（医療保険制度改革法）の負担軽減命令（EO 13765）**
        * **日付:** 2017年1月20日（就任当日に署名）
        * **要約:** オバマ前政権が推し進めた医療保険改革法による経済的・規制的負担を最小限に抑えるよう、全連邦省庁に命じた第1号令。
        * **ポイント:** 自身の公約であった「オバマケア撤廃」に向けた強い姿勢を就任初日に見せつけた。

        ---

        **3. 国境警備の強化と壁建設（EO 13767）**
        * **日付:** 2017年1月
        * **要約:** 米メキシコ国境における「物理的な壁」の即時建設を開始し、国境警備隊の増員と施設整備を命じた。
        * **ポイント:** メキシコ政府との外交摩擦を引き起こし、国境政策の抜本的変更を世界に示した。

        ---

        **4. パリ協定脱退・環境規制緩和（EO 13783）**
        * **日付:** 2017年3月
        * **要約:** クリーンパワー・プラン（火力発電規制）の見直しなど、オバマ政権の温暖化対策を巻き戻し、国内エネルギー産業を優先させる方針を決定。
        * **ポイント:** その後の「パリ協定からの離脱通告」へとつながる、国際環境協調への冷や水となった決断。

        ---

        **5. ソーシャルメディア企業の免責見直し（EO 13925）**
        * **日付:** 2020年5月
        * **要約:** SNSプラットフォーム企業（TwitterやFacebook等）が持つ「投稿内容に対する免責保護（通信品位法230条）」の解釈見直しを関係機関に命じた。
        * **ポイント:** トランプ氏自身の投稿検閲を巡りBig Tech（巨大IT企業）との直接対決姿勢を強めた、ネット言論の歴史的ターニングポイント。
        """)