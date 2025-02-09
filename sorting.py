import os
import shutil
from pathlib import Path
import numpy as np

# Sorting
os.chdir('images_for_sort')

lst=[1, 2]
for item in Path('.').glob('*.jpg'):
    name = str(item)
    res = name.rstrip('.jpg')
    r = np.random.choice(lst,1,p=[0.70, 0.30])
    if r == 1:
        shutil.move(name, '../dataset/images/train/')
        print('../dataset/images/train/'+name, '  train')
        try:
            shutil.move('../labels_for_sort/'+res+'.txt', '../dataset/labels/train/')
            print('../dataset/labels/train/'+res+'.txt', '  train')
        except:
            print('no label file')
            pass
    else:
        shutil.move(name, '../dataset/images/val/')
        print('../dataset/images/val/'+name, '  val')
        try:
            shutil.move('../labels_for_sort/'+res+'.txt', '../dataset/labels/val/')
            print('../dataset/labels/val/'+res+'.txt', '  val')
        except:
            print('no label file')
            pass

# Comma to dot
os.chdir('../dataset/labels/train')

for item in Path('.').glob('*.txt'):
    name = str(item)
    with open(name, 'r') as f:
        text = f.read()
    with open(name, 'w') as f:
        f.write(text.replace(',', '.'))
    print('dataset/labels/train/'+name, '  done')
file = open("labels.txt", "w")
file.write("Enemy")
file.close()

os.chdir('../../../dataset/labels/val')

for item in Path('.').glob('*.txt'):
    name = str(item)
    with open(name, 'r') as f:
        text = f.read()
    with open(name, 'w') as f:
        f.write(text.replace(',', '.'))
    print('dataset/labels/val/'+name, '  done')
file = open("labels.txt", "w")
file.write("Enemy")
file.close()
 
