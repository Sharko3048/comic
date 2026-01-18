import cv2
import numpy as np
from tkinter import *
#w=Tk()

WIDTH=1920
HEIGHT=1080

frames={"frame1":{
    "bubble1":(710,750),
    "bubble2":(1200,330),
    "text1":(600,730),
    "text2":(1050,320),
    "char1":(450,750),
    "char2":(1500,750)
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
    maxchar=20
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

bg=cv2.imread("/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/animation/images_4_animation/white.png",cv2.IMREAD_COLOR)
bg=cv2.resize(bg,(WIDTH,HEIGHT))



char2=cv2.imread("/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/animation/images_4_animation/Barry_Buns_S2.webp",cv2.IMREAD_UNCHANGED)
char1=cv2.imread("/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/animation/images_4_animation/kiff.png",cv2.IMREAD_UNCHANGED)
char1=cv2.resize(char1,(CHAR_WIDTH,CHAR_HEIGHT))
char2=cv2.resize(char2,(CHAR_WIDTH,CHAR_HEIGHT))
panel=overlay_image(bg,char1,frames["frame1"]["char1"])
panel=overlay_image(panel,char2,frames["frame1"]["char2"])


speech_bubbles(panel,frames["frame1"]["bubble1"],"top-left")
multiline_text(panel,frames["frame1"]["text1"],"Hello I am not a human being")
speech_bubbles(panel,frames["frame1"]["bubble2"],"bottom-right")
multiline_text(panel,frames["frame1"]["text2"],"yaasssssssssssssssss")


cv2.imshow("test,",panel)
cv2.waitKey(0)
cv2.destroyAllWindows()
