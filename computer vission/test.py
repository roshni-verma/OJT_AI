import cv2
import numpy as np

#read the image with the particular liabrary which we have imported
image = cv2.imread('cat.jpg')

if image is None:
    print("could not read the image")
    exit()

#orginal image
cv2.imshow('orginal image',image)
cv2.waitKey(0)  
cv2.destroyAllWindows()  

#convert to greyscale
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("greyscale image")

#we aplly a gaussion blur into the above image
blurred_image = cv2.GaussianBlur(grey_image,(5,5),0)
cv2.imshow('blur image',image)
cv2.waitKey(0)  
cv2.destroyAllWindows()  

#edge detection by using canny in cv2
edges = cv2.Canny(blurred_image,50,150)

cv2.imshow('orginal image',image)
cv2.waitKey(0)  

cv2.imshow('greyscale image',grey_image)
cv2.waitKey(0)  


cv2.imshow('blurred image',blurred_image)
cv2.waitKey(0)  

cv2.imshow('edges image',edges_image)
cv2.waitKey(0)  

 
cv2.destroyAllWindows()  





