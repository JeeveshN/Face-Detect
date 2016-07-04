import cv2
import sys
import os

if not "Extracted" in os.listdir("."):
    os.mkdir("extracted")
if len(sys.argv) < 2:
    print "Usage: python Detect_face.py 'image path'"
    sys.exit()
image_path=sys.argv[1]
cascade="Face_cascade.xml"

face_cascade=cv2.CascadeClassifier(cascade)

image=cv2.imread(image_path)
image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(image_grey,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0)

for x,y,w,h in faces:
    sub_img=image[y-10:y+h+10,x-10:x+w+10]
    os.chdir("Extracted")
    cv2.imwrite(str(y)+".jpg",sub_img)
    os.chdir("../")
    cv2.rectangle(image,(x,y),(x+w,y+h),(255, 255,0),2)

cv2.imshow("Faces Found",image)
cv2.waitKey(0)
