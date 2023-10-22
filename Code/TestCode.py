import numpy as np
import cv2 as cv


img = cv.imread("Rotated//FieldLeft.png", cv.IMREAD_UNCHANGED)
template = cv.imread('TemplateUp.png', cv.IMREAD_UNCHANGED)

temp_w = template.shape[1]
temp_h = template.shape[0]
result = cv.matchTemplate(img,template, cv.TM_CCOEFF_NORMED)

# matchTemplate gives an array with the confidence value for each pixel, how close they are to match the template.
# The threshold makes sure we only look at the best matching locations.
threshold = 0.5

location = np.where(result >= threshold) # Finds the location of the pixels that is over the threshold
locations = list(zip(*location[::-1])) # Puts coordinates into lists to make it easier to read

rectangles = []

for loc in locations:
    rect = [int(loc[0]), int(loc[1]), temp_w, temp_h]
    rectangles.append(rect)
    rectangles.append(rect) # Twice because groupRectangles only looks at grouped rectangles

rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5)
print(rectangles)

if len(rectangles):
    line_color = (0,255,0)
    line_type = cv.LINE_4

    for (x, y, w, h) in rectangles:
        top_left = (x, y)
        bottom_right = (x+w,y+h)

        cv.rectangle(img, top_left, bottom_right, line_color, line_type)

    print(len(rectangles))
    cv.imshow("Cave", img)
    cv.waitKey()

else:
    print("Not Found")




#Hvis ikke virker dilate og lav blob analysis


"""
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print(max_val)

threshold = 0.8
if max_val >= threshold:
    print("Found")
else:
    print("Not Found")
"""

"""
img_rgb = cv.imread('Field_1_Crown.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('CrownBlack.png', cv.IMREAD_GRAYSCALE)

w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
print(res)

threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
 cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite('res.png',img_rgb)

#cv.imshow("result", img2 )
#cv.waitKey()

"""
"""

"""
"""
img = cv.imread("Field_1_Crown.PNG")
assert img is not None, "file could not be read, check with os.path.exists()"
cv.imshow("Image", img)
cv.waitKey(0)

mask = np.zeros(img.shape[:2], dtype="uint8")
cv.rectangle(mask, (0, 90), (290, 450), 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Mask Applied to Image", masked)
cv.waitKey(0)


kernel = np.ones((2, 2), np.uint8)
Dilationimg = cv.dilate(img,kernel, iterations = 1)
#cv.imshow("dilation", Dilationimg)
#cv.waitKey()

edges = cv.Canny(img,200,200)

edgesD = cv.dilate(edges,kernel, iterations = 5)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edgesD,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

edgesDE = cv.erode(edgesD,kernel, iterations = 6)

Dilationimg = cv.dilate(edgesDE,kernel, iterations = 1)

plt.subplot(121),plt.imshow(edgesDE,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(Dilationimg,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

"""

"""
def sobel(img,thres):
    hori=[[1,2,1],
          [0,0,0],
          [-1,-2,-1]]
    verti=[[1,0,-1],
          [2,0,-2],
          [1,0,-1]]
    ishape=img.shape
    for x in range(ishape[0]):
        for y in range(ishape[1]):
            pval=0
            try:
                valh=0
                valv=0
                for xx in range(3):
                    for yy in range(3):
                        pixt= img[x+xx-1,y+yy-1]
                        grey=int((pixt[0]+pixt[1]+pixt[2])/3)
                        valh+=grey*hori[xx][yy]
                        valv+=grey*verti[xx][yy]
                pval=int((valh/6+valv/6)/2)

            except:
                print("out")
            if(pval>thres):
                img[x,y]=[255,255,255]
            else:
                img[x,y]=[0,0,0]






img =cv.imread('CrownBlackBackground.png')
img2 = cv.imread("Crown//Field_1_Crown.PNG")
result = cv.matchTemplate(img2,img, cv.TM_CCOEFF)
cv.imshow("corn",img2)
cv.imshow("crown",img)
cv.imshow("output",result)
cv.waitKey()


# Import the cv2 library
import cv2
# Read the image you want connected components of
src = cv2.imread('CrownBlackBackground.png')
# Threshold it so it becomes binary
ret, thresh = cv2.threshold(src,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# You need to choose 4 or 8 for connectivity type
connectivity = 4
# Perform the operation
output = cv2.connectedComponentsWithStats(thresh, connectivity, cv2.CV_32S)
# Get the results
# The first cell is the number of labels
num_labels = output[0]
# The second cell is the label matrix
labels = output[1]
# The third cell is the stat matrix
stats = output[2]
# The fourth cell is the centroid matrix
centroids = output[3]



import cv2
from collections import deque

def call(img):
    print(img)
    i2= grasfireque(img)
    return visualizeobjects(i2)


def visualizeobjects(img):
    ishape = img.shape
    highd=0
    for x in range(ishape[0]):
        for y in range(ishape[1]):
            if(highd<img[x,y][0]):
                highd=img[x,y][0]
    B=0
    G=255
    isiz=int(highd/256)
    collo=[[0,0,0]]
    for p in range(highd):
        collo+=[0,G,B]
        G-=isiz
        B+=isiz
    outimg=img
    for x in range(ishape[0]):
        for y in range(ishape[1]):
            if(img[x,y][0]!=0):
                outimg[x,y]=collo[img[x,y][0]]
    return outimg





def grasfire(img,cord,blid):
    x,y=cord
    burn_que=[]
    if(img[x,y] != 255):
        return blid
    burn_que.append([x,y])
    while(len(burn_que)>0):
        x,y=burn_que.pop()
        img[x,y]=blid

        if(x+1<img.shape[0] and img[x+1,y]==255):
            burn_que.append([x+1,y])
        if (y + 1 < img.shape[1] and img[x, y+1] == 255):
            burn_que.append([x, y+1])
        if (x - 1 < 0 and img[x - 1, y] == 255):
            burn_que.append([x - 1, y])
        if (y - 1 < 0 and img[x, y - 1] == 255):
            burn_que.append([x - 1, y])

        if(len(burn_que)==0):
            blid=blid+1
    return blid



def grasfireque(img):
    que=deque()
    matcht=[[0,1],[-1,0],[0,1],[1,0]]
    ishape=img.shape
    print(f"shape{ishape}")
    iout=img
    blobid=1


img = cv2.imread("2.jpg")
iout = call(img)
cv2.imshow("output",iout)
cv2.waitKey()
"""

"""
img = cv.imread("CrownBlackBackground.png")
img2 = cv.imread("Crowns//Hill_1_Crown.png")
cv.imshow('output',img2) #x 67-93, 10-29
cv.waitKey(0)

img3 = cv.imread("Crowns//Cave_2_Crowns.png")
cv.imshow('output',img3) #x 67-93, 10-29
cv.waitKey(0)


print(img.shape)
print(img[3,21])

cv.imshow('output',img)
cv.waitKey(0)

# In picture CrownBlackBackground, crown is found x = 4-31, y = 3-23.

cv.imshow('output', img[3:23])
cv.waitKey(0)

"""