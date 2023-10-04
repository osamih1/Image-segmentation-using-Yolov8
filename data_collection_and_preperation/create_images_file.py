label = "/m/09ddx"

images_id = []
with open("initial_data/train/train-annotations-object-segmentation.csv", "r") as fr:
    line = fr.readline()
    while line:
        MaskPath, ImageID, LabelName = line.split(",")[:3]
        if LabelName == label and ImageID not in images_id:
            images_id.append(ImageID)
            with open("images_file", "a") as fw:
                fw.write(f"train/{ImageID}\n")
        line = fr.readline()
    fw.close()
    fr.close()

with open("initial_data/val/validation-annotations-object-segmentation.csv", "r") as fr:
    line = fr.readline()
    while line:
        MaskPath, ImageID, LabelName = line.split(",")[:3]
        if LabelName == label and ImageID not in images_id:
            images_id.append(ImageID)
            with open("images_file", "a") as fw:
                fw.write(f"validation/{ImageID}\n")
        line = fr.readline()
    fw.close()
    fr.close()

