import numpy as np
import cv2
import extcolors
from matplotlib import pyplot as plt

0.009
path1 = "shape2.jpg"
path2 = "shape3.jpg"
path2 = "shape32.jpg"
# path2 = "shape1 - Copy.jpg"
path1 = "shape31.jpg"
# path1 = "apple_logo.jpg"
path = "img.jpg"


def bgExtract(path):
    img = cv2.imread(path, 1)
    colors, pixel_count = extcolors.extract(path)
    # print(path)
    normPercentages = []
    pieColor = []
    colorLabels = []

    for i in range(len(colors)):
        # keep here the rgb code of the color
        colorRGB = str(colors[i][0])
        colorLabels.append(colorRGB)
#       calculate the percentage of the rgb color in the picture
        percentage = colors[i][1]/pixel_count * 100
        # format the percentage and put it in the matrix of the original percentages
        colorPercentage = '{0:.3f}'.format(percentage)
        normPercentages.append(colorPercentage)

        # We normalize some small values so that they appear correclty in the pie chart
        if percentage <= 0.01:
            percentage = percentage*300
            # print("IN IF ---- with % ",percentage)
        elif percentage <= 0.1:
            percentage = percentage*30
            # print("elif ---- with % ",percentage)
        elif percentage <= 0.5:
            percentage = percentage *10

        # We enter those corrected percentages in the list of the pie chart sizes(how big is each chunk)
        pieColor.append(percentage)
        colorPercentage = '{0:.3f}'.format(percentage)
        # print(colorRGB + ": " + colorPercentage)

    # create the pie chart
    plt.figure()
    patches,texts = plt.pie(pieColor,labels=normPercentages)

    plt.legend(patches, colorLabels, loc="best")

    cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(img, 100, 200)
    cv2.imshow(path, canny)

    contours,hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        cnt = contours[0]
        area = cv2.contourArea(cnt)
        print(area)
        print("\n")

    return area


area1 = bgExtract(path1)
area2 = bgExtract(path2)
if area1 > area2:
    ratio = area1/area2
    print("so the ratio of scale is img1/img2 ---> {0:.2f}".format(ratio))

else:
    ratio = area2 / area1
    print("so the ratio of scale is img2/img1 ---> {0:.2f}".format(ratio))

# bgExtract(path)
plt.show("The colors")
cv2.waitKey()