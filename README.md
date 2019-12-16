# Template Detection
# This was the 2017-2018 project for the Python team in Tinovation.

The 2017-2018 "Notes" project hoped to use a Raspberry Pi to record a teacher's whiteboard throughout lecture. During the lecture, the Pi would stream images to a database, which would (a) identify the space within which the teacher was writing, and then (b) identify what was written.

We successfully identified the space within which the teacher was writing; however, due to time constraints, we were ultimately unable to reach out second goal of text identification.

We knew that this tastk would involve computer vision. After several attempts of trial and error, we found the sample code "face_detect.py", with which we were able to detect faces in "messi.jpg," "abba2.jpg" and "abba2.png". With this small success being achieved across multiple OS in our team, we decided that the libraries used in "face_detect.py", namely, OpenCV and numPy, were optimal in achieving our goals.

For our first attempt at identifying the text space, we tried identifying templates based off of color. To do this, we created "color_detection.py".
The input image, "color_screenshot.jpg", would have a red template in the bottom left and top right corners of a whiteboard.
The program identifies thresholds of color (in this case, red) and found the furthest xy coordinates that fit in the threshhold.
The program would then create an image called "cropped.jpg" that contained only the area between the two red templates.
This was successful in that it could find the area between the two colored symbols.

Then we realized that to be more accurate, it would help to identify templates based off of their shape.
Our second attempt was "template_ddetection2.py", which had input "template.jpg" and "screenshot.jpg".
The code searches "screenshot.jpg" and finds matching templates based off of the sample "template.jpg". It then draws a box around the two templates that are the furthest apart, and then draws a bigger box around that.
