# src/data_preparation.py
import os
import random
import shutil as sh
import kagglehub
import pandas as pd
from tqdm import tqdm

def download_and_prepare_data():

    path = kagglehub.dataset_download("sshikamaru/car-object-detection")
    print("Path to dataset files:", path)

    train_solutions = pd.read_csv(path + '/data/train_solution_bounding_boxes (1).csv')
    img_h, img_w = (380, 676)

    train_solutions['x_center'] = (train_solutions['xmin'] + train_solutions['xmax']) / 2 / img_w
    train_solutions['y_center'] = (train_solutions['ymin'] + train_solutions['ymax']) / 2 / img_h
    train_solutions['w'] = (train_solutions['xmax'] - train_solutions['xmin']) / img_w
    train_solutions['h'] = (train_solutions['ymax'] - train_solutions['ymin']) / img_h
    train_solutions['classes'] = 0

    for fold in [0]:
        val_index = train_solutions['image'].unique()[len(train_solutions) * fold // 5:len(train_solutions) * (fold + 1) // 5]
        
        for name, mini in tqdm(train_solutions.groupby('image')):
            path2save = 'val2017/' if name in val_index else 'train2017/'
            label_path = f'data/labels/{path2save}'
            image_path = f'data/images/{path2save}'

            os.makedirs(label_path, exist_ok=True)
            os.makedirs(image_path, exist_ok=True)

            with open(f'{label_path}{name}.txt', 'w') as f:
                for _, row in mini[['classes', 'x_center', 'y_center', 'w', 'h']].iterrows():
                    f.write(' '.join(map(str, row)) + "\n")

            sh.copy(f"{path}/data/training_images/{name}.jpg", f'{image_path}/{name}.jpg')

if __name__ == "__main__":
    download_and_prepare_data()
