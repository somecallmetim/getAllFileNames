__author__ = 'timbauer'

import os

directory = "/Users/timbauer/AndroidStudioProjects/LoLDraftCalculator/app/src/main/res/drawable"
#gets list of all file names in the given directory
filesList = os.listdir(directory)

#assigns a file name to 'nameOfFile' variable
nameOfFile = 'fileNames.txt'

#create new file
f = open(nameOfFile, 'w')
#iterate through the list of files and add/remove desired text
for fileName in filesList:
    #prepend current file name with its directory
    oldFileNamePlusDir = directory + "/" + fileName

    #make all char's in fileName lower case
    fileName = fileName.lower()

    #prepend new file name with it's directory
    newFileNamePlusDir = directory + "/" + fileName

    #rename all files in folder
    os.rename(oldFileNamePlusDir, newFileNamePlusDir)

    #adds 'R.drawable.' to the front of all file names and removes ".png"
    fileName = ('R.drawable.' + fileName).strip('.png')
    #write the edited file to nameOfFile and add a comma and new line char
    f.write(fileName + ',\n' )
f.close()