import os

def build(location, arr):
    for root, dirs, files in os.walk(location):
        for file in files:
            if not os.path.isdir(file):
                if  file.endswith('txt'):
                    p = root+'\\'+file
                    handle_file(p, arr)

def handle_file(filepath, arr):
    str=""
    f = open(filepath, "r")

    for line in f.readlines():
        if line !='\n':
            str += line
        else:
            arr.append( create_hash(str, filepath))
            str=""

def create_hash(arr, filepath):
    dict = {'iris_code': None}

    noprefix = prefix(filepath)

    for line in arr.splitlines():
        if 'subjectid' in line:
            list_of_words = line.split()
            subjectid = list_of_words[list_of_words.index('string') + 1]
            dict['id'] = subjectid
        elif noprefix in line:
            list2 = line.split()
            address = list2[list2.index('file')+2]
            filename= purge(address)
            dict['image'] = build_dir(filepath, filename)
    return dict

def prefix(filepath):
    rgal = filepath.split('\\')[1]
    if 'probe' in rgal:
        rgal = filepath.split('\\')[2]
    p1 = rgal.split('-')[0]
    p2= rgal.split('-')[1]
    p3 = p1+'/'+p2
    return p3

def purge(address):
    r6 = address.split('/')
    r7 = r6[len(r6)-1]
    return r7

def build_dir(filepath, filename):
    dir = os.path.dirname(filepath)
    return dir+'\\'+filename