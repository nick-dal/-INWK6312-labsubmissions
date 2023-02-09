#!/home/student/Desktop/logger-lab/bin/python3
import logging

logging.basicConfig(format='%(asctime)s - %(message)s',
datefmt='%d-%b-%y %H:%M:%S')
logging.warning('Admin logged out')
