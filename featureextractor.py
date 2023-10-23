import cv2
import os
import numpy as np

class featurespace:
    data = []
    datamax=[]
    datamin=[]
    def __init__(self,tilesource,WAB):

        filenames = os.listdir(tilesource)
        print(WAB)

        #load all features into the aray
        for x in filenames:

            img = cv2.imread("boardtiles//"+x)


            self.data.append(feature(img,x,True,WAB))
        #loop over the properties of features to find the minimum and maximum values of each feature
        min=[10000,10000,10000,10000,10000,10000,10000,10000,10000,100000]
        max=[0,0,0,0,0,0,0,0,0,0]

        for x in self.data:
            fid=0
            if(x.borderavg[0]>max[fid]):
                max[fid]=x.borderavg[0]
            elif(x.borderavg[0]<min[fid]):
                min[fid]=x.borderavg[0]
            fid=fid+1
            if (x.borderavg[1] > max[fid]):
                max[fid] = x.borderavg[1]
            elif (x.borderavg[1] < min[fid]):
                min[fid] = x.borderavg[1]
            fid = fid + 1
            if (x.borderavg[2] > max[fid]):
                max[fid] = x.borderavg[2]
            elif (x.borderavg[2] < min[fid]):
                min[fid] = x.borderavg[2]
            fid = fid + 1

            if (x.centeravg[0] > max[fid]):
                max[fid] = x.centeravg[0]
            elif (x.centeravg[0] < min[fid]):
                min[fid] = x.centeravg[0]
            fid = fid + 1
            if (x.centeravg[1] > max[fid]):
                max[fid] = x.centeravg[1]
            elif (x.centeravg[1] < min[fid]):
                min[fid] = x.centeravg[1]
            fid = fid + 1
            if (x.centeravg[2] > max[fid]):
                max[fid] = x.centeravg[2]
            elif (x.centeravg[2] < min[fid]):
                min[fid] = x.centeravg[2]
            fid = fid + 1

            if (x.histogramdat[0] > max[fid]):
                max[fid] = x.histogramdat[0]
            elif (x.histogramdat[0] < min[fid]):
                min[fid] = x.histogramdat[0]
            fid = fid + 1
            if (x.histogramdat[1] > max[fid]):
                max[fid] = x.histogramdat[1]
            elif (x.histogramdat[1] < min[fid]):
                min[fid] = x.histogramdat[1]
            fid = fid + 1
            if (x.histogramdat[2] > max[fid]):
                max[fid] = x.histogramdat[2]
            elif (x.histogramdat[2] < min[fid]):
                min[fid] = x.histogramdat[2]
            fid = fid + 1

            if (x.edgedpixels > max[fid]):
                max[fid] = x.edgedpixels
            elif (x.edgedpixels < min[fid]):
                min[fid] = x.edgedpixels

            fid = fid + 1
        self.datamax=max
        self.datamin=min
    def identifyNNx(self,unkimg,x,WAB):
        feat = feature(unkimg,"unknown",False,WAB)
        nnD=[1000000000]
        nnI=[0]
        for t in range(x):
            nnD.append(1000000000)
            nnI.append(0)
        for i in self.data:
            tdist=self.dist(i,feat,WAB)
            for y in range(x): # loop over the n closest neigbours
                if(tdist<nnD[y]):
                    disthold=tdist
                    idhold=i.fieldtype
                    for z in range(x-y):
                        # save the distance and id of this nearest neighbour
                        td=nnD[y+z]
                        ti=nnI[y+z]
                        # save the held value to this spot
                        nnD[y + z]=disthold ## set it equal to the held value
                        nnI[y+z]=idhold
                        # set held values to the previous value of this cell
                        # this means the cell in the next loop will get this cells value
                        disthold=td
                        idhold=ti
                         # hold the value of this cell
                    break
                    # since the value was greater than an earlier entry, changing the rest
                    # would on overwrite all of the nearest neigbours,
        tally=[0,0,0,0,0,0,0,0]
        for i in nnI:
            tally[i]+=1
        great=0
        graid=0
        for i in range(len(nnI)):
            if(tally[i]>great):
                graid=i
                great=tally[i]
        return graid
    def dist(self,fa,fb,WAB):
        dist=np.sqrt(
            np.power(self.sir2dif(fa.borderavg[0],fb.borderavg[0],self.datamin[0],self.datamax[0],WAB.borderweght) ,2)+
            np.power(self.sir2dif(fa.borderavg[1], fb.borderavg[1], self.datamin[1], self.datamax[1],WAB.borderweght), 2) +
            np.power(self.sir2dif(fa.borderavg[2], fb.borderavg[2], self.datamin[2], self.datamax[2],WAB.borderweght), 2) +
            np.power(self.sir2dif(fa.centeravg[0], fb.centeravg[0], self.datamin[3], self.datamax[3],WAB.centerweigt), 2) +
            np.power(self.sir2dif(fa.centeravg[1], fb.centeravg[1], self.datamin[4], self.datamax[4],WAB.centerweigt), 2) +
            np.power(self.sir2dif(fa.centeravg[2], fb.centeravg[2], self.datamin[5], self.datamax[5],WAB.centerweigt), 2) +
            np.power(self.sir2dif(fa.histogramdat[0], fb.histogramdat[0], self.datamin[6], self.datamax[6],WAB.histogramweigt), 2) +
            np.power(self.sir2dif(fa.histogramdat[1], fb.histogramdat[1], self.datamin[7], self.datamax[7],WAB.histogramweigt), 2) +
            np.power(self.sir2dif(fa.histogramdat[2], fb.histogramdat[2], self.datamin[8], self.datamax[8],WAB.histogramweigt), 2)+
            np.power(self.sir2dif(fa.edgedpixels, fb.edgedpixels, self.datamin[9], self.datamax[9], WAB.edgeweight),2)
           # np.power(self.sir2dif(fa.saturadat[0], fb.saturadat[0], self.datamin[10], self.datamax[10], WAB.saturationweight),2) +
           # np.power(self.sir2dif(fa.saturadat[1], fb.saturadat[1], self.datamin[11], self.datamax[11], WAB.saturationweight),2) +
           # np.power(self.sir2dif(fa.saturadat[2], fb.saturadat[2], self.datamin[12], self.datamax[12], WAB.saturationweight),2)

        )
        return dist
    def sir2dif(self,x,y,min,max,weight):
        xp=(x-min)/(max-min)
        yp=(y-min)/(max-min)

        return abs(xp-yp)*weight
    def printintervals(self):
        for x in range(len(self.datamax)):
            print(f"prameter {x} has range:{self.datamin[x]} to {self.datamax[x]}")
