import logging
import json
import os
import glob
import sys

import keras
from libraries.Train_model_pipeline import Train_FCNN_Model, Train_UNET_Model

logging.basicConfig(filename='/opt/ml/output/data/logs-training.txt', level=logging.DEBUG)

if __name__ == '__main__':
    logging.debug('Hello my custom SageMaker init script!')
    
    Train_FCNN_Model(
        loss=keras.losses.categorical_focal_crossentropy,
        save_path='fcnn-path',
        buffer_size=2000,
        batch_size=64,
        epochs=20,
        learning_rate=1e-3
    )

    Train_UNET_Model(
        loss=keras.losses.categorical_crossentropy,
        save_path='unet-path',
        buffer_size=2000,
        batch_size=64,
        epochs=20,
        learning_rate=1e-3
    )
