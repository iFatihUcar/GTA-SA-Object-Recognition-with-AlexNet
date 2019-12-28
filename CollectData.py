import keyboard
import time
from grabscreen import grab_screen
import cv2

####### Screen Capture Test #########
#
# last_time = time.time()
# while True:
#     Screen = grab_screen((101,51,650,600))
#     print("FPS {} ".format(((time.time()-last_time)**(-1))))
#     last_time = time.time()
#     cv2.imshow("Screen", Screen)
#     key = cv2.waitKey(100)
#     if key == ord("q"): #  if you want to exit press 'q'
#         cv2.destroyAllWindows()
#         break

############ DataSet Record ############
NumberOf = 0
counter = 0
while True:
    key = keyboard.read_key()
    if key == "k" or key == "K":
        NumberOf += 1
        counter += 1
        print(counter)
        Image = grab_screen((101, 51, 650, 600))
        Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
        cv2.imwrite("Dataset\car\car-" + str(NumberOf) +".jpg", Image)
        time.sleep(0.1)
    if key == "p":
        while True:
            cv2.imshow("Screen", Image)
            key = cv2.waitKey(0)
            if key == ord("s"):
                cv2.destroyAllWindows()
                break