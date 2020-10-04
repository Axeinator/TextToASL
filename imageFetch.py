from PIL import Image

class SLPic:
    def __init__(self, letters):
        self.letters = letters
    def display(self):
        finImg = Image.new('RGB', (512, 512))
        imageList = []
        openedImages = []
        for char in self.letters:
            if char  == " ":
                char = "space"
            imageList.append((r"./png/{}.png").format(char.lower()))
        for x in imageList:
            openedImages.append(Image.open(x))
        finImg.save("out.gif", save_all=True, append_images=openedImages, duration=1000, loop=0)





test = SLPic("this is a test")

print(test.display())
