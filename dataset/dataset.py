from utils.preprocessing import Preprocessing
import os
from configs.data_config import data_config
from utils.enums import SetType

class DiamondsDataset:
    """A class for the Diamonds dataset. This class reads the data and proprocess it"""

    def __init__(self, config):
        """Initializes the Diamonds dataset class instance."""
        self.config = config

        # Preprocessing class initialization
        self.preprocessing = Preprocessing(config.preprocess_type)

        # Reads the data
        self.data = {}
        for set_type in SetType:
            self.data[set_type.name] = self.dataframe_preprocessing(
                os.path.join(config.path_to_data, config.type[set_type.name]), set_type
            )

    def dataframe_preprocessing(path_to_dataframe: str, set_type: int) -> None:

        pass

    def __call__(self, set_type: str) -> dict:
        """Returns preprocessed data."""
        return self.data[set_type]
        

