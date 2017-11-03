import hash_builder
import os

def load_probe_script():
    pr =[]
    hash_builder.build("probes\\", pr)
    print(len(pr))
    return pr







load_probe_script()