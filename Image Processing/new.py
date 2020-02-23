import cv2
lst = []
for i in range(0,4):
    img =  cv2.imread("galaxy{}.jpg".format(i),1)
    lst.append(img)
    r_img = cv2.resize(lst[i],((int(lst[i].shape[1]/3)),(int(lst[i].shape[0]/3))))
    cv2.imwrite("galaxy_resized{}.jpg".format(i),r_img)