from PIL import Image, ImageDraw

def blurhelper(image, pixel):
    
def blur(image, w, h):
    newimg = Image.new("RGBA", (w,h))
    newimg2 = Image.Draw(newimg)
    for i in (w):
        for j in range(h):

            newimg2.point()

def main():
    path = input("Path:     ")
    path = Image.open(path)
    img = ImageDraw.Draw(path)
    blur(img,path.width, path.height)
