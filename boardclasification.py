import cv2
import boardtiles.tilearay


class cell:

    img=0
    tile=boardtiles.tilearay.artile(0,"unnamed",-1,0,"none")
    def __init__(self,type,img):

        self.typid=type
        self.img=img

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


    def __init__(self, orthimg):

        shape=orthimg.shape
        self.ix = shape[0]
        self.iy = shape[1]
        pertilex = int(self.ix/5)
        pertiley = int(self.iy/5)
        ptxh = int(pertilex / 2)
        ptyh = int(pertiley / 2)
        print(ptxh)
        print(ptyh)
        self.alltiles=boardtiles.tilearay.tilearay()

        print(orthimg.shape)
        for x in range(5):
            for y in range(5):
                if(True):
                    cpx = (x * pertilex) + ptxh
                    cpy = (y * pertiley) + ptyh

                    tcell=cell(0,orthimg[cpx-ptxh:cpx+ptxh,cpy-ptyh:cpy+ptyh])
                    print(type(tcell))
                    self.tiles[x][y]=tcell
        print("images were loaded")

        for x in range(5):

            for y in range(5):
                print(type(self.tiles[x][y]))
                tcell2=self.tiles[x][y]
                print(tcell2.img.shape)
                cv2.imshow(f"x{x} y{y} ", self.tiles[x][y].getimg())
    def analysetiles(self):
        cgd=0
        for x in range(5):
            for y in range(5):
                match=self.findmatch(self.tiles[x][y].img)
                if(match[0]):
                    self.tiles[x][y].typid=match[1]
                    cgd+=1
        return(cgd==25)
    calc=0
    cords = []
    ctype = 0
    def scorethisboard(self):
        calculated=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        self.calc=calculated
        score=0
        for x in range(5):
            for y in range(5):
                if(calculated[x][y]==0):
                    cell=self.tiles[x][y]
                    fields=1

                    print(type(cell))
                    self.cords=[]
                    self.cords+=[[x,y]]
                    ctype=cell.getid()

                    crowns=cell.typid.crowns
                    ret=self.recursivechek(self.tiles,x,y,cell.getid())
                    fields+=ret[0]
                    crowns+=ret[1]
                    score+=fields*crowns
                    print(f"the cordinates{self.cords} were of type {ctype}")
        print(f"this boardscore is {score}")

    def recursivechek(self,tilear,xp,yp,tiletypeid):
        points=[[1,0],[0,1],[-1,0],[0,-1]]

        self.calc[xp][yp]=1
        fields=0
        crowns=0
        for poi in points:
            try:
                print("1")
                cell=tilear[xp+poi[0]][yp+poi[1]]
                print("2")
                ps=self.calc[xp+poi[0]][yp+poi[1]]
                print("3")
                if(ps==0):
                    print("3.5")
                    if(cell.getid() == tiletypeid):
                        print("4")
                        fields += 1
                        print("5")
                        crowns += cell.tile.crowns
                        print("6")
                        self.cords +=[(xp+poi[0],yp+poi[1])]
                        print("7")
                        ret= self.recursivechek(tilear,xp+poi[0],yp+poi[1],tiletypeid)
                        print("8")
                        fields+=ret[0]
                        print("9")
                        crowns+=ret[1]
                        print("10")
            except:
                print("not in range")
        return (fields,crowns)


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
            return (False, boardtiles.tilearay.artile(0,"unknown",0,0,"none"))



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




