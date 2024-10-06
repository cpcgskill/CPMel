export MAYA_BIN = C:\Program Files\Autodesk\Maya2022\bin
export MAYA_PY = ${MAYA_BIN}/mayapy.exe

.PHONY: clean make_rst_from_markdown dist publish test_publish
.IGNORE: clean

clean:
	rmdir /s/q "./dist"

make_rst_from_markdown:
	pandoc -f markdown -t rst  README.md -o README.rst

dist: clean make_rst_from_markdown
	py -m pip install 'twine>=1.5.0' 'build>=1.2.2'
	py -m build

check_dist: dist
	twine check dist/*

publish: check_dist dist
	py -m twine upload --repository pypi dist/*


test_publish: check_dist dist
	py -m twine upload --repository testpypi dist/*
