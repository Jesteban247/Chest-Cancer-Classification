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