import cv2
import numpy as np


# Car[1,0]
# Human [0,1]

train_X = []
train_Y = []

test_X = []
test_Y = []

for i in range(1,101):
    image = cv2.imread("Obje-Veri-Seti/Car-Train/Araba-"+str(i) + ".jpg")
    image = cv2.resize(image, (224,224))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    train_X.append([image])
    
for i in range(1,101):
    image = cv2.imread("Obje-Veri-Seti/Human-Train/insan-"+str(i) + ".jpg")
    image = cv2.resize(image, (224,224))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    train_X.append([image])

for i in range(1,101):
    train_Y.append([1,0])#Car
for i in range(1,101):
    train_Y.append([0,1])#Human
    

################## DERİN ÖĞRENME AĞI ##############
    
    
from keras import models
from keras import layers
from keras.layers import Dense, Flatten, Reshape

model = models.Sequential()
model.add(layers.Dense(2048,activation = "relu", input_shape = (1,224,224,)))
model.add(Flatten())
model.add(layers.Dense(2, activation = "softmax"))

################ DATA SETİ ŞEKİLLENDİR ################

train_X = np.array(train_X)
train_X.reshape(-1,224,224)
print(train_X.shape)

################## EĞİTİM Y NUMPY DİZİSİ HALİNE GEİTMREK ########### 
train_Y = np.array(train_Y)


############## COMPİLE ############


model.compile(optimizer="Adam",
             loss="categorical_crossentropy",
             metrics = ["accuracy"])




############# MODELİ EĞİTMEK ############


model.fit(train_X,train_Y,epochs= 20, batch_size = 64)




############### RESİM İLE TEST #############


testCar = cv2.imread("Obje-Veri-Seti/Car-Test/Araba-26.jpg")
testCar = cv2.resize(testCar, (224,224))
testCar = cv2.cvtColor(testCar, cv2.COLOR_RGB2GRAY)

testHuman = cv2.imread("Obje-Veri-Seti/Human-Test/insan-15.jpg")
testHuman = cv2.resize(testHuman, (224,224))
testHuman = cv2.cvtColor(testHuman, cv2.COLOR_RGB2GRAY)

testPen = np.array([testCar])
model.predict(testPen.reshape(-1,1,224,224))

