@echo off

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  design     to auto-generate the python files from ui_design
	echo.  build      to build source distribution
	echo.  buildall   to also build Windows binaries - exe and msi installers
	echo.  clean      to remove unwanted auto-generated files/folders
	echo.  cleanall   to also remove manually auto-generated files
	goto end
)

if "%1" == "design" (
	pyuic4 "ui_design\BoringGorilla_design.ui" -o BoringGorilla_design.py
	pyuic4 "ui_design\Preferences_design.ui" -o Preferences_design.py
	echo.
	echo.Design file generated - BoringGorilla_design.py
	echo.Design file generated - Preferences_design.py
	echo.All the design files generated successfully.
	goto end
)

if "%1" == "build" (
    python3 setup.py build_exe
	echo.
	echo.Build build_exe finished.
	goto end
)

if "%1%" == "buildall" (
	python3 setup.py bdist_msi
	python3 setup.py bdist_wininst
	echo.
	echo.Build bdist_msi finished.
	echo.Build bdist_wininst finished.
	goto end
)

if "%1%" == "clean" (
	:clean
	rmdir /S /Q __pycache__
	rmdir /S /Q "build\bdist.win32"
	rmdir /S /Q dist
	del MANIFEST
	echo.
	echo. Removed dir  -    __pycache__
	echo. Removed dir  -    "build/bdist.win32"
	echo. Removed dir  -    dist
	echo. Removed file -    MANIFEST
	echo.Clean finished.
	goto end
)

if "%1%" == "cleanall" (
	del BoringGorilla_design.py
	del Preferences_design.py
	del config.ini
	echo.
	echo. Removed file -    BoringGorilla_design.py
	echo. Removed file -    Preferences_design.py
	echo. Removed file -    config.ini
	echo.
	goto clean
)

:end
	echo.
	echo.######################################################################
	echo.######################################################################
	echo.
