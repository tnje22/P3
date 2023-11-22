import numpy as np
import cv2 as cv

def lego_pile_recognition(img):
    # Array of colors go blue, then red, yellow, green and grey.
    bluelong=[];blueshort=[];redlong=[];redshort=[];yellowlong=[];yellowshort=[];greenlong=[];greenshort=[];greyshort=[]
    categories =[[bluelong,blueshort],[redlong,redshort],[yellowlong,yellowshort],[greenlong,greenshort],[None,greyshort]]

    color = 0 # For appending into color arrays
    size = 0 # For appending into size arrays
    count = 0 # For counting number of bricks (Temporary)

    # Picture preprocessing
    resize = img[350:750, 550:1000]
    blur = cv.bilateralFilter(resize, 9, 75, 75)
    hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

    # Thresholds
    blue_max = np.array([120, 190, 255]);red_max = np.array([19, 218, 255]);yellow_max = np.array([40, 220, 255]);green_max = np.array([95, 255, 255]);grey_max = np.array([200, 60, 220])
    blue_min = np.array([107, 80, 190]);red_min = np.array([0, 50, 187]);yellow_min = np.array([15, 0, 125]);green_min = np.array([60, 9, 100]);grey_min = np.array([90, 0, 120])
    threshold_max = [blue_max, red_max, yellow_max, green_max, grey_max]
    threshold_min = [blue_min, red_min, yellow_min, green_min, grey_min]

    for i,j in zip(threshold_max, threshold_min): # Runs for every pair of thresholds

        threshold= cv.inRange(hsv, np.array(j), np.array(i))
        kernel = np.ones((3, 3), np.uint8)
        erosion = cv.erode(threshold, kernel, iterations=2)
        dilation = cv.dilate(erosion, kernel, iterations=2)
        edges = cv.Canny(dilation, 50, 200)
        contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        #cv.imshow('frame', edges); cv.waitKey()

        for con in range(len(contours)):
            cnt = contours[con]
            (x, y), (MA, ma), angle = cv.fitEllipse(cnt)
            perimeter = cv.arcLength(cnt, True)
            #print(perimeter)
            brick = [[x, y], [angle]]

            if 115<perimeter<145:
                categories[color][size].append(brick)
            elif 65<perimeter<95:
                categories[color][size+1].append(brick)
            else:
                print('This is not a Lego Brick')

            count += 1
        #print('There is',count,'bricks of this color')
        count = 0
        color += 1

        #print(categories)
    return categories

img = cv.imread('BrickPile.png', cv.IMREAD_UNCHANGED)
bricks=lego_pile_recognition(img)
#print('All bricks has been looked at')
#print(bricks)

