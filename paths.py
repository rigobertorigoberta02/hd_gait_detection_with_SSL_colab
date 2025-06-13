import os


def ensure_exists(path: str, name: str) -> str:
    """Verify that ``path`` exists.

    Parameters
    ----------
    path: str
        Path to check.
    name: str
        Human friendly name used in the error message.

    Returns
    -------
    str
        The original path if it exists.

    Raises
    ------
    FileNotFoundError
        If the given path does not exist.
    """

    if not os.path.exists(path):
        raise FileNotFoundError(f"{name} not found: {path}")
    return path


# Default paths for running in Google Colab
RAW_DATA_AND_LABELS_DIR = ensure_exists(
    os.environ.get('RAW_DATA_AND_LABELS_DIR', '/content/data_and_labels'),
    'RAW_DATA_AND_LABELS_DIR'
)
PROCESSED_DATA_DIR = ensure_exists(
    os.environ.get('PROCESSED_DATA_DIR', '/content/processed_data'),
    'PROCESSED_DATA_DIR'
)
OUTPUT_DIR = ensure_exists(
    os.environ.get('OUTPUT_DIR', '/content/output'),
    'OUTPUT_DIR'
)
CHECKPOINT_PATH = os.environ.get(
    'CHECKPOINT_PATH', '/content/checkpoints/checkpoint.pt'
)

# Subdirectories used by ``read_data.py``
ACC_DATA_DIR = ensure_exists(
    os.environ.get(
        'ACC_DATA_DIR',
        os.path.join(RAW_DATA_AND_LABELS_DIR, 'acc_data/right_wrist')
    ),
    'ACC_DATA_DIR'
)
WS_ACC_DATA_DIR = ensure_exists(
    os.environ.get(
        'WS_ACC_DATA_DIR',
        os.path.join(RAW_DATA_AND_LABELS_DIR, 'acc_data/WS_acc_files')
    ),
    'WS_ACC_DATA_DIR'
)
LABEL_DATA_DIR = ensure_exists(
    os.environ.get(
        'LABEL_DATA_DIR',
        os.path.join(RAW_DATA_AND_LABELS_DIR, 'labeled data')
    ),
    'LABEL_DATA_DIR'
)
OPAL_LABEL_DATA_DIR = ensure_exists(
    os.environ.get(
        'OPAL_LABEL_DATA_DIR',
        os.path.join(RAW_DATA_AND_LABELS_DIR, 'labeled data/WS_label_files')
    ),
    'OPAL_LABEL_DATA_DIR'
)
DAILY_DATA_DIR = ensure_exists(
    os.environ.get(
        'DAILY_DATA_DIR',
        os.path.join(
            PROCESSED_DATA_DIR, 'daily_living_for_ssl_gait_detection_paper/HC'
        )
    ),
    'DAILY_DATA_DIR'
)
DAILY_TARGET_DIR = ensure_exists(
    os.environ.get('DAILY_TARGET_DIR', os.path.join(PROCESSED_DATA_DIR, 'HC')),
    'DAILY_TARGET_DIR'
)
PACE_DAILY_DATA_DIR = ensure_exists(
    os.environ.get(
        'PACE_DAILY_DATA_DIR',
        os.path.join(PROCESSED_DATA_DIR, 'PACEHD_for_ssl_paper')
    ),
    'PACE_DAILY_DATA_DIR'
)
PACE_DAILY_TARGET_DIR = ensure_exists(
    os.environ.get('PACE_DAILY_TARGET_DIR', os.path.join(PROCESSED_DATA_DIR, 'PACE')),
    'PACE_DAILY_TARGET_DIR'
)
