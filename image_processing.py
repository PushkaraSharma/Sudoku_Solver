import cv2
import numpy as np
import operator
#extract sudoku from image

def distance(p1, p2):
	x = p2[0] - p1[0]
	y = p2[1] - p1[1]
	return np.sqrt((x ** 2) + (y ** 2))

def preprocess_crop_image():

    image = cv2.imread('1585983417996470071301219931038.jpg')

    grey = cv2.cvtColor(image.copy(),cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(9,9),0)

    thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)

    contours, h = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    fig = contours[0]

    #corners points
    bottom_right, _ = max(enumerate([pt[0][0] + pt[0][1] for pt in fig]), key=operator.itemgetter(1))
    top_left, _ = min(enumerate([pt[0][0] + pt[0][1] for pt in fig]), key=operator.itemgetter(1))
    bottom_left, _ = min(enumerate([pt[0][0] - pt[0][1] for pt in fig]), key=operator.itemgetter(1))
    top_right, _ = max(enumerate([pt[0][0] - pt[0][1] for pt in fig]), key=operator.itemgetter(1))
    crop_rect = [fig[top_left][0], fig[top_right][0], fig[bottom_right][0], fig[bottom_left][0]]

    top_left, top_right, bottom_right, bottom_left = crop_rect[0], crop_rect[1], crop_rect[2], crop_rect[3]
    src = np.array([top_left, top_right, bottom_right, bottom_left], dtype='float32')

    # Get the longest side in the rectangle
    side = max([distance(bottom_right, top_right),
            distance(top_left, bottom_left),
            distance(bottom_right, bottom_left),
            distance(top_left, top_right)
        ])
    dst = np.array([[0, 0], [side - 1, 0], [side - 1, side - 1], [0, side - 1]], dtype='float32')
    m = cv2.getPerspectiveTransform(src, dst)

    # Performs the transformation on the original image
    cropped_image =  cv2.warpPerspective(image, m, (int(side), int(side)))

    while True:
     cv2.imshow('1',image)
     cv2.imshow('2',thresh)
     cv2.imshow('3',cropped_image)
     if cv2.waitKey(1)==27:
          break
preprocess_crop_image()