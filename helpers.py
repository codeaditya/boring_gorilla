# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Provides helper classes and functions for BoringGorilla.

"""
import logging

from PyQt4 import QtCore


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
