# Gait Detection with Self-Supervised Learning (SSL)

This project implements a self-supervised learning (SSL) approach to detect gait patterns from accelerometer data, with a focus on Huntington's Disease (HD) and neurodegenerative disorders. The pipeline consists of data preprocessing, model architecture, data augmentation, and training/evaluation.

## Project Structure
### 1. `sslmodel.py`
This module contains the training procesdure including function to load the pre-trained model, loss functions, etc. 
- currently in this file it is required to set the model_type as classification/segmentation 

### 2. `segmentation_model.py`
This file defines the J-Net segmentation model architecture used in the project. It leverages a pre-trained **ResNet18** model for feature extraction and applies custom upsampling and 1D convolutional layers to process accelerometer signals:
- **`SegModel`**: A deep learning model that can be adapted for single or multi-window inputs for segmentation tasks.
- The model is designed to handle irregular gait patterns commonly observed in HD patients.

### 3. `preprocessing.py`
This module handles the preprocessing of raw accelerometer data. It includes various utility functions for data manipulation, including:
- **`movingstd`**: Calculates the moving standard deviation, useful for signal smoothing.
- **Signal processing utilities**: preprocess the raw sensor data.
- It prepares the data before it's fed into the model for training.

### 4. `evaluation_func.py`
This module handles the evaluation and visualization of the results and includes various utility functions.

### 5. `train_hd_ssl.py`
This is the main script for training the SSL model. It includes:
- **Command-line arguments** for configuring training options such as `gait-only` mode, preprocessing, model initialization, and evaluation.
- **Training pipeline**: Loads data, applies the model, and evaluates performance on the HD dataset/ HC dataset/ PD dataset.

## How to Run
You can run the training process using:
```bash
python train_hd_ssl.py --initialize-model --training-mode --run-suffix "experiment_name"
```

### Customizing Data Paths
Default directories for raw data, processed data, model outputs and checkpoints
are defined in `paths.py`. These values point to `/content/...` so the code runs
out of the box in Google Colab. To override any of the locations on your local
machine, either edit `paths.py` or set the environment variables
`RAW_DATA_AND_LABELS_DIR`, `PROCESSED_DATA_DIR`, `OUTPUT_DIR` and
`CHECKPOINT_PATH` before running the scripts:

```bash
export RAW_DATA_AND_LABELS_DIR=/path/to/raw
export PROCESSED_DATA_DIR=/path/to/processed
export OUTPUT_DIR=/path/to/outputs
export CHECKPOINT_PATH=/path/to/checkpoint.pt
python train_hd_ssl.py
```
Data is available in:
https://zenodo.org/records/14384260

Kindly cite the following paper when using the data or the code:
D. Schwartz, L. Quinn, N. E. Fritz, L. M. Muratori, J. M. Hausdorff, and R. G. Bachrach, Detecting daily living gait amid Huntington’s disease chorea using a foundation deep learning model, 2024. arXiv:2412.11286 [cs.CV]. url: https://arxiv.org/abs/2412.11286.
