# training/config.py
# ==============================
# DATA PARAMETERS
# ==============================

IMAGE_SIZE = 224        # DenseNet input size
BATCH_SIZE = 16         # Safe for most laptops

# ==============================
# TRAINING PARAMETERS
# ==============================

EPOCHS = 15
LEARNING_RATE = 1e-4
# 1e-4=1X10^(-4)
# ==============================
# MODEL PARAMETERS
# ==============================

NUM_CLASSES = 1         # Binary classification
MODEL_NAME = "DenseNet121"

# ==============================
# PATHS
# ==============================

TRAIN_DIR = "data/train"
VAL_DIR = "data/val"
TEST_DIR = "data/test"

CHECKPOINT_DIR = "checkpoints"

# ==============================
# DEVICE
# ==============================

import torch
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ==============================
# OPTIMIZATION
# ==============================

OPTIMIZER = "adam"
LOSS_FUNCTION = "bce"
