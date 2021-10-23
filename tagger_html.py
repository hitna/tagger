
import lib
import sqlite3

output = "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"/><style>div {display: inline-block; _display: inline;}</style><body bgcolor=\"#000000\" text=\"#ffffff\">"
line_tmp = ""
conn = sqlite3.connect("ejdict.sqlite3")
# コメントファイルを読み込む
f = open('sentence.txt', 'r' ,encoding="utf-8")
lines = f.readlines()
# ""ダブルコーテーション内かどうかを判定
dialog_cnt = 0

for line in lines:
  tags = lib.analysis(line)
  i = 0
  i_max = len(tags) - 1
  for tag in tags:
    if(tag[2] == "\""):
      dialog_cnt = dialog_cnt + 1   
    mean = lib.dictionary(conn, tag[2])
    #述語動詞の判定
    if(tag[1][0] == 'V'):
      line_tmp = line_tmp + "<b title=\"[{}]{}\">{}</b> ".format(lib.dict.get(tag[1]),mean, tag[0])
    elif((tag[0] == '.' and dialog_cnt % 2 == 0) or i >= i_max):
      line_tmp = line_tmp + tag[0] + "<br>"
    else:
      line_tmp = line_tmp + "<div title=\"[{}]{}\">{}</div> ".format(lib.dict.get(tag[1]),mean,tag[0])
    i = i + 1
f.close()
conn.close()
output = output + line_tmp

# CSVファイルに書き込む
with open("tagger.html", "w" ,encoding="utf-8") as fp:
  fp.writelines(output)
