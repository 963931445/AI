import numpy as np
import cv2

import numpy as ny
import cv2
def distance(one,two):
  return ny.sqrt(ny.sum((one-two)*(one-two)))

img=cv2.imread("1.jpg");
w=img.shape[1]
h=img.shape[0]
myimg=ny.zeros((h,w,3))
black=ny.array([0,0,0]);
white=ny.array([255,255,255]);
gray=ny.array([125,125,125]);
yz =23
for y in range(0,h-1):
  for x in range(0,w-1):
    current=img[y,x,:]
    right=img[y,x+1,:]
    down=img[y+1,x+1,:]
    if distance(current,right)>yz and distance(current,down)>yz:
      myimg[y,x,:]=black;
    elif   distance(current,right)<=yz and distance(current,down)<=yz:
      myimg[y, x, :] = white;
    else:
      myimg[y, x, :]=gray;

cv2.imwrite("2.jpg",myimg);
cv2.destroyAllWindows();





