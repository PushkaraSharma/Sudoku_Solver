import cv2
import numpy as np
import operator
from keras.models import  load_model


def distance(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    return np.sqrt((x ** 2) + (y ** 2))


def preprocess_crop_image(path):
    image1 = cv2.imread(path)
    grey = cv2.cvtColor(image1.copy(), cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (9, 9), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

    contours, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    fig = contours[0]

    # corners points
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
    cropped_image = cv2.warpPerspective(image1, m, (int(side), int(side)))
    return cropped_image


def classify_image(image):
    model = load_model('model_for_digits.h5')
    model.compile(loss='binary_crossentropy',metrics=['accuracy'],optimizer='adam')
   # print(image.shape)
    image = cv2.resize(image,(28,28))
    #print(image.shape)
    image = image.reshape(1,28,28,1)
    #print(image.shape)
    pred = model.predict_classes(image)
    print(pred[0])
    return pred[0]


def grid_to_metrix(path_of_image):
    crop_image = preprocess_crop_image(path_of_image)

    image_resized = cv2.resize(crop_image, (450, 450))
    grid = np.zeros([9, 9])
    for i in range(9):
        for j in range(9):
            digit_image = image_resized[i * 50:(i + 1) * 50,
                          j * 50:(j + 1) * 50]  # size of image is 450 ie each cell is 50
            print(digit_image.sum())
            grey = cv2.cvtColor(digit_image, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(grey, (11, 11), 0)
            digit_image = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)

            digit_image = digit_image[8:46,10:45]
            wh = np.sum(digit_image==255)
            while True:
                cv2.imshow('1',digit_image)
                if(cv2.waitKey(1)==27):
                    break

            if wh > 20:
                grid[i][j] = classify_image(digit_image)
            else:
                grid[i][j] = 0

    grid = grid.astype(int)
    return  grid

grid = grid_to_metrix('sudoku_1.jpg')

print(grid)