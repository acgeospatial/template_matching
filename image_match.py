import cv2
import numpy as np

## image canvas
img_rgb = cv2.imread('...canvas')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

## template image
template = cv2.imread('...template',0)
## dimensions
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

#### Adjust this threshold value to suit you, you may need some trial runs
threshold = 0.45
loc = np.where( res >= threshold)

## create empty lists to append the coord of the 
lspoint=[]
lspoint2=[]
count = 0
for pt in zip(*loc[::-1]):
	## check that the coords are not already in the list, if they are then skip the match
	if pt[0] not in lspoint and pt[1] not in lspoint2:
		#### draw a yellow boundary around a match
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
		for i in range(((pt[0])-9), ((pt[0])+9),1):
			## append the x cooord
			lspoint.append(i)
		for k in range(((pt[1])-9), ((pt[1])+9),1):
			## append the y coord
			lspoint2.append(k)
		count+=1 ### count the number of matches
	else:
		continue
print "total objects found ", count

## show the images matched	
cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

