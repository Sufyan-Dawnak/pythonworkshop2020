import cv2 
  
cap = cv2.VideoCapture('cars.mp4') 
car_cascade = cv2.CascadeClassifier('cars.xml') 
while True: 
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
    cars = car_cascade.detectMultiScale(gray, 1.1, 3) 
    for (x,y,w,h) in cars: 
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2) 
    cv2.imshow("vedio frame",frames)
    key = cv2.waitKey(3)
    if(key== ord('q')):
        break
cv2.destroyAllWindows() 