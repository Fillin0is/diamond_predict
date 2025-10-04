import warnings
import numpy as np
from configs import experiment_config
from utils.preprocessing import Preprocessing
from configs.params_config import params_config


class BasisFunctionProcessor:
    """
    
    """
    def __init__(self, function_type: str, **kwargs):
        self.function_params = kwargs
        self.basis_function = getattr(self, f'_{function_type}', None)
        self.preprocessing = Preprocessing(experiment_config.basis_function.preprocess_type)

        self.params = {}

        if self.basis_function is None:
            warnings.warn(f"Function type '{function_type}' is not recognized. Using default function")
            self.basis_function = self._default_function

    def _polynomial():
        pass

    def _rbf():
        pass

    def _default_function():
        pass

    def preprocess(self, x: np.ndarray) -> np.ndarray:
        """Makes preprocessing for the chosen basis function if needed."""
        if self.basis_function.__name__ == "_rbf":
            transformed_x = self.basis_function(x, preprocess=True)
        else:
            transformed_x = self.basis_function(x)

        if self.function_params.get('bias', params_config.default.bias):
            return np.hstack([transformed_x[:, :1], self.preprocessing.train(transformed_x[:, 1:])])

    def transform():
        pass

