import os
import sys
import glob
import random
from random import shuffle
datasetPath = ""  ## here give a path of the directory where the data exist 
		 ##make sure the path should be in the quotes ""

dataset = glob.glob(datasetPath+'/*jpg')  ## you can glob any extension files like .jpg, .png, .txt, .xml, .json .....
for imagePath in dataset:
    name = imagePath[:-4]
    # print(name)
    txt = name + '.txt'

    if os.path.exists(txt):
        continue
    else:
        print('rm '+imagePath)
        os.system('rm "'+imagePath+'"')
        
        ## from line number 10 to 19 these lines of code would be helpful to delete the extra images more than annotations
        ## you can use that code if you found images more than annotations or else comment out those lines of code
        
print(dataset)
random.shuffle(dataset)
print(dataset)

trainEndIndices = int(0.85*len(dataset))
# print(trainEndIndices)
trainData = dataset[0:trainEndIndices]
valDataStart = trainEndIndices
valEndIndices = int(0.1*len(dataset))+valDataStart
valData = dataset[valDataStart:valEndIndices]
testDataStart = valEndIndices
testData = dataset[valEndIndices:]
outTrain = ""   ## here give a path where the train data going to copy/move
		##make sure the path should be in the quotes ""
outValid = ""   ## here give a path where the valid data going to copy/move 
		##make sure the path should be in the quotes ""
outTest = ""    ## here give a path where the test data going to copy/move 
		##make sure the path should be in the quotes ""
os.system('mkdir "' + outTrain + '"')
os.system('mkdir "' + outValid + '"')
os.system('mkdir "' + outTest + '"')

for train_data in trainData:
    # print(train_data)
    jpgTrain = train_data
    # print(jpg)
    txtNameTrain = jpgTrain.split('.jpg')[0]
    # print(txtName)
    txtTain = txtNameTrain+'.txt'  ## here you can give any type of extension according to the annotations you have (i.e.,) .xml, .json......
    # print(txt)
    print('cp "' + jpgTrain + '"  "' + outTrain + '"')
    print('cp "' + txtTain + '"  "' + outTrain + '"' )
    os.system('cp "' + jpgTrain + '"  "' + outTrain + '"')  ## here can use move command 'mv' instead of copy 'cp' when you want to move the data to the directory  if that is necessary
    os.system('cp "' + txtTain + '"  "' + outTrain + '"')   ## here can use move command 'mv' instead of copy 'cp' when you want to move the data to the directory  if that is necessary
print("[INFO] The training dataset has been copied...")


for valid_data in valData:
    jpgValid = valid_data
    # print(jpg)
    txtNameValid = jpgValid.split('.jpg')[0]
    # print(txtName)
    txtValid = txtNameValid+'.txt'  ## here you can give any type of extension according to the annotations you have (i.e.,) .xml, .json......
    print('cp "' + jpgValid + '"  "' + outValid + '"')
    print('cp "' + txtValid + '"  "' + outValid + '"')
    os.system('cp "' + jpgValid + '"  "' + outValid + '"')  ## here can use move command 'mv' instead of copy 'cp' when you want to move the data to the directory  if that is necessary
    os.system('cp "' + txtValid + '"  "' + outValid + '"')  ## here can use move command 'mv' instead of copy 'cp' when you want to move the data to the directory  if that is necessary

print("[INFO] The validation dataset has been copied....")

for test_data in testData:
    jpgTest = test_data
    txtNameTest = jpgTest.split('.jpg')[0]
    txtTest = txtNameTest+'.txt'  ## here you can give any type of extension according to the annotations you have (i.e.,) .xml, .json......
    print('cp "' + jpgTest + '"  "' + outTest + '"')
    print('cp "' + txtTest + '"  "' + outTest + '"')
    os.system('cp "' + jpgTest + '"  "' + outTest + '"')  ## here can use move command 'mv' instead of copy 'cp' when you want to move the data to the directory  if that is necessary
    os.system('cp "' + txtTest + '"  "' + outTest + '"')  ## here can use move command 'mv' instead of copy 'cp' when you want to move the data to the directory  if that is necessary

print("[INFO] The test dataset has been copied.... ")
print("[INFO] The Dataset has been created....")

