# Image-segmentation-using-Yolov8
This project is about building an image segmentation model trained on a custom dataset (ducks dataset) using Yolov8.
## Steps to follow

1. From data_collection_and_preperation create 2 sub directories one called initial_data/train for the training data and the other called initial_data/val for the validation data.

2. Download the segmented dataset from [here](https://storage.googleapis.com/openimages/web/download_v7.html#download-manually), then place each subset in its corresponding one (initial_data/train or initial_data/val).

3. Execute create_images_file.py file to get the list of images to download for your segmenation task.

4. In terminal run this command to download images: 

    ```python data_collection_and_preperation/downloader.py images_file --download_folder=data_collection_and_preperation/images```

5. Execute create_masks.py to get the mask of all the images inside masks folder.

6. Execute masks_to_polygons.py to get the polygons of the mask images inside the labels folder.

7. Execute create_dataset_yolo_fromat.py to get the datataset in the format needed to train the YOLOv8-seg model

8. Execute train.py to train the yolov8-seg model.
