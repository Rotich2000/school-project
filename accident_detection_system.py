# Open Source Computer Vision Library(opencv) => is an open-source library that includes several hundreds of computer vision algorithms
# OpenCV 2.x API is going to be used in our application,which is essentially a C++ API, 
# as opposed to the C-based OpenCV 1.x API (C API is deprecated and not tested with "C" compiler since OpenCV 2.4 releases)
# OpenCV has a modular structure meaning the package includes several shared or static libraries e.g
#  object detection, core funtionality, image processing, video annalysis, camera calibration and 3D reconstruction,Video I/O etc
import cv2 
print(cv2.__version__)

# my image
img_file = 'car.jpg'

video = cv2.VideoCapture('pedestrian.mp4')
# pedestrian_video = cv2.VideoCapture('pedestrian.mp4')


# create image using the opencv format
# img = cv2.imread(img_file)

# Convert the image to black and white
# black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# my pre-trained car-classifier
classifier_file = "car.xml"

car_tracker = cv2.CascadeClassifier(classifier_file)
pedestrian_tracker = cv2.CascadeClassifier("pedestrian.xml")

while True:
    read_successful, frame = video.read()
# If code runs successfuly then...
    if read_successful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrian = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    # print(cars) 

    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x+1,y+2), (x+w, y+h), (0,255,255), 2)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    for (x,y,w,h) in pedestrian:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,255), 2)

# Display the image using the opencv, which takes two parameters the tittle name and the image
    cv2.imshow('Car detector', frame )

# Don't auto close, wait till key press...
    cv2.waitKey(50)

    # Stop if Q is pressed
    # if key==81 or key==113:
    #      break
# stop the video and clean up the memory
video.release()

"""
# create a car classifier
# cascade => most features that i am running through in my xml file, classifier => classifying if it is a car
car_tracker = cv2.CascadeClassifier(classifier_file)


# Detect car of any scale
cars = car_tracker.detectMultiScale(black_n_white)
print(cars)

# draw rectangles around the cars

for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# Display the image using the opencv, which takes two parameters the tittle name and the image
cv2.imshow('Car detector', img )

# Don't auto close, wait till key press...
cv2.waitKey()

"""
print("code completed")