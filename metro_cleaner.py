import time
import pandas as pd
import os
import sqlalchemy



os.chdir('/home/edeo/metro_csv/csvdump/output')

df1 = pd.DataFrame.from_csv('file_Mon May 30 19:11:41 2016_done.csv')

df1.drop(df1.columns[[0]], axis=1, inplace=True)

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
df.to_sql('max', engine, if_exists='append',index=False)
df.to_sql('mean', engine, if_exists='append',index=False)

'''
max.to_csv('hello.csv')
mean.to_csv('meaner.csv')

con = sqlite3.connect('max.db')
pd.io.sql.write_frame(max, "max", con)
pd.io.sql.write_frame(mean, "mean", con)
'''

