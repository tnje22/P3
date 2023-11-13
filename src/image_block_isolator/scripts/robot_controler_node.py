

import socket
import urx
import numpy as np
import rospy
import time
from .dryveCode import targetPosition, dryveInit, homing, targetVelocity, profileVelocity, getPosition


robid="172.31.1.115"
dryveid="172.31.1.101"
rob=urx.Robot(robid)

currobotconfig=[0,0,0,0,0,0]

curdryveconfig=0


def initializeall():
    rospy.loginfo("initializing robot")
    rob = urx.Robot(robid)
    rob.set_tcp((0, 0, 0.1, 0, 0, 0))
    rob.set_payload(2, (0, 0, 0.1))
    dryveInit()
    homing()
    curdryveconfig=0
    currobotconfig=rob.get_pose
    
def stopmove():
    rob.stop

def seteepos(x,y,z,xr,yr,zr,acc,vel):
    # this function sets the end effector to a position in our table space

    edgedistance=200 #20 cm
    ur10zrotoffset=45 
    dryvepart=0
    if(abs(curdryveconfig-x)>edgedistance):
        if(x<curdryveconfig):
            dryvepart=x+edgedistance*0.5
            x-=dryvepart
        else:
            dryvepart=x-edgedistance*0.5
            x-=dryvepart


    poseactual=np.matmul(zr(ur10zrotoffset*np.pi/180),[x,y,z])
    rotactual=[xr,yr,zr+45]


    np.matmul(zr,xyzrotationmatrix())
    # the ur robots base is rotated 45 degrees in relation to thet tabels global system
    #the global system is configured such that
        #the dryves main axies is the x axies eg along the table
        #the y axis is across the table
        #the z is pointed skyward
    targetPosition(dryvepart)
    rob.movel_tool([poseactual[0],poseactual[1],poseactual[2],rotactual[0],rotactual[1],rotactual[2]],acc,vel)
    
    

    
def getrobopos():
       # this function sets the end effector to a position in our table space

    edgedistance=200 #20 cm
    ur10zrotoffset=45 
    zr(ur10zrotoffset*(np.pi/180))
    
    np.matmul(zr,xyzrotationmatrix())
    # the ur robots base is rotated 45 degrees in relation to thet tabels global system
    #the global system is configured such that
        #the dryves main axies is the x axies eg along the table
        #the y axis is across the table
        #the z is pointed skyward

        # get end effector matrix of the robot in the robots cordinate system
        # pre multiply it by a -45 degree x rotation matrix 
        # 
    pos=rob.get_pos
    [a,b,y]=rob.get_orientation
    eemat=m3x3to4x4(xyzrotationmatrix(a,b,y))
    eemat[0,3]=pos[0]
    eemat[1,3]=pos[1]
    eemat[2,3]=pos[2]

    

    return np.matmul(m3x3to4x4(zr(-ur10zrotoffset*(np.pi/180))),eemat)

    
def xyzrotationmatrix(a,b,y):
    #a=alpha=x rot,b=beta=y rot, y=gamma=z rot
    return np.matrix([[c(b)*c(y),s(a)*s(b)*c(y)-c(a)*s(y),c(a)*s(b)*c(y)+s(a)*s(y)],
                      [c(b)*s(y),s(a)*s(b)*s(y)+c(a)*c(y), c(a)*s(b)*s(y)-s(a)*c(y)],
                      [-s(b),s(a)*c(b),c(a)*c(b)]])
def xr(a):
    return np.matrix([[1,0,0],[0,c(a),-s(a)],[0,s(a),c(a)]])
def yr(a):
    return np.matrix([[c(a),0,s(a)],[0,1,0],[-s(a),0,c(a)]])
def zr(a):
    return np.matrix([[c(a),-s(a),0],[s(a),c(a),0],[0,0,1]])

def m3x3to4x4(m3x3):
    m3x4=np.matmul(np.matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,0]]),m3x3)
    return np.matmul(m3x4,np.identity(4))
    



def s(a):
    return np.s(a)
def c(a):
    return np.c(a)    



    




def movement_callback(msg):
    if(msg[8]<0):
        stopmove()
        seteepos(msg[0],msg[1],msg[2],msg[3],msg[4],msg[5],msg[6],msg[7])






if __name__ == '__main__':
    rospy.init_node("robot_mover")
    initializeall()

    rospy.loginfo("i have begun")

    rospy.sleep(1)
    sub=rospy.Subscriber("/controll/movetarget",float[9],callback=movement_callback)
    pub=rospy.Publisher("/info/robotpose",float[7],queue_size=1)

    rospy.loginfo("i have ended")

    rate = rospy.Rate(10)

    while( not rospy.is_shutdown):
        complete=False
        
        if(not complete):
            dist=0
            pos=rob.get_pos
            for x in range(8):
                dist+=abs(currobotconfig[x]-pos)

            if(dist<5):
                complete=True
            else:
                arrret=[]
                currobotconfig=rob.get_pos
                arrret.extend(curdryveconfig)
                # first 6 entries in the array are pos rot
                arrret.append(float(rob.is_running())*10)
                # the last 1 is a logical state if the robot is curently moving
                pub.publish(arrret)
            rospy.sleep(rate)
        else:
            rospy.spin()





    