class feature:
    borderavg = [0, 0, 0]
    centeravg = [0, 0, 0]
    histogramdat=[0 , 0 , 0] # format is height, angle, color of the tallest peak
    #saturadat = [0, 0, 0]  # format is height, angle, color of the tallest peak
    edgedpixels=0
    crowns = 0
    fieldtype=0
    def __init__(self,img,name,known,WAB):
        tiletypes = [ "special","ocean", "field", "corn", "forest", "cave", "desert"]
        self.borderavg=getborderavg(img,WAB)
        self.centeravg=getcenteravg(img,WAB)
        self.histogramdat=hsvhistdist(img,WAB)
        self.edgedpixels=getedgecount(img,WAB)
        #self.saturadat=saturationpeak(img,WAB)
        if(known):
            split=name.split("_")
            self.fieldtype=tiletypes.index(split[0])
            if(len(split)>2):
                self.crowns=(int(split[3]))
            else:
                self.crowns=0
    def flatten(self):
        return [self.borderavg[0],self.borderavg[1],self.borderavg[2],
                self.centeravg[0],self.centeravg[1],self.centeravg[2],
                self.histogramdat[0],self.histogramdat[1],self.histogramdat[2]]

class WAB:
    borderthickness = 0
    threshold = 0
    borderwith = 0
    histogramweigt = 0
    saturationweight=0
    centerweigt = 0
    borderweght = 0
    edgenoise=0
    edgethreshold=0
    edgeweight=0
    ekernelsize=0
    NerestNX=0


    def __init__(self,cutin,border,threshold,hist,sw,centerW,borderW,edgeW,edgnoise,edgethres,eks,nnx):
        self.borderthickness=cutin
        self.borderwith=border
        self.threshold=threshold
        self.histogramweigt=hist
        self.centerweigt=centerW
        self.borderweght=borderW
        self.edgeweight=edgeW
        self.edgethreshold=edgethres
        self.edgenoise=edgnoise
        self.ekernelsize=eks
        self.NerestNX=nnx
        self.saturationweight=sw

