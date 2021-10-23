
import lib
import sqlite3

output = lib.html
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
      line_tmp = line_tmp + "<div class=\"tooltip3\"><b>{}</b><div class=\"description3\">[{}]{}</div></div> ".format(tag[0],lib.dict.get(tag[1]),mean)
    elif((tag[0] == '.' and dialog_cnt % 2 == 0) or i >= i_max):
      line_tmp = line_tmp + "<div class=\"tooltip3\">{}<div class=\"description3\">[{}]{}</div></div><br>".format(tag[0],lib.dict.get(tag[1]),mean)
    else:
      line_tmp = line_tmp + "<div class=\"tooltip3\">{}<div class=\"description3\">[{}]{}</div></div> ".format(tag[0],lib.dict.get(tag[1]),mean)
    i = i + 1
f.close()
conn.close()
output = output + line_tmp

# CSVファイルに書き込む
with open("tagger.html", "w" ,encoding="utf-8") as fp:
  fp.writelines(output)
