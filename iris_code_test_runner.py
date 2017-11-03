import numpy as np
import cv2
import create_iris_codes as cic

img1 = cv2.imread('test/test_iris1.tiff', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('test/test_iris2.tiff', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('test/test_iris3.tiff', cv2.IMREAD_GRAYSCALE)

template1 = { 'id':1111, 'image':img1, 'iris_code':'' }
template2 = { 'id':2222, 'image':img2, 'iris_code':'' }
template3 = { 'id':3333, 'image':img3, 'iris_code':'' }

result = cic.create_iris_codes(template3, False)