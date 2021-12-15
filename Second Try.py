import cv2

# Loading cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#capture video from webcam. 
cap = cv2.VideoCapture(0)

#use video file as input 
#cap = cv2.VideoCapture('Well Lit Conditions.mp4')

while True:
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()
