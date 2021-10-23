
import lib
import sqlite3

output = ""
table_html = "<table>"
conn = sqlite3.connect("ejdict.sqlite3")
# コメントファイルを読み込む
f = open('sentence.txt', 'r' ,encoding="utf-8")
lines = f.readlines()
for line in lines:
  line_tmp = "<p>"
  tags = lib.analysis(line)
  i = 0
  for tag in tags:
    mean = lib.dictionary(conn, tag[2])
    #述語動詞の判定
    if(tag[1][0] == 'V'):
      line_tmp = line_tmp + "<b>{}</b> ".format(tag[0])
      table_html = table_html + "<tr><td><b>{}</b></td><td><b>{}</b></td><td><b>{}</b></td><td>{}</td></tr>\n".format(tag[0], tag[2], lib.dict.get(tag[1]), mean)
    elif(tag[0] == '.' or i >= len(tags) - 1):
      table_html = table_html + "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n".format(tag[0], tag[2], lib.dict.get(tag[1]), mean)
      line_tmp = line_tmp + tag[0] + "</p>"
      output = output + line_tmp
      table_html = table_html + "</table>"
      output = output + table_html
      line_tmp = "<p>"
      table_html = "<table>"
    else:
      table_html = table_html + "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n".format(tag[0], tag[2], lib.dict.get(tag[1]), mean)
      line_tmp = line_tmp + tag[0] + " "
    i = i + 1
f.close()
conn.close()

# CSVファイルに書き込む
with open("tagger.html", "w" ,encoding="utf-8") as fp:
  fp.writelines(output)
