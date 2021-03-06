import cv2

#Open a image file
img = cv2.imread('2.jpg')

#Open a png (retain transparency)
#img = cv2.imread('transparent.png',cv2.IMREAD_UNCHANGED)

print(img)
print(f"num of dim {img.ndim}")
print(img.shape) #shape of image 3 for channels and if 4 then alpha

#accessing every pixel using loops
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        print(f"{i+1},{j+1} -> {img[i][j]}")
        img[i][j]=100

#write image after changes
cv2.imwrite("2changed.jpg",img)

#show preview
cv2.imshow("frame1",img)
cv2.waitKey(0) #if not mentioned image will close instantly
