import cv2
import numpy as np
from tkinter import *
#w=Tk()

WIDTH=1920
HEIGHT=1080

frames={"frame1":{
    "bubble1":(720,700),
    "bubble2":(1450,680),
    "text1":(600,680),
    "text2":(1405,695),
    "char1":(450,750),
    "char2":(1500,750),
    #"char3":(1200,730)
},
"frame2":{
    "bubble1":(710,330),
    "bubble2":(1200,750),
    "text1":(600,320),
    "text2":(1050,730),
    "char1":(450,750),
    "char2":(1500,750)
}}

spb_triangle={"top-left":[-105,-60,-105,-100,-75,-70],
        "top-right":[105,-60,105,-100,75,-70],
        "bottom-left":[-105,60,-105,100,-75,70],
        "bottom-right":[105,60,105,100,75,70]}

#drawing speech bubbles
def speech_bubbles(img,pos,triangle_pos):
    x,y=pos
    tp=spb_triangle[triangle_pos]

    cv2.ellipse(img,pos,(190,80),0,0,360,(0,0,0),4)
    coords=np.array([[[x+tp[0],y+tp[1]],[x+tp[2],y+tp[3]],[x+tp[4],y+tp[5]]]])
    cv2.polylines(img,coords,False,(0,0,0),4)

def multiline_text(img,pos,text):
    x,y=pos
    maxchar=15
    linegap=45
    words=text.split()
    lines=[]
    line=""
    for word in words:
        if len(line)+len(word)<=maxchar:
            line=line+word+" "
        else:
            lines.append(line.strip())
            line=word+" "
    lines.append(line.strip())
    for line in lines:
        cv2.putText(img,line,(x,y),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),4)
        y+=linegap

CHAR_WIDTH=300
CHAR_HEIGHT=300

def overlay_image(bg,char,pos):
    x,y=pos
    b,g,r,a=cv2.split(char)
    alpha=(a/255)
    for i in range(3):
        bg[y:y+CHAR_HEIGHT,x:x+CHAR_WIDTH,i]=char[:,:,i]*alpha + (1-alpha)*bg[y:y+CHAR_HEIGHT,x:x+CHAR_WIDTH,i]
    return bg

filepath="/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/animation/"
imgfpath="images_4_animation/"
fname="comic.txt"

file=open(filepath+fname,"r")

for line in file:
    info=line.strip().split(",")
    frame=info[1]

    bg=cv2.imread(filepath+imgfpath+info[0],cv2.IMREAD_COLOR)
    bg=cv2.resize(bg,(WIDTH,HEIGHT))

    print(filepath+imgfpath+info[2],)

    char1=cv2.imread(filepath+imgfpath+info[2],cv2.IMREAD_UNCHANGED)
    char2=cv2.imread(filepath+imgfpath+info[5],cv2.IMREAD_UNCHANGED)
    #char3=cv2.imread(filepath+imgfpath+info[8],cv2.IMREAD_UNCHANGED)
    char1=cv2.resize(char1,(CHAR_WIDTH,CHAR_HEIGHT))
    char2=cv2.resize(char2,(CHAR_WIDTH,CHAR_HEIGHT))
    #char3=cv2.resize(char3,(CHAR_WIDTH,CHAR_HEIGHT))
    panel=overlay_image(bg,char1,frames[frame]["char1"])
    panel=overlay_image(panel,char2,frames[frame]["char2"])
    #panel=overlay_image(panel,char3,frames[frame]["char3"])

    speech_bubbles(panel,frames[frame]["bubble1"],info[4])
    multiline_text(panel,frames[frame]["text1"],info[3])
    speech_bubbles(panel,frames[frame]["bubble2"],info[7])
    multiline_text(panel,frames[frame]["text2"],info[6])

    cv2.imshow("test,",panel)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
