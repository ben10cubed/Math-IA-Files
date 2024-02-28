import pandas as pd
import os
import glob

import re
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

# Step 1: get a list of all csv files in target directory
my_dir = os.getcwd()
filelist = []
filesList = []
print(os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Step 2: Build up list of files:
for files in sorted(glob.glob("*.txt"), key=numericalSort):
    fileName, fileExtension = os.path.splitext(files)
    print(fileName)
    filelist.append(fileName) #filename without extension
    filesList.append(files) #filename with extension

# Step 3: Build up DataFrame:
df = pd.concat([pd.read_csv(item, names=[item[:-4]]) for item in filesList], axis=1)
df.to_excel("output.xlsx",
             sheet_name='Sheet_name_1')