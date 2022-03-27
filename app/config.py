from pathlib import Path
import logging

APP_ROOT = Path(__file__).parent.resolve()

LOGGING_CONFIG = dict(filename=APP_ROOT.joinpath('app.log'),
                      level=logging.INFO,
                      format='%(asctime)s:%(levelname)s:%(message)s',
                      datefmt='%Y-%m-%d %H:%M:%S')

PARSING_QUEUE_NAME = 'Parsing'
ERRORS_QUEUE_NAME = 'Errors'
