import pandas as pd
import numpy as np

class_df = pd.read_csv('/home/dvm/Desktop/dataframes/class_df.csv')
class_df = class_df.drop( axis=1 , columns='0' )
class_df = class_df.rename(columns={'1': 'Class'} )
class_df

count = 1
old = ('nocall')
for row in class_df.itertuples(name='Class', index=False):
    if old == row:
        count = count + 1
        if count > 4:
            count = 4           
    else:
        print(old, count)
        count = 1
    old = row

class_df.to_csv('./sequence.csv', index=False)



