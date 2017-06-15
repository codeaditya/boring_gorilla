#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is a setup script which creates a a folder containing Windows
executable (*.exe) file and all the required components for it to run
in a portable environment (without the associated console).

Run the build process by running the following command:

    python3 setup.py build

If everything works well you should find a subdirectory in the build
subdirectory that contains the files needed to run the application

To create an *.msi installer which would allow you to install the file
like other windows programs, run the following command:

    python3 setup.py bdist_msi

"""

import sys

from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {'build_exe': dict(includes='atexit',
                             include_files=['LICENSE.txt'],
                             silent=True)}
executables = [Executable(script='BoringGorilla.py',
                          initScript=None,
                          base=base,
                          targetName='BoringGorilla.exe',
                          icon=None)]

setup(name='BoringGorilla',
      version='0.1',
      description='Downloads and processes data for Stock Markets',
      author='Aditya',
      options=options,
      executables=executables
      )
