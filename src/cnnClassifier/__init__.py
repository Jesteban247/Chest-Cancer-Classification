import os  # Import the os module for interacting with the operating system
import sys  # Import the sys module for system-specific parameters and functions
import logging  # Import the logging module for logging events

# Define the logging format string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory and file path for the log file
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Set the logging format
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)   # Log to the console (stdout)
    ]
)

# Create a logger object for the cnnClassifier
logger = logging.getLogger("cnnClassifierLogger")
