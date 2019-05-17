import pandas as pd
import os
from google_drive_downloader import GoogleDriveDownloader as gdd

##save all the individual files in this script directory
#read the script path
path = os.path.dirname(os.path.realpath('__file__'))
path = path.replace("\\","/")

#read all the text file in this folder
arr = []
for file in os.listdir(path):
    if file.endswith(".txt"):
        arr.append(file)

all_files = [f for f in arr]  

li=[]

#append all the files into one single text file
for filename in all_files:
    df = pd.read_csv(filename,  sep = '\t')
    li.append(df)
frame = pd.concat(li, axis=0, ignore_index=True)

#only keep the stock code with digits
frame= frame[~frame['Stock_Code'].str.contains("A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z")]

filter = frame['Stock_Code'].astype(str).str.len() <= 4
frame =frame.loc[filter]

#vlookup the additional information
gdd.download_file_from_google_drive(file_id='1FEDP2c-sCcXu3gj7fF4BVmLSyNvcVZMP',
                                    dest_path='./Segmentation.txt')
segment = pd.read_csv('./Segmentation.txt', sep = '\t', encoding='latin-1')
frame['Stock_Code'] = frame['Stock_Code'].astype(int)
merge = pd.merge(frame, segment, how = 'left', left_on = ['Company', 'Stock_Code'], right_on = ['Company', 'Stock_Code'])

#save the dataset into text file
merge.to_csv('Market_Stock_Data.txt', sep = '\t', index =False)
