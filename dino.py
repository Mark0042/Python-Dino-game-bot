import pyautogui as pyg
import cv2
from PIL import Image, ImageGrab
import numpy as np
import time


def takeScreenshot():
    image = pyg.screenshot()
    image2=image.convert('L')
    return image2


def hit(key):
    pyg.press(key)
    return


def iscolliding(data):
    for i in range(400, 500):
        for j in range(450, 480):
            if data[i,j]<100:
                hit('up')
                return
    for i in range(370, 400):
       for j in range(390, 400):
           if data[i,j]<100:
               hit('down')
               return
    return




def draw():
    image = takeScreenshot()
    data = image.load()
    for i in range(400, 450):
        for j in range(450,480):
            data[i, j] = 0
    for i in range(370, 400):
        for j in range(390,400):
            data[i, j] = 171
    image.show()


if __name__ == "__main__":
    time.sleep(3)
    draw()
    hit('up')
    while True:
          image = takeScreenshot()
          data = image.load()
          iscolliding(data)
