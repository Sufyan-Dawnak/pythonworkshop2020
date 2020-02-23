#_______
import cv2
lst = []
for i in range(0,4):
    img = cv2.imread('galaxy{}.jpg'.format(i),1)
    lst.append(img)
#print(img)
# print(type(img))
# print(img.shape)
# print(img.ndim)
# cv2.imshow("galaxy",img)
# cv2.waitKey(3000)
# cv2.destroyAllWindows
# _______RESIZE IMAGE________
# resize_img = cv2.resize(img,(4,4000))
# cv2.imshow("newIMAGE",resize_img)
# cv2.waitKey(30000)
    r_img = cv2.resize(lst[i],((int(lst[i].shape[1]/2)),(int(lst[i].shape[1]/2))))
    # cv2.imshow("image",r_img)
    # cv2.waitKey(3000)
    cv2.imwrite("galaxy_resize{}.jpg".format(i),r_img)
    #print(img)
    
