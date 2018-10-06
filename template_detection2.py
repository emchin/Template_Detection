import cv2
import numpy as np
from matplotlib import pyplot as plt

#If the SCREENSHOT/BIG PICTURE used has a different name (ex: "screenshot2.jpg")
#Change the string name (link) below:
imgFile = '/Users/emily/Desktop/screenshot.jpg'
img_rgb = cv2.imread(imgFile, 0)

# Check if the imread command worked
if img_rgb is None:
    print ("Could not read:", imgFile)

#If the TEMPLATE used has a different name (ex: "template2.jpg")
#Then change the string name (link) below:
inFile = '/Users/emily/Desktop/template.jpg'

templateFile = inFile

template = cv2.imread(templateFile,0)
if template is None: # <-- Meaning: if the program can't pull up the template
    print("Could not read:", templateFile)

#h, w = template.shape[::-1]
h,w = template.shape[::-1]
print (h,w)

# Now look for the template in the image file
res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold) #loc = where the picture is border of template
for pt in zip(*loc[::-1]): #this is an inverse zip of loc (as seen above)
    cv2.rectangle(img_rgb, pt, (pt[0] + h, pt[1] + w), (0,0,255), 2)
#This command creates the two individual boxes around the identified templates
#pt[0] is the x-coordinates of the left side of the border
#pt[1] is the y-coordinates of the top of the border
#pt[0] + w takes edge of the template on image, adds w and creates right wall
#pt[1] + h takes bottom of template, adds h and creates bottom

#For all x-values in the big picture:
for x in loc[:0:-1]:
	firstx = min(x) + 8 #this is the far left of the picture
	secondx = max(x) + w + 16 #this is the far right of the picture

#For all y-values in the big picture:
for y in loc[0::-1]:
	firsty = max(y) +  h + 8 #this is the bottom of the picture
	secondy = min(y) + 4 #this is the top of the picture

#The numbers above in purple (+8, +4 and +16) can be changed for cosmetics...haven't quite figured that out

#This creates the larger rectangle between the two found templates.
cv2.rectangle(img_rgb, (firstx, firsty), (secondx, secondy), (0,0,255), 2)
#(firstx, firsty) gives the coordinate point for the bottom left corner
#(secondx, secondy) gives the coordinate point for the top right corner

#print pt[0]
#print loc[0::-1]
#print loc[:0:-1]

# display the image
cv2.imshow('res', img_rgb)

#If you want to save the image (for funsies), un-comment the lower code:
cv2.imwrite('example.png',img_rgb)

# show screen until a certain key is pressed
# the key it is looking for is '0' 'zero'
# although ESC works as well
key = 0
if cv2.waitKey(key) & 0xff == 27:
  cv2.destroyAllWindows()
