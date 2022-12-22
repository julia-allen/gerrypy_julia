import sys
sys.path.append('../gerrypy')

import os
import time
import json
import numpy as np
from data.buffalo_data.load import load_state_df
import pandas as pd

def population_tolerance():
    state_df = load_state_df()
    populations = state_df.groupby(['Council2'])['TOTAL_ADJ'].sum()
    pop_dif = max(populations)-min(populations)
    pop_tolerance = pop_dif/np.mean(populations)
    return pop_tolerance

if __name__ == "__main__":
    population_tolerance()