import sys
from pydub import AudioSegment
from subprocess import call
import subprocess
import sound_recorder

def enrollSpeaker(playerName):
	#method to run code to enroll a new speaker
	#use existing folder of wav file
	#original cmd line call: ./speaker-recognition.py -t enroll -i "./bob/" -m model.out
	
	audioFolder = "./"+playerName+"/"
	#call method to record the voice
	sound_recorder.recordVoiceEnroll(playerName)
	#convert to mono wav file
	mysound = AudioSegment.from_wav(audioFolder+playerName+"1.wav")
	mysound = mysound.set_channels(1)
	mysound.export(audioFolder+playerName+"1.wav", format="wav")
	print("sound has been recorded")
	
	try:
		valid = subprocess.call(["python speaker-recognition.py -t enroll -i "+ audioFolder +" -m model.out"], shell=True)
		#print(valid)
		if(valid == 0):
			print("The speaker "+playerName+" has been enrolled.")
	except IndexError:
		print("Error enrolling speaker")
	#Valid = 1 : error | Valid = 0 : good
	return valid 
	
def predictSpeaker(audioFile):
	#Method to determine speaker based on wav file
	sound_recorder.recordVoicePredict()
	mysound = AudioSegment.from_wav(audioFile)
	mysound = mysound.set_channels(1)
	mysound.export(audioFile, format="wav")
	try:
		name =subprocess.check_output(["python speaker-recognition.py -t predict -i "+ audioFile +" -m model.out"], shell=True)
		print("The speaker detected is: ")
		splitName = name.split()
		finalName = splitName[len(splitName)-1]
		print(finalName)
	except IndexError:
		print("Error recognizing speaker")

def createCurrentSpeakerFile(playerName):
	#method to run code to enroll a new speaker
	#use existing folder of wav file
	#original cmd line call: ./speaker-recognition.py -t enroll -i "./bob/" -m model.out
	
	#audioFolder = "./"++"/"
	#call method to record the voice
	audioFolder = "./currentSpeaker/"
	sound_recorder.recordVoiceEnroll("currentSpeaker")
	#convert to mono wav file
	mysound = AudioSegment.from_wav(audioFolder+"currentSpeaker1.wav")
	mysound = mysound.set_channels(1)
	mysound.export(audioFolder+ "currentSpeaker1.wav", format="wav")
	print("sound has been recorded")
	
	try:
		valid = subprocess.call(["python speaker-recognition.py -t enroll -i "+ audioFolder +" -m model.out"], shell=True)
		#print(valid)
		if(valid == 0):
			print("The speaker "+playerName+" has been enrolled.")
	except IndexError:
		print("Error enrolling speaker")
	#Valid = 1 : error | Valid = 0 : good
	return valid 
	
def main():
	speakerName = "Kira"
	voiceToPredict = "currentSpeaker.wav"
	enrollSpeaker(speakerName)
	predictSpeaker(voiceToPredict)
	
#main()

