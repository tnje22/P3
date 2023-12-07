import cv2 as cv
import numpy as np


def get_contour_of_board(img): #Finds contour for the green board, with all the pixel values
    green_max = np.array([191, 255, 140]);green_min = np.array([82, 119, 0])

    threshold = cv.inRange(img, green_min, green_max)
    #cv.imshow('frame', threshold);cv.waitKey()
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv.erode(threshold, kernel, iterations=3)
    dilation = cv.dilate(erosion, kernel, iterations=3)
    edges = cv.Canny(dilation, 50, 200)
    #cv.imshow('frame', edges);cv.waitKey()
    contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    return contours, hierarchy

def partition(height,witdth,img): # Makes multidimentional array for the board
    xpix=img.shape[0]
    ypix=img.shape[1]

    xstep=float(xpix)/float(witdth)
    ystep=float(ypix)/float(height)

    output=[]

    for x in range(witdth):
        row=[]
        for y in range(height):
            row.append(img[int(x*xstep):int((x+1)*xstep),int(y*ystep):int((y+1)*ystep)])
        output.append(row)
    return output

def iscol(min_thres,max_thres,avg):
    ret=False
    icount=0
    for x in range(len(avg)):
        if (avg[x]<max_thres[x] and avg[x]>min_thres[x]):
            icount+=1
    return icount==len(avg)

def findid(theshlist_max,threshlist_min,avg):
    for x in range(len(theshlist_max)):
        if(iscol(threshlist_min[x],theshlist_max[x],avg)):
            return x
    return 0

def board_brick_recognition(img):
    #print(img.shape)
    blur = cv.bilateralFilter(img, 9, 75, 75)
    #cv.imshow('frame', blur);cv.waitKey()
    contours, hierarchy=get_contour_of_board(blur)
    count = 0

    for con in range(len(contours)):
        cnt = contours[con]
        perimeter = cv.arcLength(cnt, True)
        #print(perimeter)

        if 1300>perimeter>950:
            (x, y), (MA, ma), angle = cv.fitEllipse(cnt)
            #print(angle)
            rect = cv.minAreaRect(cnt)
            boxpoints = cv.boxPoints(rect)
            #print(boxpoints)
            count = 1

            # Finds two opposite corner points, the one with the biggest and smallest values
            for i in range(len(boxpoints)):
                for j in range(len(boxpoints)):
                    if boxpoints[i][0]<boxpoints[j][0] and boxpoints[i][1]<boxpoints[j][1]: #Finds the point with the smallest values
                        minx = boxpoints[i][0] + 22
                        miny = boxpoints[i][1] + 22
                    if boxpoints[i][0]>boxpoints[j][0] and boxpoints[i][1]>boxpoints[j][1]: #Finds the point with the biggest values
                        maxx = boxpoints[i][0] - 21
                        maxy = boxpoints[i][1] - 21
            break
    #print(count)
    if count == 0:
        #print('No pile, something is in the way!')
        return
    resize = img[int(miny):int(maxy), int(minx):int(maxx)]
    board = partition(20, 20, resize)
    #cv.imshow('frame', resize);cv.waitKey()

    boardcolors = []
    #Finds average color for each cell on the board
    for x in range(len(board[0])):
        row=[]
        for y in range(len(board)):
            image = board[x][y]
            average = np.average(image, axis = (0,1))
            #print(average)

            blue_max = np.array([255, 215, 142]);red_max = np.array([195, 190, 255]);yellow_max = np.array([230, 255, 255]);green_max = np.array([191, 255, 140])
            blue_min = np.array([171, 90, 38]);red_min = np.array([55, 70, 190]);yellow_min = np.array([106, 220, 211]);green_min = np.array([82, 119, 0])

            threshlist_max = (green_max,blue_max,red_max,yellow_max)
            threshlist_min = (green_min,blue_min, red_min, yellow_min)

            ids=findid(threshlist_max, threshlist_min, average) #Thresholds the average to figure out if they are brick or board
            #print(ids)
            row.append(ids)
        boardcolors.append(row)
    # The schematic has the zero point at the left bottom corner, where open cv has it at the upper left, so we flip the array.
    boardcolors=np.flip(boardcolors,0)
    returnboard=[]
    for x in boardcolors:
        returnboard.extend(x)
    #print(boardcolors)
    #print(returnboard)

#Resizes window to make it easier to see images when using imshow.
#cv.namedWindow('frame', cv.WINDOW_NORMAL)
#cv.resizeWindow('frame', 600, 400)

img = cv.imread('pic 9_35.png', cv.IMREAD_UNCHANGED)
#cv.imshow('frame',img);cv.waitKey()
bricks = board_brick_recognition(img)



