import sys
import time
import schedule
import logging
from utils.process import process_document

def run():
    schedule.every().day.at("08:30").do(process_document)

    while True:
        logging.info('Success: Quote of the day sent')
        schedule.run_pending()
        time.sleep(1)

try:
    run()
except Exception as e:
    print(e)
    print('Error: Could not get quote of the day')
    sys.exit(1)
