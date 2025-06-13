import os

# Default paths for running in Google Colab
RAW_DATA_AND_LABELS_DIR = os.environ.get('RAW_DATA_AND_LABELS_DIR', '/content/data_and_labels')
PROCESSED_DATA_DIR = os.environ.get('PROCESSED_DATA_DIR', '/content/processed_data')
OUTPUT_DIR = os.environ.get('OUTPUT_DIR', '/content/output')
CHECKPOINT_PATH = os.environ.get('CHECKPOINT_PATH', '/content/checkpoints/checkpoint.pt')
