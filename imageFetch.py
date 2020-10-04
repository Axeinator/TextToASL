from PIL import Image

class SLPic:
    def __init__(self, letters):
        self.letters = letters
    def display(self):
        finImg = Image.new('RGB', (512, 512))
        imageList = []
        openedImages = []
        curChar = 0
        for char in self.letters:
            if char  == " ":
                char = "space"
            if char == self.letters[curChar - 1] and curChar != 0:
                imageList.append(r"./png/doubleLetter.png")
            imageList.append((r"./png/{}.png").format(char.lower()))
            curChar += 1
        for x in imageList:
            openedImages.append(Image.open(x))
        finImg.save("out.gif", save_all=True, append_images=openedImages, duration=1000, loop=0)





test = SLPic("aaa")

test.display()
