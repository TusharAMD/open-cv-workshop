import cv2
 
 
def on_change(val):
    #print(val)
    pass
img = cv2.imread('newspaper.jpg')
cv2.namedWindow('frame')
cv2.createTrackbar('from', "frame", 0, 255, on_change)
cv2.createTrackbar('to', "frame", 0, 255, on_change)
while True: 

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    from_val = cv2.getTrackbarPos('from','frame')
    to_val = cv2.getTrackbarPos('to','frame')
    
    print(from_val,to_val)
    ret,thresh_img = cv2.threshold(gray_img, from_val, to_val, cv2.THRESH_BINARY) 
    #cv2.imshow("image", img)
    cv2.imshow("frame", thresh_img)
    k = cv2.waitKey(1)
    if k==27:
        break
    
    
        
cv2.destroyAllWindows()