from PIL import Image, ImageDraw


def pixel_adjust(pixel):

    avg = int((pixel[0]+ pixel[1] + pixel[2])/3)
    return (avg, avg, avg)

def remove_text(pixel):
    if pixel[1] >= 140 and pixel[0] <= 50 and pixel[2] <= 200:
        return (0, 0, 0)
    else: 
        return pixel
    
def rotate180(image, w, h):
    y = Image.new("RGBA", (w,h))
    y2 = ImageDraw.Draw(y)
    for i in range(w):
        for j in range(h):
            y2.point((w-i, h-j), image.getpixel((i,j)) )
    y.save("thing.png")

def rotate90(image, w, h):
    y = Image.new("RGBA", (h,w))
    y2 = ImageDraw.Draw(y)
    for i in range(h):
        for j in range(w):
            y2.point((h-i, w-j), image.getpixel((j,i)))
    y.save("90.png")
    



#def adjust(image, w, h, img):
    #for i in range(w):
        #for j in range(h):
            #img.point((i,j), (remove_text(image.getpixel((i,j)))))
            


def mainr():
    t = input("path")
    t = Image.open(t)
    img = ImageDraw.Draw(t)
    rotate90(t, t.width,t.height)
    t.save("g2.png")




mainr()