import numpy as np
from utils.enums import PreprocessingType


class Preprocessing:
    """A class for data preprocessing"""

    def __init__(self, preprocess_type: PreprocessingType):
        self.preprocess_type = preprocess_type
        
        # A dictionary with the following keys and values:
        #   - {'min': min values, 'max': max values} when preprocess_type is PreprocessingType.normalization
        #   - {'mean': mean values, 'std': std values} when preprocess_type is PreprocessingType.standardization
        self.params = {}

        # Select the preprocess function according to self.preprocess_type
        self.preprocess_func = getattr(self, self.preprocess_type.name)

    def identical(self, x: np.ndarray, init=False) -> np.ndarray:
        """Identity function."""
        self.params['identical'] = True
        return x
    
    def train(self, x: np.ndarray) -> np.ndarray:
        """Initializes preprocessing function on training data"""
        return self.preprocess_func(x, init=True)
    
    def __call__(self, x: np.ndarray) -> np.ndarray:
        """Returns preprocessed data"""
        if len(self.params) == 0:
            raise Exception(f"{self.preprocess_type.name} instance is not trained yet. Please call 'train' first")
        return self.preprocess_func(x, init=False)
    