from PIL import Image, ImageDraw
import random


def thing():
    rando = random.randint(1,255)
    rando2 = random.randint(1,255)
    rando3 = random.randint(1,255)
    rando4 = 255
    return rando,rando2,rando3,rando4
def imager(name):
    w = 1920
    h = 1080
    img = Image.new("RGBA", (w, h))
    img2 = ImageDraw.Draw(img)
    for i in range(w):
        for j in range(h):
            img2.point((i,j), thing())
    img.save(f"image\\{name}")
for i in range(500):
    imager(f"{i}.png")



