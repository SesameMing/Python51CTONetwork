#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

import logging

#create logger
logger = logging.getLogger('TEST-LOG') #get the logger object first
logger.setLevel(logging.INFO) #set a global log level


# create console handler and set level to debug
ch = logging.StreamHandler() #print the log on monitor
ch.setLevel(logging.DEBUG) #

# create file handler and set level to warning
fh = logging.FileHandler("access.log")
fh.setLevel(logging.WARNING)
fh_err = logging.FileHandler("error.log")
fh_err.setLevel(logging.ERROR)


# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter_for_file = logging.Formatter('%(asctime)s - %(module)s -%(lineno)d - %(levelname)s - %(message)s')

# add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter_for_file)
fh_err.setFormatter(formatter)

# add ch and fh to logger
logger.addHandler(ch) #tell the logger to input the log into specified handler
logger.addHandler(fh)
logger.addHandler(fh_err)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')