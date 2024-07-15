# Script to merge experiment1 and experiment2

import pandas as pd
import numpy as np
import os

EXPERIMENT1_FOLDER=os.path.join("dataset", "experiment1")
EXPERIMENT2_FOLDER=os.path.join("dataset", "experiment2")
MERGED_FOLDER=os.path.join("dataset", "both_experiments")

if not os.path.exists(MERGED_FOLDER):
    os.makedirs(MERGED_FOLDER)

for file in os.listdir(EXPERIMENT1_FOLDER):
    data1 = pd.read_csv(os.path.join(EXPERIMENT1_FOLDER, file))
    data2 = pd.read_csv(os.path.join(EXPERIMENT2_FOLDER, file))
    data = pd.concat([data1, data2], axis=0)
    data.to_csv(os.path.join(MERGED_FOLDER, file), index=False)

