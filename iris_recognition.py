import cv2
import numpy as np

THRESHOLD = 0.45

def iris_recognition(gallery, probe):
    probe_code = collapse_iris_code_into_array(probe['iris_code'])
    closest_template = {}
    lowest_hamming_distance = 1
    for template in gallery:
        template_code = collapse_iris_code_into_array(template['iris_code'])
        hamming_distance = compare_codes(template_code, probe_code)
        if lowest_hamming_distance > hamming_distance:
            lowest_hamming_distance = hamming_distance
            closest_template = template
    match = False
    if closest_template['id'] == probe['id']:
        match = True
    accept = False
    if lowest_hamming_distance < THRESHOLD:
        accept = True
    return { 'match': match, 'accept': accept, 'hd': lowest_hamming_distance }

def collapse_iris_code_into_array(code_image):
    code_array = []
    code_array = list(code_image.flat)
    return code_array

def compare_codes(template_code, probe_code):
    count = 0
    differences = 0
    for index in template_code:
        if index != probe_code[count]:
            differences += 1
        count += 1
    distance = differences/count
    return distance