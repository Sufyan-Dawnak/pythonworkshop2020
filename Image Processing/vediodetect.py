import cv2
video = cv2.VideoCapture("faceDetection.mp4")
# check, frame = video.read()
# print(type(video))
# print(type(check))
# print(frame)
'''___BY ME__
while True:
    check, frame = video.read()
    cv2.imshow("vedio ka frame",frame)
    cv2.waitKey(2500)
cv2.destroyAllWindows
video.release()'''
check = True
while check:
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    check, frame = video.read()
    img = frame
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.45,minNeighbors=5)

    for x,y,w,h in faces :
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    
    cv2.imshow("vedio frame",frame)
    key = cv2.waitKey(1)
    if(key== ord('q')):
        break

cv2.destroyAllWindows
video.release()