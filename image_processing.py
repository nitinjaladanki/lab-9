import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("baby_turtle.jpg") 
dimensions = img.shape
print(dimensions)
blue_turtle = img[:,:,0]
green_turtle = img[:,:,1]
red_turtle = img[:,:,2]
fig, ax = plt.subplots(1,3, figsize = (15, 10))
ax[0].imshow(red_turtle, cmap="Reds")
ax[1].imshow(green_turtle, cmap="Greens")
ax[2].imshow(blue_turtle, cmap="Blues")
plt.show()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

hue_turtle = hsv[:,:,0]
sat_turtle = hsv[:,:,1]
val_turtle = hsv[:,:,2]

fig, ax = plt.subplots(1,3, figsize = (15, 10))
ax[0].imshow(hue_turtle, cmap="hsv")
ax[1].imshow(sat_turtle, cmap="binary")
ax[2].imshow(val_turtle, cmap="Oranges")
fig.colorbar(plt.cm.ScalarMappable(cmap="hsv"), ax=ax)
plt.show()