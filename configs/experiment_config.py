from easydict import EasyDict
from utils.enums import PreprocessingType


experiment_config.basis_function = EasyDict()
experiment_config.basis_function.name = 'default_function' # From ('rbf', 'default_function')
experiment_config.basis_function.params = {} # For 'rbf' can be {'n_centers': 1000, 'bandwidth': 1, 'bias': True}
experiment_config.basis_function.preprocess.type = PreprocessingType.identical