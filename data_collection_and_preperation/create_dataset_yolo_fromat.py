import os
import shutil

# creating the images folder for the training and validation data
data_dir = "../data"
images_dir = "images"

os.makedirs(os.path.join(data_dir, images_dir, "train"))
os.makedirs(os.path.join(data_dir, images_dir, "val"))

images_list = os.listdir(images_dir)
limit_count = int(len(images_list) * 0.8)

for image in images_list[:limit_count]:
    source_file = os.path.join(images_dir, image)
    destination_folder = os.path.join(data_dir, images_dir, "train")
    shutil.copy(source_file, destination_folder)

for image in images_list[limit_count:]:
    source_file = os.path.join(images_dir, image)
    destination_folder = os.path.join(data_dir, images_dir, "val")
    shutil.copy(source_file, destination_folder)

# creating the labels folder for the training and validation data
labels_dir = "labels"

os.makedirs(os.path.join(data_dir, labels_dir, "train"))
os.makedirs(os.path.join(data_dir, labels_dir, "val"))

labels_list = os.listdir(labels_dir)

for labels in labels_list[:limit_count]:
    source_file = os.path.join(labels_dir, labels)
    destination_folder = os.path.join(data_dir, labels_dir, "train")
    shutil.copy(source_file, destination_folder)

for labels in labels_list[limit_count:]:
    source_file = os.path.join(labels_dir, labels)
    destination_folder = os.path.join(data_dir, labels_dir, "val")
    shutil.copy(source_file, destination_folder)