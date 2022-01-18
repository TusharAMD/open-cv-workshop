import cv2

#img = cv2.imread('1.jpg')

img = cv2.imread('newspaper.jpg')


print(img.shape)

#resize - first parm img then tuple with size and then interpolation method
resized_img = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)

#Drawing Circle
#cv2.circle(img, center, radius, color[,thickness [, lineType[,shift]]])  
cv2.circle(img, (100,100), 50, (255,0,255),5)

#Draw a rectangle
#cv2.rectangle(img, pt1, pt2, color[, thickness[,lineType[,shift]]])

#Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(gray_img.shape)
#print(gray_img)

#Threshold
ret,thresh_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_BINARY) 


cv2.imshow("image", img)
cv2.imshow("thresh", thresh_img)

cv2.waitKey(0)

