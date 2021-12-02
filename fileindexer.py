import glob
import pandas as pd

files = glob.glob('./recordings/*.*')

folder_index = pd.DataFrame(files, columns=['wav_filename'])
folder_index.to_csv('./dataframes/recordings.csv', index=False)




