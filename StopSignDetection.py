import cv2

##passed in image
img = cv2.imread('Testing\StopSignTest.jpg')

# convert color image to grey image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Trained model goes here
ss = cv2.CascadeClassifier('StopSign.xml')

# detect stop signs

stop = ss.detectMultiScale(gray_img)

#Bounding box



# draw rectangle around the stop signs
for (x,y,w,h) in stop:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
    cv2.putText(img, 'Stop Sign', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)


cv2.imshow('Screen',img)

cv2.waitKey()
