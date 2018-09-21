#日志模块
import os
import platform
import logging

if platform.platform().startswith('Window'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'),'test.txt')
else:
    logging_file = os.path.join(os.getenv('HOME'),'test.txt')

print('Logging to', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s: %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w'
)

logging.debug('start of the program')
logging.info('Doing something')
logging.warning('Dying now')