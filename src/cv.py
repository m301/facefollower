# https://github.com/opencv/opencv/tree/master/data/haarcascades
import cv2
import dlib
import serial
import time

ser = serial.Serial('/dev/ttyUSB0')

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faceLBPCascade = cv2.CascadeClassifier("lbpcascade_frontalface_improved.xml")
upperCascade = cv2.CascadeClassifier("haarcascade_upperbody.xml")
eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
detector = dlib.get_frontal_face_detector()


video_capture = cv2.VideoCapture(0)
fgbg = cv2.BackgroundSubtractorMOG2()
previous = None
lastSent = None
oldData = None
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    height, width, channel = frame.shape

    # frame = cv2.GaussianBlur(frame,(2,2),0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # fgmask = fgbg.apply(frame)
    # cv2.imshow('frame',fgmask)

    # ret,thresh1 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # kernel = np.ones((1,1),np.uint8)
    # dilated = cv2.dilate(thresh1,kernel,iterations = 18)
    # cinza = cv2.erode(dilated,kernel,iterations = 10)

    # if previous is None :
    #     previous = gray
    #     continue

    # img =  previous -gray
    # previous = gray

    img = frame

    dets, scores, idx = detector.run(img, 1)
    for i, d in enumerate(dets):
        print("Detection {}, score: {}, face_type:{}".format(
            d, scores[i], idx[i]))
        cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 255, 0), 2)

        if lastSent is None or time.time() - lastSent > 1:
            serX = int((float(d.right()) / width) * 254)
            serY = int((float(d.bottom()) / height) * 180)
            data = "0;" + str(serX) + ";" + str(serY) + "\n"

            if (oldData != data):
                print data
                oldData = data
                ser.write(data)

            lastSent = time.time()

    #     faces = faceCascade.detectMultiScale(
    #         img,
    #         scaleFactor=1.1,
    #         minNeighbors=5,
    #         minSize=(30, 30),
    #         flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    #     )
    #
    #
    # # Draw a rectangle around the faces
    #     for (x, y, w, h) in faces:
    #     #
    #     #     roi_gray = gray[y:y + h, x:x + w]
    #     #     roi_color = frame[y:y + h, x:x + w]
    #     #
    #     #     eyes = eyeCascade.detectMultiScale(roi_gray)
    #     #     for (ex, ey, ew, eh) in eyes:
    #     #         cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    #     #
    #         # if len(eyes) >= 2:
    #
    #     alignedFace = align.align(image_dimension, rgbImg, bb,
    #                               landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)


    # Display the resulting frame
    cv2.imshow('Video', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        ser.close()
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
