all : BoringGorilla_design.py Preferences_design.py
.PHONY : all

BoringGorilla_design.py : ui_design/BoringGorilla_design.ui
	pyuic4 ui_design/BoringGorilla_design.ui -o BoringGorilla_design.py

Preferences_design.py : ui_design/Preferences_design.ui
	pyuic4 ui_design/Preferences_design.ui -o Preferences_design.py

.PHONY : build buildall

build :
	python3 setup.py sdist

buildall : build
	python3 setup.py bdist_msi
	python3 setup.py bdist_wininst

.PHONY : clean cleanall

clean :
	rm -rf __pycache__
	rm -f *.pyc
	rm -rf MANIFEST

cleanall : clean
	rm -f BoringGorilla_design.py
	rm -f Preferences_design.py
