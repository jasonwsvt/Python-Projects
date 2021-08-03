import shutil, os, time, datetime

#current working directory
cwd = os.path.dirname(os.path.realpath(__file__))

#set where the source of the files are
source = cwd + '/Folder_A/'

#set the destination path
destination = cwd + '/Folder_B/'
files = filter(lambda x: x.endswith(".txt"), os.listdir(source))

#Conversion from unix timestamp to days
tsToDays = 24 * 60 * 60



for i in files:
    #move the files represented by 'i' to their new destination
    file = os.path.normpath(os.path.join(source, i))
    
    #The time the file was modified
    modificationTime = os.stat(file).st_mtime
    
    print(file)
    print(modificationTime)
    print(time.time())
    print((time.time() - modificationTime) / tsToDays)
    
    #If the amount of time between now and the file modification time in days is less than 1
    #move the file
#    if((time.time() - modificationTime) / tsToDays >= 1):
#        shutil.move(file, destination)