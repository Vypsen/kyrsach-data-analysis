import numpy as np
import pandas as pd

def chiSquare(data):
    statistical_significance = 0.05
    chi_square = 0
    critical_value = 3.84
    value = np.array([data.iloc[0][0:4].values,
                      data.iloc[1][0:4].values,
                      data.iloc[2][0:4].values])
    df = (value.shape[0] - 1 - 1)*(value.shape[0] - 1 - 1)
    total = value[value.shape[0] - 1][value.shape[0] - 1]

    for i in range(value.shape[0] - 1):
        for j in range(value.shape[0] - 1):
            expected_value = (value[i][value.shape[0] - 1]*value[value.shape[0] - 1][j])/total
            chi_square += (value[i][j] - expected_value)**2/expected_value

    return chi_square