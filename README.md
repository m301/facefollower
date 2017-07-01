# facefollower

Simple face feature detection using haarcascade & dlib - follower using arduino and 3d printed parts.


# Demo
 ![demo](demo.gif)
 

# Scope
- It can be used for camera stablization by adjusting few calculation like direction of facemovement and moving accordingly to keep face at center.
- Can be combined with [openface](https://github.com/cmusatyalab/openface) to follow a specific person

- **Note :** This is not a performance oriented project, it is just experiment of idea, it has been done before.


# Hardware
- 1x Arduino
- 2x Servo

Get any xy model with a mount, connect X-Axis to `GPIO9` and Y-Axis to `GPIO8`, upload [arduino.ino](arduino/arduino.ino) to your board.

# Software 

 - Install `OpenCV2`, `dlib` manually.
 - Install library for serial communication using `pip install pyserial`
 - Execute facedetector and follower using `python src/cv.py`
