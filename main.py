import numpy
import cv2

import boardclasification


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def showlion():
    img = cv2.imread("lion.jpg")
    cv2.imshow("input", img)

    sx = len(img)
    sy = len(img[0])
    sz = len(img[0][0])
    print(sx)
    print(sy)
    print(sz)

    for x in range(sx):
        for y in range(sy):
            pix = img[x,y]
            r = int(pix[0])
            g = int(pix[1])
            b = int(pix[2])
            avg = (r + g + b) / 3

            img[x,y] = int(avg)
    cv2.imshow("output", img)
    cv2.waitKey()

def averageimg(img,radius):
    sx = len(img)
    sy = len(img[0])
    sz = len(img[0][0])

    oimg=img
    #generate filter size
    filtercords = []
    filtercoef = []
    idx=0
    for x in range(radius*2+1):
        for y in range(radius*2+1):
            filtercords+= [0]
            filtercords[idx]=[x-radius,y-radius]
            filtercoef += [1]
            idx+=1
    flen = len(filtercords)
    normnum=flen
    print(filtercords)
    cutpix=0

    for x in range(sx):
        for y in range(sy):
            try:

                Rsum=0
                Gsum=0
                Bsum=0
                for p in range(flen):

                    pixsum=img[x+filtercords[p][0]][y+filtercords[p][1]]
                    Rsum+=pixsum[0]
                    Gsum+=pixsum[1]
                    Bsum+=pixsum[2]




                oimg[x][y][0] = int(Rsum / normnum)
                oimg[x][y][1] = int(Gsum / normnum)
                oimg[x][y][2] = int(Bsum / normnum)
            except:
                oimg[x][y][0] = 0
                oimg[x][y][1] = 0
                oimg[x][y][2] = 0
                cutpix+=1
    print(f"a number of pixels were cut: {cutpix}")
    return oimg

def meanimg(img,radius):
    sx = len(img)
    sy = len(img[0])
    sz = len(img[0][0])

    oimg=img
    #generate filter size
    filtercords = []
    filtercoef = []
    idx=0
    for x in range(radius*2+1):
        for y in range(radius*2+1):
            filtercords+= [0]
            filtercords[idx]=[x-radius,y-radius]
            filtercoef += [1]
            idx+=1
    flen = len(filtercords)
    normnum=flen
    print(filtercords)
    cutpix=0

    for x in range(sx):
        for y in range(sy):
            try:

                Rlist=[]
                Glist=[]
                Blist=[]
                for p in range(flen):

                    pixsum=img[x+filtercords[p][0]][y+filtercords[p][1]]
                    Rlist+=[pixsum[0]]
                    Glist+=[pixsum[1]]
                    Blist+=[pixsum[2]]

                Rlist.sort()
                Glist.sort()
                Blist.sort()


                oimg[x][y][0] =Rlist[int(len(Rlist) / 2)]
                oimg[x][y][1] =Glist[int(len(Glist) / 2)]
                oimg[x][y][2] =Blist[int(len(Blist) / 2)]
            except:
                oimg[x][y][0] = 0
                oimg[x][y][1] = 0
                oimg[x][y][2] = 0
                cutpix+=1
    print(f"a number of pixels were cut: {cutpix}")
    return oimg
