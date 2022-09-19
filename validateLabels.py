## This python file can be helpful for yolo datset only you can modify the annotation class ID in the text file  

import os
import glob
import sys

path = ""  ## here need to give the data path with .txt extensions for the use of yolo dataset only
           ## make sure the path should be in between the quotes " "
outPath = "" ## here need to give the path where we need to write the modified data 
os.system('mkdir "' + outPath + '"')
labelsPath = glob.glob(path+'/*txt')
# print(labelsPath)
for label_path in labelsPath:
    # print(label_path)
    fileName = os.path.split(label_path)[1]
    newLine = open(outPath+'/'+fileName, 'w')
    with open(label_path, mode='r') as labelFile:
        lines = labelFile.read().splitlines()
        # print(file)
        for line in lines:
            txt = line.split(' ')
            txt[0] = '2' ## here you can modify the class ID in the quotes ''
            modData = ' '.join(txt)
            print(modData)
            newLine.write(modData+'\n')
    newLine.close()

