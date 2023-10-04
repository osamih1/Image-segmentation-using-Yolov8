from zipfile import ZipFile

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

# extracting only ducks masks from the training and validation data masks
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']:
    with ZipFile(f"initial_data/train/train-masks-{i}.zip", "r") as zip:
        file_list = zip.namelist()

        for file in file_list:
            if file in maskpath_id.keys():
                zip.extract(file, "masks")

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']:
    with ZipFile(f"initial_data/val/validation-masks-{i}.zip", "r") as zip:
        file_list = zip.namelist()

        for file in file_list:
            if file in maskpath_id.keys():
                zip.extract(file, "masks")

