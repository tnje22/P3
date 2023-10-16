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


img = cv2.imread("shapes.png")
iout= call(img)
cv2.imshow("output",iout)
cv2.waitKey()