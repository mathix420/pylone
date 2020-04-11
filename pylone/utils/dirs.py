import os

def makedirs(directories):
	for directory in directories:
		try:
			os.mkdir(directory)
		except FileExistsError:
			print(directory, 'already exists')
		except Exception as e:
			print('Error when creating directories')
			print(e)