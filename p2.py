import cv2

img = cv2.imread("428690.jpg")

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)	# convert color in to gray

cv2.imwrite("Gray_428690.jpg",grayImg)

cv2.imshow("original", img)
cv2.imshow("Gray", grayImg)

cv2.waitKey(0)

cv2.destroyAllWindows()