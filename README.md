https://github.com/Babyhamsta/Aimmy

1. First start `install.bat`
2. Place all the images in the `images_for_sort` folder and the labels in `labels_for_sort` and run `sorting.bat`. 70℅ of the images will be randomly transferred to `dataset/images/train` (also labels: `dataset/labels/train`), and 30℅ to `dataset/images/val` (also labels: `dataset/labels/val`).
3. Then start training: `start_train.bat`
4. If the training session is interrupted, run `resume.bat`
