import numpy as np


class LinearRegression:
    """A class for lenear regression model implementation"""

    def __init__(self, m: int, experiment_config):
        """
        Args:
            m: The number of basis functions (or model weights vector shape in case of vanilla linear regression).
            experiment_config: Experiment configuration
        """
        self.config = experiment_config
        self.weights = np.random.randn(m)
        self.params_logger = ParamsLogger(experiment_config)

    def _pseudo_inverse_matrix(self, matrix, reg_coefficient):
        pass

    def train_normal_equation(self, inputs: np.ndarray, targets: np.ndarray):
