from easydict import EasyDict
import os
from utils.enums import PreprocessingType


experiment_config = EasyDict()
experiment_config.checkpoints_dir = os.path.join(
    experiment_config.logs_dir, experiment_config.experiment_name, "checkpoints"
)
experiment_config.train_type = TrainType.normal_equation # Later with parameter can be change to gradient_descent

experiment_config.params = {
    TrainType.normal_equation.name: {} # Now with parameters is empty, but later that parameter will be enclose by regularisation_coefficient
}


experiment_config.basis_function = EasyDict()
experiment_config.basis_function.name = 'default_function' # From ('rbf', 'default_function')
experiment_config.basis_function.params = {} # For 'rbf' can be {'n_centers': 1000, 'bandwidth': 1, 'bias': True}
experiment_config.basis_function.preprocess.type = PreprocessingType.identical