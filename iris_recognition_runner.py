import numpy as np
import matplotlib as plt
import cv2

import create_iris_codes as cic
import load_script as ls
import iris_recognition as ir
import stats_runner as sr

# Run script to load gallery
iris_gallery = []
iris_gallery = ls.load_gallery_script()

# Run script to load probes
iris_probes = []
iris_probes = ls.load_probe_script()

# Create iris codes
gallery_iris_code_errors = 0
probe_iris_code_errors = 0
for template in iris_gallery:
    try:
        cic.create_iris_codes(template)
    except cv2.error:
        gallery_iris_code_errors += 1

for probe in iris_probes:
    try:
        cic.create_iris_codes(probe)
    except cv2.error:
        probe_iris_code_errors += 1

# Purge error templates
iris_gallery = ir.purge_errors(iris_gallery)
iris_probes = ir.purge_errors(iris_probes)

# Run recognition and measure stats
stats = []
iris_recognition_errors = 0
index = 0
for probe in iris_probes:
    print(index, "out of ", len(iris_probes))
    index += 1
    try:
        stat = ir.iris_recognition(iris_gallery, probe)
        stats.append(stat)
    except:
        iris_recognition_errors += 1

# Print and save results
true_match = 0
true_nonmatch = 0
false_match = 0
false_nonmatch = 0
for stat in stats:
    if stat['accept'] and stat['match']:
        true_match += 1
    elif not stat['accept'] and not stat['match']:
        true_nonmatch += 1
    elif stat['accept'] and not stat['match']:
        false_match += 1
    elif not stat['accept'] and stat['match']:
        false_nonmatch += 1
