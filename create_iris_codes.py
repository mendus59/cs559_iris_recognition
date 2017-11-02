import cv2
import numpy as np
from matplotlib import pyplot as plt

def create_iris_codes(template_hash, test_mode=False):

    img = template_hash['image']
    rimg = resize_image(img)
    edge_image = canny_edge(rimg)
    circles = hough_transform(edge_image)
    cropped_iris = crop_iris(rimg, circles['iris'])
    iris_map = map_to_rectangle(cropped_iris, circles['iris'])
    thresh = threshold(iris_map)

    template_hash['iris_code'] = thresh

    if test_mode:
        test_display(img, rimg, edge_image, circles, cropped_iris, iris_map, thresh)

    return template_hash

def resize_image(image):
    resized_image = image[120:400, 160:520]
    return resized_image

def canny_edge(image):
    img = cv2.blur(image, (10, 10))
    edges = cv2.Canny(img,0,25)
    return edges

def hough_transform(image):
    img = image

    iris = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 13, 250,
                                param1=50, param2=50, minRadius=10, maxRadius=150)
    pupil = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, .9, 200,
                                param1=50, param2=50, minRadius=10, maxRadius=150)
    
    circles = { 'iris': iris[0][0], 'pupil':pupil[0][0] }
    return circles

def crop_iris(image, iris_circle):
    x1 = int(round(iris_circle[0]-iris_circle[2]))
    x2 = int(round(iris_circle[0]+iris_circle[2]))
    y1 = int(round(iris_circle[1]-iris_circle[2]))
    y2 = int(round(iris_circle[1]+iris_circle[2]))
    cropped_image = image[y1:y2, x1:x2]
    return cropped_image

def map_to_rectangle(image, circle):
    rows, cols = image.shape
    mapped = cv2.linearPolar(image, (rows/2, cols/2), circle[2], cv2.WARP_FILL_OUTLIERS)
    mapped = cv2.resize(mapped,(120, 620), interpolation = cv2.INTER_CUBIC)
    mapped = np.rot90(mapped)
    return mapped

def threshold(image):
    im_bw = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    return im_bw

def test_display(img, rimg, edge_image, circles, cropped_iris, iris_map, thresh):
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyWindow('img')

    cv2.imshow('rimg', rimg)
    cv2.waitKey(0)
    cv2.destroyWindow('rimg')

    cv2.imshow('edge_image', edge_image)
    cv2.waitKey(0)
    cv2.destroyWindow('edge_image')

    cimg = cv2.cvtColor(rimg,cv2.COLOR_GRAY2BGR)
    icircles = np.uint16(np.around(circles['iris']))
    cv2.circle(cimg,(icircles[0],icircles[1]),icircles[2],(0,255,0),2)
    pcircles = np.uint16(np.around(circles['pupil']))
    cv2.circle(cimg,(pcircles[0],pcircles[1]),pcircles[2],(0,255,0),2)
    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyWindow('detected circles')

    cv2.imshow('cropped_iris', cropped_iris)
    cv2.waitKey(0)
    cv2.destroyWindow('cropped_iris')

    cv2.imshow('iris_map', iris_map)
    cv2.waitKey(0)
    cv2.destroyWindow('iris_map')

    cv2.imshow('threshold', thresh)
    cv2.waitKey(0)
    cv2.destroyWindow('threshold')
