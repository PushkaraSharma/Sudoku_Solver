import cv2
import numpy as np
import operator
from keras.models import  load_model
import algo 

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
    model = load_model('digit_recognisor.h5')
    model.compile(loss='binary_crossentropy',metrics=['accuracy'],optimizer='adam')
    img = cv2.resize(image, (32, 32))
    img = img / 255
    image = img.reshape(1, 32, 32, 1)
    classInx = int(model.predict_classes(image))
    pred = model.predict(image)
    probVal = np.amax(pred)
    if(probVal>0.86):
        pred1 = classInx
        #print(probVal)
    else:
        pred1 = 0
        #print(probVal)
    return pred1


def grid_to_metrix(path_of_image):
    crop_image = preprocess_crop_image(path_of_image)

    image_resized = cv2.resize(crop_image, (450, 450))
    image_resized = cv2.fastNlMeansDenoisingColored(image_resized,None,10,10,7,21)
    grid = np.zeros([9, 9])
    for i in range(9):
        for j in range(9):
            digit_image = image_resized[i * 50:(i + 1) * 50,
                          j * 50:(j + 1) * 50]
            digit_image = digit_image[8:46,10:45]  # size of image is 450 ie each cell is 50
            temp = cv2.resize(digit_image, (32, 32), interpolation=cv2.INTER_AREA)
            temp = temp[4:-4, 4:-4]
            temp = cv2.resize(temp, (32, 32), interpolation=cv2.INTER_AREA)
            grey1 = cv2.cvtColor(digit_image, cv2.COLOR_BGR2GRAY)
            temp_for_null = cv2.GaussianBlur(grey1, (21, 21), 0)
            temp_for_null = cv2.adaptiveThreshold(grey1, 255, 1, 1, 11, 2)
            
            # while True:
            #     cv2.imshow('1',temp_for_null)
            #     if(cv2.waitKey(1)==27):
            #         break
            wh = np.sum(temp_for_null==255)
            print(wh)
            if wh>100:
                grid[i][j] = classify_image(grey1)
            else:
                grid[i][j] = 0

            

    grid = grid.astype(int)
    return  grid

#grid = grid_to_metrix('1585983417996470071301219931038.jpg')

#print(grid)
# if algo.solve(grid) :
#     print('#'*34+'\nSolved ans is : ')
#     algo.print_board(grid)
# else:
#     print("Detection Error!")
