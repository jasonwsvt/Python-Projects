import sys, os, time

def getPath():
	if len(sys.argv) == 1:
		path = os.getcwd()
	else:
		path = sys.argv[1]
	path = os.path.abspath(path)
	return path

def getFiles(path):
	results = []

	for name in os.listdir(path):
		if name.endswith('.txt'):
			results.append(name)

	return results

def readFile(file, path):
	fullPath = os.path.join(path, file)
	t = time.ctime(os.path.getmtime(fullPath))
 
	print("Reading " + fullPath + " (" + t + ")")
	with open(fullPath, 'r') as f:
		data = f.read()
		print(data)
		f.close()

def chooseFile(files, path):
	print(path)
	print('\nWhich file would you like to read (any other key to quit)?')
	for i in range(0, len(files)):
		print(str(i) + " " + files[i])

	num = int(input("\n0 to " + str(len(files) - 1) + " >>> "))
	if num not in range(0, len(files)):
		quit()
	file = files[num]
	return file

if __name__ == "__main__":
	path = getPath()
	while True:
		files = getFiles(path)
		file = chooseFile(files, path)
		readFile(file, path)
else:
	print("Please run this from the command prompt.")