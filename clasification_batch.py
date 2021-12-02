import numpy as np
import pandas as pd
import wave
from scipy.io import wavfile
import os
import librosa
from librosa.feature import melspectrogram
import warnings
from PIL import Image
from uuid import uuid4
import sklearn
from tqdm import tqdm

from tensorflow import keras
from tensorflow.keras.models import Model
birds_to_recognise = ['House Sparrow', 'Common Blackbird', 'Great Tit', 'Common Starling', 'Eurasian Blue Tit', 'Eurasian Tree Sparrow', 'Eurasian Magpie', 'Common Wood Pigeon', 'European Robin', 'Common House Martin', 'Common Swift', 'Carrion Crow', 'Common Chaffinch', 'Eurasian Collared Dove', 'European Goldfinch', 'Great Spotted Woodpecker', 'Barn Swallow', 'Eurasian Jay', 'Rock Dove', 'Eurasian Bullfinch']

classes_to_predict = birds_to_recognise

model = keras.models.load_model("./model/nachtall_final.h5")

def predict_on_melspectrogram(song_sample, sample_length):
    N_mels=216

    if len(song_sample)>=sample_length:
        mel = melspectrogram(song_sample, n_mels=N_mels, sr=22050)
        db = librosa.power_to_db(mel)
        normalised_db = sklearn.preprocessing.minmax_scale(db)
        db_array = (np.asarray(normalised_db)*255).astype(np.uint8)
        prediction = model.predict(np.array([np.array([db_array, db_array, db_array]).T]))
        predicted_bird = classes_to_predict[np.argmax(prediction)]
        if predicted_bird=="Barn Swallow":
            predicted_bird="nocall"
   #     db_image =  Image.fromarray(np.array([db_array, db_array, db_array]).T)
   #     demo_img = db_image
   #     plt.imshow(demo_img)
   #     plt.show()
        return predicted_bird
    else:
        return "nocall"

wav_df = pd.read_csv('./dataframes/wav_dataframe.csv')

classification = []

for index, row in wav_df.iterrows():
    print(row[0])
    chunk_filename = row[0]
    wave_data, wave_rate = librosa.load(chunk_filename, sr=22050)
    sample_length = 5*wave_rate
    song_sample = np.array(wave_data[0:sample_length])
    predicted_bird = predict_on_melspectrogram(song_sample, sample_length)
    classification.append(predicted_bird)
    print(predicted_bird)


classification_df = pd.DataFrame(classification, columns=['Classification'])
class_new = pd.concat([wav_df, classification_df], axis=1, ignore_index=True )
class_new.to_csv('./dataframes/class_df.csv', index=False)





# %% [markdown]
# Below, We can test our prediction function using the examples provided.

