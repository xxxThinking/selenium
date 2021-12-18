'''
@File:log.py
@DateTime:18/12/2021 下午 7:08
@Author:sweet
@Desc:
'''

import logging
from selenium_day05.config.config_1 import log_path

logger = logging.getLogger()
logger.setLevel(logging.INFO)

format = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
logfile = log_path
fh = logging.FileHandler(logfile,mode= 'a',encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(format)
logger.addHandler(fh)