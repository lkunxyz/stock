import tushare as ts
import pandas as pd
import sys, math;
reload(sys);
sys.setdefaultencoding('utf-8') 

#df = ts.get_index()
#df = ts.get_hist_data('000001')

keys = ''
values = ''
df = ts.get_stock_basics()
for idx,row in df.head(1).iterrows():
    s = dict(row)
    for k,v in s.items():
        if keys != '':
            keys += ','
        keys += k
        if values != '':
            values += ','
        
        if isinstance(v, str):
            print 'aaaa'
            values += ("'" + v + "'")
        else:
            values += str(v)
    sql = "insert into t_stock_code(%s) values (%s)" %(keys, values)
    print sql


