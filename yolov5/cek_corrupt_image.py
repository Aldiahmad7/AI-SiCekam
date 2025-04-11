# import os
# import cv2

# image_dir = 'D:/Coding/Project/AI SiCekam/yolov5/datasets/broiler/valid/images'
# corrupt_count = 0
# total = 0

# for filename in os.listdir(image_dir):
#     if filename.endswith(('.jpg', '.jpeg', '.png')):
#         total += 1
#         path = os.path.join(image_dir, filename)
#         img = cv2.imread(path)
#         if img is None:
#             print("Corrupt image:", path)
#             corrupt_count += 1

# print(f"\nTotal images checked: {total}")
# print(f"Total corrupt images : {corrupt_count}")


# import os

# label_dir = 'D:/Coding/Project/AI SiCekam/yolov5/datasets/broiler/valid/labels'
# for filename in os.listdir(label_dir):
#     path = os.path.join(label_dir, filename)
#     if os.stat(path).st_size == 0:
#         print("Label kosong:", path)


# import os

# image_dir = 'D:/Coding/Project/AI SiCekam/yolov5/datasets/broiler/train/images'
# label_dir = 'D:/Coding/Project/AI SiCekam/yolov5/datasets/broiler/train/labels'

# for filename in os.listdir(label_dir):
#     label_path = os.path.join(label_dir, filename)
#     if os.stat(label_path).st_size == 0:
#         image_filename = filename.replace('.txt', '.jpg')  # atau .png tergantung format
#         image_path = os.path.join(image_dir, image_filename)

#         print("Menghapus:", label_path)
#         os.remove(label_path)

#         if os.path.exists(image_path):
#             print("Menghapus:", image_path)
#             os.remove(image_path)


# import torch
# print(torch.cuda.get_device_name(0))
