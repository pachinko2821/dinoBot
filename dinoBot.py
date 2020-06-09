import pyautogui
import time
import numpy as np
from PIL import ImageOps


def start(): # starts game by pressing space
    pyautogui.keyDown("space")
    pyautogui.keyUp("space")

def jump(): # instructs dino to jump
    pyautogui.keyDown("space")
    time.sleep(0.05) #wait for 0.05 seconds
    pyautogui.keyUp("space")
    print("Jump!")

def imageGrab(x, y): # detects obstacles 
    checkBox = pyautogui.screenshot(region=(x+90, y, 300, 2)) #screenshot small rectangular box infront of dino, length 300px, height 2pixel 
    checkBox = ImageOps.grayscale(checkBox) #convert screenshot to grayscale
    pixel_array = np.array(checkBox.getcolors()) #get list of colors in the image
    #print(pixel_array.sum())
    return pixel_array.sum() #return the calculated sum. sum changes if an obstacle is detected, since colors in the screenshot change


time.sleep(5) #wait for 5 seconds
dino_x, dino_y = pyautogui.locateCenterOnScreen("/home/pachinko/Desktop/dino.png") #locate dino on the screen and get its coordinates
start()  #start the game
checksum = imageGrab(dino_x, dino_y) #get initial pixel sum for comparison
while True:
   if imageGrab(dino_x, dino_y) != checksum: #compare updated checksum with initial checksum
       jump() #if checksum changes then jump