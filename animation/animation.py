import cv2
import numpy as np

image=cv2.imread("/Users/Arora/Desktop/AOA-Jetlearn projects/opencv/images_cuz_yas/sukuna.jpg",cv2.IMREAD_COLOR)

#drawing speech bubbles
def speech_bubbles(img,pos,text):
    x,y=pos
    cv2.ellipse(img,pos,(170,80),0,0,360,(255,255,255),4)
    cv2.putText(img,text,(x-80,y-40),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),4)
    coords=np.array([[x-85,y-10],[x-65,y-40]])
    cv2.polylines(image,coords,False,(255,255,255),4)

speech_bubbles(image,(500,500),"Hello I am not a human being")
cv2.imshow("test,",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
    