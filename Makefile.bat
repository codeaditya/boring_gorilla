pyuic4 BoringGorilla_design.ui -o BoringGorilla_design.py
python3 setup.py sdist
python3 setup.py bdist_msi
python3 setup.py bdist_wininst
