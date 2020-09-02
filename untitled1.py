

import cv2
import numpy as np
from keras.models import load_model
import algo as Algo
import math
import os
import shutil


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
    add = myPoints.sum(1)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew

new_model = load_model('digit_recognisor.h5')
try:
    os.mkdir('final_grid')
except:
    shutil.rmtree('final_grid')
    os.mkdir('final_grid')


img_original = cv2.imread("sudoku_1.jpg")
try:
    gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)

    ########################################################################
    # bilateral is when we have to blur the image without bluring threshold
    bilateral_filter = cv2.bilateralFilter(gray, 5, 40, 40)
    adaptive_threshold_bi = cv2.adaptiveThreshold(bilateral_filter, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                  cv2.THRESH_BINARY, 11, 3)

    ########################################################################
    img_contours = img_original.copy()
    contours, hierarchy = cv2.findContours(adaptive_threshold_bi, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

    # Finding biggest one
    area = []
    MAX = 0
    second_max = 0
    cntt = []
    height, width = img_contours.shape[:2]

    for cnt in contours:
        curr_area = int(cv2.contourArea(cnt))
        area.append(curr_area)
        if curr_area > MAX and curr_area < ((height - 20) * (width - 20)):
            MAX = curr_area
            cntt = cnt
    peri = cv2.arcLength(cntt, True)
    approx = cv2.approxPolyDP(cntt, 0.02 * peri, True)


    ##########################----------------------------
    #Detect Square
    detect_guide = True
    if detect_guide :
        # joining points

        #x1,y1 x2,y2
        x1 = int(approx[0][0][0]);x2 = approx[1][0][0];y1= approx[0][0][1];y2=approx[1][0][1]
        len1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        x1=approx[0][0][0]; y1=approx[0][0][1]; x2=approx[3][0][0]; y2=approx[3][0][1]
        len2 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        x1 = approx[3][0][0]; y1 = approx[3][0][1];x2 = approx[2][0][0];y2 =  approx[2][0][1]
        len3 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        x1 = approx[1][0][0]; y1 = approx[1][0][1];x2 = approx[2][0][0];y2 =  approx[2][0][1]
        len4 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(len1,len2,len3,len4)
        if (max([len1, len2, len3, len4]) - min([len1, len2, len3, len4])) <= 30 and min([len1, len2, len3, len4])>100:
            cv2.line(img_original, (approx[0][0][0], approx[0][0][1]), (approx[1][0][0], approx[1][0][1]),(0, 255, 0), 2)
            cv2.line(img_original, (approx[0][0][0], approx[0][0][1]), (approx[3][0][0], approx[3][0][1]),(0, 255, 0), 2)
            cv2.line(img_original, (approx[3][0][0], approx[3][0][1]), (approx[2][0][0], approx[2][0][1]),(0, 255, 0), 2)
            cv2.line(img_original, (approx[1][0][0], approx[1][0][1]), (approx[2][0][0], approx[2][0][1]),(0, 255, 0), 2)
            # ploting dots on contour
            cv2.drawContours(img_original, approx, -1, (0, 0, 255), 8)
            print('Detected')
    ##########################----------------------------

        cv2.imshow('image_biggest', img_original)  #capture pic at this time
        approx = reorder(approx)
        pts1 = np.float32(approx)
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        img_wrap = cv2.warpPerspective(adaptive_threshold_bi, matrix, (width, height))
        maX = height if (height > width) else width
        img_wrap = cv2.resize(img_wrap, (maX, maX), interpolation=cv2.INTER_AREA)
        size = maX//9
        cv2.imwrite('final_grid/A_sudoku.jpeg', img_wrap)  # wrap image

        path = []
        x1 = 0;y1 = 0
        for i in range(9):  #saving in to folder
            x1 = 0
            for j in range(9):
                temp = img_wrap[x1:x1 + size, y1:y1 + size]
                temp = cv2.resize(temp, (32, 32), interpolation=cv2.INTER_AREA)
                temp = temp[4:-4, 4:-4]
                temp = cv2.resize(temp, (32, 32), interpolation=cv2.INTER_AREA)
                x1 += size
                name = 'temp_' + str(j) + str(i) + '.jpeg'
                cv2.imwrite('final_grid/' + name, temp)

            y1 += size
            
except:
    pass



def predict_grid():   #ANN
    img_arr = [([0] * 9) for _ in range(9)]
    for i in range(9):
        for j in range(9):
            name = 'final_grid/temp_' + str(i) + str(j) + '.jpeg'
            img=cv2.imread(name,1)

            img = cv2.resize(img, (32, 32))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = img / 255
            img = img.reshape(1, 32, 32, 1)
            classIndex = int(new_model.predict_classes(img))
            predictions = new_model.predict(img)
            probVal = np.amax(predictions)
            if probVal > 0.95:
                print(f'{name} -> {classIndex} | {(probVal * 100)}%')  # detect no with accuracy
                img_arr[i][j] = classIndex
            else:
                print(f'{name} -> {0} | {(probVal * 100)}%')  # detect no with accuracy
                img_arr[i][j] = 0
    return img_arr


board = predict_grid()
Algo.print_board(board)

######################################################################
#solve with backtrack
if Algo.solve(board) :
    print('#'*34+'\nSolved ans is : ')
    Algo.print_board(board)
else:
    print("Detection Error!")

