import cv2
import numpy as np 

#The image is now in BGR (sketchy? adjust if necessary)
img = cv2.imread('/Users/emily/Desktop/red_balloons.jpg', 1)

#The BGR image is now in HSV with this:
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#The array is the lowest and highest range of BGR for the color red.
#Meaning: what range of colors is "red"?
#dtype simply says that the data type will be an 8-digit integer
lower_range = np.array([169, 100, 100], dtype=np.uint8)
upper_range = np.array([189, 255, 255], dtype=np.uint8)

#The mask is the area (in hsv) where the pixels are within the uppper and lower ranges
mask = cv2.inRange(hsv, lower_range, upper_range)

#This code below is trying to map the white pixels to a coordinate plane
listy = []    #---stores coordinate corresponding to height of the image
listx = []    #---stores coordinate corresponding to width of the image

#mask.shape[0] is a numpy function. 
#mask.shape(n, m) where n = rows and m = columns
#So mask.shape[0] is max number of rows, and we iterate from 0 to max
#And mask.shape[1] is max number of columns, and we iterate from 0 over that
for y in range(0, mask.shape[0]):
    for x in range(0, mask.shape[1]):
        if(mask[y, x] == 255):
            listy = np.append(listy, y)
            listx = np.append(listx, x)

maxy = int(max(listy))
maxx = int(max(listx))

miny = int(min(listy))
minx = int(min(listx))

#miny + maxx = top left corner
#maxy + minx = bottom right corner

cv2.rectangle(img, (minx, maxy), (maxx, miny), (255, 0, 0), 3)

#This apparently shows the original image? You can delete this unnecessary
cv2.imshow('image', img)

crop_img = img[miny: maxy, minx: maxx]
cv2.imshow('cropped', crop_img)
cv2.imwrite('/Users/emily/Desktop/cropped.jpg', crop_img)

# Wait until 'ESC' key it entered in picture frame
# 27 is ASCII value of ESC key
while(1):
	k = cv2.waitKey(0)
	if (k==27):
		break

cv2.destroyAllWindows()