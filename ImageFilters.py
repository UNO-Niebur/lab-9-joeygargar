# Lab 9 – Image Processing
# Name: Mia Garcia 
# Date: 4/6/26
# Assignment: Lab 9 

from PIL import Image


def swapGreenBlue(img):
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]
            
            pixels[x, y] = (red, blue, green)

    img.save("swapGB.png")


def darken(img, amount):
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]

            red = max(0, red - amount)
            green = max(0, green - amount)
            blue = max(0, blue - amount)

            pixels[x, y] = (red, green, blue)

    img.save("darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            red, green, blue = pixels[x, y]
            avg = (red + green + blue) // 3
            pixels[x, y] = (avg, avg, avg)

    img.save("bwImg.png")


def main():
    myImg = Image.open("durango.png").convert("RGB")
    #bwFilter(myImg)
    #swapGreenBlue(myImg)
    darken(myImg, 20)

    


if __name__ == "__main__":
    main()





    