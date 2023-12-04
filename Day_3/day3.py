import math

testing = False

if testing:
    data = r'Day_3/ex.txt'
else:
    data = r'Day_3/data.txt'


class Pixel:
    def __init__(self,x,y,value):
        self.location = (x,y)
        self.value = value
        self.gear_ratio = 1

    def isneighbor(self,pixel):
        if math.dist(self.location,pixel.location) > 0 and math.dist(self.location,pixel.location) < 2:
            return True
        return False
    
    def isgear(self,pixels):
        if self.value =='*' and len(determine_partnumber(pixels,self)) == 2:
            return True
        return False
        

def parseData(data):
    pixels = []
    with open(data) as f:
        data = f.read()
        x,y = [0,0]
        for char in data:
            if char == '\n':
                y += 1
                x = 0
            else:
                pixels.append(Pixel(x,y,char))
                x += 1
    return pixels

def look_left(pixels,pixel):
    for left_pixel in pixels:
        if math.dist(left_pixel.location,pixel.location) == 1 and left_pixel.location[0] < pixel.location[0]:
            return left_pixel
    return False

def look_right(pixels,pixel):
    for right_pixel in pixels:
        if math.dist(right_pixel.location,pixel.location) == 1 and right_pixel.location[0] > pixel.location[0]:
            return right_pixel
    return False

def determine_partnumber(pixels,pixel):
    partnumber = pixel.value
    left_pixel = look_left(pixels,pixel)
    right_pixel = look_right(pixels,pixel)
    while left_pixel and left_pixel.value.isdecimal():
        partnumber = left_pixel.value + partnumber
        left_pixel = look_left(pixels,left_pixel)
    while right_pixel and right_pixel.value.isdecimal():
        partnumber += right_pixel.value
        right_pixel = look_right(pixels,right_pixel)
    return partnumber



def day3(data):
    pixels = parseData(data)
    partnumbers = []
    gearratios = []
    for pixel in pixels:
        if not pixel.value.isdecimal() and pixel.value != '.':
            temp_partnumbers = []
            pixel_neighbors = [np for np in pixels if np.isneighbor(pixel)]
            for np in pixel_neighbors:
                if np.value.isdecimal():
                    if int(determine_partnumber(pixels,np)) not in temp_partnumbers:
                        temp_partnumbers.append(int(determine_partnumber(pixels,np)))
            for partnum in temp_partnumbers:
                partnumbers.append(partnum)
            if pixel.value == '*' and len(temp_partnumbers) == 2:
                gearratios.append(math.prod(temp_partnumbers))

    
    print(sum(partnumbers))
    print(sum(gearratios))
                    

day3(data)