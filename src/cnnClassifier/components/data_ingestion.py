import os
import zipfile
import subprocess
from cnnClassifier import logger
from cnnClassifier.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Download data from Kaggle using the Kaggle CLI.
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir, exist_ok=True)  # Ensure the root directory exists
            
            logger.info(f"Downloading data from Kaggle using dataset URL: {dataset_url}")

            # Using subprocess to call the Kaggle CLI command for dataset download
            command = f"kaggle datasets download -d maedemaftouni/large-covid19-ct-slice-dataset -p {self.config.root_dir}"
            subprocess.run(command, shell=True, check=True)

            # Move the downloaded file to the specified location
            if os.path.exists(zip_download_dir):
                logger.info(f"Downloaded data to {zip_download_dir}")
            else:
                raise FileNotFoundError(f"Failed to download dataset. File not found at {zip_download_dir}")

        except Exception as e:
            logger.error(f"An error occurred while downloading the file: {e}")
            raise e

    def extract_zip_file(self):
        """
        Extract the zip file into the data directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted zip file to {unzip_path}")
        except zipfile.BadZipFile as e:
            logger.error(f"Failed to extract zip file: {e}")
            raise e
        except FileNotFoundError as e:
            logger.error(f"Zip file not found: {e}")
            raise e
