import threading
import time
import requests
import pandas as pd
import os
os.chdir("metro_csv/csvdump/input")
x = str(time.asctime(time.localtime(time.time())))
os.makedirs(x)
os.chdir(x)


def do_every (interval, worker_func, iterations):
  if iterations != 1:
    threading.Timer (
      interval,
      do_every, [interval, worker_func, 0 if iterations == 0 else iterations-1]
    ).start ()
    worker_func ()


def metroreport():
    y = requests.get("https://api.wmata.com/StationPrediction.svc/json/GetPrediction/ALL?api_key=bce6ec600e2342f28bc7751435ac0f52" )
    z=y.json()
    t = pd.DataFrame.from_dict(z['Trains'])
    t['time'] = time.time()
    sts = t[(t['Min'] == 'BRD')|(t['Min'] == 'ARR')]
    sts.to_csv(str(time.time())+'sts.csv')
    print(sts)

do_every(2 , metroreport, 1800)

