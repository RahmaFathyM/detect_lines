##import cv2
##import numpy as np
##img = cv2.imread(r"C:\Users\DELL\OneDrive\Desktop\x.png")
###gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
###cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
##circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,
## param1=100,param2=30,minRadius=0,
## maxRadius=0)
##circles = np.uint16(np.around(circles))
##for i in circles[0,:]:
## # draw the outer circle
## cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
## # draw the center of the circle
## cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
##cv2.imwrite("planets_circles.jpg", img)
##cv2.imshow("HoughCirlces", img)
##cv2.waitKey()
##cv2.destroyAllWindows()
import cv2
import numpy as np
img = cv2.imread(r"C:\Users\DELL\OneDrive\Desktop\detect lines\bgr.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,200,apertureSize=3 )
minLineLength = 10
maxLineGap = 2
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,
 maxLineGap)#2nd para rho =xcos theta+y sin theta  ,3rd para theta ,4th threshold
#print(lines.size)
for x in range(lines.shape[0]):
 for x1,y1,x2,y2 in lines[x]:
  cv2.line(img,(x1,y1),(x2,y2),(255,255,0),1)#last parameter refer to thickness of line
cv2.imshow("edges", edges)
cv2.imshow("lines", img)
cv2.imwrite("lines_detect.png",img)
cv2.waitKey()
cv2.destroyAllWindows()
