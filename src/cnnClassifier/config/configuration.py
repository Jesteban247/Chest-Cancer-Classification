from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import (DataIngestionConfig,
                                                PrepareBaseModelConfig)


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
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        """
        Retrieves the configuration for preparing the base model.

        Returns:
            PrepareBaseModelConfig: An instance of PrepareBaseModelConfig populated with data from the configuration and parameters files.
        """
        # Extract the 'prepare_base_model' section from the configuration file
        config = self.config.prepare_base_model
        
        # Create the directory specified for the base model
        create_directories([config.root_dir])

        # Instantiate and return the PrepareBaseModelConfig with values from the configuration and parameters
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config