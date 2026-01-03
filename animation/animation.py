import cv2
import numpy as np
from tkinter import *
#w=Tk()

WIDTH=1920
HEIGHT=1080

bg=cv2.imread("/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/images_cuz_yas/sukuna.jpg",cv2.IMREAD_COLOR)

bg=cv2.resize(bg,(WIDTH,HEIGHT))

#drawing speech bubbles
def speech_bubbles(img,pos):
    x,y=pos

    cv2.ellipse(img,pos,(190,80),0,0,360,(255,255,255),4)
    coords=np.array([[[x-105,y-60],[x-105,y-100],[x-75,y-70]]])
    cv2.polylines(img,coords,False,(255,255,255),4)

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

speech_bubbles(bg,(720,750))
multiline_text(bg,(600,730),"Hello I am not a human being")


cv2.imshow("test,",bg)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
