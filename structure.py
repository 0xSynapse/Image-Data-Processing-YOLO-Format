import os
import shutil
from sklearn.model_selection import train_test_split
import numpy as np

# Define the source directories
source_images_dir = 'organized_data/Images'
source_labels_dir = 'organized_data/Labels'

# Define the destination directory structure
dest_dir = 'final_data'
train_dir = os.path.join(dest_dir, 'train')
valid_dir = os.path.join(dest_dir, 'valid')
test_dir = os.path.join(dest_dir, 'test')

# Function to create directory structure
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Create the directory structure for train, valid, and test sets
for directory in [train_dir, valid_dir, test_dir]:
    create_dir(os.path.join(directory, 'Images'))
    create_dir(os.path.join(directory, 'Labels'))

# Get all image files
image_files = sorted([f for f in os.listdir(source_images_dir) if f.endswith('.jpg')])
# Ensure labels match the images
label_files = [f.replace('.jpg', '.txt') for f in image_files]

# Shuffle files while maintaining correspondence
indices = np.arange(len(image_files))
np.random.shuffle(indices)
shuffled_image_files = np.array(image_files)[indices]
shuffled_label_files = np.array(label_files)[indices]

# Split the dataset into train, validation, and test sets (80%, 10%, 10%)
train_img, test_img, train_lbl, test_lbl = train_test_split(shuffled_image_files, shuffled_label_files, test_size=0.2, random_state=42)
valid_img, test_img, valid_lbl, test_lbl = train_test_split(test_img, test_lbl, test_size=0.5, random_state=42)

# Function to copy files to their respective directories
def copy_files(files, source_dir, dest_dir):
    for file in files:
        shutil.copy(os.path.join(source_dir, file), os.path.join(dest_dir, file))

# Copy files to their respective directories
copy_files(train_img, source_images_dir, os.path.join(train_dir, 'Images'))
copy_files(train_lbl, source_labels_dir, os.path.join(train_dir, 'Labels'))
copy_files(valid_img, source_images_dir, os.path.join(valid_dir, 'Images'))
copy_files(valid_lbl, source_labels_dir, os.path.join(valid_dir, 'Labels'))
copy_files(test_img, source_images_dir, os.path.join(test_dir, 'Images'))
copy_files(test_lbl, source_labels_dir, os.path.join(test_dir, 'Labels'))

print("Dataset successfully organized for training, validation, and testing.")