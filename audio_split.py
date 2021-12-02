
from pydub import AudioSegment
from pydub.utils import make_chunks
from uuid import uuid1
import pandas as pd

def wav_split(rec_filename, chunk_length_ms):
    audiofile = AudioSegment.from_wav(rec_filename , "wav")
    chunks = make_chunks(audiofile, chunk_length_ms)
    for i, chunk in enumerate(chunks):
        chunk_filename = rec_filename.replace('.wav', '')
        chunk_name = chunk_filename +"_N{0}.wav".format(i)
        print ("exporting", chunk_name)         
        chunk.export(chunk_name, format="wav")
        wav_files.append(chunk_name)

recordings = pd.read_csv('./dataframes/recordings.csv')
wav_files = []

for index, row in recordings.iterrows():
    print(row[1])
    rec_filename = row[1]
    chunk_length_ms = 5000 
    wav_split(rec_filename , chunk_length_ms)

wav_dataframe = pd.DataFrame(wav_files, columns=['wav_chunks_filename'])
wav_dataframe.to_csv('./dataframes/wav_dataframe.csv', index=False)


