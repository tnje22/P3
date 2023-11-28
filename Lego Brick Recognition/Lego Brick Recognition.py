import numpy as np
import cv2 as cv

#Creates a mask that removes everything, but the area marked of for the pile of lego bricks.
def find_pile(img):
    cache = img.copy()
    blur = cv.bilateralFilter(img, 9, 75, 75)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

    white_max = np.array([170, 13, 255]);white_min = np.array([0, 0, 170])

    threshold = cv.inRange(hsv, white_min, white_max)
    cv.imshow('frame', threshold);cv.waitKey()
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv.erode(threshold, kernel, iterations=3)
    dilation = cv.dilate(erosion, kernel, iterations=3)
    edges = cv.Canny(dilation, 50, 200)
    #cv.imshow('frame', edges);cv.waitKey()
    contours, hierarchy = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # print(len(contours))

    for con in range(len(contours)):
        cnt = contours[con]
        perimeter = cv.arcLength(cnt, True)

        if 2100>perimeter>1800: #Checks all contours to find the one that corresponds to the tape, that marks the pile area.
            rect = cv.minAreaRect(cnt)
            box = cv.boxPoints(rect)
            box = np.int0(box)
            ed = cv.drawContours(img, [box], 0, (0, 0, 255), 2)
            filled = cv.fillConvexPoly(ed, np.array([box], 'int32'), (0, 0, 255))
            cv.imshow('frame', filled);cv.waitKey()
            red = np.array([0, 0, 255])
            mask = cv.inRange(filled, red, red)
            cv.imshow('frame', mask);cv.waitKey()
            result = cv.bitwise_and(cache, cache, mask=mask)
            cv.imshow('frame', result);cv.waitKey(0)
            break

    return result

def lego_pile_recognition(img):
    # The array of colors go blue, then red, then yellow.
    # Categories is the big array used to send the needed information on. It has several arrays inside it:
    # Categories --> array for each color --> array for short and long bricks--> array for each brick of that size and color --> has the midpoint and angle of the brick.
    bluelong=[];blueshort=[];redlong=[];redshort=[];yellowlong=[];yellowshort=[]
    categories =[[bluelong,blueshort],[redlong,redshort],[yellowlong,yellowshort]]

    color = 0 # For appending into color arrays
    size = 0 # For appending into size arrays

    # Picture preprocessing
    resize = find_pile(img) #Applies a mask to the image to only look at the pile.
    blur = cv.bilateralFilter(resize, 9, 75, 75)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

    # Thresholds
    blue_max = np.array([120, 190, 255]);red_max = np.array([19, 218, 255]);yellow_max = np.array([40, 220, 255])
    blue_min = np.array([107, 80, 190]);red_min = np.array([0, 50, 187]);yellow_min = np.array([15, 0, 125])
    threshold_max = [blue_max, red_max, yellow_max]
    threshold_min = [blue_min, red_min, yellow_min]

    for i,j in zip(threshold_max, threshold_min): #Runs for every pair of thresholds.

        threshold= cv.inRange(hsv, np.array(j), np.array(i)) #thresholds for each color brick.
        cv.imshow('frame', threshold);cv.waitKey()

        kernel = np.ones((3, 3), np.uint8)
        erosion = cv.erode(threshold, kernel, iterations=2) #Opening to remove noise.
        dilation = cv.dilate(erosion, kernel, iterations=2)

        edges = cv.Canny(dilation, 50, 200)
        cv.imshow('frame', edges);cv.waitKey()
        contours, hierarchy = cv.findContours(edges, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

        for con in range(len(contours)): #Runs through all contours for each color
            cnt = contours[con]
            if hierarchy[0][con][2] < 0:  #Ensures non-closed contours are not looked at, since they can not be bricks.
                print('This contour is not closed')
            else:
                (x, y), (major, minor), angle = cv.fitEllipse(cnt) #Finds the midpoint and angle of the bricks.
                print((x, y), angle, (major, minor))
                perimeter = cv.arcLength(cnt, True) #Finds perimeter of contour.
                print(perimeter)
                brick = [[x, y], [angle]]

                # Sorts by size of perimeter and dimensions of the contour
                if 115 < perimeter < 145 and 17 < major < 33 and 43 < minor < 65:
                    categories[color][size].append(brick)
                elif 65 < perimeter < 95 and 17 < major < 35 and 17 < minor < 35:
                    categories[color][size + 1].append(brick)
                else:
                    print('This is not a Lego Brick')

        color += 1 # Changes color array that is appended Blue --> Red --> Yellow

        print(categories)
    return categories

#This part is used for testing.

#Resizes window to make it easier to see images when using imshow.
cv.namedWindow('frame', cv.WINDOW_NORMAL)
cv.resizeWindow('frame', 600, 400)

img = cv.imread('PileSetupB.png', cv.IMREAD_UNCHANGED)

# Applies mask to remove the ground and robot
# (Only for testing, this mask will already be on pictures gained from the Kinect)
mask = cv.imread('tablemask.png', cv.IMREAD_UNCHANGED)
thresh_max = np.array([255, 255, 255]);thresh_min = np.array([1, 1, 1])
binary_mask = cv.inRange(mask, thresh_min, thresh_max)
#cv.imshow('frame', binary_mask);cv.waitKey()
img= cv.bitwise_and(img, img, mask=binary_mask)
cv.imshow('frame', img);cv.waitKey()

bricks=lego_pile_recognition(img)

print('All bricks has been looked at')
print(bricks)
