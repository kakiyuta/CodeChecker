# 変数の宣言場所を検索し、変数一覧をCSVファイルに出力する。

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

# 検索対処の型名(正規表現)
reservied_word = ["static", "const", "signed", "unsigned", "extern", "volatile",
				  "register", "return", "goto", "if", "else", "switch", "case",
				  "default", "break", "for", "while", "do", "continue",
				  "typedef", "struct", "enum", "union", "sizeof"]
#検索結果格納
result = []
#csvのヘッダー行
result.append(("\"ファイル名\"", "\"行数\"", "\"宣言部\""))

# 検索ワードを作成
search_word = []
for word in reservied_word:
	# 予約語の"("の後にスペースを入れていない場合
	search_word.append(word + r"\(")
	# 予約語の"("の後にスペースが二つ以上ある場合
	search_word.append(word + r" {2,}\(")
# ")"と"{"間のスペースを確認する正規表現も追加
search_word.append(r"\)\{")
search_word.append(r"\) {2,}\{")

# 各ファイルごとに規約をチェック
for file in file_list:
	# プロジェクトフォルダからのパス
	relative_path = file.replace(project_dir, "")

	# 1行ずつ取得
	for i, line in enumerate(Common.utilities.read_line(file)):
		# 型検索ループ
		for word in search_word:
			# 型名を単語単位で検索する。("int32"などの検索結果を除外するため)
			regex = word
			search_result = re.search(regex, line)
			if search_result != None:
				# "line[:-1]"は末尾改行を削除している(末尾は必ず改行があること前提)
				tmp = (relative_path, i + 1, line[:-1])
				result.append(tmp)
				break

# ヘッダー分の1行があるため長さが2以上の場合がデータ有りと判定する
if len(result) >= 2:
	#結果出力
	print("{0} result found for variable" .format(len(result)-1))

	if is_output:
		# CVS形式で出力
		Common.utilities.output_csv(result, args[2])
	else:
		for data in result:
			print(data)
else:
	print("No results found for variable")

print()
