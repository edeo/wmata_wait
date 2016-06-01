import os
import time
import pandas as pd
import shutil



os.chdir('/home/edeo/metro_csv/csvdump/input/')
dir = os.listdir('/home/edeo/metro_csv/csvdump/input/')
os.chdir(dir[0])
thedir = os.getcwd()
allFiles = os.listdir(thedir)



frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
    print(df)

frame = pd.concat(list_)
frame.to_csv('/home/edeo/metro_csv/csvdump/output/file_'+str(time.asctime( time.localtime(time.time())))+'_done.csv')


filelist = os.listdir()
for f in filelist:
    os.remove(f)

os.chdir('/home/edeo/metro_csv/csvdump/input/')
thedir = os.getcwd()
dirlist = os.listdir(thedir)
shutil.rmtree(dirlist[0])

import time
import pandas as pd
import os
import sqlalchemy




result = df1.sort(['LocationCode', 'Line','Group','time'])

data = result.values.tolist()

for i in range(len(data)):
    item = data[i]
    before = i-1
    prior = data[before]
    data[i].append(item[8]==prior[8])



df = pd.DataFrame(data)

names = ['Car','Destination','DestinationCode','DestinationName','Group','Line','LocationCode','LocationName','Min','time','Before']

df.columns = names


arrival = df[(df['Before'] ==False) &(df['Min'] =='BRD')]
brdlist = arrival.values.tolist()
for i in range(len(brdlist)):
    item = brdlist[i]
    before = i-1
    prior = brdlist[before]
    brdlist[i].append(item[9]-prior[9])

brddf =  pd.DataFrame(brdlist)

brdnames = ['Car','Destination','DestinationCode','DestinationName','Group','Line','LocationCode','LocationName','Min','time','Before','wait']
brddf.columns = brdnames

nonzero = brddf[(brddf['wait']>0 )]



df = nonzero

mean = pd.DataFrame({'mean' :df['wait'].groupby([df['LocationName'], df['Line'], df['Group']]).mean()}).reset_index()
max = pd.DataFrame({'max' :df['wait'].groupby([df['LocationName'], df['Line'], df['Group']]).max()}).reset_index()


max['Date']  = time.strftime("%m/%d/%Y", time.localtime(time.time()))
mean['Date'] = time.strftime("%m/%d/%Y", time.localtime(time.time()))

engine = sqlalchemy.create_engine('sqlite:///max.db')
max.to_sql('max', engine, if_exists='append',index=False)
mean.to_sql('mean', engine, if_exists='append',index=False)