def getedgecount(img,WAB):
    xl=img.shape[0]
    yl=img.shape[1]
    im2=cv2.blur(img,(2,2))

    res = cv2.Canny(im2,WAB.edgenoise,WAB.edgethreshold)

    kernel = np.ones((WAB.ekernelsize, WAB.ekernelsize), np.uint8)
    res2=cv2.dilate(res,kernel,iterations=1)
    #cv2.imshow("rest2",res2)
    #save=res2
    #cv2.waitKey()
    global blobimg
    blobimg=res2

    pcount=1
    callcount=0
    for x in range(xl):
        for y in range(yl):
            if(res2[x,y]!=0):
                pcount=grasfire(res2,[x,y],pcount)

    #cv2.imshow(f"rest2 pcount:{pcount} ", save)
    return pcount
blobimg=0
def grasfire(img,cord,blid):
    global blobimg


    img=blobimg
    x,y=cord
    burn_que=[]
    #print("curent blob id is"+str(blid))
    if(img[x,y] !=255):

        #print("returning")
        return blid
    burn_que.append([x,y])
    #print("burn que was "+str(burn_que))
    while(len(burn_que)>0):
        x,y=burn_que.pop()
        if (blid<255):
            img[x,y]=blid
        else:
            img[x,y]=254


        if(x + 1 < img.shape[0] and img[x + 1 , y]==255):
            burn_que.append([x + 1 , y ])
        if (y + 1 < img.shape[1] and img[ x , y + 1] == 255):
            burn_que.append([x, y + 1])
        if (x - 1 >= 0 and img[x - 1, y]== 255):
            burn_que.append([x - 1, y])
        if (y - 1 >= 0 and img[x , y - 1]== 255):
            burn_que.append([ x , y - 1])
        #print("curent image id is"+str(blid))
        if(len(burn_que)==0):
            blid=blid+1
    blobimg=img
    return blid

def getborderavg(img,WAB ):
    bordth=WAB.borderwith
    xs=WAB.borderthickness
    xw=img.shape[0]-xs
    ys=xs
    yh=img.shape[1]-ys


    topcut=img[xs:xw,ys:bordth]

    leftcut=img[xs:bordth+xs,bordth+ys:yh-bordth]

    righttcut = img[xw-bordth:xw, bordth:yh-bordth]

    botcut=img[xs:xw, yh-bordth:yh]

    ptop=topcut.shape[0]*topcut.shape[1]
    plef=leftcut.shape[0]*leftcut.shape[1]
    prig=righttcut.shape[0]*righttcut.shape[1]
    pbot=botcut.shape[0]*botcut.shape[1]
    totalpix= (ptop+plef+prig+pbot)

    atop=imgavg(topcut)
    alef=imgavg(leftcut)
    arig=imgavg(righttcut)
    abot=imgavg(botcut)

    ravg = (atop[0] * ptop + alef[0] * plef + arig[0] * prig+abot[2]*pbot) / (totalpix )
    gavg = (atop[1] * ptop + alef[1] * plef + arig[1] * prig+abot[2]*pbot) / (totalpix )
    bavg = (atop[2] * ptop + alef[2] * plef + arig[2] * prig+abot[2]*pbot) / (totalpix )

    if(avg3vdist1(atop,alef,arig,abot)>WAB.threshold):
        ravg = (atop[0] * ptop + alef[0] * plef + arig[0] * prig ) / (totalpix-pbot)
        gavg = (atop[1] * ptop + alef[1] * plef + arig[1] * prig ) / (totalpix-pbot)
        bavg = (atop[2] * ptop + alef[2] * plef + arig[2] * prig ) / (totalpix-pbot)
    if (avg3vdist1(atop, alef, abot, arig) > WAB.threshold):
        ravg = (atop[0] * ptop + alef[0] * plef + abot[0] * pbot) / (totalpix - prig)
        gavg = (atop[1] * ptop + alef[1] * plef + abot[1] * pbot) / (totalpix - prig)
        bavg = (atop[2] * ptop + alef[2] * plef + abot[2] * pbot) / (totalpix - prig)
    if (avg3vdist1(atop, abot, arig, alef) > WAB.threshold):
        ravg = (atop[0] * ptop + abot[0] * pbot + arig[0] * prig) / (totalpix - plef)
        gavg = (atop[1] * ptop + abot[1] * pbot + arig[1] * prig) / (totalpix - plef)
        bavg = (atop[2] * ptop + abot[2] * pbot + arig[2] * prig) / (totalpix - plef)
    if (avg3vdist1(alef, abot, arig, atop) > WAB.threshold):
        ravg = (alef[0] * plef + abot[0] * pbot + arig[0] * prig) / (totalpix - ptop)
        gavg = (alef[1] * plef + abot[1] * pbot + arig[1] * prig) / (totalpix - ptop)
        bavg = (alef[2] * plef + abot[2] * pbot + arig[2] * prig) / (totalpix - ptop)




    return [ravg,gavg,bavg]

