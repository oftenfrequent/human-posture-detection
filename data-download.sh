#!/bin/bash
# if you experience issues, try granting permissions to this file via:
# chmod +x data_download.sh 
mkdir -p ./data
source .env
kaggle_auth_file="$HOME/.kaggle/kaggle.json"

# Check if the directory exists, if not, create it
if [ ! -d "$(dirname "$kaggle_auth_file")" ]; then
    echo "Kaggle directory does not exist. Be sure to pip install first!"
    echo "Also, this script was intended for MacOS/Linux."
    echo "If you are running this from a different OS, check the contents of data-download.sh and try manually downloading the datasets at the bottom of the file."
    exit 1
fi

if [ -f "$kaggle_auth_file" ]; then
    echo "Kaggle Auth file already exists. Skipping this step."
else
    echo "Creating Kaggle Auth file from environment variables."
    touch "$kaggle_auth_file" && chmod 600 "$kaggle_auth_file"
    file_details='{"username":"'$KAGGLE_USERNAME'","key":"'$KAGGLE_API_KEY'"}'
    echo "$file_details" > $kaggle_auth_file
fi

echo "Now downloading datasets"
kaggle datasets download -d shrutisaxena/yoga-pose-image-classification-dataset -p ./data/yoga-pose-classification --unzip
kaggle datasets download -d tr1gg3rtrash/yoga-posture-dataset -p ./data/yoga-posture-dataset --unzip
