from enum import IntEnum


SetType = IntEnum('SetType', ('train', 'valid', 'test'))
PreprocessingType = IntEnum('PreprocessingType', ('normalization', 'standardization', 'identical'))
TrainType = IntEnum('TrainType', ('gradient_descent', 'normal_equation'))
LoggingParamType = IntEnum('LoggingParamType', ('loss', 'metric', 'regularization_term'))