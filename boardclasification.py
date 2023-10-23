import cv2
import tilearay
import featureextractor
import Crown_Recognition

class cell:

    img=0
    tile= tilearay.artile(0, "unnamed", -1, 0, "none")
    crowns=0
    def __init__(self,type,img,):

        self.typid=type
        self.img=img
        self.crowns=0

    def getimg(self):
        return self.img
    def getid(self):
        return self.typid.type
class board:
    ix=0
    iy=0
    tiles=[[cell(0,-1),cell(0,-1),cell(0,-1),cell(0,-1),cell(0,-1)]
        ,  [cell(0,-1),cell(0,-1),cell(0,-1),cell(0,-1),cell(0,-1)]
        ,  [cell(0,-1),cell(0,-1),cell(0,-1),cell(0,-1),cell(0,-1)]
        ,  [cell(0,-1),cell(0,-1),cell(0,-1),cell(0,-1),cell(0,-1)],
           [cell(0,-1),cell(0,-1),cell(0,-1),cell(0,-1),cell(0,-1)]]
    alltiles=0

    fspace=0
    def __init__(self, orthimg,fspace):
        self.fspace=fspace

        shape=orthimg.shape
        self.ix = shape[0]
        self.iy = shape[1]
        pertilex = int(self.ix/5)
        pertiley = int(self.iy/5)
        ptxh = int(pertilex / 2)
        ptyh = int(pertiley / 2)
        print(ptxh)
        print(ptyh)
        print(orthimg.shape)
        for x in range(5):
            for y in range(5):
                if(True):
                    cpx = (x * pertilex) + ptxh
                    cpy = (y * pertiley) + ptyh

                    tcell=cell(0,orthimg[cpx-ptxh:cpx+ptxh,cpy-ptyh:cpy+ptyh])
                    self.tiles[x][y]=tcell
        print("images were loaded")

    def analysetiles(self):
        cgd=0
        for x in range(5):
            for y in range(5):
                match=self.findmatch(self.tiles[x][y].img)
                if(match[0]):
                    self.tiles[x][y].typid=match[1]
                    cgd+=1
        return(cgd==25)
    def featurechek(self,WAB):
        WABS=WAB


        tiletypes = [ "special","ocean", "field", "corn", "forest", "cave", "desert"]
        cgd = 0
        for x in range(5):
            for y in range(5):
                self.tiles[x][y].typid= self.fspace.identifyNNx(self.tiles[x][y].img,WABS.NerestNX,WABS)
                #print(f"tile x:{x},y:{y} was of type {tiletypes[self.tiles[x][y].typid]}")
                #cv2.imshow(f"x:{x},y:{y},type {tiletypes[self.tiles[x][y].typid]}",self.tiles[x][y].img)
                cgd+=1
        return (cgd == 25)
    calc=0
    cords = []
    ctype = 0
    def crownchek(self,WAB,d):
        for x in range(5):
            for y in range(5):
                self.tiles[x][y].crowns = Crown_Recognition.CrownDetectionRotation(self.tiles[x][y].img )
                crowc=self.tiles[x][y].crowns
                if(crowc>0 and self.tiles[x][y].typid==0):
                    self.tiles[x][y].typid=6
        tiletypes = ["special", "ocean", "field", "corn", "forest", "cave", "desert"]
        for x in range(5):
            for y in range(5):
                cv2.imshow(f"{x}{y} : {tiletypes[self.tiles[x][y].typid]} has {self.tiles[x][y].crowns} crowns ",self.tiles[x][y].img)
        cv2.waitKey(10000)

    burtileglob=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    def scorethisboard(self):
        burnttiles=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        global burtileglob
        burtileglob=burnttiles
        for x in range(5):
            for y in range(5):
                burtileglob[x][y]=self.tiles[x][y].typid

        score=0
        for x in range(5):
            for y in range(5):
                score+=self.blobchek([x,y] ,self.tiles[x][y].typid)
        return score


    def blobchek(self,cord,tiletypeid):
        #print("cheking")
        global burtileglob
        ida = burtileglob
        x, y = cord
        burn_que = []
        crownsinblob=0
        tilesinblob=0
        #print("curent blob id is" + str(tiletypeid))
        if (ida[x][y] == 0):
            #print("returning")
            return 0
        burn_que.append([x, y])
        #print("burn que was " + str(burn_que))
        xle = len(ida)
        yle = len(ida[0])
        while (len(burn_que) > 0):
            x, y = burn_que.pop()
            tilesinblob+=1
            crownsinblob+=self.tiles[x][y].crowns

            ida[x][ y] = 0

            if (x + 1 < xle and ida[x + 1][ y] == tiletypeid):
                burn_que.append([x + 1, y])
            if (y + 1 < yle and ida[x][ y + 1] == tiletypeid):
                burn_que.append([x, y + 1])
            if (x - 1 >= 0 and ida[x - 1][ y] == tiletypeid):
                burn_que.append([x - 1, y])
            if (y - 1 >= 0 and ida[x][ y - 1] == tiletypeid):
                burn_que.append([x, y - 1])
            #print("curent image id is" + str(tiletypeid))

        burtileglob = ida
        return crownsinblob*tilesinblob



    def findmatch(self,img):
        found=False
        mint=1000
        minid=0
        for t in range(len(self.alltiles.tiles)):
            sm=self.cellmatch(img,self.alltiles.getimgat(t),10)

            if(sm[0]&(sm[1]<mint)):
                mint=sm[1]
                minid=t
                found=True
        if(found):
            return (True,self.alltiles.tiles[minid])
        else:
            cv2.imshow("missing",img)
            print("no matches found, consider expanding the tileset")
            return (False, tilearay.artile(0, "unknown", 0, 0, "none"))



    def cellmatch(self,img1,img2,threshold):
        RGBhist1=[0,0,0]
        color=("b","g","r")
        for n in range(len(color)):
            RGBhist1[n]=[cv2.calcHist([img1],[n],None,[256],[0,256])]

        RGBhist2 =[0,0,0]
        for n in range(len(color)):
            RGBhist2[n]=[cv2.calcHist([img2], [n], None, [256], [0, 256])]
        #normalize histograms, even if one has more pixels all distributuions should be closer
        RGBhist1=self.normalizehist(img1,RGBhist1)
        RGBhist2=self.normalizehist(img1,RGBhist2)

        total=0
        for n in range(len(RGBhist1[0])):
            dist=0
            dist += abs(RGBhist1[0][n] - RGBhist2[0][n])
            dist += abs(RGBhist1[1][n] - RGBhist2[1][n])
            dist += abs(RGBhist1[2][n] - RGBhist2[2][n])
            total+=dist

        return ((total<threshold),total-threshold)


    def normalizehist(self,img,hist):
        img1=img
        RGBhist1=hist
        pixcount1 = img1.shape[0] * img1.shape[1]

        for n in range(len(RGBhist1[0][0][0])):

            RGB1=[RGBhist1[0][0][0][n],RGBhist1[1][0][0][n],RGBhist1[2][0][0][n]]

            NRGB1=[float(RGB1[0])/float(pixcount1),float(RGB1[1])/float(pixcount1),float(RGB1[2])/float(pixcount1)]
            RGBhist1[0][n] = NRGB1[0]*100
            RGBhist1[1][n] = NRGB1[1]*100
            RGBhist1[2][n] = NRGB1[2]*100

        return RGBhist1

        # compare the hisograms with a threshold




