export MAYA_BIN = C:\Program Files\Autodesk\Maya2022\bin
export MAYA_PY = ${MAYA_BIN}/mayapy.exe

.PHONY: clean make_rst_from_markdown dist publish test_publish

clean:
	rm -fr ./build
	rm -fr ./dist

make_rst_from_markdown:
	pandoc -f markdown -t rst  README.md -o README.rst

dist: clean make_rst_from_markdown
	"${MAYA_PY}" -m pip install 'twine>=1.5.0'
	"${MAYA_PY}" setup.py sdist bdist_wheel

check_dist: dist
	twine check dist/*

publish: dist
	"${MAYA_PY}" -m twine upload --repository pypi dist/*

test_publish: dist
	"${MAYA_PY}" -m twine upload --repository testpypi dist/*
