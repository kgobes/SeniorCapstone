#!/usr/bin/env python
import wave
import speech_recognition as sr
from Queue import Queue
import lili_audio.srv
import lili_audio.msg
import audio_common_msgs.msg
import rospy
import sys
sys.path.insert(0,'/home/christie/catkin_ws/src/lili_storytelling/src') #ADD path to test speaker recog
import testSpeakerRecog
import scipy.io.wavfile
import sound_recorder
import text_to_speech


class ROSAudioStream(object):
    def __init__(self):
        # queue is thread-safe, so it can safely pass messages to the speech
        # recognition library
        self.queue = Queue()

    # transfer from ROS audio topic to queue
    def audio_subscription(self, data):
        for elem in data.data:
            self.queue.put(elem)

    # transfer from queue to speech recognition library
    def read(self, size):
        output = b''
        for i in range(size):
            output += self.queue.get()
        return output

class ROSAudioSource(sr.AudioSource):
    def __init__(self, topic_name, chunk, depth, sample_rate):
        self.topic_name = topic_name
        self.CHUNK = chunk
        self.SAMPLE_RATE = sample_rate
        self.SAMPLE_WIDTH = depth
        self.stream = None
        self.sub = None

    def __enter__(self):
        assert self.stream is None, "This audio source is already inside a context manager"

        self.stream = ROSAudioStream()
        # the audio source only subscribes to audio topic when it is in context
        self.sub = rospy.Subscriber(self.topic_name,
            audio_common_msgs.msg.AudioData, self.stream.audio_subscription)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.sub.unregister()
        self.sub = None
        self.stream = None

def recognize_speech_handler(req):
    targetStrings = None
    text = None

    recog = sr.Recognizer()
    recog.pause_threshold = 1

    chunk = rospy.get_param('~chunk', 1024)
    depth = rospy.get_param('~depth', 2)
    sample_rate = rospy.get_param('~sample_rate', 16000)
  #  ros_source = ROSAudioSource('audio', chunk, depth, sample_rate)
    sound_recorder.recordCurrentVoice()
    print("done recording the current speaker")
    while text == None:
        # use ROS audio topic as the audio source
      	with sr.WavFile('enrolledSpeakers/currentSpeaker.wav') as source:
	 # with ros_source as source:
            recog.energy_threshold = 2200
            recog.adjust_for_ambient_noise(source, duration = 0.5)
            #rospy.loginfo("Listening...")
            # listen for the first phrase and extract it into audio dataprint "heard"
            audio = recog.record(source)
	    global name
	    name =testSpeakerRecog.predictSpeaker('./enrolledSpeakers/currentSpeaker.wav')

		#audio = recog.listen(source)
#      	    voice1 = wave.open("voiceWavFile.wav",'w')
	    #scipy.io.wavfile.write("voiceWavFile.wav", sample_rate, audio)
	    print('voice recognize, identifying speaker...')
	    #testSpeakerRecog.createCurrentSpeakerFile("uselessname")
	    #sound_recorder.recordVoicePredict()
	    #testSpeakerRecog.predictSpeaker("./currentSpeaker1.wav")
	try:
            all_list = recog.recognize_google_cloud(audio, preferred_phrases=targetStrings)
            text = str(all_list)
            # recognize speech using Google Speech Recognition
        except sr.UnknownValueError: # speech is unintelligible
            rospy.loginfo("could not understand; retrying")
            text = None
    rospy.loginfo("response: " + str(text))
    return lili_audio.srv.RecognizeSpeechResponse(str(text))

def speech_recog_server():
    rospy.init_node('speech_recognition')
    s = rospy.Service('recognize_speech', lili_audio.srv.RecognizeSpeech, recognize_speech_handler)
    rospy.spin()


if __name__ == "__main__":
    speech_recog_server()
