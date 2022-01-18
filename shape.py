import cv2
import numpy as np

img = cv2.imread('shapes.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

flag = 0

for cnt in contours:

    if flag==0:
        flag=1
        continue
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [cnt], 0, (0, 0, 255), 5)


    #centroid
    M = cv2.moments(cnt)
    x = int(M['m10']/M['m00'])
    y = int(M['m01']/M['m00'])
    
    #area
    area = cv2.contourArea(cnt)
    
    
    
    if len(approx) == 3:
        cv2.putText(img, f'Triangle, Area {area}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
  
    elif len(approx) == 4:
        cv2.putText(img, f'Rectangle, Area {area}', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
  
    elif len(approx) == 5:
        cv2.putText(img, f'Pentagon Area {area}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
  
    elif len(approx) == 10:
        cv2.putText(img, f'Star Area {area}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
  
    else:
        cv2.putText(img, f'circle Area {area}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

cv2.imshow('shapes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()