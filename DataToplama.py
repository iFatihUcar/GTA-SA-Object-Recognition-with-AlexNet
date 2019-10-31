import keyboard
import time
from grabscreen import grab_screen
import cv2

######## EKRAN TESTİ İÇİN
# last_time = time.time()
# while True:
#     resim = grab_screen((200,230,1000,640))
#     print("Nö")
#     print("FPS {} ".format(time.time()-last_time))
#     last_time = time.time()
#     cv2.imshow("Pencere", resim)
#     if cv2.waitKey(100) and 0xFF == ord("q"):
#         cv2.destroyAllWindows()
#         break
#
sayı = 0
while True:
    key = keyboard.read_key()
    if key == "k" or key == "K":
        sayı += 1
        print("Aynen kanka oldu")
        resim = grab_screen()
        cv2.imwrite("Araba\Araba-"+ str(sayı)+".jpg", resim)
        time.sleep(0.1)
    if key == "p":
        while True:
            cv2.imshow("Pencere", resim)
            key = cv2.waitKey(0)
            if key == ord("s"):
                cv2.destroyAllWindows()
                break
