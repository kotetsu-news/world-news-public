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
                st.markdown(f"- [{title}]({link})")
        else:
            st.info("ニュースを取得できませんでした。")
    except Exception as e:
        st.error(f"読み込みエラー: {e}")

# ---------------------------------------------------------
# サイドバーによる画面切り替え（3ページ構成）
# ---------------------------------------------------------
st.sidebar.title("📌 Navigation")
app_mode = st.sidebar.radio(
    "表示するページを選択",
    [
        "🌐 World News (メイン速報)",
        "🏛️ トランプ大統領令・インパクトTop5",
        "🧭 海外主要メディアの立場・特徴マップ"
    ]
)

# =========================================================
# ページ 1: メインニュース速報
# =========================================================
if app_mode == "🌐 World News (メイン速報)":
    st.title("🌐 World News")
    st.caption("世界の主要メディア・最新ニュース速報")

    # 1. トランプ速報
    st.header("🔥 トランプ速報・最新注目ニュース")
    trump_rss = "https://news.google.com/rss/search?q=Trump&hl=ja&gl=JP&ceid=JP:ja"
    display_feed(trump_rss, limit=7)

    st.divider()

    # 2. 海外21主要メディア一覧
    st.header("🌍 海外主要メディア一覧（21媒体）")

    with st.expander("CNN News (アメリカ)"):
        display_feed("https://news.google.com/rss/search?q=CNN&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The New York Times (アメリカ)"):
        display_feed("https://news.google.com/rss/search?q=%22New+York+Times%22+OR+%22%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%A9%E3%83%BC%E3%82%AF%E3%83%88%E3%83%BC%E3%83%A0%E3%82%BA%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Washington Post (アメリカ)"):
        display_feed("https://news.google.com/rss/search?q=%22Washington+Post%22+OR+%22%E3%83%AF%E3%82%B7%E3%83%B3%E3%83%88%E3%83%B3%E3%83%9D%E3%82%B9%E3%83%88%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("RT (Russia Today) (ロシア)"):
        display_feed("https://news.google.com/rss/search?q=RT+OR+%22%E3%83%AD%E3%82%B7%E3%82%A2%E3%83%88%E3%82%A5%E3%83%87%E3%82%A4%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Sputnik News (ロシア)"):
        display_feed("https://news.web.sputniknews.jp/rss/sputnik.xml")
    with st.expander("BBC News (イギリス)"):
        display_feed("https://news.google.com/rss/search?q=BBC&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Guardian (イギリス)"):
        display_feed("https://news.google.com/rss/search?q=Guardian+OR+%22%E3%82%AC%E3%83%BC%E3%83%87%E3%82%A3%E3%82%A2%E3%83%B3%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Reuters (イギリス/国際)"):
        display_feed("https://news.google.com/rss/search?q=%E3%83%AD%E3%82%A4%E3%82%BF%E3%83%BC&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Independent (イギリス)"):
        display_feed("https://news.google.com/rss/search?q=Independent+OR+%22%E3%82%A4%E3%83%B3%E3%83%87%E3%82%A3%E3%83%9A%E3%83%B3%E3%83%87%E3%83%B3%E3%83%88%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Le Monde (フランス)"):
        display_feed("https://news.google.com/rss/search?q=%22Le+Monde%22+OR+%22%E3%83%AB%E3%83%BB%E3%83%A2%E3%83%B3%E3%83%89%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Al Jazeera (カタール)"):
        display_feed("https://news.google.com/rss/search?q=%22Al+Jazeera%22+OR+%22%E3%82%A2%E3%83%AB%E3%82%B8%E3%83%A3%E3%82%B6%E3%83%BC%E3%83%A9%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("Deutsche Welle (ドイツ)"):
        display_feed("https://news.google.com/rss/search?q=%22Deutsche+Welle%22+OR+%22%E3%83%89%E3%82%A4%E3%83%84%E5%85%AC%E5%85%B1%EBroadcast%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("China Daily (中国)"):
        display_feed("https://news.google.com/rss/search?q=%22China+Daily%22+OR+%22%E3%83%81%E3%83%A3%E3%82%A4%E3%83%8A%E3%83%87%E3%82%A4%E3%83%AA%E3%83%BC%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("South China Morning Post (香港)"):
        display_feed("https://news.google.com/rss/search?q=SCMP+OR+%22%E5%8D%97%E8%8F%AF%E6%97%A9%E5%A0%B1%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Globe and Mail (カナダ)"):
        display_feed("https://news.google.com/rss/search?q=%22Globe+and+Mail%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Sydney Morning Herald (オーストラリア)"):
        display_feed("https://news.google.com/rss/search?q=%22Sydney+Morning+Herald%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Times of India (インド)"):
        display_feed("https://news.google.com/rss/search?q=%22Times+of+India%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("El País (スペイン)"):
        display_feed("https://news.google.com/rss/search?q=%22El+Pais%22+OR+%22%E3%82%A8%E3%83%AB%E3%83%BB%E3%83%91%E3%82%A4%E3%82%B9%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Straits Times (シンガポール)"):
        display_feed("https://news.google.com/rss/search?q=%22Straits+Times%22+OR+%22%E3%82%B9%E3%83%88%E3%83%AC%E3%83%BC%E3%83%84%E3%83%BB%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%BA%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("The Japan Times (日本)"):
        display_feed("https://news.google.com/rss/search?q=%22Japan+Times%22&hl=ja&gl=JP&ceid=JP:ja")
    with st.expander("USGS Earthquake Hazards (アメリカ/防災)"):
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

# =========================================================
# ページ 3: 海外主要メディアの立場・特徴マップ（新規追加）
# =========================================================
elif app_mode == "🧭 海外主要メディアの立場・特徴マップ":
    st.title("🧭 海外主要メディアの立場・特徴マップ")
    st.caption("海外ニュースを読み解くための基本ガイド（各メディアの立ち位置・特徴まとめ）")

    st.info("💡 **読み方のコツ：** 海外メディアは日本の新聞以上に「政治的スタンス」や「国益の視点」がはっきりしています。同じニュースでも複数のメディアを見比べると、世界の立体的な見え方が分かります。")

    tab_us, tab_eu, tab_ru_cn, tab_other = st.tabs([
        "🇺🇸 アメリカ・中立通信社",
        "🇪🇺 ヨーロッパ主要紙",
        "🇷🇺🇨🇳 ロシア・中国・中東",
        "🌏 アジア・太平洋・防災"
    ])

    with tab_us:
        st.subheader("🇺🇸 アメリカ・国際通信社")
        st.markdown("""
        * **Reuters（ロイター｜イギリス/国際）**
          * **スタンス:** 中立・事実重視（通信社）
          * **特徴:** 世界中の報道機関にニュースを配信する通信社。感情的な論評を避け、事実を淡々と最も早く伝えるため、基準点として最適。
        * **CNN News（アメリカ）**
          * **スタンス:** 中道左派・リベラル寄り
          * **特徴:** 24時間ニュース専門局の草分け。国際ニュースや速報性に強みがある一方、アメリカ国内政治ではリベラル（民主党寄り）な論調が見られる。
        * **The New York Times（アメリカ）**
          * **スタンス:** リベラル・進歩派の代表格
          * **特徴:** 圧倒的な取材力と調査報道を誇る高級紙。人権・環境・多様性を重視する論調で、トランプ政権など保守派に対しては批判的な視点が多い。
        * **The Washington Post（アメリカ）**
          * **スタンス:** リベラル寄り・政治調査報道
          * **特徴:** 首都ワシントンを拠点とし、ホワイトハウスや連邦政府の内部事情・政治スクープに極めて強い影響力を持つ。
        """)

    with tab_eu:
        st.subheader("🇪🇺 ヨーロッパ主要メディア")
        st.markdown("""
        * **BBC News（イギリス）**
          * **スタンス:** 公共放送・中立志向
          * **特徴:** 受信料で運営される英国の公共放送。世界の国際報道のスタンダードとされ、バランス感覚と信頼性が非常に高い。
        * **The Guardian（イギリス）**
          * **スタンス:** リベラル・左派寄り
          * **特徴:** 環境問題、人権、格差是正に非常に熱心。記事を無料で公開しており、世界中のリベラル層から広く読まれている。
        * **The Independent（イギリス）**
          * **スタンス:** 中道左派・リベラル
          * **特徴:** どの政党にも属さない「独立系」として創刊。現在はデジタル専業となり、欧州や国際政治の分析記事に定評がある。
        * **Le Monde（ル・モンド｜フランス）**
          * **スタンス:** 中道左派・知性派高級紙
          * **特徴:** フランスを代表する夕刊紙。EU（欧州連合）の動向やアフリカ情勢、国際外交に関する深い分析が特徴。
        * **Deutsche Welle（ドイチェ・ヴェレ｜ドイツ）**
          * **スタンス:** 公共国際放送・EU視点
          * **特徴:** ドイツの国際放送局。欧州経済、エネルギー問題、ロシア・ウクライナ情勢をEUの中核国の視点から分かりやすく報じる。
        * **El País（エル・パイス｜スペイン）**
          * **スタンス:** 中道左派
          * **特徴:** スペイン語圏で最大の影響力を持つ高級紙。ヨーロッパだけでなく、中南米（ラテンアメリカ）の政治・経済ニュースに非常に強い。
        """)

    with tab_ru_cn:
        st.subheader("🇷🇺🇨🇳 ロシア・中国・中東（欧米とは異なる視点）")
        st.markdown("""
        * **RT / Russia Today（ロシア）**
          * **スタンス:** ロシア政府系・反西側（国益主張）
          * **特徴:** ロシア政府の資金で運営される国際メディア。欧米（アメリカ・NATO）の政策や矛盾を厳しく批判し、ロシア側の主張や多極化世界を強調する。
        * **Sputnik News（スプートニク｜ロシア）**
          * **スタンス:** ロシア国営通信社系・国益主張
          * **特徴:** 日本語版も展開。欧米メディアが報じない角度からの軍事・外交ニュースや、西側諸国への批判的な論調が特徴。
        * **China Daily（チャイナ・デイリー｜中国）**
          * **スタンス:** 中国政府系・公式見解
          * **特徴:** 中国共産党・政府の公式な立場や経済発展の成果を英語で世界に発信する国営英字紙。中国政府の公式見解を知るための一次ソース。
        * **South China Morning Post（SCMP｜香港）**
          * **スタンス:** 中立〜やや親中・ビジネス重視
          * **特徴:** 香港の伝統ある英字紙（アリババグループ傘下）。中国本土の経済・テクノロジー・政治の裏事情を英語で最も詳しく知ることができる。
        * **Al Jazeera（アルジャジーラ｜カタール）**
          * **スタンス:** 中東・グローバルサウス視点
          * **特徴:** カタール王室系メディア。中東紛争（パレスチナ・イスラエル問題など）や途上国の視点を重視し、欧米メディアとは異なる角度から鋭い報道を行う。
        """)

    with tab_other:
        st.subheader("🌏 アジア・太平洋・公式防災機関")
        st.markdown("""
        * **The Straits Times（シンガポール）**
          * **スタンス:** 現実主義・アジア経済中心
          * **特徴:** 東南アジアを代表する英字紙。米中対立の狭間にあるASEAN諸国の冷静な視点や、アジアの金融・貿易ニュースに強い。
        * **The Times of India（インド）**
          * **スタンス:** インド国益・経済成長重視
          * **特徴:** 世界最大の発行部数を誇る英字紙。「グローバルサウス」のリーダーとして台頭するインドの外交・IT・経済の勢いを体感できる。
        * **The Globe and Mail（カナダ）**
          * **スタンス:** 中道〜中道右派・経済重視
          * **特徴:** カナダを代表する高級紙。アメリカ経済との結びつきが強く、北米全体の視点からアメリカの政治を客観的に分析する記事が多い。
        * **The Sydney Morning Herald（オーストラリア）**
          * **スタンス:** 中道左派・インド太平洋重視
          * **特徴:** オーストラリアの老舗紙。対中国関係や太平洋島嶼国、日本の安全保障とも関わりが深い「インド太平洋地域」の動向に敏感。
        * **The Japan Times（日本）**
          * **スタンス:** 中立・日本発の国際発信
          * **特徴:** 日本最古の英字紙。日本の政治・経済・社会ニュースが海外に向けてどのように英語で説明されているかを確認できる。
        * **USGS Earthquake Hazards（アメリカ地質調査所）**
          * **スタンス:** 公式科学データ（報道機関ではない）
          * **特徴:** アメリカ政府の科学機関による世界中のリアルタイム地震速報（M2.5以上）。メディアの推測を挟まない純粋な一次観測データ。
        """)