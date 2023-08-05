import cv2

img = cv2.imread("428690.jpg")

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ThresImg = cv2.threshold(grayImg,190,190,cv2.THRESH_BINARY)[1]

cv2.imwrite("threshold_428690_190_190.jpg",ThresImg)

cv2.destroyAllWindows()