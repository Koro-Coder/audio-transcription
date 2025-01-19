from utils import speech_to_text
from utils import record_audio
from utils import text_to_speech

################# Record Audio and saves in my_recording.wav ######################
########### To stop recording interupt session - press Ctrl + C ###################
# record_audio()



################## Convert my_recording.wav to Text ##############################
# text = speech_to_text()
# print(text)


################# Convert Text to Audio ##########################################
text_to_speech('Hi How are you?')