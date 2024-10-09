import logging
from main import main

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    logging.info("Starting ETL process...")
    try:
        main()
        logging.info("ETL process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during the ETL process: {str(e)}")