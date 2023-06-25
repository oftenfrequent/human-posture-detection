#!/bin/bash
# if you experience issues, try granting permissions to this file via:
# chmod +x data_download.sh 
mkdir -p ./data
kaggle datasets download -d shrutisaxena/yoga-pose-image-classification-dataset -p ./data/yoga-pose-classification --unzip
kaggle datasets download -d tr1gg3rtrash/yoga-posture-dataset -p ./data/yoga-posture-dataset --unzip
