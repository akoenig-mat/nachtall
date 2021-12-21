import pandas as pd
import numpy as np

class_df = pd.read_csv('./dataframes/class_df.csv')
class_df = class_df.drop( axis=1 , columns='0' )
#class_df = class_df.rename(columns={'1': 'Class'} )
class_df

sequence = []
classification = []

count = 1
old = ('nocall')
for row in class_df.itertuples(name='Class', index=False):
    if old == row:
        count = count + 1
        if count > 2:
            count = 2           
    else:
        #print(old, count)
        sequence.append(count)
        classification.append(old)
        count = 1
    old = row

sequence.pop(0)
classification.pop(0)
sequence_df = pd.DataFrame(sequence, columns=['Sequence'])
classification_df = pd.DataFrame(classification, columns=['Class'])
sequence_df = pd.concat([classification_df, sequence_df], axis=1, ignore_index=True )
sequence_df.to_csv('./dataframes/sequence_df.csv', index=False)



