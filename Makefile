.PHONY : all design build buildall clean cleanall

all : design

design : BoringGorilla_design.py Preferences_design.py

BoringGorilla_design.py : ui_design/BoringGorilla_design.ui
	pyuic4 ui_design/BoringGorilla_design.ui -o BoringGorilla_design.py

Preferences_design.py : ui_design/Preferences_design.ui
	pyuic4 ui_design/Preferences_design.ui -o Preferences_design.py

build :
	python3 setup.py sdist

buildall : build
	python3 setup.py bdist_msi
	python3 setup.py bdist_wininst

clean :
	rm -rf __pycache__
	rm -rf build/bdist.win32
	rm -rf dist
	rm -f MANIFEST

cleanall : clean
	rm -f BoringGorilla_design.py
	rm -f Preferences_design.py
	rm -f config.ini
