from pydub import AudioSegment
import numpy as np

def tomp3(data,rate):

  audio_segment = AudioSegment(data.tobytes(), frame_rate=rate, sample_width=2, channels=1)
  #louder
  audio_segment  = audio_segment + 10 
  audio_segment.export("test" + ".mp3", format="mp3")



data =np.load('abnormal_X.npy')

data_0 = data[0]

tomp3(data_0[9].astype("int16") , 1000)