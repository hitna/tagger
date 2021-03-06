import warnings
warnings.simplefilter('ignore', FutureWarning)
import treetaggerwrapper as ttw

html = '''
<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/>
<style>
div {display: inline-block; _display: inline;}
.tooltip3{
    position: relative;
    cursor: pointer;
    display: inline-block;
}
.tooltip3 p{
    margin:0;
    padding:0;
}
.description3 {
    display: none;
    position: absolute;
    padding: 10px;
    font-size: 14px;
    line-height: 1.6em;
    color: #000000;
    border-radius: 5px;
    background: #ffffff;
    width: 500px;
    z-index: 10;
}

.tooltip3:hover .description3{
    display: inline-block;
    top: 30px;
    left: 0px;
}
</style>
<body bgcolor=\"#000000\" text=\"#ffffff\">

'''

dict = {
"CC":"等位接続詞",
"CD":"基数",
"DT":"限定詞",
"EX":"存在文のthere",
"FW":"外国語",
"IN":"前置詞または従位接続詞",
"IN/that":"補文素",
"JJ":"形容詞",
"JJR":"形容詞の比較級",
"JJS":"形容詞の最上級",
"LS":"リスト項目のマーカー",
"MD":"法助動詞",
"NN":"名詞の単数形または不可算名詞",
"NNS":"名詞の複数形",
"NP":"固有名詞の単数名",
"NPS":"固有名詞の複数形",
"PDT":"前限定詞",
"POS":"所有格語尾",
"PP":"人称代名詞",
"PP$":"所有代名詞",
"RB":"副詞",
"RBR":"副詞の比較級",
"RBS":"副詞の最上級",
"RP":"不変化詞(句動詞を構成する前置詞)",
"SENT":"文末の句読点記号",
"SYM":"記号",
"TO":"前置詞またはto不定詞",
"UH":"間投詞",
"VB":"be動詞の原形",
"VBD":"be動詞の過去形",
"VBG":"be動詞の動名詞または現在分詞",
"VBN":"be動詞の過去分詞",
"VBZ":"be動詞の三人称単数形現在",
"VBP":"be動詞の三人称単数形以外の現在",
"VD":"do動詞の原形",
"VDD":"do動詞の過去形",
"VDG":"do動詞の動名詞または現在分詞",
"VDN":"do動詞の過去分詞",
"VDZ":"do動詞の三人称単数形現在",
"VDP":"do動詞の三人称単数形以外の現在",
"VH":"have動詞の原形",
"VHD":"have動詞の過去形",
"VHG":"have動詞の動名詞または現在分詞",
"VHN":"have動詞の過去分詞",
"VHZ":"have動詞の三人称単数形現在",
"VHP":"have動詞の三人称単数形以外の現在",
"VV":"動詞の原形",
"VVD":"動詞の過去形",
"VVG":"動詞の動名詞または現在分詞",
"VVN":"動詞の過去分詞",
"VVZ":"動詞の三人称単数形現在",
"VVP":"動詞の三人称単数形以外の現在",
"WDT":"Wh限定詞",
"WP":"Wh代名詞",
"WP$":"所有関係代名詞",
"WRB":"Wh副詞",
":":"一般結合記号",
"$":"通貨記号",
}

# 解析関数
def analysis(text):
    # word, pos, lemma からなるタブ区切りの文字列のリストを取得する。
    tags_tabseparated = ttw.TreeTagger(TAGLANG='en').tag_text(text)
    # word, pos, lemma からなるタプルのリストを作成する。
    tags_tuple = ttw.make_tags(tags_tabseparated)
    # word, pos, lemma の一覧を表示する。
    return tags_tuple

# 辞書出力
def dictionary(conn, word):
  # データベースへ接続する --- (*3)
    c = conn.cursor()
    # SQLを実行して単語データを取り出す --- (*4)
    sql = '''SELECT * FROM items WHERE word = ?
    ORDER BY level DESC LIMIT 5'''
    rows = c.execute(sql, (word,))
    result = ""
    for n in rows:
        result += "{}\n".format(n[2])
    return result