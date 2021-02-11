import argparse
import math
import cv2 as cv
import numpy as np

src = ["C:/Users/wgalk/OneDrive/KOLOKWIUM 2/input/photo0006.png",
       "C:/Users/wgalk/OneDrive/KOLOKWIUM 2/input/photo0008.png",
       "C:/Users/wgalk/OneDrive/KOLOKWIUM 2/input/photo0009.png"]

img = cv.imread(src[0])


class ScannedImg:
    def __init__(self):
        self.img = None  # image to process
        self.mask = None  # mask with objects

    def set_img(self, img):
        self.img = img

    def get_img(self):
        return self.img

    def find_images(self):
        # FIXME: FIND BEST PARAMETERS
        blur = cv.medianBlur(img, 15)
        gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)

        ddepth = cv.CV_16S
        grad_x = cv.Sobel(gray, ddepth, dx=1, dy=0, ksize=3, borderType=cv.BORDER_DEFAULT)
        grad_y = cv.Sobel(gray, ddepth, dx=0, dy=1, ksize=3, borderType=cv.BORDER_DEFAULT)

        abs_grad_x = cv.convertScaleAbs(grad_x)
        abs_grad_y = cv.convertScaleAbs(grad_y)

        grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

        self.save_img(grad,"xd.jpg")
        self.img_preview(grad)

        # TODO: CREATE CONTOURS FROM EDGES

    def img_preview(self, img):
        # w = img_width * 800 / img_height
        w = int(800 * img.shape[1] / img.shape[0])
        # h = 1280 * img_height / img_width
        h = int(1280 * img.shape[0] / img.shape[1])

        if h <= 800:
            w = 1280
        else:
            h = 800
        ping = cv.resize(img, (h, w))
        cv.imshow("img", ping)
        cv.waitKey()

    def save_img(self, img, name):
        cv.imwrite(name, img)


ob = ScannedImg()
# ob.img_preview(img)
ob.set_img(img)
ob.find_images()
