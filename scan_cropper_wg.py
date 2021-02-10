import argparse
import math
import cv2 as cv

src = ["C:/Users/wgalk/OneDrive/KOLOKWIUM 2/input/photo0006.png",
       "C:/Users/wgalk/OneDrive/KOLOKWIUM 2/input/photo0008.png",
       "C:/Users/wgalk/OneDrive/KOLOKWIUM 2/input/photo0009.png"]

img = cv.imread(src[0])


class ScannedImg:
    def __init__(self):
        self.img = None  # image to process
        self.mask = None  # mask with objects

    # !!!!! sprawdzić czy jeśli wgramy zdjecie to po wywolaniu funkcji nie zmieni ona jego rozmiarów
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


ob = ScannedImg()
ob.img_preview(img)
