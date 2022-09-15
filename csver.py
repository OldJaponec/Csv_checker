import pandas as pd
import os


def directory_list(folder):
	'''
		Return a list of files in directory
	'''
	# the folder is assumed to be in the root folder
	try:
		return sorted(os.listdir(os.curdir + "/" + folder))
	except:
		print('No such directory')


def is_matching(file_1, file_2):
	'''
		Check files for the same structure and headers
	'''
	# open files is all we need from pandas
	try:
		structure_1 = pd.read_csv(file_1).columns
		structure_2 = pd.read_csv(file_2).columns
	except:
		print("Something is wrong, maybe there is a non csv file" )

	# check the number of columns and their names
	if len(structure_1) == len(structure_2):
		for i in range(len(structure_1)):
			if structure_1[i] != structure_2[i]:
				return False
		return True
	return False


def search_files(folder_1, folder_2):
	'''
		Append identical files to matching_files and others to unmatching_files 
	'''
	matching_files = []
	unmatching_files = []

	for file_1 in directory_list(folder_1):
		for file_2 in directory_list(folder_2):
			if file_1 == file_2:
				if is_matching(folder_1 + '/' + file_1, folder_2 + '/' + file_2):
					matching_files.append(file_1)
				else:
					unmatching_files.append(file_1)

	return matching_files, unmatching_files


'''
	Test
'''
# There are already two folders with csv files in the root folder
if __name__ == '__main__':
	matching_files   = search_files('folder_1', 'folder_2')[0]
	unmatching_files = search_files('folder_1', 'folder_2')[1]

	print('Matcing files:')
	for file in matching_files:
		print(file)

	print('\n')

	print('Unmatcing files:')
	for file in unmatching_files:
		print(file)


