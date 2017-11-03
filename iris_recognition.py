import cv2
import numpy as np

THRESHOLD = 0.3

def iris_recognition(gallery, probe):
    probe_code = collapse_iris_code_into_array(probe['iris_code'])
    closest_template = {}
    lowest_hamming_distance = 1
    match = False
    for template in gallery:
        if template['id'] == probe['id']:
            match = True
        template_code = collapse_iris_code_into_array(template['iris_code'])
        hamming_distance = compare_codes(template_code, probe_code)
        if lowest_hamming_distance > hamming_distance:
            lowest_hamming_distance = hamming_distance
            closest_template = template
    
    accept = False
    if lowest_hamming_distance < THRESHOLD:
        accept = True
    return { 'match': match, 'accept': accept, 'hd': lowest_hamming_distance, 'closest_match_id': closest_template['id'], 'probe_id': probe['id'] }

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

def purge_errors(templates):
    purged_templates = []
    for template in templates:
        if template['iris_code'] is not None:
            purged_templates.append(template)
    return purged_templates