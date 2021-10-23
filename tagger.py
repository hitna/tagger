import csv
import lib

output = []
output_tmp = []
# コメントファイルを読み込む
f = open('sentence.txt', 'r')
lines = f.readlines()
for line in lines:
  line_tmp = ""
  tags = lib.analysis(line)
  for tag in tags:
    output_tmp.append([tag[0], tag[2], lib.dict.get(tag[1])])
    if(tag[0] == '.'):
      line_tmp = line_tmp + tag[0]
      output.append([line_tmp])
      output = output + output_tmp
      output_tmp = []
      line_tmp = ""
    else:
      line_tmp = line_tmp + tag[0] + " "
f.close()

# CSVファイルに書き込む
with open("tagger.csv", "w", encoding="shift_jis", newline="") as fp:
  writer = csv.writer(fp,delimiter=',')
  writer.writerows(output)