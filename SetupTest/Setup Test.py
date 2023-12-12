import numpy as np
import cv2 as cv

#Creates a mask that removes everything, but the area marked of for the pile of lego bricks.
def find_pile(img):
    cache = img.copy()
    blur = cv.bilateralFilter(img, 9, 75, 75)
    #cv.imshow('frame', hsv);cv.waitKey()

    white_max = np.array([255, 255, 255]);white_min = np.array([205, 205, 205])

    threshold = cv.inRange(blur, white_min, white_max)
    #cv.imshow('frame', threshold);cv.waitKey()
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv.erode(threshold, kernel, iterations=3)
    dilation = cv.dilate(erosion, kernel, iterations=3)
    edges = cv.Canny(dilation, 50, 200)
    #cv.imshow('frame', edges);cv.waitKey()
    contours, hierarchy = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # print(len(contours))
    count = 0


    for con in range(len(contours)):
        cnt = contours[con]
        perimeter = cv.arcLength(cnt, True)
        #print(perimeter)

        if len(contours[con]) > 5: # only for testing since real program will have mask
            (x, y), (major, minor), angle = cv.fitEllipse(cnt)
        if 2100>perimeter>1800 and 620>major>580 and 710>minor>680: #Checks all contours to find the one that corresponds to the tape, that marks the pile area.
            rect = cv.minAreaRect(cnt) # Makes a rectangle that contains all the other most points of the contour, the minimum area rectangle.
            box = cv.boxPoints(rect) # Finds corner points of rectangle.
            box = np.int0(box)
            ed = cv.drawContours(img, [box], 0, (0, 0, 255), 2)
            filled = cv.fillConvexPoly(ed, np.array([box], 'int32'), (0, 0, 255))
            #cv.imshow('frame', filled);cv.waitKey()
            red = np.array([0, 0, 255])
            mask = cv.inRange(filled, red, red)
            #cv.imshow('frame', mask);cv.waitKey()
            result = cv.bitwise_and(cache, cache, mask=mask)
            #cv.imshow('frame', result);cv.waitKey(0)
            count = 1
            break
    if count == 0:
        return count
    return result

def lego_pile_recognition(img):
    # The array of colors go blue, then red, then yellow.
    # Categories is the big array used to send the needed information on. It has several arrays inside it:
    # Categories --> array for each color --> array for short and long bricks--> array for each brick of that size and color --> has the midpoint and angle of the brick.
    bluelong=[];blueshort=[];redlong=[];redshort=[];yellowlong=[];yellowshort=[]
    categories =[[bluelong,blueshort],[redlong,redshort],[yellowlong,yellowshort]]
    drawcolors = [(0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0), (255, 0, 255)]

    color = 0 # For appending into color arrays
    size = 0 # For appending into size arrays

    # Picture preprocessing
    resize = find_pile(img) #Applies a mask to the image to only look at the pile.
    #print(len(resize))
    if len(resize) == 1 :
        print('No pile, something is in the way!')
        return
    blur = cv.bilateralFilter(resize, 9, 75, 75)
    #cv.imshow('frame', blur); cv.waitKey()

    # Thresholds (in BGR)
    #Early day thresholds
    #blue_max = np.array([255, 215, 140]);red_max = np.array([195, 190, 255]);yellow_max = np.array([230, 255, 255])
    #blue_min = np.array([190, 120, 50]);red_min = np.array([130, 130, 220]);yellow_min = np.array([140, 220, 220])
    # Midday thresholds
    #blue_max = np.array([255, 206, 142]);red_max = np.array([166, 174, 255]);yellow_max = np.array([208, 255, 255])
    #blue_min = np.array([171, 102, 38]);red_min = np.array([102, 111, 211]);yellow_min = np.array([106, 227, 211])
    #Later day thresholds
    #blue_max = np.array([255, 180, 140]);red_max = np.array([155, 170, 255]);yellow_max = np.array([230, 255, 255])
    #blue_min = np.array([175, 90, 40]);red_min = np.array([55, 70, 190]);yellow_min = np.array([140, 220, 220])

    blue_max = np.array([255, 215, 142]);red_max = np.array([195, 190, 255]);yellow_max = np.array([230, 255, 255])
    blue_min = np.array([171, 90, 38]);red_min = np.array([55, 70, 190]);yellow_min = np.array([106, 220, 211])

    threshold_max = [blue_max, red_max, yellow_max]
    threshold_min = [blue_min, red_min, yellow_min]

    for i,j in zip(threshold_max, threshold_min): #Runs for every pair of thresholds.

        threshold= cv.inRange(blur, np.array(j), np.array(i)) #thresholds for each color brick.
        #cv.imshow('frame', threshold);cv.waitKey()

        kernel = np.ones((3, 3), np.uint8)
        erosion = cv.erode(threshold, kernel, iterations=2) #Opening to remove noise.
        dilation = cv.dilate(erosion, kernel, iterations=2)

        edges = cv.Canny(dilation, 50, 200)
        #cv.imshow('frame', edges);cv.waitKey()
        contours, hierarchy = cv.findContours(edges, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

        for con in range(len(contours)): #Runs through all contours for each color
            cnt = contours[con]
            if hierarchy[0][con][2] < 0:  #Ensures non-closed contours are not looked at, since they can not be bricks.
                print('This contour is not closed')
            elif len(contours[con])<5:
                print('Too small')
            else:
                (x, y), (major, minor), angle = cv.fitEllipse(cnt) #Finds the midpoint and angle of the bricks.
                #print((x, y), angle, (major, minor))

                perimeter = cv.arcLength(cnt, True)  # Finds perimeter of contour.
                # print(perimeter)
                rect = cv.minAreaRect(cnt)
                box = cv.boxPoints(rect)
                # print(box)
                boxt = np.int0(box)

                brick = [[x, y], [angle]]

                # Sorts by size of perimeter and dimensions of the contour
                if 125 < perimeter < 160 and 20 < major < 45 and 47 < minor < 65:
                    categories[color][size].append(brick)
                    cv.drawContours(resize, [boxt], 0, drawcolors[color], 2)
                elif 75 < perimeter < 110 and 20 < major < 45 and 20 < minor < 45:
                    # print('small')
                    categories[color][size + 1].append(brick)
                    cv.drawContours(resize, [boxt], 0, drawcolors[color + 3], 2)
                else:
                    print('This is not a Lego Brick')

        color += 1 # Changes color array that is appended Blue --> Red --> Yellow

        print(categories)
    return resize, categories

#This part is used for testing.

#Resizes window to make it easier to see images when using imshow.
cv.namedWindow('frame', cv.WINDOW_NORMAL)
cv.resizeWindow('frame', 600, 400)

img = cv.imread('calibrationmiddaty.png', cv.IMREAD_UNCHANGED)
#print(img.shape)
#cv.imshow('frame', img);cv.waitKey()

resize,bricks=lego_pile_recognition(img)

print('There were', len(bricks[0][0]),'blue long bricks(red) and',len(bricks[0][1]),'blue short bricks(light blue).')
print('There were', len(bricks[1][0]),'red long bricks(yellow) and',len(bricks[1][1]),'red short bricks(dark blue).')
print('There were', len(bricks[2][0]),'yellow long bricks(green) and',len(bricks[2][1]),'yellow short bricks(magenta).')
cv.imshow('frame', resize);cv.waitKey()


