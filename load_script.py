import hash_builder
import os

def load_probe_script():
    pr =[]
    hash_builder.build("probes\\", pr)
    return pr

def load_gallery_script():
   arr =[]
   hash_builder.build("gallery\\", arr)
   return arr