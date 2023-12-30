import os
import numpy as np

# set random seed at 42
np.random.seed(42)

# BASIC CONFIG

data_dir = 'C:\\Users\\qnwje\\OneDrive\\바탕 화면\\zerobase\\딥러닝 팀플\\yolo_block\\data\\truck_step'
train_dir = os.path.join(data_dir, 'train/')
val_dir = os.path.join(data_dir, 'val/')
test_dir = os.path.join(data_dir, 'test/')

# get all images inside the first directory in train_dir
train_img_dir = os.path.join(train_dir, 'images')
img_list = os.listdir(train_img_dir)

# Ensure the list is sorted to maintain the order
img_list.sort()

# Split the images into sets of 3
img_sets = [img_list[i:i+3] for i in range(0, len(img_list), 3)]

# Shuffle and split the sets into 8:2 ratio
np.random.shuffle(img_sets)

split_index = int(len(img_sets) * 0.8)
train_img_sets = img_sets[:split_index]
val_img_sets = img_sets[split_index:]

# Flatten the lists to get individual image names
train_img_names = [img for set in train_img_sets for img in set]
val_img_names = [img for set in val_img_sets for img in set]

print('TOTAL SETS: ', len(img_sets))
print('TRAIN SETS: ', len(train_img_sets))
print('VAL SETS: ', len(val_img_sets))
print('TRAIN IMAGES: ', len(train_img_names))
print('VAL IMAGES: ', len(val_img_names))

# Move validation images to val_dir + 'images'
for img_name in val_img_names:
    os.rename(os.path.join(train_img_dir, img_name), os.path.join(val_dir, 'images/', img_name))

# Move corresponding label files for validation images to val_dir + 'labels'
for img_name in val_img_names:
    label_name = img_name.split('.')[0] + '.txt'  # Assuming image and label files share the same base name
    os.rename(os.path.join(train_dir, 'labels/', label_name), os.path.join(val_dir, 'labels/', label_name))
