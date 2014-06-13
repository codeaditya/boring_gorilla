# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Provides helper classes and functions for BoringGorilla.

"""
import logging
import os.path

from PyQt4 import QtCore

###############################################################################
#### Add logging functionality ################################################
FORMATTER = logging.Formatter("{asctime} - {module:15s} - {process} - "
                              "{levelname:8s} - {message}", style="{")
LOGGING_LEVEL = logging.DEBUG
# logging.Logger object
logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)
# Console handler
ch = logging.StreamHandler()
ch.setFormatter(FORMATTER)
logger.addHandler(ch)
###############################################################################

COMTYPES_AVAILABLE = False
try:
    import comtypes
    import comtypes.client
    logger.debug("cometypes module available.")
    COMTYPES_AVAILABLE = True
except ImportError:
    logger.debug("comtypes module not available.")


def import_data_in_amibroker(database_path, import_file_list, import_format,
                             amibroker_visibility=False):
    """Import the data in Amibroker.

    :param database_path: location of the database folder of AmiBroker
    :param import_file_list: data files to be imported in AmiBroker
    :param import_format: format definition file for AmiBroker

    :type database_path: str
    :type import_file_list: list of str
    :type import_format: str
    """
    if COMTYPES_AVAILABLE:
        logger.debug("Starting import.")
        comtypes.CoInitializeEx()
        ami = comtypes.client.CreateObject("Broker.Application")
        ami.Visible = amibroker_visibility
        ami.LoadDatabase(database_path)
        for import_file in import_file_list:
            filename = os.path.basename(import_file)
            logger.info("Importing: {0}".format(filename))
            ami.Import(0, import_file, import_format)
        ami.RefreshAll()
        ami.SaveDataBase()
        ami.Quit()
        logger.debug("Data imported in AmiBroker Database: {0}"
                     "".format(database_path))
    else:
        logger.warning("Data cannot be imported in AmiBroker since comtypes "
                       "module is not available.")


class WorkerThread(QtCore.QThread):
    """Create a QThread to run the functions in a separate Qt Thread.

    :param func: the function that needs to be run
    :param args: the arguments that should be passed to the function

    :type func: function
    :type args: tuple
    """

    def __init__(self, func, args):
        super(WorkerThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        """
        The statements that are run when the thread starts.
        """
        self.func(*self.args)


class GuiLogHandler(logging.Handler):
    """Create a QtCore.QObject which emits the formatted log messages.

    :param sig_emitter: the object that emits the log message.

    :type sig_emitter: QtCore.QObject
    """

    def __init__(self, sig_emitter):
        super(GuiLogHandler, self).__init__()
        self.sig_emitter = sig_emitter

    def emit(self, log_record):
        """Emits the formatted log message.

        :param log_record: the logging statement
        """
        message = self.format(log_record)
        self.sig_emitter.emit(QtCore.SIGNAL("log_msg(QString)"), message)
