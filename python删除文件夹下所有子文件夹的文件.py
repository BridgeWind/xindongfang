# encoding=utf-8
import os

filepath = 'D:/Desktop/xdf/day5'
del_dir = os.listdir(filepath)
dir_set = []
for f in del_dir:
	file_path = os.path.join(filepath, f)
	if os.path.isdir(file_path):
		#print(file_path)
		dir_set.append(f)
		sub_dir = os.listdir(file_path)
		for files in sub_dir:
			#print(files)
			file_path2 = os.path.join(file_path, files)
			if os.path.isdir(file_path2):
				del_files(f_path)
			else:
				os.remove(file_path2)
print(dir_set)