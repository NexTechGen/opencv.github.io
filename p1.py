import cv2	# import opencv library

img = cv2.imread("parrot.jpg")	# read an image

cv2.imwrite("Open_CV_parrot.png",img)	# save an image

cv2.imshow("Open_CV",img)
cv2.waitKey(0)

cv2.destroyAllWindows()