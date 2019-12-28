# This file shows us sample of data augmentation methods we used.

import cv2

image = cv2.imread("Dataset/car/car-1.jpg")
image = cv2.resize(image, (224,224))
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
Augment1 = cv2.flip(image, 1)
a,Augment2 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
a,Augment3 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)

while True:
    cv2.imshow("1", image)
    cv2.imshow("2", Augment1)
    cv2.imshow("3", Augment2)
    cv2.imshow("4", Augment3)

    key = cv2.waitKey(100)
    if key == ord("q"): #  if you want to exit press 'q'
        cv2.destroyAllWindows()
        break