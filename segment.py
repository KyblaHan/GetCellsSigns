import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from skimage import io
from skimage import segmentation
from skimage.color import rgb2gray
from skimage.exposure import histogram
from skimage.feature import canny
from skimage.filters import sobel

path = r"C:\_Programming\TestSegment\out\Output101.bmp"

image = io.imread(path)
gray = rgb2gray(image)

hist, hist_centers = histogram(gray)

fig, axes = plt.subplots(1, 2, figsize=(8, 3))
axes[0].imshow(gray, cmap=plt.cm.gray)
axes[0].axis('off')
axes[1].plot(hist_centers, hist, lw=2)
axes[1].set_title('histogram of gray values')
plt.xticks(np.arange(0.2, 1, 0.1))
plt.grid()
plt.show()

elevation_map = sobel(gray)

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(elevation_map, cmap=plt.cm.gray)
ax.set_title('elevation map')
ax.axis('off')
plt.show()

markers = np.zeros_like(gray)
markers[gray < 0.5] = 1
markers[gray > 0.6] = 2

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(markers, cmap=plt.cm.nipy_spectral)
ax.set_title('markers')
ax.axis('off')
plt.show()

segmentation = segmentation.watershed(elevation_map, markers)

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(segmentation, cmap=plt.cm.gray)
ax.set_title('segmentation')
ax.axis('off')
plt.show()
io.imsave("test.bmp", segmentation)
# io.imsave("test.bmp",elevation_map)

image = cv2.imread(path)
image_g = cv2.imread("test.bmp")
edged = cv2.Canny(image_g, 10, 15)
cv2.imshow('canny edges', edged)

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(edged, cmap=plt.cm.nipy_spectral)
ax.set_title('edged')
ax.axis('off')
plt.show()

contours, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# cv2.imshow('canny edges after contouring', edged)
# use -1 as the 3rd parameter to draw all the contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
cv2.imshow('contours', image)

print(len(contours))
img = cv2.imread(path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
for i in range(0, len(contours)):
    if cv2.contourArea(contours[i]) > 3400:
        idx = i  # The index of the contour that surrounds your object
        mask = np.zeros_like(gray)  # Create mask where white is what we want, black otherwise
        cv2.drawContours(mask, contours, idx, 255, -1)  # Draw filled contour in mask
        out = np.zeros_like(img)  # Extract out the object and place into output image
        out[mask == 255] = img[mask == 255]
        # Now crop
        (y, x) = np.where(mask == 255)
        (topy, topx) = (np.min(y), np.min(x))
        (bottomy, bottomx) = (np.max(y), np.max(x))
        out = out[topy:bottomy + 1, topx:bottomx + 1]

        # Show the output image
        cv2.imshow('Output' + str(i), out)
        cv2.imwrite('out\Output' + str(i) + ".bmp", out)

cv2.waitKey(0)
cv2.destroyAllWindows()