def gausblurimg(img,radius):
    sx = len(img)
    sy = len(img[0])
    sz = len(img[0][0])

    oimg=img
    #generate filter size
    filtercords = []
    filtercoef = []
    idx=0
    normnum=0
    for x in range(radius*2+1):
        for y in range(radius*2+1):
            filtercords+= [0]
            filtercords[idx]=[x-radius,y-radius]
            invmanhattandist=radius*2-(abs(filtercords[idx][0])+abs(filtercords[idx][1])) # the manhattan distance to the filter cell, from the center inverted
            # at max dist = to zero

            filtercoef += [2**invmanhattandist]
            normnum+=filtercoef[idx]
            idx+=1
    flen = len(filtercords)

    print(filtercords)
    cutpix=0

    for x in range(sx):
        for y in range(sy):
            try:
                Rsum = 0
                Gsum = 0
                Bsum = 0
                for p in range(flen):
                    pixsum = img[x + filtercords[p][0]][y + filtercords[p][1]]
                    Rsum += pixsum[0]*filtercoef[p]
                    Gsum += pixsum[1]*filtercoef[p]
                    Bsum += pixsum[2]*filtercoef[p]

                oimg[x][y][0] = int(Rsum / normnum)
                oimg[x][y][1] = int(Gsum / normnum)
                oimg[x][y][2] = int(Bsum / normnum)
            except:
                oimg[x][y][0] = 0
                oimg[x][y][1] = 0
                oimg[x][y][2] = 0
                cutpix+=1
    print(f"a number of pixels were cut: {cutpix}")
    return oimg

def templatematch(img,temp):
    Msx=len(img)
    Msy=len(img[0])
    Msz=len(img[0][0])

    Tsx=len(temp)
    Tsy=len(temp[0])
    Tsz=len(temp[0][0])

    normnum=Tsx*Tsy
    Rsumnorm=0
    Gsumnorm = 0
    Bsumnorm = 0
    for xt in range(Tsx):
        for yt in range(Tsy):
            Rsumnorm +=  temp[xt][yt][0]
            Gsumnorm +=  temp[xt][yt][1]
            Bsumnorm +=  temp[xt][yt][2]


    outimg=img
    persentagedone=0
    maxpix=(Msx-Tsx)*(Msy-Tsy)
    lastp=0
    for x in range(Msx-Tsx):
        for y in range(Msy-Tsy):


            Rsum=0
            Gsum=0
            Bsum=0

            for xt in range(Tsx):
                for yt in range(Tsy):
                    Rsum+=int( img[x+xt][y+yt][0])*int(temp[xt][yt][0])
                    Gsum+=int(img[x+xt][y+yt][1])*int(temp[xt][yt][1])
                    Bsum+=int(img[x+xt][y+yt][2])*int(temp[xt][yt][2])

            outimg[x][y][0] = Rsum / Rsumnorm
            outimg[x][y][1] = Gsum / Gsumnorm
            outimg[x][y][2] = Bsum / Bsumnorm
            persentagedone+=1
            if(lastp+0.01<float(persentagedone)/float(maxpix)):
                lastp=float(persentagedone)/float(maxpix)
                print(lastp)

    return outimg

def hit(size,center,img):
    ishape = img.shape

    for x in range(ishape[0]):
        for y in range(ishape[1]):
            try:
                hitb=False
                for xx in range(size[0]):
                    for yy in range(size[1]):
                        pix=img[x+xx-center[0],y+yy-center[1]]
                        if(pix[0]<1&pix[1]<1&pix[2]<1):
                            hitb=True

                        if(hitb==True):
                            break
                    if(hitb==True):
                        break
                if(hitb==True):
                    img[x,y]=[255,255,255]
                else:
                    img[x,y]=[0,0,0]
            except:
                print("out")

def fit(size,center,img):
    ishape = img.shape
    fitc=ishape[0]*ishape[1]
    count=0
    for x in range(ishape[0]):
        for y in range(ishape[1]):
            try:
                hitb = True
                for xx in range(size[0]):
                    for yy in range(size[1]):
                        pix = img[x + xx - center[0], y + yy - center[1]]
                        if (pix[0] < 1 & pix[1] < 1 & pix[2] < 1):
                            count+=1
                        else:
                            hitb = False

                        if (hitb == False):
                            break
                    if (hitb == False):
                        break
                if (fitc == count):
                    img[x, y] = [255, 255, 255]
                else:
                    img[x, y] = [0, 0, 0]
            except:
                print("out")

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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    boardimage= cv2.imread("King Domino dataset//Cropped and perspective corrected boards//1.jpg")
    board = boardclasification.board(boardimage)
    cv2.imshow("board",boardimage)
    ret=board.analysetiles()
    if(ret):
        board.scorethisboard()





    cv2.waitKey()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
