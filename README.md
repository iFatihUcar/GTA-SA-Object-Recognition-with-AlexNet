
<h1> Grand Theft Auto San Andreas Object Recognition </h1>

I used Alexnet on Keras.
If you want to run algorithm. You must setup this following librarys.

- numpy
- opencv-python
- tensorflow-gpu ( before you need to instal CUDA and cudNN ) 
- keras
- costum grabscreen algoritihm created by Frannecklp
- keyboard

Here is the modded game link : GAME LINK

Here is the trained model : [CNN MODEL ( old version ) ](https://www.mediafire.com/file/s8ljjiczhx0hddo/GTA%2825.12.5%29.rar/file)

<h1> Dataset </h1>

Dataset contains 5000 car and image 5000 human image.
Here is the some samples.

<h4> Human </h4>

![human](https://github.com/mcagricaliskan/GTA-SA-Object-Recognition/blob/master/Dataset/human/human-24.jpg?raw=true)


<h4> Car </h4>

![car](https://github.com/mcagricaliskan/GTA-SA-Object-Recognition/blob/master/Dataset/car/car-14.jpg?raw=true)



Dataset is 1 GB. so i cant upload here. I upload it MeadiaFire.
Here is the link : [Dataset LINK](https://www.mediafire.com/file/uqa8v4ej9jz884o/Dataset.rar/file).

Dataset collectec by İsmail Fatih Uçar


<h1> Data Augmentation </h1>

First I resized images to 227x227 and recolor it gray for feeding CNN.

I used 3 augmentation method. ( need to be increased with different and useful methods for this case.)







