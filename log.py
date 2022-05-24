import logging
from datetime import datetime
from os import remove
#remove("./addSensors.log")
#------------------------- Start Logging ---------------------------------
def initLog(name):
    logging.basicConfig(filename='./' + str(name)+'.log', level=logging.DEBUG)
    logging.debug(datetime.now())
    logging.debug('Starting...')
    #--------------------------------------------------------------------------
def logRegister(txt):
    logging.debug(datetime.now())
    logging.debug(txt)
def logWarning(txt):
    logging.warning(datetime.now())
    logging.warning(txt)