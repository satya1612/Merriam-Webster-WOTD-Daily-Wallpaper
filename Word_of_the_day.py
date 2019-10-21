import requests
from   bs4 import BeautifulSoup #Scrapping
from PIL import Image, ImageDraw, ImageFont #Drawing over Image Libs

url  = 'http://www.merriam-webster.com/word-of-the-day' #URL...duh
r    = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})

soup = BeautifulSoup(r.content, 'html5lib')
word = soup.h1.text
print(word)
print(type(word))
image = Image.open('C:/Users/admin/Documents/Word_Wallpaper/Background.jpg') #Open Background Image...basically your canvas  Photo by Kelly Sikkema on Unsplash
# initialise the drawing context with
# the image object as background
draw = ImageDraw.Draw(image) 
Word_font = ImageFont.truetype('C:/Users/admin/Documents/Word_Wallpaper/PlayfairDisplay-Black.ttf', size=400)
(x, y) = (500, 500)
#message = "Happy Birthday!"
color = 'rgb(255, 255, 255)' # White

# draw the message on the background
Word_Day = word.encode('utf-8') 
draw.text((x, y), Word_Day, fill=color, font=Word_font)
#Word_Written

x=x+10
y=y+500
meaning_font = ImageFont.truetype('C:/Users/admin/Documents/Word_Wallpaper/SpecialElite-Regular.ttf', size=100)
tag  = soup.h2.find_next_sibling()
while tag.name == 'p':
    print(tag.text)
    meaning = tag.text.encode('utf-8')
    print(len(meaning))
    y=y+100
    draw.text((x, y), meaning, fill=color, font=meaning_font)
    tag = tag.find_next_sibling()

# save the edited image
 
image.save('C:/Users/admin/Documents/Word_Wallpaper/Stage1.png')


####################ADD NOISE####################
import numpy as np
import random
import cv2

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

image = cv2.imread('C:/Users/admin/Documents/Word_Wallpaper/Stage1.png',0) # Only for grayscale image
noise_img = sp_noise(image,0.01)
cv2.imwrite('C:/Users/admin/Documents/Word_Wallpaper/Final.png', noise_img)
####################WINDOWS DESKTOP CHANGE####################
#import ctypes
#ctypes.windll.user32.SystemParametersInfoW(20, 0, "Final.png" , 0)
####################WINDOWS DESKTOP CHANGE####################
#import os User=str(os.getenv('USERPROFILE')) os.system(r'''reg add "hkcu\Control panel\desktop" /v wallpaper /d "'''+ User+r'\Local Settings\Application Data\Microsoft\Wallpaper1.bmp" /f') os.system(r'''reg add "hkcu\Control panel\desktop" /v WallpaperStyle /d 2 /f''') os.system(r'''RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True''') 
import ctypes
filename = r"C:\Users\admin\Documents\Word_Wallpaper\Final.png"
ctypes.windll.user32.SystemParametersInfoA(20, 0, filename, 2)