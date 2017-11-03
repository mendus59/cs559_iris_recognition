import cv2
import iris_recognition as ir
import create_iris_codes as cic

img1 = cv2.imread('test/test_iris1.tiff', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('test/test_iris2.tiff', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('test/test_iris3.tiff', cv2.IMREAD_GRAYSCALE)

template1 = { 'id':1111, 'image':img1, 'iris_code':'' }
template2 = { 'id':2222, 'image':img2, 'iris_code':'' }
template3 = { 'id':1111, 'image':img3, 'iris_code':'' }

gallery = []
probes = []
gallery.append(template1)
probes.append(template1)
probes.append(template2)
probes.append(template3)

stats = []

for template in gallery:
    template = cic.create_iris_codes(template)
for template in probes:
    template = cic.create_iris_codes(template)

for probe in probes:
    stat = ir.iris_recognition(gallery, probe)
    stats.append(stat)

print(stats)