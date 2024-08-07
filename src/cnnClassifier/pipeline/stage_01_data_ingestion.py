# Import necessary modules from the project and standard libraries
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

# Define a constant for the stage name
STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    """
    Class to handle the data ingestion pipeline for training.
    """

    def __init__(self):
        """
        Initialize the DataIngestionTrainingPipeline class.
        """
        pass

    def main(self):
        """
        Main method to execute the data ingestion pipeline.
        """
        # Create an instance of ConfigurationManager to access configuration settings
        config = ConfigurationManager()
        
        # Retrieve data ingestion configuration
        data_ingestion_config = config.get_data_ingestion_config()
        
        # Create an instance of DataIngestion with the retrieved configuration
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        # Download the dataset from the specified source
        data_ingestion.download_file()
        
        # Extract the downloaded dataset from the zip file
        data_ingestion.extract_zip_file()

# Check if the script is being executed directly
if __name__ == '__main__':
    try:
        # Log the start of the data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Create an instance of DataIngestionTrainingPipeline
        obj = DataIngestionTrainingPipeline()
        
        # Run the main method of the DataIngestionTrainingPipeline class
        obj.main()
        
        # Log the completion of the data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Log the exception if any error occurs and re-raise it
        logger.exception(e)
        raise e
