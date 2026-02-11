import numpy as np
import os

PATH_DATA = 'data'

# This file should contain code ONLY related to working with data

def make_data(n: int=100, low: int=0, high: int=25) -> np.ndarray: # ALWAYS TYPE INT!
    """Return an nX2 array of random integers between 'low' and 'high' (inclusive)
    """
    return np.random.randint(low=low, high=high+1, size=(n,2))

def save_data(data: np.ndarray, filename: str) -> None:
    """Save a numpy array to the default output folder, ensuring that the folder exists
    """
    full_filename = os.path.join(PATH_DATA, filename)

    # Ensure the output directory exists
    if not os.path.exists(PATH_DATA):
        os.mkdir(PATH_DATA)
    
    # Ensure the data is in an numpy array
    if type(data) != np.ndarray:
        raise TypeError(f'Data should be a numpy array but a {type(data)} was provided')
    
    # Don't overwrite an existing file
    if os.path.exists(full_filename):
        raise FileExistsError(f'File {full_filename} already exists')
    
    # Save array as .npy file
    np.save(full_filename, data)

    return None

def load_data(file_name: str) -> np.ndarray:
    """Loads data from an .npy file located in the default data directory
    """
    return np.load(os.path.join(PATH_DATA, file_name))