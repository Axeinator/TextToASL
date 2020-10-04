import speech_recognition as sr

class speechRecog:
    @classmethod
    def start(cls):
        cls.r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say Something")
            audio = cls.r.listen(source)
            return audio
    @classmethod
    def convert(cls):
        audio = speechRecog.start()
        try:
           return cls.r.recognize_google(audio) # checks if audio is recognizable and returns if it is
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return "Could not request results from Google Speech Recognition service; {0}".format(e)
