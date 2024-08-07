from dataclasses import dataclass
from pathlib import Path

# Define a data class to hold configuration details for data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    # The root directory where all data ingestion artifacts will be stored
    root_dir: Path
    
    # The URL or identifier of the data source (e.g., a Kaggle dataset URL or identifier)
    source_URL: str
    
    # The local file path where the downloaded data file will be saved
    local_data_file: Path
    
    # The directory where the data file will be unzipped or extracted
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    # Directory where the base model and other related files are stored
    root_dir: Path
    
    # Path to the pre-trained base model file
    base_model_path: Path
    
    # Path where the updated base model will be saved after modifications
    updated_base_model_path: Path
    
    # List defining the size of input images (e.g., [224, 224, 3])
    params_image_size: list
    
    # Learning rate used for training the model (e.g., 0.01)
    params_learning_rate: float
    
    # Boolean flag indicating whether to include the top layers of the model (True/False)
    params_include_top: bool
    
    # String specifying the weights initialization method (e.g., 'imagenet')
    params_weights: str
    
    # Number of output classes for the classification task (e.g., 2 for binary classification)
    params_classes: int