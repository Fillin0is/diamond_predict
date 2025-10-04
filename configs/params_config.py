import numpy as np
from easydict import EasyDict

params_config = EasyDict()

# Default values 
params_config.default = EasyDict()
params_config.default.polynomial_max_degree = 10
params_config.default.rbf_n_centers = 5
params_config.default.rbf_bandwidth = 1
params_config.default.bias = True
params_config.default.min_delta = 0.01
params_config.default.patience = 10
params_config.default.reg_coefficient = 0

# Validation values
params_config.validation = EasyDict()
params_config.validation.samples_num = 40
params_config.validation.steps_num = 10
params_config.validation.basis_function_type = 'rbf'
params_config.validation.bias = True
params_config.validation.reg_coefficient = 1e-2
params_config.validation.params_range = {
    'rbf': {
        'n_centers': np.logspace(np.log10(1), np.log10(500), params_config.validation.samples_num, dtype=int),
        'bandwidth': np.logspace(np.log10(1), np.log10(10), params_config.validation.samples_num)
    }
}
params_config.validation.weights_shape = {'rbf': 'n_centers'}

print(params_config)