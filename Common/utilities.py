import os
import re
import csv

# 引数で指定したディレクトリ配下のファイルを再帰的に収集する。
def fild_all_files(dir):
	file_list = []
	for root, dirs, files in os.walk(dir):
		for file in files:
			file_list.append(os.path.join(root, file))
	# ファイルリストを返却
	return file_list

# listからextensionsに一致したもののみ返却する
def filter_extension(list, extensions):
	filter_result = []
	for i in range(len(list)):
		for extension in extensions:
			regex = r".+" + extension + '$'
			match_result = re.search(regex, list[i])
			if match_result != None:
				filter_result.append(list[i])
				break
	# 正規表現でヒットした項目のみ返却
	return filter_result

# 引数で指定したファイルから1行ずつ読み込む
def read_line(file):
	with open(file, 'r') as f:
		for line in f:
			yield line

# CSVファイルにデータを出力
# 引数：output_dataはタプル型の配列か2次元配列の必要あり
def output_csv(output_data, output_dir):
	with open(output_dir, 'w') as f:
		writer = csv.writer(f, lineterminator='\n')
		writer.writerows(output_data)
