import cv2
import os
import sys

label = "/m/09ddx"

# getting the masks path for the training and validation data
maskpath_id = {}
with open("initial_data/train/train-annotations-object-segmentation.csv") as fr:
    line = fr.readline()
    while line:
        MaskPath, ImageID, LabelName = line.split(",")[:3]
        if LabelName == label:
            maskpath_id[MaskPath] = ImageID
        line = fr.readline()
    fr.close()

with open("initial_data/val/validation-annotations-object-segmentation.csv") as fr:
    line = fr.readline()
    while line:
        MaskPath, ImageID, LabelName = line.split(",")[:3]
        if LabelName == label:
            maskpath_id[MaskPath] = ImageID
        line = fr.readline()
    fr.close()

input_dir = "masks"
output_dir = "labels"
os.makedirs("labels")

for j in os.listdir(input_dir):
    image_path = os.path.join(input_dir, j)
    mask = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

    H, W = mask.shape
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # convert the contours to polygons
    polygons = []
    for cnt in contours:
        if cv2.contourArea(cnt)>200:
            polygon = []
            for point in cnt:
                x, y = point[0]
                polygon.append(x/W)
                polygon.append(y/H)
            polygons.append(polygon)

    # print the polygons
    with open("{}.txt".format(os.path.join(output_dir, maskpath_id[j])), "a") as fw:
        for polygon in polygons:
            for p_, p in enumerate(polygon):
                if p_ == len(polygon) - 1:
                    fw.write("{}\n".format(p))
                elif p_ == 0:
                    fw.write("0 {} ".format(p))
                else:
                    fw.write("{} ".format(p))
        fw.close()