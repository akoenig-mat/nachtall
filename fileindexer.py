import glob
import pandas as pd

files = glob.glob('./recordings/*.*')

folder_index = pd.DataFrame(files)
folder_index.to_csv('./dataframes/recordings.csv')

folder_index


