import keyboard
import time
from grabscreen import grab_screen
import cv2
import numpy as np
from keras.models import load_model

model = load_model("GTA(25.12.5).h5")

####### TEST ALEXNET MODEL #########

last_time = time.time()
while True:
    Image = grab_screen((101, 51, 650, 600))
    Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
    prediction = cv2.cvtColor(Image, cv2.COLOR_RGB2GRAY)
    prediction = cv2.resize(prediction, (224, 224))
    prediction_array = np.array([prediction])
    value = model.predict(prediction_array.reshape(-1, 224, 224, 1))
    if value[0][0] > 0.98:
        print("CAR")
    elif value[0][1] > 0.98:
        print("HUMAN")
    else:
        print("WHAT IS THAT?")
    print("FPS {} ".format(((time.time()-last_time)**(-1))))
    last_time = time.time()
    cv2.imshow("Screen", prediction)
    key = cv2.waitKey(100)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