def avg3vdist1(a,b,c,d):
    r=(a[0]+b[0]+c[0])/3
    g=(a[1]+b[1]+c[1])/3
    b=(a[2]+b[2]+c[2])/3

    return np.sqrt(np.power(r-d[0],2)+np.power(g-d[1],2)+np.power(b-d[2],2))

def getcenteravg(img,WAB ):
    bordth=WAB.borderwith
    xw=img.shape[0]
    yh=img.shape[1]
    centercut=img[bordth:xw-bordth,bordth:yh-bordth]
    avgcent=imgavg(centercut)

    return avgcent

def imgavg(img):
    rtotal=0
    gtotal = 0
    btotal = 0

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            rtotal=img[x,y][0]+rtotal
            gtotal=img[x,y][1]+gtotal
            btotal=img[x,y][2]+btotal
    pixc=img.shape[0]*img.shape[1]

    return [int(rtotal/pixc),int(gtotal/pixc),int(btotal/pixc)]

def hsvhistdist(img,WAB):
    hsi=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist=cv2.calcHist(hsi,[0],None,[256],[0,256])

    foundpeaks=[]


    last1 = 0
    last2 = 0
    last3 = 0
    curent= 0
    next1 = 0
    next2 = 0
    next3 = 0
    for i in range(len(hist)):
        last1=last2
        last2=last3
        last3=curent
        curent=next1

        next1=next2
        next2=next3
        next3=hist[i]


        lavg=(last1+last2+last3)/3
        navg=(next1+next2+next3)/3
        if(curent>lavg and curent>navg):
            calcangle= ((lavg+navg)/2)/curent
            foundpeaks.append([hist[i],calcangle,i])
    maxcount=0
    maxid=0
    for i in range(len(foundpeaks)):
        if(maxcount<foundpeaks[i][0]):
            maxcount=foundpeaks[i][0]
            maxid=i

    return foundpeaks[maxid]
def saturationpeak(img,WAB):
    hsi=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist=cv2.calcHist(hsi,[1],None,[256],[0,256])

    foundpeaks=[]


    last1 = 0
    last2 = 0
    last3 = 0
    curent= 0
    next1 = 0
    next2 = 0
    next3 = 0
    for i in range(len(hist)):
        last1=last2
        last2=last3
        last3=curent
        curent=next1

        next1=next2
        next2=next3
        next3=hist[i]


        lavg=(last1+last2+last3)/3
        navg=(next1+next2+next3)/3
        if(curent>lavg and curent>navg):
            calcangle= ((lavg+navg)/2)/curent
            foundpeaks.append([hist[i],calcangle,i])
    maxcount=0
    maxid=0
    for i in range(len(foundpeaks)):
        if(maxcount<foundpeaks[i][0]):
            maxcount=foundpeaks[i][0]
            maxid=i

    return foundpeaks[maxid]

