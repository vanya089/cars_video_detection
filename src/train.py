# src/train.py
import os
import yaml
from yolov5 import train

def train_model():
    data_yaml = {
        'train': 'data/images/train2017',
        'val': 'data/images/val2017',
        'nc': 1,
        'names': ['car']
    }

    with open('data/data.yaml', 'w') as outfile:
        yaml.dump(data_yaml, outfile, default_flow_style=False)

    train.run(data='data/data.yaml', imgsz=676, batch_size=16, epochs=30, weights='yolov5s.pt')

if __name__ == "__main__":
    train_model()
