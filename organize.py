import os
import shutil

# Define the source directory where the class folders are located
source_dir = "test_data/"

# Define the destination directory and subdirectories for images and labels
dest_dir = "organized_data"
dest_images_dir = os.path.join(dest_dir, "Images")
dest_labels_dir = os.path.join(dest_dir, "Labels")

# Create the destination directories if they don't exist
os.makedirs(dest_images_dir, exist_ok=True)
os.makedirs(dest_labels_dir, exist_ok=True)

# List of class folder names
class_folders = ["buffalo", "elephant", "rhino", "zebra"]

# Initialize global counter for images and labels
counter = 1


# Function to generate a new filename based on the counter
def get_new_filename(extension):
    global counter
    new_filename = f"{str(counter).zfill(4)}{extension}"  # Ensures the format 0000.ext
    return new_filename


# Iterate through each class folder
for class_folder in class_folders:
    full_class_path = os.path.join(source_dir, class_folder)
    all_files = sorted(os.listdir(full_class_path))  # Sort files to ensure sequence

    for file in all_files:
        if file.endswith(".txt"):
            base_name = os.path.splitext(file)[0]
            corresponding_img_file = f"{base_name}.jpg"
            img_path = os.path.join(full_class_path, corresponding_img_file)
            label_path = os.path.join(full_class_path, file)

            # Check if the corresponding .jpg file exists
            if os.path.exists(img_path):
                # Generate new filenames for label and image
                new_label_filename = get_new_filename(".txt")
                new_img_filename = get_new_filename(".jpg")
                """print(f"Processing {new_label_filename}")"""  # Display the file number in desired format

                # Copy files to their respective destination folders
                shutil.copy(img_path, os.path.join(dest_images_dir, new_img_filename))
                shutil.copy(label_path, os.path.join(dest_labels_dir, new_label_filename))
                counter += 1  # Increment counter after each matched pair
            else:
                print(f"No corresponding .jpg file found for {file} - Expected {corresponding_img_file}")

print(f"Total files processed: {counter-1}")
