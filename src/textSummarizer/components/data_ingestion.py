import os
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with the following info: {headers}")
        else:
            logger.info(f"File already exists")
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the destination directory if not already extracted
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        # Get list of files in unzip directory excluding the zip file itself
        extracted_files = [f for f in os.listdir(unzip_path) 
                         if f != os.path.basename(self.config.local_data_file)]
        
        # Check if extracted files already exist
        if len(extracted_files) > 0:
            logger.info(f"Files already extracted in {unzip_path}")
            return
            
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Zip file extracted successfully")
