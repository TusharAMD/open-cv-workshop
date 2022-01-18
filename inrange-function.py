import cv2

#img = cv2.imread("color-model.png")
img = cv2.imread("apple.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask1 = cv2.inRange(hsv, (0, 50, 0), (15, 255,255))

mask2 = cv2.inRange(hsv, (170,0,0), (180, 255, 255))


mask = cv2.bitwise_or(mask1, mask2)

target = cv2.bitwise_and(img,img, mask=mask)

cv2.imshow("result", target)
cv2.waitKey(0)