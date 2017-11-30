import pyaudio
import wave
import os
import shutil

def recordVoiceEnroll(name):
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "./"+name+"/"+name+"1.wav"

	audio = pyaudio.PyAudio()
	print(WAVE_OUTPUT_FILENAME)
	#start recording
	stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
	print "recording..."
	frames = []

	for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
	print "finished recording"

	#stop recording
	stream.stop_stream()
	stream.close()
	audio.terminate()
	
	dir = './'+name
	if os.path.exists(dir):
		shutil.rmtree(dir)
	os.makedirs(dir)
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()

#don't really need this ultimately because eventually will take from LILI instead of microphone
def recordVoicePredict():
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "currentSpeaker.wav"

	audio = pyaudio.PyAudio()

	#start recording
	stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
	print "recording..."
	frames = []

	for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
	print "finished recording"

	#stop recording
	stream.stop_stream()
	stream.close()
	audio.terminate()

	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()

