# Yoga Pose Classification Model

## Introduction
This is a pose classification model that explore several different options for determining the pose of a person in an image. The model is trained off a combination of two different datasets publicly available on Kaggle.

1. [Yoga Pose Dataset](https://www.kaggle.com/niharika41298/yoga-poses-dataset)
2. [Yoga Posture Dataset](https://www.kaggle.com/tr1gg3rtrash/yoga-posture-dataset)

Note: I am awaiting approval for an additional dataset that could make this model more robust. The dataset is available at [Yoga 82](https://sites.google.com/view/yoga-82/home).

## Getting Started

This project is built off of [Detectron2](https://github.com/facebookresearch/detectron2/), Meta's open source library for computer vision-based applications such as object detection, segmentation, and pose estimation. While it is possible to run this project on a local machine, it is recommended to run this project on a GPU-enabled machine.

### Prerequisites
* Python 3.8
* GPU-enabled machine
* Kaggle API Key (See directions [here](https://www.kaggle.com/discussions/general/74235))

### Installing
1. Clone the repo
```
git clone
```
2. Install the required packages
```
pip install -r requirements.txt
```
3. Set up environment variables from `.env.example` and update values as needed.
```
cp .env.example .env
```
4. Download the Datasets via file 
```
bash data-download.sh
```
This will produce the following directory structure:
```
data
├───yoga-pose-classification
│   ├───dataset
│   │   ├───yoga-pose-1-name
│   │   │   ├───image_file_01.jpg
│   │   │   ├───image_file_02.png
│   │   │   ├───image_file_...
│   │   ├───yoga-pose-2-name
│   │   │   ├───image_file_...
├───yoga-posture-dataset
│   ├───yoga-pose-1-name
│   │   ├───image_file_01.jpg
│   │   ├───image_file_02.png
│   │   ├───image_file_...
...
```
5. Run `something.py` to generate the keypoints for the images
```
python something.py
```
6. Run `train.py` to train the model
```
python train.py
```
7. Run `test.py` to test the model
```
python test.py
```



