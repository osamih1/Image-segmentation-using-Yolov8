from ultralytics import YOLO
import os
import numpy as np
import cv2

# loading the trained model
model_path = "runs/segment/train2/weights/last.pt"
model = YOLO(model_path)

# getting the results from the prediction
for j,  image in enumerate(os.listdir("data/images/val")[:12]):
    results = model(os.path.join("data/images/val", image))

    img_array = results[0].orig_img
    if results[0].masks != None:
        mask_array = np.array(results[0].masks.data)
        mask_transpose_array = mask_array.transpose((1,2,0))

        print("Image shape: ", img_array.shape)
        print("Mask shape: ", mask_array.shape)
        print("Mask transpose shape: ", mask_transpose_array.shape)
        print()

        polygon_vertices = []
        for polygon_mask in results[0].masks.xy:
            vertices = np.array(polygon_mask, dtype=np.int32)
            polygon_vertices.append(vertices)

        cv2.fillPoly(img_array, polygon_vertices, (255,255,0))

        cv2.imshow("Image", img_array)
        cv2.waitKey(0)