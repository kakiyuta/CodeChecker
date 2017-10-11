# コメントに禁則文字が含まれていないかを検査し、CSVファイルに出力する。
# 現在対応している禁則文字とは以下の通り
#    ・半角カナ
#    ・全角英数字
import sys
import os.path
import re

import Common

# 引数取得
args = sys.argv
# CSV出力フラグ
is_output = False

# 引数チェック
if len(args) == 2:
	is_output = False
elif len(args) == 3:
	is_output = True
else:
	print("Please input \"python {0} [project dir] ([output csv file path])\"" .format(args[0]))
	sys.exit()

# 検査対象プロジェクトディレクトリ
project_dir = args[1]

# 引数の検査対象ディレクトチェック
if os.path.isdir(project_dir) != True:
	# 指定されたディレクトリが無いため強制終了
	print("Error! No such directory: " + project_dir)
	sys.exit()

# 指定ディレクトリ直下のファイルリストを取得
file_list = Common.utilities.fild_all_files(project_dir)
# ファイルリストから指定した拡張子のファイルのみ取得(".c", ".h"ファイルのみ)
file_list = Common.utilities.filter_extension(file_list, [".c",".h"])

#検索結果格納
result = []
#csvのヘッダー行
result.append(("\"Path\"", "\"line\"", "\"string\"", "\"type\""))

# 各ファイルごとに規約をチェック
for file in file_list:
	# プロジェクトフォルダからのパス
	relative_path = file.replace(project_dir, "")

	# 1行ずつ取得
	line_num = 0
	for line in Common.utilities.read_line(file):
		line_num += 1

		# 半角ｶﾅ検索
		regex = r"[ｦ-ﾟ]+"
		hankana = re.search(regex, line)
		if hankana != None:
			tmp = (relative_path, line_num, line, "半角ｶﾅ")
			result.append(tmp)

		# 全角英数字
		regex = r"[Ａ-Ｚａ-ｚ０-９]+"
		zenei = re.search(regex, line)
		if zenei != None:
			tmp = (relative_path, line_num, line, "全角英数字")
			result.append(tmp)

# ヘッダー分の1行があるため長さが2以上の場合がデータ有りと判定する
if len(result) >= 2:
	#結果出力
	print("{0} result found for \"半角カナ\" or \"全角英数字\"" .format(len(result)-1))

	if is_output:
		# CVS形式で出力
		Common.utilities.output_csv(result, args[2])
	else:
		for data in result:
			print(data)
else:
	print("No results found for \"半角カナ\" or \"全角英数字\"")
