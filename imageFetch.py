from PIL import Image
import speech_recognition
import webbrowser
import os
from speechRecog import speechRecog
import speech_recognition
class SLPic:
    def __init__(self, letters):
        self.letters = letters
        
    @classmethod
    def speechSL(cls):
        speech = speechRecog.convert()
        if "not understand" in speech:
            raise ValueError("We could not understand what you said. Please try again.")
        if "not request" in speech:
            raise Exception("Google Speech Recognition was unable to connect. Please try again.")
        return speech

    def display(self):
        finImg = Image.new('RGB', (512, 512)) # creates a new image for the gif to save to
        imageList = [] # the list of all images
        openedImages = [] # the list of PIL.Image objects
        curChar = 0
        for char in self.letters:
            if char  == " ":
                char = "space" # space is a black image
            if char.lower() == self.letters[curChar - 1].lower() and curChar != 0:
                imageList.append(r"./png/doubleLetter.png") # double letters like aa or Tt are spaced with a dakr green image
            imageList.append((r"./png/{}.png").format(char.lower()))
            curChar += 1
            if curChar == len(self.letters):
                imageList.append(r"./png/done.png") # at the end of the phrase, a red image is shown
        for x in imageList:
            openedImages.append(Image.open(x)) # makes the images PIL.image objects
        finImg.save("out.gif", save_all=True, append_images=openedImages, duration=600, loop=0)
        webbrowser.open("file:///" + os.path.realpath("out.gif")) # opens the gif in the browser
        print(imageList) # letters for debugging

text = SLPic(SLPic.speechSL())
text.display()
