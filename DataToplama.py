import keyboard
import time
from grabscreen import grab_screen
import cv2

# ####### EKRAN TESTİ İÇİN
# last_time = time.time()
# while True:
#     resim = grab_screen((101,51,650,600))
#     print("Nö")
#     print("FPS {} ".format(time.time()-last_time))
#     last_time = time.time()
#     cv2.imshow("Pencere", resim)
#     if cv2.waitKey(100) and 0xFF == ord("q"):
#         cv2.destroyAllWindows()
#         break

# KAYIT KISMI
sayı = 0
sayac=0
while True:
    key = keyboard.read_key()
    if key == "k" or key == "K":
        sayı += 1
        sayac += 1
        print(sayac)
        resim = grab_screen((101,51,650,600))
        resim = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)
        cv2.imwrite("car\car-"+ str(sayı)+".jpg", resim)
        time.sleep(0.1)
    if key == "p":
        while True:
            cv2.imshow("Pencere", resim)
            key = cv2.waitKey(0)
            if key == ord("s"):
                cv2.destroyAllWindows()
                break