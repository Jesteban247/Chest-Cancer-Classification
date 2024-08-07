from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH):
        
        # Initialize the ConfigurationManager with file paths for config and parameters
        # Read the configuration and parameters from the specified file paths
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        # Create the root directory specified in the configuration
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Extract the data ingestion configuration from the loaded config
        config = self.config.data_ingestion
        
        # Create the directory specified in the data ingestion config
        create_directories([config.root_dir])
        
        # Create and return a DataIngestionConfig object using the extracted data
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config