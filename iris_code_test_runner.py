import numpy as np
import cv2

import create_iris_codes as cic

img = cv2.imread('test/test_iris.tiff', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('test/test_iris2.tiff', cv2.IMREAD_GRAYSCALE)

template = { 'id':1234, 'image':img, 'iris_code':'' }
template2 = { 'id':1234, 'image':img2, 'iris_code':'' }

result = cic.create_iris_codes(template, True)
result = cic.create_iris_codes(template2, True)