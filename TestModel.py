import keyboard
import time
from grabscreen import grab_screen
import cv2
import numpy as np
from keras.models import load_model

model = load_model("GTA(18.24).h5")


 ####### EKRAN TESTİ İÇİN
last_time = time.time()
while True:
    resim = grab_screen((101,51,650,600))
    resim = cv2.cvtColor(resim, cv2.COLOR_BGR2RGB)
    Tahmin = cv2.cvtColor(resim, cv2.COLOR_RGB2GRAY)
    Tahmin = cv2.resize(Tahmin, (224,224))
    TahminDizi = np.array([Tahmin])
    Deger = model.predict(TahminDizi.reshape(-1,224,224,1))
    if Deger[0][0] > 0.99:
        print("Araba")
    elif 0.99 < Deger[0][1]:
        print("İnsan")
    else:
        print("Bu ne la")
    print("FPS {} ".format(time.time()-last_time))
    last_time = time.time()
    cv2.imshow("Pencere", Tahmin)
    key = cv2.waitKey(100)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
