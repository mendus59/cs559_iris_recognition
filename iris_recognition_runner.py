import numpy as np
import matplotlib as plt
import cv2

import create_iris_codes as cic
import load_probe_script as lss
import load_gallery_script as lts
import iris_recognition as ir
import stats_runner as sr

# Run script to load gallery
iris_gallery = []
iris_gallery = lts.load_gallery_script()

# Run script to load probes
iris_probes = []
iris_probes = lss.load_probe_script()

# Create iris codes
for template in iris_gallery:
    cic.create_iris_codes(template)

for probe in iris_probes:
    cic.create_iris_codes(probe)

# Run recognition and measure stats
stats = {}
stats = ir.iris_recognition(iris_gallery, iris_probes)

# Print and save results
sr.save_stats(stats)
sr.print_stats(stats)